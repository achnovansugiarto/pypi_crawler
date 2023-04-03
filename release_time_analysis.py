"""
TODO:
- [X] Load (package, release, updatetime) from data/latest
    - [X] Ignore release that does not fit a,b,c
    - [X] Updatetime -> max update date
- [ ] Sort by datetime 
"""
import os
import json
from datetime import datetime
from src.ignore import ignore_filter


def load_releases(paths):
    for path in paths:
        with open(path, 'r') as f:
            result = json.load(f)
        for version, release_content in result['releases'].items():
            if ignore_filter._pattern.match(version) and release_content:
                times = [content['upload_time'] for content in release_content]
                dates = [datetime.strptime(t, "%Y-%m-%dT%H:%M:%S") for t in times]
                try:
                    yield (
                        result['info']['name'], version, 
                        max(dates)
                    )
                except BaseException as e:
                    print(f'error in {version}:\n', release_content)
                    raise e
file_names = sorted(os.listdir('data/latest'))
paths = map(lambda x: f'data/latest/{x}', file_names)
releases = load_releases(paths)
if __name__ == '__main__':
    for release in releases:
        print(release)





