import os
from pathlib import Path

package_name="Customer-Personality-Analysis"

list_of_files = [
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/components/data_ingestion.py",
    f"src/{package_name}/components/data_transformation.py",
    f"src/{package_name}/components/data_validation.py",
    f"src/{package_name}/components/model_evaluation.py",
    f"src/{package_name}/components/model_pusher.py",
    f"src/{package_name}/components/model_trainer.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/entity/artifacts_entity.py",
    f"src/{package_name}/entity/config_entity.py",
    f"src/{package_name}/constants/training/__init__.py",
    f"src/{package_name}/exception.py",
    f"src/{package_name}/logger.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/pipeline/training_pipeline.py",
    f"src/{package_name}/pipeline/batch_prediction.py"
    f"src/{package_name}/utils.py",
    "template/index.html",
    "template/result.html",
    "application.py",
    "requirements.txt",
    ".gitignore"
]


# here will create a directory

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    
    """ how exist_ok works:if "directory" already exists, 
    os.makedirs() will not raise an error, and it will do nothing. 
    If "my_directory" doesn't exist, it will create the directory.
    """
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
    else:
        print("file already exists")

# here will use the file handling