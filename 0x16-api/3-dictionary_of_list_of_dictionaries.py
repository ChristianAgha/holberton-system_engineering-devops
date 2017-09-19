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
    tasks = requests.get(url + "todos")
    tasks = tasks.json()
    users = requests.get(url + "users/")
    users = users.json()

    for user in users:
        for item in tasks:
            if item["userId"] == user["id"]:
                json_dict = {}
                json_dict["username"] = user.get("username")
                json_dict["task"] = item["title"]
                json_dict["completed"] = item["completed"]
                dict_list.append(json_dict)
        employee_dict[user.get("id")] = dict_list
        dict_list = []
    file = "todo_all_employees.json"
    with open(file, 'w', encoding="utf-8") as json_file:
        dump = json.dumps(employee_dict)
        json_file.write(dump)
