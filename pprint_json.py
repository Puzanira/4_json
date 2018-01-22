import json
import sys
import os


def load_from_json(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def pretty_print_json(json_data):
    print(json.dumps(json_data, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Error: define file path')
        print('Usage example: python pprint_json.py <path to file>')
    else:
        if os.path.isfile(sys.argv[1]):
            json_data = load_from_json(sys.argv[1])
            pretty_print_json(json_data)
        else:
            print('Error: No such file in directory')

