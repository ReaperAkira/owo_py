import requests


# Get the new version of the file from GitHub
def update_bot():
    print("Updating...")
    update = requests.get(
        "https://raw.githubusercontent.com/ReaperAkira/owo_py/main/up_update_file.py"
    )

    # Save the new version to the local file system
    with open("owo_console\\up_update_file.py", "wb") as f:
        f.write(update.content)
    print("Update complete!")

version = requests.get('https://raw.githubusercontent.com/ReaperAkira/owo_py/main/version.json')
if version  != 2.0 :
    update_bot()
#it work lol
# SO GOOD BRO
