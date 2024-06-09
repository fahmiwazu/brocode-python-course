############ Copy file in python
import shutil
#copyfile() =   copy content of file
#copy()     =   copyfile()  +   permission mode + destination can be a directory
#copy2()    =   copy()  +   copies metadata (file's creation and modification times)
shutil.copyfile('test.txt', 'copy.txt') #src.dst