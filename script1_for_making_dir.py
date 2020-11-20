# This script is intended to be run only once and that too only at the beginning of starting with the application.

# This is strictly a one time run only script.

import os
import os.path
# The essesntial purpose of this script is to take the user's name, email and other detailed information when the user accesses the application for the first time. It creates a text file with that name.
# Then every time it checks the text file for that details. If those details does not exists or if the file has been deleted, then it again asks for the information.
# It also creates a directory with the name the user provides.




# This is a function to print logs, directories and setup logs. I have commented this because I will be making a seperate script for this
# def log_files():
#     # print(os.getcwd())
#     current_directory = os.getcwd()
#     print(current_directory)



def making_new_directory():
    current_directory = os.getcwd()
    # User name is taking as the input to create an initial directory to store files. A feature will be added to it as well to allow users to create more internal directories.
    user_name = input('Enter the name of the directory you want to make ')


    # This commented command can also be used instead of adding \\  as string
    # print(os.path.join(current_directory, user_name))
    # Now I have to cheack for and create a new directory if it doesn't exist
    current_directory = current_directory + str("\\") + user_name + str("\\")
    # This will be the new path of the directory
    print(current_directory)

    # Now I have to check whether this path exists
    does_directory_exists = os.path.isdir(current_directory)
    print(does_directory_exists)
    
    # The variable does_directory_exists is a boolean variable
    if does_directory_exists == False:
        print('A directory has been created')
        os.mkdir(current_directory)
        print('Your file directory has been created at the location', current_directory)





making_new_directory()