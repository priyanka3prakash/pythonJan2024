import json
from pprint import pprint, pp

book = {}
book["title"] = "Python Programming Essentials"
book["tags"] = ("Python", "Programming")
book["published"] = True
book["comment_link"] = None
book["author"] = "Udhay"
book["id"] = 786

# print(book)
# pprint(book)

pp(book)
print("type(book) is ", type(book))



# Serilazation
with open("ebook.json", "w") as f:
    json.dump(book, f, indent=2)
    f.close()


# De-serialization
print("\ndeserializing the json data \n")
with open("ebook.json", "rb") as g:
    data = json.load(g)
    g.close()

# print("data = ", data)
pp(data)


# Assignemnt ; try to work with json.load and json.dumps- json.loads