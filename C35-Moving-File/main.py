############ Move file using python
import os

source = "C:\\Users\\fahmi\\PycharmProjects\\hellloworlde\\C34-Copy-File\\copy.txt"
# source = "floder"
destination = "C:\\Users\\fahmi\\PycharmProjects\\hellloworlde\\C35-Moving-File\\copy2.txt"

try:
    if os.path.exists(destination):
        print("there's a file there ")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print("file not found")
