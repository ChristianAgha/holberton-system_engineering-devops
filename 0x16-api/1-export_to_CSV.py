#!/usr/bin/python3
""" Write data to a CSV file path """
import csv
import requests
from sys import argv


def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
        for line in data:
            writer.writerow(line)

if __name__ == "__main__":
    """ Func Def """
    tasks = []
    name = ""
    user_id = ""
    task_completed_status = ""
    req1 = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = req1.json()
    req2 = requests.get("https://jsonplaceholder.typicode.com/users")
    users = req2.json()

    for user in users:
        if int(user["id"]) == int(argv[1]):
            name = user["username"]

    for item in todos:
        if int(item["userId"]) == int(argv[1]):
            if item["completed"] is True:
                task_completed_status = 'True'
            else:
                task_completed_status = 'False'
            row = '{},{},{},{}'.format(argv[1], name,
                                       task_completed_status,
                                       item["title"])
            tasks.append(row.split(","))

    path = str(argv[1]) + ".csv"
    csv_writer(tasks, path)
