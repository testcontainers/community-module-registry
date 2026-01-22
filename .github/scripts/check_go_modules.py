#!/usr/bin/env python3
"""
This script validates that all Go modules from testcontainers-go repository
have corresponding entries in the community-module-registry.

When missing modules are detected and a GitHub token is provided, it will
create issues in the testcontainers-go repository to track the missing modules.
"""
import sys
import subprocess
import tempfile
import shutil
import os
import json
import urllib.request
import urllib.error
import urllib.parse
from pathlib import Path
from typing import Dict, List

# Define known mappings where Go module names differ from registry names
MODULE_MAPPINGS = {
    "postgres": ["postgresql", "postgis", "pgvector"],
    "gcloud": ["google-cloud"],
    "dockermcpgateway": ["docker-mcp-gateway"],
    "grafana-lgtm": ["grafana"],
    "registry": ["distribution-registry"],
    "azure": ["azurite", "cosmodb", "azure-eventhubs", "azure-servicebus"],
}

# Utility modules that don't represent standalone services
# These are infrastructure/utility modules and don't need catalog entries
UTILITY_MODULES = ["compose", "socat"]

# GitHub API timeout in seconds
GITHUB_API_TIMEOUT = 30


def get_go_modules(repo_path: Path) -> List[str]:
    """Get list of all Go modules from testcontainers-go repository."""
    modules_dir = repo_path / "modules"
    if not modules_dir.exists():
        print(f"Error: {modules_dir} does not exist", file=sys.stderr)
        sys.exit(1)
    
    modules = []
    for item in modules_dir.iterdir():
        # Skip hidden directories and files
        if item.is_dir() and not item.name.startswith('.'):
            modules.append(item.name)
    
    return sorted(modules)


def get_registry_modules_with_go(registry_path: Path) -> Dict[str, bool]:
    """Get modules in registry and check if they have Go support."""
    modules_dir = registry_path / "modules"
    if not modules_dir.exists():
        print(f"Error: {modules_dir} does not exist", file=sys.stderr)
        sys.exit(1)
    
    modules = {}
    for module_dir in modules_dir.iterdir():
        if module_dir.is_dir():
            index_file = module_dir / "index.md"
            if index_file.exists():
                content = index_file.read_text(encoding='utf-8')
                has_go = "id: go" in content
                modules[module_dir.name] = has_go
    
    return modules


def check_coverage(go_modules: List[str], registry_modules: Dict[str, bool]) -> tuple:
    """Check if all Go modules are covered in the registry.
    
    Returns a tuple of (missing_modules_info, missing_go_support) where
    missing_modules_info is a list of dicts with 'name' and 'mapped_to' keys.
    """
    missing_modules = []
    missing_go_support = []
    
    for go_mod in go_modules:
        # Skip utility modules
        if go_mod in UTILITY_MODULES:
            continue
        
        # Check direct match
        if go_mod in registry_modules:
            if registry_modules[go_mod]:
                continue  # Found with Go support
            else:
                missing_go_support.append(go_mod)
                continue
        
        # Check mappings
        if go_mod in MODULE_MAPPINGS:
            mapped_names = MODULE_MAPPINGS[go_mod]
            found = False
            for mapped_name in mapped_names:
                if mapped_name in registry_modules and registry_modules[mapped_name]:
                    found = True
                    break
            if not found:
                missing_modules.append({
                    'name': go_mod,
                    'mapped_to': mapped_names
                })
                continue
        else:
            # Not found anywhere
            missing_modules.append({
                'name': go_mod,
                'mapped_to': None
            })
    
    return missing_modules, missing_go_support


def check_existing_issue(token: str, module_name: str) -> bool:
    """Check if an issue already exists for the missing module.
    
    Args:
        token: GitHub API token
        module_name: Name of the module to check
        
    Returns:
        True if an issue already exists, False otherwise
    """
    # Search for existing issues
    search_query = f"repo:testcontainers/testcontainers-go is:issue is:open \"Add {module_name} module to community module registry\" in:title"
    url = f"https://api.github.com/search/issues?q={urllib.parse.quote(search_query)}"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=GITHUB_API_TIMEOUT) as response:
            result = json.loads(response.read().decode('utf-8'))
            return result.get('total_count', 0) > 0
    except Exception as e:
        # If we can't check, assume no issue exists to avoid blocking
        print(f"  ! Could not check for existing issue for {module_name}: {str(e)}", file=sys.stderr)
        return False


