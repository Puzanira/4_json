import json
import sys


def load_from_json(filepath):
    
# в официальной документации python сказано, что with open действует аналогично блоку
# try fiinally, и также выкинет ошибку, если его не существует
# проверка уже встроена, ничего не сломается

    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def pretty_print_json(json_data):
    print(json.dumps(json_data, indent=4, ensure_ascii = False))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("Error: define file path")
        print ("Usage example: python pprint_json.py <path to file>")
    else:
        json_data = load_from_json(sys.argv[1])
        pretty_print_json(json_data)
