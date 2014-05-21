#-*-coding:utf8-*-

todos = []
def create_todo(todos, title, description, level):
    todo = {"title": title,
            "description": description,
            "level": level}
    todos.append(todo)

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
            "test": [test, ["abcd", "hijk"]]
            }

def mainloop():
    user_input = ""
    while True:
        print run_command(user_input)
        user_input = raw_input(">")
        if user_input.lower().startswith("quit"):
            print("Exit")
            break

if __name__ == '__main__':
    mainloop()
