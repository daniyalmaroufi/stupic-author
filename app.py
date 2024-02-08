#!python3

from StupidAuthor import StupidAuthor


if __name__ == '__main__':
    app = StupidAuthor()
    
    while True:
        command = input().split()
        if command[0] == 'exit':
            break
        elif command[0] in app.COMMANDS:
            app.handle_command(command)
        else:
            print("Command not found. See the list of commands with show_the_list_of_commands.")

