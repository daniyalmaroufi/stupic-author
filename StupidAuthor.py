import csv
import os

from configs import *


class StupidAuthor:

    def __init__(self) -> None:
        self.stories = []
        self.genres = {}
        self.analyzed_stories = []
        self.import_genres()

    def import_genres(self):
        for genre in GENRES:
            try:
                with open(GENREPATH + genre + ".csv", "r") as file:
                    genre_keywords = []
                    csv_reader = csv.reader(file, delimiter=",")
                    line_count = 0
                    for row in csv_reader:
                        line_count += 1
                        if line_count == 1 or not row:
                            continue
                        genre_keywords.append((row[0], int(row[1])))

                    self.genres[genre] = genre_keywords
            except:
                print("Error importing genre keywords. Please check keyword files.")

    def import_story(self, filename: str) -> None:
        story_name = filename.replace(".txt", "")

        if not os.path.isfile(filename):
            print("File not found.")
            return

        try:
            with open(filename, "r") as file:
                story = file.read().split()
                self.stories.append((story_name, story))
                print(f"{story_name} imported successfully.")

        except:
            print("Error importing the story.")

    def analyze_story(self, story_index: int, output_file_name: str) -> None:
        story = self.stories[story_index]
        story_name = story[0]
        story = story[1]
        story_analysis = self.analyze(story)
        self.analyzed_stories.append((story_name, story_analysis))

        self.dump_analysis(story_name, story_analysis, output_file_name)
        print(
            f"The genre of the story {story_name} is {story_analysis['predictied_genre']}."
        )

    def analyze(self, story: list[str]) -> dict:
        genre_scores = {}
        genre_number_of_keywords = {}
        for genre in self.genres:
            genre_number_of_keywords[genre] = 0
            genre_scores[genre] = 0
            for keyword in self.genres[genre]:
                genre_number_of_keywords[genre] += story.count(keyword[0])
                genre_scores[genre] += story.count(keyword[0]) * keyword[1]
        predicted_genre = max(genre_scores, key=genre_scores.get)
        genre_confidence = {}
        for genre in genre_scores:
            genre_confidence[genre] = genre_scores[genre] / sum(genre_scores.values())

        common_keywords = self.find_common_keywords(story, predicted_genre)

        story_analysis = {
            "genre_number_of_keywords": genre_number_of_keywords,
            "genre_scores": genre_scores,
            "genre_confidence": genre_confidence,
            "predictied_genre": predicted_genre,
            "common_keywords": common_keywords,
        }
        return story_analysis

    def dump_analysis(
        self, story_name: str, story_analysis: dict, output_file_name: str
    ) -> None:
        with open(output_file_name, "w") as file:
            file.write(f"Story Name: {story_name}\n")
            file.write(f"Predicted Genre: {story_analysis['predictied_genre']}\n\n")
            file.write("Genre, Number of Keywords, Confidence\n")
            for genre in self.genres.keys():
                file.write(
                    f"{genre}, {story_analysis['genre_number_of_keywords'][genre]}, {story_analysis['genre_confidence'][genre]}\n"
                )
            file.write("The common keywords of the story are: ")
            for i, common_keyword in enumerate(story_analysis["common_keywords"]):
                if i < len(story_analysis["common_keywords"]) - 1:
                    file.write(f"{common_keyword[0]}, ")
                else:
                    file.write(f"{common_keyword[0]}.\n")

    def find_common_keywords(self, story: list[str], predicted_genre) -> list[tuple]:
        keywords_occurance = {}
        for keyword in self.genres[predicted_genre]:
            keywords_occurance[keyword[0]] = story.count(keyword[0])

        common_keywords = sorted(
            keywords_occurance.items(), key=lambda item: item[1], reverse=True
        )[:5]

        return common_keywords
