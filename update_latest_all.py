import sys
import os
import subprocess
from update_latest_json import update
PATH = 'data/package_names.txt'
SPLIT_PATH = '/tmp'
def update_all(index, split_cnt=10):
  # Get total package count
  out = subprocess.check_output(['wc', '-l', PATH])
  total = int(out.decode("utf-8").split(PATH)[0])
  print(f"line count of {PATH}: {total}")
  # Create Split Path
  if not os.path.exists(SPLIT_PATH):
    os.mkdir(SPLIT_PATH)
  # Do Split
  pkg_cnt_per_file = int(total / split_cnt)
  subprocess.run(['split', '-l', str(pkg_cnt_per_file),
                       PATH, SPLIT_PATH + '/'])
  files = os.listdir(SPLIT_PATH)
  print(f"split files: {files}")
  file = files[index]
  print(f"selected file: {file}")
  # Do update
  with open(file, 'r') as f:
    for pkg in map(lambda x: x.strip(), f):
      print(f"=============\t\t\t {pkg} \t\t\t================")
      update(pkg)
      print('=================================================')

if __name__ == '__main__':
  update_all(sys.argv[1], split_cnt=sys.argv[2])
