import os
from datetime import datetime

# Get the current date in YYYY-MM-DD format
current_date = datetime.now().strftime("%Y-%m-%d")

# Prompt the user to input the file name
input_file_name = input("Article Title: ")

# Replace spaces with hyphens
formatted_file_name = input_file_name.replace(" ", "-")

# Combine the date and formatted file name
full_file_name = f"{current_date}-{formatted_file_name}.md"

# Define the _posts directory
posts_directory = "_posts"

# Ensure the _posts directory exists
os.makedirs(posts_directory, exist_ok=True)

# Define the full path for the new file
file_path = os.path.join(posts_directory, full_file_name)

# Create the file
with open(file_path, 'w') as file:
    file.write("")  # Creating an empty file

print(f"File created: {file_path}")
