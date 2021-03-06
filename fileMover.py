import os, shutil

def MoveFiles():
    print("Your path MUST be full path and follow the format - SOME_DISK:/some_folder/srcORdestFolder/ ")
    source, dest = input("Enter src path first and then dest path using space: ").split()
    ListOfFiles = os.listdir(source) #restuns a list of files located at source.
    counter = 0
    FilesToBeMoved = [] 
    MostUsedExtensions = ('avi', 'ai', 'csv', 'doc', 'docx',  
                          'gif', 'htm', 'html', 'jpg', 'jpeg', 
                          'mp3', 'mp4','mov', 'pdf', 'ppt',     
                          'pptx', 'png', 'psd', 'rar', 'svg',
                          'txt', 'wma', 'xlsx', 'zip', '7z')

    for extensions in MostUsedExtensions: print(extensions) 

    ext = input("What kind of file would you like to move?")
    if ext in MostUsedExtensions:
        ext = "." + ext
        for files in ListOfFiles:
            if files.endswith(ext): 
                counter += 1
                FilesToBeMoved.append(files)
        print(f'---There are {counter} files ready to be moved---\n',FilesToBeMoved)
        MoveOrNotToMove = input(str('Do you want to move the above files to destination folder?\n(y/n)'))
    else: 
        print("The file extension provided is not supported.")


    if MoveOrNotToMove == "y" or MoveOrNotToMove == "Y":
        for junk in FilesToBeMoved:
            shutil.move(source + junk, dest)
            print(junk, 'was moved to the destination folder.') 
    elif MoveOrNotToMove == "n" or MoveOrNotToMove == "N":      
        print("Files were not modified.")
    else:
        print("Invalid input.")
