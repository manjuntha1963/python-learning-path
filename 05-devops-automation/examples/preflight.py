from pathlib import Path

print("Deployment preflight")
print("Dockerfile present:", Path("Dockerfile").exists())
print("Run tests before deploying: python -m pytest")
