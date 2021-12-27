import sys,os
import shutil
root = "/hdd/Backup/Coding/"
replaceroot = "/hdd2/Study/Coding/"
# path = os.path.join(root, "targetdirectory")
for path, subdirs, files in os.walk(root):
    for name in files:
        if name.endswith(".cpp") or name.endswith(".C") or name.endswith(".json") or name.endswith(".csproj") or name.endswith(".cs") or name.endswith(".h") or name.endswith(".js") or name.endswith(".hbs") or name.endswith(".html") or name.endswith(".sh") or name.endswith(".py") or name.endswith(".ipynb"):
            if "node_modules" in path or "DrRepair-master" in path:
                pass
            else:
                print(os.path.join(path, name))
                if os.path.isfile(os.path.join(path, name).replace(root, replaceroot)):
                    os.remove(os.path.join(path, name).replace(root, replaceroot))
                # if os.stat(os.path.join(path, name)).st_mtime != os.stat(os.path.join(path, name).replace(root, replaceroot)).st_mtime:

                if os.path.isdir(path.replace(root, replaceroot)):
                    print("Copying: " + os.path.join(path, name))
                    shutil.copy2(os.path.join(path, name), os.path.join(path, name).replace(root, replaceroot))
                else:
                    os.makedirs(os.path.join(path, name).replace(root, replaceroot))
                    shutil.copy2(os.path.join(path, name), os.path.join(path, name).replace(root, replaceroot))

