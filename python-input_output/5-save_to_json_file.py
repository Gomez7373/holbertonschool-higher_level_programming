#!/usr/bin/python3

def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be written to the file.
        filename (str): The name of the file to write to.

    """
    import json

    with open(filename, 'w') as file:
        json.dump(my_obj, file)
