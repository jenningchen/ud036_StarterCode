import fresh_tomatoes
import media

# multiple instances of the Movie class
inception = media.Movie("Inception",
                        "A man who plants ideas in the subconscious",
                        "http://www.impawards.com/2010/posters/inception_xlg.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")

zootopia = media.Movie("Zootopia",
                       "A planet of animals with a mystery to be solved",
                       "http://www.impawards.com/2016/posters/zootopia_xlg.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=jWM0ct-OLsM")

la_la_land = media.Movie("La La Land",
                         "A musical romance between two aspiring entertainers",
                         "https://images-na.ssl-images-amazon.com/images/I/61pVLV%2Bz11L._AC_UL320_SR216,320_.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=0pdqf4P9MB8")

whiplash = media.Movie("Whiplash",
                       "A young drummer enters conflict with his instructor",
                       "http://i.wp.pl/a/f/film/008/64/81/0408164.jpg",
                       "https://www.youtube.com/watch?v=7d_jQycdQGo")

wonder_woman = media.Movie("Wonder Woman",
                           "A sheltered Amazon princess leaves her home"
                           "to end a raging war",
                           "http://cdn1-www.comingsoon.net/assets/uploads/gallery/wonder-woman/wwpost345.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=1Q8fG0TtVAY")

sing_street = media.Movie("Sing Street",
                          "A high-schooler in Dublin forms a band to"
                          "impress a girl he likes",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEzODA3MDcxMl5BMl5BanBnXkFtZTgwODgxNDk3NzE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=C_YqJ_aimkM")


# list of Movie instances
movies = [inception, zootopia, la_la_land, whiplash, wonder_woman, sing_street]

# open webpage
fresh_tomatoes.open_movies_page(movies)

