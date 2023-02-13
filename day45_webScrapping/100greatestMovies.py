import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

movies_webpage = response.text

sp = BeautifulSoup(movies_webpage, "html.parser")

# the <h3> tag doesn't show up in the soup. So I decided to grab the alt of the images: the name of the movies is there.
images = sp.find_all(name = "img")

# we need to get rid of so many amazon logos...
movies_list = [image["alt"] for image in images if image["alt"] != "Amazon"]

# and then we need to drop the first image (of The God Father) and the last 3: Facebook, Twitter and Pinterest:
# new_list = [old_list[i] for i, e in enumerate(old_list) if i not in pos]
ml = movies_list[1:101]

# challenge requires list in ascending order, page is in descending order:
ml.reverse()

with open("HundredGreatestMovies.txt", "w") as file1:
    for i in ml:
        file1.write(f"{i}\n")


