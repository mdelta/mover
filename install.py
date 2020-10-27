import json
from pathlib import Path
from shutil import copyfile, copytree

# global variables
#ROOT_DIR = "/home/vagrant/lfs"
ROOT_DIR = Path(__file__).parent.joinpath("test")


def loadConfiguration():
    # Get configuration path
    installPaths = Path(__file__).parent.joinpath("install.json")

    # Load configuration JSON file
    with open(installPaths) as f:
        data = json.load(f)

    return data


def processFolder(data, srcPath=Path(__file__).parent):
    for entry in data:
        if isinstance(data[entry], dict):
            processFolder(data[entry], srcPath.joinpath(entry))
        else:
            copyFile(srcPath.joinpath(entry), ROOT_DIR.joinpath(data[entry]))


def createDirectory(crtPath):
    if not Path.exists(crtPath):
        Path.mkdir(crtPath, True, True)


def copyFile(src, target):
    if src.exists() == False:
        return

    if target.exists() == True:
        return

    print("Copy {} to {}".format(src, target))
    createDirectory(target.parent)

    copyfile(src, target)


if __name__ == "__main__":
    cfg = loadConfiguration()

    processFolder(cfg, Path(__file__).parent)
