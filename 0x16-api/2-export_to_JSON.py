#!/usr/bin/python3
""" Export data in JSON """
import json
import requests
from sys import argv


if __name__ == "__main__":
    """ Func Def """
    dict_list = []
    employee_dict = {}

    url = "https://jsonplaceholder.typicode.com/"
    tasks = requests.get(url + "todos?userId=" + argv[1])
    tasks = tasks.json()
    user = requests.get(url + "users/" + argv[1])
    user = user.json()
    USER_ID = user.get("id")
    username = user.get("username")

    for item in tasks:
        json_dict = {}
        json_dict["username"] = username
        json_dict["task"] = item["title"]
        json_dict["completed"] = item["completed"]
        dict_list.append(json_dict)

    employee_dict[argv[1]] = dict_list
    file = argv[1] + ".json"
    with open(file, 'w', encoding="utf-8") as json_file:
        dump = json.dumps(employee_dict)
        json_file.write(dump)
