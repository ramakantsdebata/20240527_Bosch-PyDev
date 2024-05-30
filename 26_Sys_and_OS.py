#!/usr/bin/env py
import sys
import os

def run_sys():
    print("Printing the args to the script:")
    for index, arg in enumerate(sys.argv):
        print(f"{index}\t{arg}")

    # if sys.argv[0] != r"./26_Sys_and_OS.py":
    #     print("Full auth not granted")

    print("\nModule search path (sys.path)")
    for path in sys.path:
        print(f"{path}")

    print(f"\nVersion : {sys.version}")

def run_OS():
    current_dir = os.getcwd()
    print(f"\nCurrent Working Directory - {current_dir}")

    # Create a new dir
    new_dir = os.path.join(current_dir, 'demo_dir')
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
        print(f"\nCreated 'demo_dir' directory at '{new_dir}'")
    else:
        print(f"\n'demo_dir' already exists at '{new_dir}'")

    print("\nFiles and folders in the current directory:")
    for item in os.listdir(current_dir):
        print(item)

    # Create a new file in the demo dir
    new_file_path = os.path.join(new_dir, 'demo_file.txt')


    # # Option 1
    # file = open(new_file_path, 'w')
    # file.write("This is a demo file")
    # file.close()

    # Option 2
    with open(new_file_path, 'w') as file:
        file.write("This is a demo file")



    print(f"\nThe demo file 'demo_file.txt' has been created at '{new_file_path}'.")

    # Check if the file exists
    if os.path.exists(new_file_path):
        print(f"\n File 'demo_file.txt' exists at {new_file_path}.")
    else:
        print(f"File not found at {new_file_path}.")

    # Remove the file
    os.remove(new_file_path)
    print(f"\nThe file 'demo_file.txt' has been removed from {new_file_path}.")

    # Remove directory
    os.rmdir(new_dir)
    print(f"\nThe folder 'demo_dir' has been removed from {new_dir}.")

if __name__ == "__main__":
    run_sys()
    run_OS()