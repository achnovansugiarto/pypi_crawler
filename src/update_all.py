"""
Update JSON representing the latest status of a python package

The package is listed in data/package_names.txt
"""
import sys
import os
import subprocess
import tqdm

PATH = "data/package_names.txt"
SPLIT_PATH = "tmp"


def update_all(update, index, split_cnt=10):
    """
    Args:
      - update_func: the update function to be callback
      - index: the index to select the splitted target file
      - split_cnt: number of total parallel count
    """
    # Get total package count
    out = subprocess.check_output(["wc", "-l", PATH])
    total = int(out.decode("utf-8").split(PATH)[0])
    print(f"line count of {PATH}: {total}")
    # Create Split Path
    if not os.path.exists(SPLIT_PATH):
        os.mkdir(SPLIT_PATH)
    # Do Split
    pkg_cnt_per_file = int(total / split_cnt)
    subprocess.run(["split", "-l", str(pkg_cnt_per_file), PATH, SPLIT_PATH + "/"])
    files = os.listdir(SPLIT_PATH)
    print(f"split files: {files}")
    file = files[index]
    print(f"selected file: {file}")
    # Do update
    with open(f"{SPLIT_PATH}/{file}", "r") as f:
        pkgs = list(map(lambda x: x.strip(), f))
        for pkg in tqdm.tqdm(pkgs):
            print(f"=============\t\t\t {pkg} \t\t\t================")
            update(pkg)
            print("=================================================")
