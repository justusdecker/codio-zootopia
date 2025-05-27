from json import load as jsload

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as file_in:
        return jsload(file_in)