# This script is being used to keep a track record of files.
# It's purpose is to keep a date and time record of when a file is uploaded, and how many times a file has been downloaded

# Currently I am confused whether I should use a sqlite database, an excel file, or a simple plain spacce seperated text file.
# 
# 
# I think that this script will not be a stand alone script and will later have to be merged with some other program.

import os, time



f = open('main_directory_path.txt', 'r')
main_dir_path = f.read()
print(main_dir_path)


# One solution that I have found online is that I can refresh and get an updated list every 10-20 seconds of the ls command. 
# Then I can compare the two obtained lists of files to see if there is any changes

print(os.listdir(main_dir_path))

before = dict ([(f, None) for f in os.listdir (main_dir_path)])

while 1:
    time.sleep(20)
    after = dict ([(f, None) for f in os.listdir (main_dir_path)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]
    if added: print("Added: ", ", ".join (added))
    if removed: print("Removed: ", ", ".join (removed))
    before = after
    break



# The above code prints out the new file added or a file removed. This is an active code, and it runs actively in the background. 

# The code to maintain an sqlite database for file history etc will be maintained below.



