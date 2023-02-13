 # from bs4 import BeautifulSoup
# # import lxml

# with open("website.html", "r") as file1:
#     website_content = file1.read()

# soup = BeautifulSoup(website_content, "html.parser") # could use lxml.parser too

# # print(soup.title)
# # print(soup.title.string)

# # print(soup)
# # print(soup.prettify())

# # print(soup.p) # gets hold of the first <p>

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))


# print(soup.find(name = "h3", class_ = "heading")) # class_ to avoid error due to clashing with the reserved word class.

# # CSS selector can be used:

# print(soup.select_one(selector = "p a")) # this is the only a that sits inside a p.
# print(soup.select_one(selector = ".heading")) # class selector
# print(soup.select(selector = "#name")) # id selecto

# ---------------- Read a real site ----------------
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

article_texts = [tag.string for tag in soup.select(".titleline a")]

article_links = [tag.get("href") for tag in soup.select(".titleline a")]

article_upvote = [tag.string for tag in soup.find_all(name = "span", class_ = "score")]

article_upvote = [int(i.split(" ")[0]) for i in article_upvote]

most_upvoted_article = article_upvote.index(max(article_upvote))
print(article_texts[most_upvoted_article])
print(article_links[most_upvoted_article])
