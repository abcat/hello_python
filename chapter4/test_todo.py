#-*-coding:utf-8-*-
#!/usr/bin/env python
import todo
import os

def test_create_todo():
    todo.todos = []
    todo.create_todo(todo.todos, title="Test title",
                description="This is a description of test",
                level="important")

    assert len(todo.todos) > 0, "Create failed, todos is zero"
    assert todo.todos[0]["title"] == "Test title"
    assert (todo.todos[0]["description"] ==
            "This is a description of test")
    assert todo.todos[0]["level"] == "important"
    print("Ok-create_todo.")


def test_get_function():
    assert todo.get_function("new") == todo.create_todo
    print("Ok-get_function.")

def test_get_field():
    assert (todo.get_field("new") ==
            ["title", "description", "level"])
    print("Ok-get_field")

def test_run_command():
    result = todo.run_command("test",
                {"abcd": "efgh", "hijk": "hlmk"})
    expected = """Command 'test' returns:
abcd:efgh
hijk:hlmk"""
    assert result == expected, result +"!=" + expected
    print("Ok-run_command")

def test_show_todos():
    todo.todos = [
            {"title": "test todo",
                "description": "This is a test",
                "level": "Important"
            }]
    result = todo.show_todos(todo.todos)
    lines = result.split("\n")

    first_line = lines[0]
    assert "Item" in first_line
    assert "Title" in first_line
    assert "Description" in first_line
    assert "Level" in first_line

    second_line = lines[1]
    assert "test todo" in second_line
    assert "This is a test" in second_line
    assert "Important" in second_line

    print("Ok-show_todos")

def test_todo_sort_order():
    """add three possible level, then sort using list comprehensions"""
    todo.todos = [
            {   "title": "Test unimportant todo",
                "description": "unimportant todo",
                "level": "unimportant"},
            {   "title": "Test medium todo",
                "description": "medium todo",
                "level": "medium"},
            {   "title": "Test important todo",
                "description": "important todo",
                "level": "important"}]

    result = todo.todo_sort_order(todo.todos)
    assert "important" in result[0]["level"]
    assert "medium" in result[1]["level"]
    assert "unimportant" in result[2]["level"]
    print("Ok-todo_sort_order")

def test_wrap_text():
    todo.todos = [{"title": "Test unimportant todo",
                "description": "unimportant todo with"
                " a very long description",
                "level": "unimportant"}]
    result = todo.wrap_text(todo.todos[0], 1)
    lines = result.split("\n")
    assert "Test unimportant" in lines[0]
    assert "todo" in lines[1]
    assert "unimportant todo with" in lines[0]
    assert "very long description" in lines[1]
    print("Ok-wrap_text")

def test_save_todo_list():
    todos_original = [{"title": "test todo",
        "description": "This is a test",
        "level": "Important"}]
    todo.todos = todos_original
    assert "todo.pickle" not in os.listdir(".")

    todo.save_todo_list()
    assert "todo.pickle" in os.listdir(".")

    todo.load_todo_list()
    assert todo.todos == todos_original
    os.unlink("todo.pickle")
    print("Ok-save_todo_list")

if __name__ == '__main__':
    test_create_todo()
    test_get_function()
    test_get_field()
    test_run_command()
    test_show_todos()
    test_todo_sort_order()
    test_wrap_text()
    test_save_todo_list()
