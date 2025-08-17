import os
import gui

def listPDFs(folder_path):
    pdf_files = []
    for files in os.listdir(folder_path):
        if files.lower().endswith(".txt"):
            pdf_files.append(files)
    print(files)

gui.startMainScreen()
directory = gui.getFileDirectory()
listPDFs(directory)
