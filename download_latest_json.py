import sys
import requests
import json

def get_data(pkg_name):
    url = f'https://pypi.org/pypi/{pkg_name}/json'
    result = requests.get(url).json()
    return result

if __name__ == '__main__':
    pkg_name = sys.argv[1]
    result = get_data(pkg_name)
    rc = len(result['releases'].keys())
    with open(f'data/latest/{pkg_name}.rc{rc}.json', 'w', encoding='utf8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)