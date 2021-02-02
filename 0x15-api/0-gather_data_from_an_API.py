#!/usr/bin/python3
""" For a given employee ID, returns information about TODO list progress """
from requests import get
from sys import argv


if __name__ == "__main__":
    total_tasks = 0
    completed_tasks = 0
    task_list = []
    user = get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(argv[1])).json()
    url = "https://jsonplaceholder.typicode.com/todos"
    for task in get(url).json():
        if user["id"] == task["userId"]:
            total_tasks += 1
            if task["completed"] is True:
                task_list.append(task["title"])
                completed_tasks += 1
    print("Employee {} is done with tasks({}/{}):".format(
        user["name"], completed_tasks, total_tasks))
    for title in task_list:
        print("\t {}".format(title))
