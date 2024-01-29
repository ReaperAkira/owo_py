import requests

print("Updating...")
update = requests.get(
    "https://raw.githubusercontent.com/ReaperAkira/owo_py/main/update_def.py"
)

# Save the new version to the local file system
with open("owo_console\\update_def.py", "wb") as f:
    f.write(update.content)
print("Update complete!")
#hmm so good
