import sys
from update_latest_json import update
def update_all(alpha):
  with open('data/package_names.txt', 'r') as f:
    for pkg in filter(lambda x: x.startswith(alpha), map(lambda x: x.strip(), f)):
      print(f"=============\t\t\t {pkg} \t\t\t================")
      update(pkg)
      print('=================================================')

if __name__ == '__main__':
  update_all(sys.argv[1])