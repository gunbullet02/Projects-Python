from bs4 import BeautifulSoup

with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

tags = doc.find_all(["option"],text = "Undergraduate")

print(tags)