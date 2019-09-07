import os
import shutil
import fnmatch
import glob

def stu_activities(pattern, path):
    result = [] # Starting out with an empty list
    for root, dirs, files in os.walk(path):
        for name in dirs:
            if fnmatch.fnmatch(name, pattern): # Looking for the naming pattern
                result.append(os.path.join(root, name))
                # print(result)
    
    copyList = result # Now we have something in the list

    for f in copyList:
        # shutil.copytree(f, 'TextCopy')
        dir_copy(f, 'StuFolders') # Calling another function here
        #  copyDirectory(f,'TextCopy')
    print(result) # Something to show what the list is looking light to make sure we have data           
    return result


# Tried this function first but really didn't like the result I was getting
def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)
    

# This is the function that I decided to run with
def dir_copy(srcpath, dstdir):
    dirname = os.path.basename(srcpath)
    dstpath = os.path.join(dstdir, dirname)
    try:
        shutil.copytree(srcpath, dstpath)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)
    #  shutil.copytree(srcpath, dstpath)

# find('*.txt', '/')



    # dest_folder = os.mkdir("HWPYfiles")
    # folder_path = os.path.join("../../../../")
    # files = glob.iglob(os.path.join(folder_path, "*.py"))


    # for file in files:
    #     if os.path.isfile(file):
    #         shutil.copy(file, dest_folder)

    # The os.walk() function is used to navigate through a collection of folders/files
    # This function returns three values for each step it takes: root, dirs, and files.

    # for root, dirs, files in os.walk(folder_path):
    #     for file in files:
    #         if os.path.isfile(file):
    #             shutil.copy(file, "HWPYfiles")
    

stu_activities('*-Stu_*', 'GT-ATL-CYBER-PT-08-2019-E-C-GEDigital')

#  dir_copy("GT-ATL-CYBER-PT-08-2019-E-C-GEDigital", "TextCopy")


