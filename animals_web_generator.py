import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

def print_data(data):

    for animal in data:
        name = animal.get("name")
        diet = animal.get("characteristics").get("diet")
        location = animal.get("locations")[0]
        type_ = animal.get("characteristics").get("type")
        if name:
            print(f"Name: {name}")

        if diet:
            print(f"Diet: {diet}")

        if location:
            print(f"Location: {location}")

        if type_:
            print(f"Type: {type_}")

        print()


print_data(animals_data)
