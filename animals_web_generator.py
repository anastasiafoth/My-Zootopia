import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data("animals_data.json")


def serialize_animal(animal):
    output = ""
    name = animal.get("name")
    diet = animal.get("characteristics").get("diet")
    location = animal.get("locations")[0]
    type_ = animal.get("characteristics").get("type")
    slogan = animal.get("characteristics").get("slogan")
    color = animal.get("characteristics").get("color")

    output += "<li class='cards__item'>\n"

    if name:
        output += f"<div class='card__title'>{name}</div>\n"

    output += "<div class='card__text'>\n<ul class='list_format'>\n"
    if diet:
        output += f"<li class='list_enumeration'><strong>Diet:</strong> {diet}</li>\n"

    if location:
        output += f"<li class='list_enumeration'><strong>Location:</strong> {location}</li>\n"

    if type_:
        output += f"<li class='list_enumeration'><strong>Type:</strong> {type_}</li>\n"

    if slogan:
        output += f"<li class='list_enumeration'><strong>Slogan:</strong> {slogan}</li>\n"

    if color:
        output += f"<li class='list_enumeration'><strong>Color:</strong> {color}</li>\n"

    output += '</ul>\n</div>\n </li>\n'
    return output

def print_data(data):
    output = ""
    for animal in data:
        # append information to string
        output += serialize_animal(animal)
    return output


def load_html(file_path):
    with open(file_path, "r") as file:
        return file.read()


output = print_data(animals_data)
html = load_html("animals_template.html")
html = html.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals_template.html", "w") as file:
    file.write(html)

