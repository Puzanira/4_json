# Prettify JSON

Simple console script to look at .json file

### What it does:

Opens a raw .json file and then prints it in your 
 terminal with spaces and indentations in an _easy-to-read_ way
  

### How to use:

Example of script **launch** on Linux, Python 3.5:

```bash

$ python pprint_json.py <path to file>
```
**Raw JSON file:**
```json
{"employees":[{ "firstName":"John", "lastName":"Doe" },{ "firstName":"Anna", "lastName":"Smith" }]}
```

**Output:**
```json
{
    "employees": [
        {
            "firstName": "John",
            "lastName": "Doe"
        },
        {
            "firstName": "Anna",
            "lastName": "Smith"
        }
    ]
}

```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
