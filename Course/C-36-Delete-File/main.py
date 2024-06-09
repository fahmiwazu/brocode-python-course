############# delete file with python
import os
import shutil
path = "isi"

try:
    # os.remove(path)       # delete a file
    # os.rmdir(path)        # delete an empty directory
    shutil.rmtree(path)     # delete a directory containing  files
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("not-auth")
except OSError:
    print(" you cannot delete that using that function")
else:
    print(path+" was deleted ")