# PyPi Crawler

Crawl the package and release information from PyPi API and store the result into Google Drive. 

# Plan:

- [ ] Build each component:
  - [ ] A program uploading a file to a specific directory of Google Drive. 
  - [ ] A program extracting all package name from PyPi 
  - [ ] A program downloading a json from PyPi api given specific package name 
  - [ ] A program downloading json from a specific pypi release 
- [ ] Build a program checking the status of Google Drive directory and do ETL action. 
  - [ ] If the package jsonl does not exists, download json(s) of all releases for such package and upload the jsonl. 
  - [ ] If the package jsonl exists, check the name to determine whether the latest release has not been uploaded. Refresh the jsonl if it should be updated. (Use <packagename>_<latest_release_version>.jsonl as file name)
- [ ] Design .yml workflow for crawling automatically. 
