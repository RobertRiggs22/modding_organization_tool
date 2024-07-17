import os

#describes the type of files you want compiled into your new folder
suffix = ".pak"
#describes the name of the new folder you want with all the files this program grabbed end up
folder_name = "new " + suffix + " mod files"
#describes the parent folder that contains the child folders that you want the program to search through
parent_path = "~/Downloads"
#describes how many folders you want the tool to check starting from most recent
num_files = 50

#converts the ~ into the expanded path
parent_path = os.path.expanduser(parent_path)

#the path to the created folder
folder_path = parent_path + "/" + folder_name

#creates new folder, if it already exists, pass
try:
    os.mkdir(folder_path)
except FileExistsError:
    pass

i = 0

#iterating over the files in the parent_path
for filename in sorted(os.listdir(parent_path), reverse=True):
    if i > num_files:
        #only checks the most recent num_files amount of folders
        break
    if (os.path.isdir(parent_path + "/" + filename)):
        if filename == folder_name:
            #this is the folder where we want the files to end up, so there is no need to move them from here
            pass
        else:
            #move files with the given suffix from this folder to folder_path
            for childfilename in os.listdir(parent_path + "/" + filename):
                if "." in childfilename and childfilename[childfilename.index("."):] == suffix:
                    print("Found .pak file " + childfilename)
                    os.rename(parent_path + "/" + filename + "/" + childfilename, folder_path + "/" + childfilename)
            i = i + 1