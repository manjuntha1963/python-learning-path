from pathlib import Path

# Display the learning path name
print("Python Learning Path")

# Get and show the current working directory
# This helps verify that the script is running from the expected location
current_directory = Path.cwd()
print(f"Running from: {current_directory}")

# Guide the user to the first module
print("Start with the README in 01-basic-python.")
print("Each example file demonstrates one concept from the module.")
