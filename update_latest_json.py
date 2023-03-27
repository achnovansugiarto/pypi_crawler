import sys
import requests
import json
import os

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
        print('package latest json saved into:', save_path)
        return True
    else:
        print(save_path, 'already exists')
        return False

def remove_old(pkg_name, result):
    rc = len(result['releases'].keys())
    if rc - 1 > 0:
        old_json_path = f'data/latest/{pkg_name}.rc{rc-1}.json'
        if os.path.exists(old_json_path):
            os.remove(old_json_path)
            print(old_json_path, 'removed')
        else:
            print(old_json_path, 'does not exists')
    else:
        print('no older version')
    
if __name__ == '__main__':
    pkg_name = sys.argv[1]
    result = get_data(pkg_name)
    if download_new(pkg_name, result):
        remove_old(pkg_name, result)