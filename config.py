import os

temp_pdf_folder = f"{os.getcwd()}\\temp"
converted_file_folder = f"{os.getcwd()}\\converted_file"

# Create the directories if they do not exist
os.makedirs(temp_pdf_folder, exist_ok=True)
os.makedirs(converted_file_folder, exist_ok=True)
