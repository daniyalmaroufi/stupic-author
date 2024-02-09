import csv

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
