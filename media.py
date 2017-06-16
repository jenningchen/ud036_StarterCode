import webbrowser


class Movie():

    """This class provides a way to store movie related information"""

# constructor for media object, initializes instance variables
# including movie_title, movie_storyline, poster_image, trailer_youtube
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# function show_trailer opens youtube trailer in a browser window
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
