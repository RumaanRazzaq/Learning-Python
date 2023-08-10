# Write your solution here:
class Series:
    def __init__(self, title, season_no, genres) -> None:
        self.title = title
        self.season_no = season_no
        self.genres = genres
        self.ratings = []

    def rate(self, rating: int):
        self.ratings.append(rating)

    def average(self):
        if len(self.ratings) > 0:
            return sum(self.ratings) / len(self.ratings)
    
    def __str__(self) -> str:
        genre_string = ", ".join(self.genres)
        ratings_string = ""
        if len(self.ratings) == 0:
            ratings_string += "no ratings"
        else:
            ratings_string = f"{len(self.ratings)} ratings, average {sum(self.ratings) / len(self.ratings):.1f} points"
        string = f"{self.title} ({self.season_no} seasons)\ngenres: {genre_string}\n{ratings_string}"
        return string
    
def minimum_grade(rating: float, series_list: list):
    list = []
    for series in series_list:
        if series.average() >= rating:
            list.append(series)
    return list
    
def includes_genre(genre: str, series_list: list):
    list = []
    for series in series_list:
        for ser_genre in series.genres:
            if ser_genre == genre:
                list.append(series)
                break
    return list

if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        pass
        #print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        pass
        #print(series.title)