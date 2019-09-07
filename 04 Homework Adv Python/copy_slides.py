import os
import shutil
import fnmatch
import glob

def stu_activities(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    
    copyList = result

    for f in copyList:
        shutil.copy(f, 'ClassSlides')
    print(result)            
    return result


    

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
    

stu_activities('*.pdf', 'GT-ATL-CYBER-PT-08-2019-E-C-GEDigital')


