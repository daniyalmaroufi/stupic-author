#!python3
from StupidAuthor import StupidAuthor
from configs import *

class CLI:
    COMMANDS = (
        "show_the_list_of_commands",
        "import_story",
        "show_the_list_of_stories",
        "analyze_story",
        "analyzed_stories_list",
        "show_story_analysis",
        "dump_analyzed_stories",
        "exit",
        "find_the_first_character",
    )

    def __init__(self) -> None:
        self.stupid_author = StupidAuthor()

    def run(self) -> None:
        while True:
            command = input().split()
            if command[0] == "exit":
                break
            self.handle_command(command)

    def handle_command(self, command: list[str]) -> None:
        if command[0] == "show_the_list_of_commands":
            self.show_the_list_of_commands()
        elif command[0] == "import_story":
            self.import_story(command)
        elif command[0] == "show_the_list_of_stories":
            self.show_the_list_of_stories()
        elif command[0] == "analyze_story":
            self.analyze_story()
        elif command[0] == "analyzed_stories_list":
            self.analyzed_stories_list()
        elif command[0] == "show_story_analysis":
            self.show_story_analysis()
        elif command[0] == "dump_analyzed_stories":
            self.dump_analyzed_stories()
        elif command[0] == "find_the_first_character":
            self.find_the_first_character()
        else:
            print(
                "Command not found. See the list of commands with show_the_list_of_commands."
            )

    def show_the_list_of_commands(self) -> None:
        for command in self.COMMANDS:
            print(command)

    def import_story(self) -> None:
        self.stupid_author.import_story()


if __name__ == "__main__":
    app = CLI()
    app.run()