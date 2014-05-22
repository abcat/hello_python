#-*-coding:utf8-*-
import textwrap
import pickle
import os


todos = []
def create_todo(todos, title, description, level):
    todo = {"title": title,
            "description": description,
            "level": level}
    todos.append(todo)
    return ("Successed add %s todo item" %(title))

def todo_sort_order(todos):
    important = [todo for todo in todos
            if todo["level"].lower() == "important"]
    medium = [todo for todo in todos
            if todo["level"].lower() != "important" and
            todo["level"].lower() != "unimportant"]
    unimportant = [todo for todo in todos
            if todo["level"].lower() == "unimportant"]
    sorted_todo = important + medium + unimportant
    return sorted_todo

def wrap_text(todo, index):
    wraped_title = textwrap.wrap(todo["title"], 16)
    wraped_descr = textwrap.wrap(todo["description"], 24)

    output = str(index + 1).ljust(8)
    output += wraped_title[0].ljust(16) + "  "
    output += wraped_descr[0].ljust(24) + "  "
    output += todo["level"].ljust(16)
    output += "\n"

    max_len = max(len(wraped_title), len(wraped_descr))

    for index in range(1, max_len):
        output += " " * 8
        if index < len(wraped_title):
            output += wraped_title[index].ljust(18)
        else:
            output += " " * 18
        if index < len(wraped_descr):
            output += wraped_descr[index].ljust(26)
        else:
            output += " " * 26
        output += "\n"
    return output


def show_todos(todos):
    output = "Item".ljust(8) + "Title".ljust(18) + \
            "Description".ljust(26) + "Level".ljust(16)
    output += "\n"
    sorted_todo = todo_sort_order(todos)
    for index, todo in enumerate(sorted_todo):
        # line = str(index + 1).ljust(8)
        # for key, length in [("title", 16),
        #                     ("description", 24),
        #                     ("level", 16)]:
        #     line += str(fields[key]).ljust(length)
        # output += line
        # output += "\n"
        output += wrap_text(todo, index)
    return output

def save_todo_list():
    save_file = file("todo.pickle", "w")
    pickle.dump(todos, save_file)
    save_file.close()

def load_todo_list():
    global todos
    if os.access("todo.pickle", os.F_OK):
        save_file = file("todo.pickle")
        todos = pickle.load(save_file)


def get_input(fields):
    user_input = {}
    for field in fields:
        user_input[field] = raw_input(field + ">")
    return user_input

def get_function(command):
    return commands[command][0]

def get_field(command):
    return commands[command][1]

def test(todos, abcd, hijk):
    return "Command 'test' returns:\n" + \
            "abcd:" + abcd + "\nhijk:" + hijk

def run_command(user_input, data=None):
    user_input = user_input.lower()
    if user_input not in commands:
        return user_input + "?" + "I don't know what that command is"
    else:
        the_func = get_function(user_input)

    if data is None:
        the_fields = get_field(user_input)
        data = get_input(the_fields)
    return the_func(todos, **data)

commands = {
            "new": [create_todo, ["title", "description", "level"]],
            "test": [test, ["abcd", "hijk"]],
            "show":[show_todos, []]
            }

def mainloop():
    user_input = ""
    load_todo_list()
    while True:
        print run_command(user_input)
        user_input = raw_input(">")
        if user_input.lower().startswith("quit"):
            print("Exit")
            break
    save_todo_list()

if __name__ == '__main__':
    mainloop()
