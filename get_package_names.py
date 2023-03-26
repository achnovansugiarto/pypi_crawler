import requests
from bs4 import BeautifulSoup
def download_pypi_package_names():
    pypi_index = 'https://pypi.python.org/simple/'
    print(f'GET list of packages from {pypi_index}')
    try:
        resp = requests.get(pypi_index, timeout=5)
    except requests.exceptions.RequestException:
        print('ERROR: Could not GET the pypi index. Check your internet connection.')
        exit(1)

    print(f'NOW parsing the HTML (this could take a couple of seconds...)')
    try:
        soup = BeautifulSoup(resp.text, 'html.parser')
        body = soup.find('body')
        links = (pkg for pkg in body.find_all('a'))
        pkg_names = [link['href'].split('/')[-2] for link in list(links)]
    except BaseException:
        print('ERROR: Could not parse pypi HTML.')
        exit(1)
    return pkg_names

def save_pkg_name_file(pkg_names):
    with open('data/package_names.txt', 'w') as f:
        for n in pkg_names:
            f.write(n + '\n')

if __name__ == '__main__':
    pkg_names = download_pypi_package_names()
    save_pkg_name_file()