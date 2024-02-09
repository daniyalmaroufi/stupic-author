import csv
import os

from configs import *

class StupidAuthor:

    def __init__(self) -> None:
        self.stories = []
        self.genres = {}
        self.import_genres()

    def import_genres(self):
        for genre in GENRES:
            try:
                with open(GENREPATH + genre + ".csv", "r") as file:
                    genre_keywords = []
                    csv_reader = csv.DictReader(file, delimiter=',')
                    for row in csv_reader:
                        genre_keywords.append(row)
                    
                    self.genres[genre] = genre_keywords
            except:
                print("Error importing genre keywords. Please check keyword files.")

    def import_story(self, filename: str) -> None:
        story_name = filename.replace('.txt', '')
        
        if(not os.path.isfile(filename)):
            print("File not found.")
            return
        
        try:
            with open(filename, "r") as file:
                story = file.read().split()
                self.stories.append((story_name, story))
                print(f"{story_name} imported successfully.")

        except:
            print("Error importing the story.")

