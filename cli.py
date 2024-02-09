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
            try:
                command = input()
                if not command:
                    continue
                command = command.split()
                if command[0] == "exit":
                    break
                self.handle_command(command)
            except EOFError:
                break
            except KeyboardInterrupt:
                break

    def handle_command(self, command: list[str]) -> None:
        if command[0] == "show_the_list_of_commands":
            self.show_the_list_of_commands()
        elif command[0] == "import_story":
            self.import_story(command)
        elif command[0] == "show_the_list_of_stories":
            self.show_the_list_of_stories()
        elif command[0] == "analyze_story":
            self.analyze_story(command)
        elif command[0] == "analyzed_stories_list":
            self.analyzed_stories_list()
        elif command[0] == "show_story_analysis":
            self.show_story_analysis(command)
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

    def import_story(self, command: list[str]) -> None:
        if len(command) < 2:
            print("import_story {story_name.txt}")
            return
        filename = command[1]
        self.stupid_author.import_story(filename)

    def show_the_list_of_stories(self) -> None:
        print("List of all imported stories:")
        for i, story in enumerate(self.stupid_author.stories):
            print(f"{i+1}. {story[0].capitalize()}")

    def validate_story_index(self, story_index: int) -> bool:
        if story_index < 0 or story_index >= len(self.stupid_author.stories):
            print("Invalid story index.")
            return False
        return True

    def analyze_story(self, command: list[str]) -> None:
        if len(command) < 3:
            print("analyze_story {story_index} {output_file_name.txt}")
            return
        story_index = int(command[1]) - 1
        if not self.validate_story_index(story_index):
            return

        self.stupid_author.analyze_story(story_index, command[2])

    def analyzed_stories_list(self) -> None:
        print(
            f"""The analyzed stories are: {
                ', '.join(
                    [
                        analyzed_story[0].capitalize() if i == 0 else analyzed_story[0] 
                        for (i, analyzed_story) in enumerate(self.stupid_author.analyzed_stories[:4])
                    ]
                )
            } and {self.stupid_author.analyzed_stories[-1][0]}."""
        )

    def show_story_analysis(self, command) -> None:
        if len(command) < 2:
            print("show_story_analysis {story_index}")
            return
        story_index = int(command[1]) - 1
        
        if not self.validate_story_index(story_index):
            return
        
        if not story_index in [item[-1] for item in self.stupid_author.analyzed_stories]:
            print("This story has not been analyzed yet. Please use the analyze_story command.")
            return
        
        story = next(
            (
                analyzed_story
                for analyzed_story in self.stupid_author.analyzed_stories
                if analyzed_story[2] == story_index
            ),
            None,
        )
        print(f"Story Name: {story[0]}")
        print(f"Predicted Genre: {story[1]['predictied_genre']}")
        print("Genre, Number of Keywords, Confidence")
        for genre in self.stupid_author.genres.keys():
            print(
                f"{genre}, {story[1]['genre_number_of_keywords'][genre]}, {story[1]['genre_confidence'][genre]}"
            )
        print("The common keywords of the story are: ", end="")
        for i, common_keyword in enumerate(story[1]["common_keywords"]):
            if i < len(story[1]["common_keywords"]) - 1:
                print(common_keyword[0], end=", ")
            else:
                print(common_keyword[0], end ='.\n')
        

if __name__ == "__main__":
    app = CLI()
    app.run()
