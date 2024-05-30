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
    

run_sys()