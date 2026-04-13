#--------------------------------------------------------
# Project name: Rule-Drive
# Version: 1.0
#--------------------------------------------------------


# Questions about why I use these libraries
#--------------------------------------------------------
'''
Why do I use the "os" library? 

Answer: The "os" library is used for interacting with the operating system. 
It provides functions for creating, removing, and changing directories, 
as well as for handling file paths and environment variables. 
In this project, it may be used to manage file and directory operations, 
such as creating folders for storing data or accessing files needed for the rule-driven system.


Why do I use the "shutil" library? 

Answer: The "shutil" library is used for high-level file operations, such as copying, moving, and deleting files, 
and directories. It provides a more convenient and portable way to perform these operations compared to using 
the "os" library directly.


Why do I use the "time" library? 

Answer: The "time" library is used for handling time-related operations, such as measuring the execution time of code 
blocks or formatting timestamps. In this project, it may be used to track the performance of rule evaluation or to log 
events with timestamps.
'''
#--------------------------------------------------------


# How the code works:
#--------------------------------------------------------
'''
1. The script starts by importing the necessary libraries: "os" for file and directory operations, "shutil" for 
high-level file operations, and "time" for handling time-related functions.

2. The main function "organize_files" is defined, which takes a target directory as an argument. 
This function contains a dictionary called "file_rules" that defines the rules for organizing files based on their 
extensions.

3. The function checks if the target directory exists. If it does not exist, it prints a message and returns.

4. The function iterates through the files in the target directory. For each file, it checks if it is 
a file (not a directory) and retrieves its extension.

5. The function then iterates through the defined file rules and checks if the file extension matches any of the 
extensions in the rules. If a match is found, it creates the destination folder if it does not exist and moves the file 
to the appropriate folder based on its extension.

6. If no rule matches the file extension, it prints a message indicating that no rule was found for the file.

7. The script includes an entry point that prompts the user to enter the folder path to organize and calls 
the "organize_files" function with the provided path.

8. The script uses time.sleep() to introduce delays between operations, which can help in observing the file 
organization process in real-time.

9. Overall, the script is designed to help users organize their files in a specified directory based on predefined rules 
for file extensions, making it easier to manage and access files.
'''
#--------------------------------------------------------


# Import libraries
#--------------------------------------------------------
import os
import shutil
import time
#--------------------------------------------------------


# Main function to organize files based on predefined rules
#--------------------------------------------------------
def organize_files(target_directory):
    file_rules = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Archives': ['.zip', '.rar', '.7z'],
        'Scripts': ['.py', '.js', '.html', '.css']
    }

    # Check if the target directory exists
    if not os.path.exists(target_directory):
        print("The path does not exist.")
        return
    
    # Iterate through files in the target directory and move them based on the defined rules
    for filename in os.listdir(target_directory):
        filepath = os.path.join(target_directory, filename)

        # Check if the path is a file (not a directory) before processing
        if os.path.isfile(filepath):
            file_ext = os.path.splitext(filename)[1].lower()

            moved = False

            # Iterate through the file rules and move the file to the appropriate folder based on its extension
            for folder, extensions in file_rules.items():
                time.sleep(1)

                # Check if the file extension matches any of the extensions defined in the rules
                if file_ext in extensions:
                    dest_folder = os.path.join(target_directory, folder)
                    
                    os.makedirs(dest_folder, exist_ok=True)
                    
                    # Move the file to the destination folder
                    shutil.move(filepath, os.path.join(dest_folder, filename))
                    print(f"Moved {filename} to {folder}")
                    moved = True
                    time.sleep(2)
                    break

            # If no rule matches the file extension, print a message indicating that no rule was found for the file
            if not moved:
                print(f"No rule found for file: {filename}")


# Entry point of the script
if __name__ == "__main__":
    # Prompt the user to enter the folder path to organize and call the organize_files function with the provided path
    path_to_clean = input("Enter the folder path to organize: ")
    organize_files(path_to_clean)
#--------------------------------------------------------
