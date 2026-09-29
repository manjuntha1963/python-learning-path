from pathlib import Path

# Purpose: Find and list all text files in the current directory.
# This demonstrates file system operations using pathlib.

# glob() searches for files matching a pattern (*.txt means all .txt files)
# sorted() arranges them alphabetically by filename
text_files = sorted(Path(".").glob("*.txt"))

# Display the count of text files found
print(f"Found {len(text_files)} text files")

# Loop through each file and print its name
# This is useful for batch processing or auditing file contents
for file in text_files:
    print(f"  - {file.name}")

# Practical use: This pattern is common in DevOps for finding logs, configs, or reports
print("\nTo test this, create a few .txt files in the current directory.")
