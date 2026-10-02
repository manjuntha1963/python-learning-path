# Module 02 example: file system listing
# This example shows how to iterate over files in a folder and print their names

from pathlib import Path

# `Path('.')` refers to the current folder
# `.glob('*.txt')` finds all text files in that folder
files = list(Path('.').glob('*.txt'))

# Print the count of files found
print(f"Found {len(files)} text files")

# Print each file name one by one
for file in files:
    print(file.name)

# This pattern is useful for automation scripts, report generation, and cleanup tasks
