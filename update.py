import requests
import shutil
import os
import sys
import json

def download_file(url, file_path):
    response = requests.get(url)
    with open(file_path, "wb") as f:
        f.write(response.content)

def check_version():
    version_url = "https://raw.githubusercontent.com/ReaperAkira/owo-farm/main/version.json"
    version_file = "version.json"

    if not os.path.exists(version_file):
        download_file(version_url, version_file)

    with open(version_file) as f:
        remote_version = json.load(f)["updater"]

    if remote_version != get_local_version():
        download_file("https://raw.githubusercontent.com/ReaperAkira/owo-farm/main/update.py", "update.py")
        print("Update script downloaded. Please run it to update the bot.")
        sys.exit(0)

def get_local_version():
    with open("version.json") as f:
        local_version = json.load(f)["updater"]
    return local_version

if __name__ == "__main__":
    check_version()

    # Rest of the code for updating main.py goes here
    # ...
    # lmao this really update it self
