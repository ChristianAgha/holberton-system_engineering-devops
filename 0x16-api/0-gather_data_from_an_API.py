#!/usr/bin/python3
""" Gather data from an API """
import json
import requests
from sys import argv


if __name__ == "__main__":
    """ Func Def """
    comp_task = 0
    total_tasks = 0
    tasks = []
    name = ""

    req1 = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = req1.json()
    req2 = requests.get("https://jsonplaceholder.typicode.com/users")
    users = req2.json()

    for user in users:
        if int(user["id"]) == int(argv[1]):
            name = user["name"]

    for item in todos:
        if int(item["userId"]) == int(argv[1]):
            if item["completed"] is True:
                tasks.append(item["title"])
                comp_task += 1
                total_tasks += 1
            else:
                total_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(
        name, comp_task, total_tasks))
    for task in tasks:
        print(task)
