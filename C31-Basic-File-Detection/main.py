############### basic file detection in python
import os
# path = "C:\\Users\\fahmi\\PycharmProjects\\hellloworlde\\C31-Basic-File-Detection"
path = "C:\\Users\\fahmi\\PycharmProjects\\hellloworlde\\C31-Basic-File-Detection\\text.txt"

if os.path.exists(path):
    print("That location existed")
    if os.path.isfile(path):
        print("that is a file")
    elif os.path.isdir(path):
        print("that is directory")
else:
    print("That location doesnt")
