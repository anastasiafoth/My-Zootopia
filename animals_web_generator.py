import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data("animals_data.json")

def print_data(data):
    output = ""
    for animal in data:
        name = animal.get("name")
        diet = animal.get("characteristics").get("diet")
        location = animal.get("locations")[0]
        type_ = animal.get("characteristics").get("type")

        if name:
            output += f"Name: {name}\n"

        if diet:
            output += f"Diet: {diet}\n"

        if location:
            output += f"Location: {location}\n"

        if type_:
            output += f"Type: {type_}\n"

        output += "\n"
    return output


def load_html(file_path):
    with open(file_path, "r") as file:
        return file.read()


output = print_data(animals_data)
html = load_html("animals_template.html")

html = html.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals_template.html", "w") as file:
    file.write(html)

