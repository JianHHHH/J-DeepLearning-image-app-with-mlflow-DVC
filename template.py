import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "Image-Classifier"

# created all the file and directory names, and store them in python string list.
list_of_files = [
    ".github/workflows/.gitkeep", # this folder is used for ML yaml meant for later on CICD jobs
    f"src/{project_name}/__init__.py", # used to service and the customized package/source code of this application.
    f"src/{project_name}/components/__init__.py", # this module used to build different stage, data ingestion, model trainer
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml", # for dvc
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb", # where we do IP 1 experiment before modular coding.
    "templates/index.html" # used for store HTML file


]

# using for loop to created these file and folders by go through this filepath list.

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")