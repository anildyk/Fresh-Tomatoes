import fresh_tomatoes
import media

toy_story_3 = media.Movie("Toy Story 3 ",
                        " With their beloved Andy preparing to leave for college, Woody (Tom Hanks), Buzz Lightyear (Tim Allen), Jessie (Joan Cusack), and the rest of the toys find themselves headed for the attic but mistakenly wind up on the curb with the trash",
                        "http://resizing.flixster.com/Tv9f7mIJrCc--JvPXl60rMI3Pkw=/180x266/dkpu1ddg7pbsk.cloudfront.net/movie/11/13/43/11134356_ori.jpg",
                        "https://www.youtube.com/watch?v=ZZv1vki4ou4")
avatar = media.Movie("Avatar",
                     "On the lush alien world of Pandora live the Na'vi, beings who appear primitive but are highly evolved",
                     "http://resizing.flixster.com/OPDpDBP1P_qiiOjKOW9042R4R3g=/180x270/dkpu1ddg7pbsk.cloudfront.net/movie/11/17/67/11176792_ori.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
tomorrowland = media.Movie("Tomorrowland",
                           "Whenever Casey Newton (Britt Robertson) touches a lapel pin with the letter T on it, she finds herself transported to Tomorrowland, a city filled with huge robots and sleek buildings",
                           "http://resizing.flixster.com/dH2TEhqdJ5A6xxV3mQBPZ_1yEac=/180x267/dkpu1ddg7pbsk.cloudfront.net/movie/11/19/06/11190666_ori.jpg",
                           "https://www.youtube.com/watch?v=lWZ7O-RrATY")
interstellar = media.Movie("Interstellar",
                           "In Earth's future, a global crop blight and second Dust Bowl are slowly rendering the planet uninhabitable. Professor Brand (Michael Caine), a brilliant NASA physicist, is working on plans to save mankind by transporting Earth's population to a new home via a wormhole",
                           "http://resizing.flixster.com/l9yjA-72sZMYECeOjx-r14mgXtU=/180x270/dkpu1ddg7pbsk.cloudfront.net/movie/11/19/08/11190860_ori.jpg",
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")
transfers_4 = media.Movie("Transformers: Age of Extinction",
                          "After an epic battle, a great city lies in ruins, but the Earth itself is saved. As humanity begins to pick up the pieces, a shadowy group emerges to try to take control of history. Meanwhile, an ancient and powerful new menace sets its sights on Earth",
                          "http://resizing.flixster.com/jXWcxIKVUq4G-2vl7aClbKnOXr4=/180x270/dkpu1ddg7pbsk.cloudfront.net/movie/11/18/05/11180556_ori.jpg",
                          "https://www.youtube.com/watch?v=r8HPIH5JCak")
dawn_of_the_planet_of_the_apes = media.Movie("Dawn of the Planet of the Apes",
                                             "Ten years after simian flu wiped out much of the world's homosapiens, genetically enhanced chimpanzee Caesar (Andy Serkis) and his ever-growing band of followers have established a thriving colony just outside San Francisco in Muir Woods. Meanwhile, a small band of human survivors emerges, which forces Caesar -- as leader -- to grapple with the dual challenge of protecting his people and re-establishing a relationship with the remaining human population -- the latter being Caesar's secret wish",
                                             "http://resizing.flixster.com/gDtbA1iPxTYEjBZeSsIYktCtUiw=/180x270/dkpu1ddg7pbsk.cloudfront.net/movie/11/18/91/11189194_ori.jpg",
                                             "https://www.youtube.com/watch?v=3sHMCRaS3ao")
movies = [toy_story_3,avatar,tomorrowland,interstellar,transfers_4,dawn_of_the_planet_of_the_apes]
fresh_tomatoes.open_movies_page(movies)
