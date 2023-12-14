This code defines a simple in-memory file system through a Python class called InMemoryFileSystem. It provides a command-line interface (CLI) to interact with the virtual file system. 
Users can perform operations like creating directories, navigating through directories, listing contents, searching for patterns in files, displaying file contents, creating and modifying
files, moving or copying files, and deleting files or directories.

1. Class InMemoryFileSystem:

	Attributes:

		current_directory: Represents the current working directory in the virtual file system.
		in_memory_files: A dictionary to store the content of files in memory.
	Methods:

		mkdir: Creates a new directory.
		cd: Changes the current directory.
		ls: Lists the contents of a directory.
		grep: Searches for a pattern in a file (bonus command).
		cat: Displays the contents of a file.
		touch: Creates a new empty file.
		echo: Writes text to a file.
		mv: Moves a file or directory.
		cp: Copies a file or directory.
		rm: Removes a file or directory.

2. Function print_help:
	Prints a help message displaying the available commands.

3. Function main:
	Initializes an instance of InMemoryFileSystem.
	Enters a loop to repeatedly accept user input.
	Parses user input to execute the corresponding file system command.
	Handles errors and provides appropriate messages.
	Exits the loop when the user enters "exit."

4. Execution:
	The script runs the main function if executed as the main program.

5. Command-line Interface:
	Users interact with the file system through a command-line interface by typing commands like mkdir, cd, ls, etc.

6. Usage:
	Users can perform various file system operations by entering commands in the console.
