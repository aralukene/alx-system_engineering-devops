#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    name = requests.get(f"{url}users/{sys.argv[1]}").json()
    tasks = requests.get(f"{url}users/{sys.argv[1]}/todos").json()
    c_tasks = [task for task in tasks if task.get("completed")]
    titles = [task.get("title") for task in tasks if task.get("completed")]
    
    print(f"Employee {name.get('name')} is done with tasks({len(c_tasks)}/{len(tasks)}):")
    for title in titles:
        print(f"\t{title}")
