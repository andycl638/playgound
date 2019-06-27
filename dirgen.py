import os

def generate_dir(directory_structure):
    """
    Generate a 5 level nested directory structure
    """

    import shutil
    #items = directory_structure.items()

    #for key, value in items:
    #    print(key, value)

    folderlvl3 = "Lvl3 folder"
    folderlvl3num = 16
    folderlvl4 = "lvl4 folder"
    folderlvl4num = 16
    folderlvl5 = "lvl5 folder"
    folderlvl5num = 6

    """
    Creating initial directory structure that will be copied for other directories
    5 levels
    """
    initDir = os.path.join(folderlvl3 + str(1), folderlvl4 + str(1))
    os.makedirs(initDir)
    folderlvl3num -= 1
    print(folderlvl3num)
    folderlvl4num -= 1
    print(folderlvl4num)

    for num in range(1, folderlvl5num+1):
        print(num)
        os.makedirs(os.path.join(folderlvl3 + str(1), folderlvl4 + str(1), folderlvl5 + str(num)))

    """
    Copy initial directory structure to level 4 directory
    """
    for num in range(2, folderlvl4num + 2):
        print(num)
        shutil.copytree(initDir, os.path.join(folderlvl3 + str(1), folderlvl4 + str(num)))

    for num in range(2, folderlvl3num + 2):
        print(num)
        shutil.copytree(folderlvl3 + str(1), folderlvl3 + str(num))

def generate_dir_list(foldernum):
    file = open("directory list", "w")

    for num in range(1, foldernum+1):
        for root, dirs, files in os.walk('Lvl3 folder' + str(num), topdown=False):
            for name in dirs:
                print(os.path.join(root, name))
                file.write(os.path.join(root, name) + '\n')

    file.close()

if __name__ == '__main__':
    directory_structure = {"lvl3" : 16, "lvl4" : 16, "lvl5" : 6}
    #generate_dir(directory_structure)
    generate_dir_list(16)



('Folder1 Lvl5', 'Folder2 Lvl5', 'Folder3 Lvl5', 'Folder4 Lvl5', 'Folder5 Lvl5', 'Folder6 Lvl5')
