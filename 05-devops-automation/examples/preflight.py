from pathlib import Path

# Purpose: Verify that a project is ready for deployment.
# DevOps uses preflight checks to catch problems early.

print("=== Deployment Preflight Check ===")
print()

# Check 1: Does the Dockerfile exist?
# Docker is required to containerize the application
dockerfile_exists = Path("Dockerfile").exists()
status = "✓ Found" if dockerfile_exists else "✗ Missing"
print(f"Dockerfile:     {status}")

# Check 2: Does the requirements.txt exist?
# This file lists Python dependencies needed by the application
requirements_exists = Path("requirements.txt").exists()
status = "✓ Found" if requirements_exists else "✗ Missing"
print(f"requirements.txt: {status}")

# Check 3: Does the .env template exist?
# This file stores configuration and secrets (should not include real secrets)
env_template_exists = Path(".env.example").exists()
status = "✓ Found" if env_template_exists else "✗ Missing"
print(f".env.example:   {status}")

print()
print("Deployment steps:")
print("  1. Ensure all checks pass")
print("  2. Run tests: python -m pytest")
print("  3. Build Docker image: docker build -t app:1.0 .")
print("  4. Push to registry")
print("  5. Deploy to production")
