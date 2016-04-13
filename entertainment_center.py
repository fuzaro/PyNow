import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys",
                        "https://pt.wikipedia.org/wiki/Ficheiro:Movie_poster_toy_story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "https://pt.wikipedia.org/wiki/Ficheiro:Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=aVdO-cx-McA")
#print(avatar.storyline)
#avatar.show_trailer()
movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)
