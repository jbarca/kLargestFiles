# Author: Jacob Barca
# Since: 14/12/2019
# Last Modified: 14/12/2019

#TODO: Search sub-directories in the folder provided
# to achieve maximum functionality

import sys
import os

def main():
    num_arguments = len(sys.argv) - 1
    if num_arguments == 0 or num_arguments == 1 or num_arguments > 2:
        print ("Usage: python klargestfiles.py <DIRECTORY_TO_SEARCH> <NUM_LARGEST_FILES>")
    else:
        get_largest_files(sys.argv[1], int(sys.argv[2]))

def get_largest_files(directory, k):
    # Check if directory is valid
    if not os.path.isdir(directory):
        print("Invalid directory specified. Quitting.")
        return

    files = []
    # Get all files in directory
    for f in os.listdir(directory):
        file_path = os.path.join(directory, f)
        if os.path.isfile(file_path):
            files.append([f, os.path.getsize(file_path)])

    # Sort based on file size
    files.sort(key=lambda x: x[1], reverse=True)

    # Print the k largest files (or len(files) if k > len(files))
    for i in range(min(len(files), k)):
        print(str(i + 1) + ". " + files[i][0] + " - " + str(files[i][1]) + " B")


main()