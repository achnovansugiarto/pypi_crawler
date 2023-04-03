"""
Update the package names stored in data/package_names.txt

The package names are from the pypi.python.org/simple page
"""
import requests
from bs4 import BeautifulSoup

PYPI_URL = "https://pypi.python.org/simple/"
PATH = "data/package_names.txt"


def download_pypi_package_names():
    print(f"GET list of packages from {PYPI_URL}")
    try:
        resp = requests.get(PYPI_URL, timeout=5)
    except requests.exceptions.RequestException:
        print("ERROR: Could not GET the pypi index. Check your internet connection.")
        exit(1)

    print(f"NOW parsing the HTML (this could take a couple of seconds...)")
    try:
        soup = BeautifulSoup(resp.text, "html.parser")
        body = soup.find("body")
        links = (pkg for pkg in body.find_all("a"))
        pkg_names = [link["href"].split("/")[-2] for link in list(links)]
    except BaseException:
        print("ERROR: Could not parse pypi HTML.")
        exit(1)
    return pkg_names


def save_pkg_name_file(pkg_names):
    with open(PATH, "w") as f:
        for n in pkg_names:
            f.write(n + "\n")
    print("package names saved into", PATH)


def load_pkg_names():
    with open(PATH, "r") as f:
        package_names = [x.strip() for x in f]
        package_names = [x for x in package_names if len(x) > 0]
    return package_names


if __name__ == "__main__":
    loaded_pkg_names = load_pkg_names()
    print("number of loaded pkg names:", len(loaded_pkg_names))
    current_pkg_names = download_pypi_package_names()
    print("number of current pkg names:", len(current_pkg_names))
    new_pkgs = set(current_pkg_names) - set(loaded_pkg_names)
    if len(new_pkgs):
        print("Number of new packages: ", len(new_pkgs))
        pkgs = sorted(list(set(new_pkgs) | set(loaded_pkg_names)))
        print("Number of joined pkgs:", len(pkgs))
        save_pkg_name_file(pkgs)
    else:
        print("No new released pacakge")
