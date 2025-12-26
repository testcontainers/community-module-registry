#!/usr/bin/env python3
"""
This script validates that all Go modules from testcontainers-go repository
have corresponding entries in the community-module-registry.
"""
import sys
import subprocess
import tempfile
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


def get_go_modules(repo_path: Path) -> List[str]:
    """Get list of all Go modules from testcontainers-go repository."""
    modules_dir = repo_path / "modules"
    if not modules_dir.exists():
        print(f"Error: {modules_dir} does not exist", file=sys.stderr)
        sys.exit(1)
    
    modules = []
    for item in modules_dir.iterdir():
        if item.is_dir():
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
    """Check if all Go modules are covered in the registry."""
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
                missing_modules.append(f"{go_mod} (maps to {', '.join(mapped_names)})")
                continue
        else:
            # Not found anywhere
            missing_modules.append(go_mod)
    
    return missing_modules, missing_go_support


def main():
    # Determine paths
    script_dir = Path(__file__).parent
    registry_path = script_dir.parent.parent  # Go up to repo root
    
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
                    print(f"  - {mod}")
            
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
        import shutil
        if go_repo_path.exists():
            shutil.rmtree(go_repo_path)


if __name__ == "__main__":
    main()
