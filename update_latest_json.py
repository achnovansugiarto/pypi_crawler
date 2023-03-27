import sys
import requests
import json
import os

def update(pkg_name):
    result = get_data(pkg_name)
    if 'releases' in result:
        if download_new(pkg_name, result):
            remove_old(pkg_name, result)
        else:
            print('Already exists')
    else:
        print('No releases')

def get_data(pkg_name):
    url = f'https://pypi.org/pypi/{pkg_name}/json'
    result = requests.get(url).json()
    return result

def download_new(pkg_name, result):
    rc = len(result['releases'].keys())
    save_path = f'data/latest/{pkg_name}.rc{rc}.json'
    if not os.path.exists(save_path):
        with open(save_path, 'w', encoding='utf8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        return True
    else:
        return False

def remove_old(pkg_name, result):
    rc = len(result['releases'].keys())
    if rc - 1 > 0:
        old_json_path = f'data/latest/{pkg_name}.rc{rc-1}.json'
        if os.path.exists(old_json_path):
            os.remove(old_json_path)
            print(f'{old_json_path} removed')
        else:
            print(f'{old_json_path} does not exist')
    else:
        print(f'No older version')
    
if __name__ == '__main__':    
    update(sys.argv[1])