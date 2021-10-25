class Song:
    def __init__(self, title, author, lyrics):  # constructor method called upon creation of object
        #         # we add everything that we want done when we first create object from our class blueprints

        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(f"New Song made {title} by {author}")

    def sing(self, ):
        #print(f"{self.title} by {self.author}: {self.lyrics}")
        self.do_lyrics(self.lyrics)
        return self

    def yell(self, ):
        capital_lyrics = self.lyrics.upper()
        self.do_lyrics(capital_lyrics)
        return self

    def do_lyrics(self, lyrics):
        print(lyrics)



new_song = Song("Habits", "Ed Sheeran", "My bad habits lead to you")
new_song.sing()
new_song.yell()