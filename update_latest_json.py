import sys
import requests
import json
import os

def get_data(pkg_name):
    url = f'https://pypi.org/pypi/{pkg_name}/json'
    result = requests.get(url).json()
    return result

if __name__ == '__main__':
    pkg_name = sys.argv[1]
    result = get_data(pkg_name)
    rc = len(result['releases'].keys())
    save_path = f'data/latest/{pkg_name}.rc{rc}.json'
    if not os.path.exists(save_path):
        with open(save_path, 'w', encoding='utf8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print('package latest json saved into:', save_path)
        old_json_path = f'data/latest/{pkg_name}.rc{rc-1}.json'
        if os.path.exists(old_json_path):
            os.remove(old_json_path)
            print(old_json_path, 'removed')
    else:
        print(save_path, 'already exists')