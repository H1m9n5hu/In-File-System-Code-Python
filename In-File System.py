import os
import re
import shutil

class InMemoryFileSystem:

    def __init__(self):
        self.current_directory = os.getcwd()
        self.in_memory_files = {}

    def mkdir(self, directory_name):
        new_directory_path = os.path.join(self.current_directory, directory_name)
        os.makedirs(new_directory_path, exist_ok=True)

    def cd(self, path="."):
        if path == "/":
            self.current_directory = os.path.expanduser("~")
        elif path == "~":
            self.current_directory = os.path.expanduser("~")
        elif path == "..":
            self.current_directory = os.path.dirname(self.current_directory)
        else:
            new_directory_path = os.path.join(self.current_directory, path)
            if os.path.exists(new_directory_path) and os.path.isdir(new_directory_path):
                self.current_directory = new_directory_path
            else:
                print(f"Directory not found: {new_directory_path}")

    def ls(self, path="."):
        if path == ".":
            path = self.current_directory
        elif path.startswith("/"):
            path = path
        else:
            path = os.path.join(self.current_directory, path)

        if os.path.exists(path):
            if os.path.isdir(path):
                print(f"\nContents of Directory: {path}")
                print("Files:")
                for file_name in os.listdir(path):
                    print(f"  {file_name}")
                print("Directories:")
                for dir_name in os.listdir(path):
                    dir_path = os.path.join(path, dir_name)
                    if os.path.isdir(dir_path):
                        print(f"  {dir_name}")
            else:
                print(f"\nContents of File: {path}")
                with open(path, 'r') as file:
                    print(file.read())
        else:
            print(f"Path not found: {path}")

    def grep(self, pattern, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                content = file.read()
                matches = re.findall(pattern, content)
                print(f"Matches in {file_path}: {matches}")
        else:
            print(f"File not found: {file_path}")



    # Add this method to your InMemoryFileSystem class
    def cat(self, *args):
        for file_path in args:
            file = self._get_file_by_path(file_path)
            if file:
                print(f"\nContents of {file_path}:\n{file.content}")
            else:
                print(f"File not found: {file_path}")


    def cat(self, file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"\n{file_path}:\n{content}")

    def touch(self, file_path):
        new_file_path = os.path.join(self.current_directory, file_path)
        open(new_file_path, 'w').close()

    def echo(self, text, file_path):
        with open(file_path, 'w') as file:
            file.write(text)

    def mv(self, source_path, destination_path="."):
        source_path = os.path.join(self.current_directory, source_path)
        destination_path = os.path.join(self.current_directory, destination_path)

        if os.path.exists(source_path):
            shutil.move(source_path, destination_path)
        else:
            print(f"Error: Source path '{source_path}' not found.")


    def cp(self, source_path, destination_path="."):
        source_path = os.path.join(self.current_directory, source_path)
        destination_path = os.path.join(self.current_directory, destination_path)
        if os.path.exists(source_path):
            if os.path.isdir(source_path):
                shutil.copytree(source_path, destination_path)
            else:
                shutil.copy2(source_path, destination_path)
        else:
            print(f"Source not found: {source_path}")

    def rm(self, path):
        path = os.path.join(self.current_directory, path)
        if os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)
        else:
            print(f"Path not found: {path}")


def print_help():
    print("\nCommands:")
    print("mkdir <directory_name> - Create a new directory.")
    print("cd [<path>] - Change the current directory.")
    print("ls [<path>] - List the contents of the current or specified directory.")
    print("grep <pattern> <file_path> - Search for a pattern in a file. (Bonus command)")
    print("cat <file_path> - Display the contents of a file.")
    print("touch <file_path> - Create a new empty file.")
    print("echo <text> <file_path> - Write text to a file.")
    print("mv <source_path> <destination_path> - Move a file or directory.")
    print("cp <source_path> [<destination_path>] - Copy a file or directory.")
    print("rm <path> - Remove a file or directory.")
    print("exit - Exit the program.")


def main():
    file_system = InMemoryFileSystem()
    print("\nWelcome to the File System CLI!")
    print_help()

    while True:
        user_input = input("\n$ ")
        if user_input.lower() == "exit":
            print("Exiting the program. Goodbye!")
            break

        try:
            command, *args = user_input.split()
            if command == "mkdir":
                file_system.mkdir(*args)
            elif command == "cd":
                file_system.cd(*args)
            elif command == "ls":
                file_system.ls(*args)
            elif command == "grep":
                file_system.grep(*args)
            elif command == "cat":
                file_system.cat(*args)
            elif command == "touch":
                file_system.touch(*args)
            elif command == "echo":
                text = " ".join(args[:-1])
                file_system.echo(text, args[-1])
            elif command == "mv":
                file_system.mv(*args)
            elif command == "cp":
                file_system.cp(*args)
            elif command == "rm":
                file_system.rm(*args)
            elif command == "help":
                print_help()
            else:
                print(f"Command not recognized: {command}. Type 'help' for a list of commands.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
