import data_fetcher


def serialize_animal(animal):
    output = ""
    name = animal.get("name", {})
    diet = animal.get("characteristics", {}).get("diet")
    location = animal.get("locations", [None])[0]
    type_ = animal.get("characteristics", {}).get("type")
    slogan = animal.get("characteristics", {}).get("slogan")
    color = animal.get("characteristics", {}).get("color")
    skin_type = animal.get("characteristics", {}).get("skin_type")

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


def return_data_based_on_user_input(user_input):
    output = ""
    animals_data = data_fetcher.load_data_from_api(user_input)

    if animals_data:
        for animal in animals_data:
            output += serialize_animal(animal)
    else:
        output += f"<p style='color: #b00;'><strong>Notice:</strong> The animal '{user_input}' doesn't exist.</p>"

    return output


def load_html(file_path):
    with open(file_path, "r") as file:
        return file.read()


def write_html(user_input, html):
    output = return_data_based_on_user_input(user_input)

    html = html.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w") as file:
        file.write(html)


def main():

    while True:
        user_input = input("Enter a name of an animal: ").lower().strip()

        if user_input.isdigit():
            print("Please enter a string!")
        elif not user_input:
            print("Input shouldn´t be empty!")
        else:
            break

    html = load_html("animals_template.html")
    write_html(user_input, html)
    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()