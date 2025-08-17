import os
import gui

#testing git

def listPDFs(folder_path):
    pdf_files = []
    for files in os.listdir(folder_path):
        if files.lower().endswith(".txt"):
            pdf_files.append(files)
    print(files)