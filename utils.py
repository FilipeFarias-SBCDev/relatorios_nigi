import os
import logging


def clear_folder(folder):
    for file in os.listdir(f"{folder}"):
        file_path = os.path.join(f"{folder}", file)

        if os.path.isfile(file_path):
            os.remove(file_path)


def upload_file(files, temp_pdf_folder):
    if "pdfFile" not in files:
        logging.error("No file part")

    file = files["pdfFile"]

    if file.filename == "":
        logging.error("No selected file")

    if file and file.filename.endswith(".pdf"):
        filename = file.filename
        file.save(os.path.join(temp_pdf_folder, filename))
        logging.info("File successfully uploaded")

    else:
        logging.error("Invalid file type")
