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
    skin_type = animal.get("characteristics").get("skin_type")

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

    if skin_type:
        output += f"<li class='list_enumeration'><strong>Skin Type:</strong> {skin_type}</li>\n"

    output += '</ul>\n</div>\n </li>\n'
    return output


def skin_types_in_list(data):
    skin_types_list = []
    for animal in data:
        skin_type = animal.get("characteristics").get("skin_type")
        if skin_type and skin_type not in skin_types_list:
            skin_types_list.append(skin_type)
    return skin_types_list


def return_data_based_on_skin_type(skin_type_input):
    output = ""

    for animal in animals_data:
        if skin_type_input == animal.get("characteristics").get("skin_type").lower():
            output += serialize_animal(animal)
    return output


def load_html(file_path):
    with open(file_path, "r") as file:
        return file.read()


def write_html(skin_type_input):
    output = return_data_based_on_skin_type(skin_type_input)

    html = load_html("animals_template.html")
    html = html.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals_template.html", "w") as file:
        file.write(html)


def main():
    skin_types_list = skin_types_in_list(animals_data)
    skin_types_as_string = ", ".join(skin_types_list)

    while True:
        skin_type_input = input(f"Here are the skin types of foxes: \n{skin_types_as_string}\nPlease enter one: ").lower().strip()
        if skin_type_input.isdigit():
            print("Please enter a string!")
        elif not skin_type_input:
            print("Input shouldn´t be empty!")
        elif skin_type_input:
            for skin_type in skin_types_list:
                if skin_type.lower() == skin_type_input:
                    break
            else:
                print("Skin type not found!")

            break

    write_html(skin_type_input)


if __name__ == "__main__":
    main()