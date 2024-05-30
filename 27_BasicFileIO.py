'''
Basic File I/O Methods

    open():
        Opens a file and returns a file object.
        Syntax: open(filename, mode)
        Common modes:
            'r': Read (default mode). Opens the file for reading.
            'w': Write. Opens the file for writing (and creates/truncates the file).
            'a': Append. Opens the file for appending (and creates the file if it doesn't exist).
            'b': Binary mode. Used with other modes for binary files (e.g., 'rb', 'wb').

    close():
        Closes an open file. It is important to close a file after finishing with it to free up system resources.
        Syntax: file.close()

    read():
        Reads the entire content of a file or a specified number of bytes.
        Syntax: file.read(size=-1)

    readline():
        Reads a single line from the file.
        Syntax: file.readline(size=-1)

    readlines():
        Reads all lines in a file and returns them as a list of strings.
        Syntax: file.readlines(hint=-1)

    write():
        Writes a string to the file.
        Syntax: file.write(string)

    writelines():
        Writes a list of strings to the file.
        Syntax: file.writelines(lines)

    flush():
        Flushes the internal buffer, ensuring all data is written to the file.
        Syntax: file.flush()

    seek():
        Moves the file cursor to a specified position.
        Syntax: file.seek(offset, whence=0)
        whence values:
            0: Absolute file positioning (default).
            1: Seek relative to the current position.
            2: Seek relative to the file's end.

    tell():
        Returns the current file cursor position.
        Syntax: file.tell()

    truncate():
        Truncates the file to a specified size.
        Syntax: file.truncate(size=None)

    with Statement (Context Manager):
        Ensures proper acquisition and release of resources, automatically closing the file.
        Syntax: with open(filename, mode) as file:
'''

# Open a file for writing
with open('example.txt', 'w') as file:
    file.write("Hello, world!\n")
    file.write("This is a file I/O demo.\n")

# Open the file for reading
with open('example.txt', 'r') as file:
    content = file.read()
    print("File content:")
    print(content)

# Append to the file
with open('example.txt', 'a') as file:
    file.write("Appending some text.\n")

# Read line by line
with open('example.txt', 'r') as file:
    print("Reading line by line:")
    for line in file:
        print(line, end='')

# Demonstrate seek and tell
with open('example.txt', 'r') as file:
    print("\nSeek and tell demonstration:")
    file.seek(0)  # Go to the beginning of the file
    print(f"Cursor position: {file.tell()}")
    print(f"First 5 characters: {file.read(5)}")
    print(f"Cursor position after reading 5 characters: {file.tell()}")
