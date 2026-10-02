# Module 05 example: preflight deployment checks
# This shows how DevOps automation validates setup before deployment

from pathlib import Path

# Check whether required files exist
required_files = ["Dockerfile", "requirements.txt"]

for file_name in required_files:
    file_exists = Path(file_name).exists()
    print(f"{file_name}: {file_exists}")

# If all checks pass, the system is ready to deploy
print("Deployment ready only if all required files are present.")
