from pathlib import Path

files = sorted(Path(".").glob("*.txt"))
print(f"Found {len(files)} text files")
for file in files:
    print(file.name)