def create_github_issue(token: str, module_info: dict) -> bool:
    """Create a GitHub issue in testcontainers-go repository for a missing module.
    
    Args:
        token: GitHub API token
        module_info: Dict with 'name' and 'mapped_to' keys
        
    Returns:
        True if issue was created successfully, False otherwise
    """
    module_name = module_info['name']
    mapped_to = module_info['mapped_to']
    
    # Construct issue title
    title = f"Add {module_name} module to community module registry"
    
    # Construct issue body
    body_parts = [
        f"## Missing Module in Community Registry",
        "",
        f"The `{module_name}` module exists in testcontainers-go but is not listed in the [community module registry](https://github.com/testcontainers/community-module-registry).",
        "",
        "### Instructions to Add Module to Website",
        "",
        "1. Fork and clone the [community-module-registry](https://github.com/testcontainers/community-module-registry) repository",
        "",
        "2. Create a new module directory:",
    ]
    
    if mapped_to:
        body_parts.extend([
            f"   - The module should be named `{mapped_to[0]}` (or one of: {', '.join(mapped_to)})",
            f"   - Create directory: `modules/{mapped_to[0]}/`",
        ])
    else:
        body_parts.extend([
            f"   - Create directory: `modules/{module_name}/`",
        ])
    
    body_parts.extend([
        "",
        "3. Create `index.md` file with the module information:",
        "   ```yaml",
        "   ---",
        "   title: <Module Title>",
        "   categories:",
        "     - <category>  # e.g., relational-database, nosql-database, message-broker, etc.",
        "   docs:",
        "     - id: go",
        f"       url: https://golang.testcontainers.org/modules/{module_name}/",
        "       maintainer: core",
        "       example: |",
        "         ```go",
        "         // Add example code here",
        "         ```",
        "       installation: |",
        "         ```bash",
        f"         go get github.com/testcontainers/testcontainers-go/modules/{module_name}",
        "         ```",
        "   description: |",
        "     <Add module description here>",
        "   ---",
        "   ```",
        "",
        "4. Optionally add a `logo.svg` file (60x60, square SVG)",
        "",
        "5. Run the validation:",
        "   ```bash",
        "   python3 .github/scripts/check_go_modules.py",
        "   ```",
        "",
        "6. Submit a pull request to the community-module-registry repository",
        "",
        "For more details, see the [README](https://github.com/testcontainers/community-module-registry#readme).",
        "",
        "---",
        f"*This issue was automatically created by the Go modules coverage validation script.*"
    ])
    
    body = "\n".join(body_parts)
    
    # Create the issue using GitHub API
    import urllib.request
    import urllib.error
    
    url = "https://api.github.com/repos/testcontainers/testcontainers-go/issues"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    
    data = json.dumps({
        "title": title,
        "body": body,
        "labels": ["documentation", "help wanted"]
    }).encode('utf-8')
    
    try:
        req = urllib.request.Request(url, data=data, headers=headers, method='POST')
        with urllib.request.urlopen(req, timeout=GITHUB_API_TIMEOUT) as response:
            result = json.loads(response.read().decode('utf-8'))
            issue_url = result.get('html_url', '')
            print(f"  ✓ Created issue for {module_name}: {issue_url}")
            return True
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8')
        print(f"  ✗ Failed to create issue for {module_name}: {e.code} - {error_body}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"  ✗ Failed to create issue for {module_name}: {str(e)}", file=sys.stderr)
        return False


def main():
    # Determine paths
    script_dir = Path(__file__).parent
    registry_path = script_dir.parent.parent  # Go up to repo root
    
    # Check if GitHub token is available for creating issues
    github_token = os.environ.get('GITHUB_TOKEN', '')
    
    # Clone testcontainers-go to a unique temporary directory
    go_repo_path = Path(tempfile.mkdtemp(prefix="testcontainers-go-"))
    try:
        print("Cloning testcontainers-go repository...")
        result = subprocess.run(
            ["git", "clone", "--depth", "1", "https://github.com/testcontainers/testcontainers-go.git", str(go_repo_path)],
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )
        if result.returncode != 0:
            print(f"Error cloning repository: {result.stderr}", file=sys.stderr)
            sys.exit(1)
    
        # Get modules
        print("Checking Go modules coverage...")
        go_modules = get_go_modules(go_repo_path)
        registry_modules = get_registry_modules_with_go(registry_path)
        
        # Check coverage
        missing_modules, missing_go_support = check_coverage(go_modules, registry_modules)
        
        # Report results
        print(f"\n{'='*80}")
        print(f"Go Modules Coverage Report")
        print(f"{'='*80}")
        print(f"Total Go modules: {len(go_modules)}")
        print(f"Utility modules (skipped): {len(UTILITY_MODULES)} ({', '.join(UTILITY_MODULES)})")
        print(f"Modules checked: {len(go_modules) - len(UTILITY_MODULES)}")
        
        if missing_modules or missing_go_support:
            print(f"\n❌ VALIDATION FAILED")
            
            if missing_modules:
                print(f"\nMissing {len(missing_modules)} module(s) in registry:")
                for mod in missing_modules:
                    if mod['mapped_to']:
                        print(f"  - {mod['name']} (maps to {', '.join(mod['mapped_to'])})")
                    else:
                        print(f"  - {mod['name']}")
                
                # Create GitHub issues if token is available
                if github_token:
                    print(f"\nChecking for existing issues and creating new ones for missing modules...")
                    success_count = 0
                    skipped_count = 0
                    for mod in missing_modules:
                        # Check if issue already exists
                        if check_existing_issue(github_token, mod['name']):
                            print(f"  ⊘ Issue already exists for {mod['name']}, skipping")
                            skipped_count += 1
                        elif create_github_issue(github_token, mod):
                            success_count += 1
                    
                    print(f"\nCreated {success_count} new issue(s), skipped {skipped_count} existing issue(s) out of {len(missing_modules)} total.")
                else:
                    print(f"\nNote: Set GITHUB_TOKEN environment variable to automatically create issues for missing modules.")
            
            if missing_go_support:
                print(f"\nMissing Go support in {len(missing_go_support)} existing module(s):")
                for mod in missing_go_support:
                    print(f"  - {mod}")
            
            sys.exit(1)
        else:
            print(f"\n✅ VALIDATION PASSED")
            print(f"All Go modules from testcontainers-go are covered in the community-module-registry!")
            sys.exit(0)
    finally:
        # Clean up temporary directory
        if go_repo_path.exists():
            shutil.rmtree(go_repo_path)


if __name__ == "__main__":
    main()
