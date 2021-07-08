# File Mover

# Description
Suppose a user has many files of a specific extension but he or she does not have time to move all those files manually. This program lets the user specify three things. Source and destination folders, and the file extension of files that are going to be moved. 
# Structure of the Project

## Variables
There are seven variables described below...__
"**source**" - the source folder where the files at. (SOME_DISK:/some_folder/srcFolder/)__
"**dest**" - the destination folder where files will be moved to. (SOME_DISK:/some_folder/destFolder/)__
"**counter**" - displays how many files were in the source folder based on 'ext' value.__
"**FilesToBeMoved**" - an empty list where we put the files that will be moved to new location.__
"**MostUsedExtensions**" - a tuple with most used extensions based on Windows OS.__
"**ext**" - an extension user passes to move specific files from MostUsedExtensions tuple, i.e. jpg, csv, pdf, etc.  

## The "ext" block
This part of a program asks what kind of files a user wants to move. After the user provided the source and destinations folders, a column of supported extensions will be printed to let the user pick one to work with the files. For instance, a user wants to move a bunch of images, so he will choose between 'jpg, 'jpeg or 'png' extensions. Then, the script will check how many files ends with the specified extension and display those files. The user will then be asked if he wants to move the files by passing 'y' or 'n' from the keyboard. If 'y' is passed, the files will move to destination folder. If 'n' is passed, nothing will happen, files stay at source folder and program stops. 

## The "move" block
If the user passed 'y' in the above part, program iterates on 'FilesToBeMoved' list and move all the files to destination folder. The moved files will be displayed.

# Technical Notes
The script was written on **Python 3.9.5** using **shutil** and **os** modules. 
The code was tested on **Windows 10** Home, version **21H1**, build 19043.1083. 
The code was **NOT** tested on Linux/Mac operating systems, so the feedback from users on those platforms would be appreciated. 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
