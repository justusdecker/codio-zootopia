from modules.load_data import load_data

animals = load_data('animals_data.json')

if __name__ == '__main__':
    for animal in animals:

        name = animal["name"]
        diet = animal["characteristics"].get('diet',None)
        location = animal["locations"][0]
        ttype = animal["characteristics"].get('type',None)
        print(f'{name}\n{diet}\n{location}{"\n" + ttype if ttype is not None else ""}\n')