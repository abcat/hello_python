#-*-coding:utf-8-*-
#!/usr/bin/env python
import todo


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

if __name__ == '__main__':
    test_create_todo()
    test_get_function()
    test_get_field()
    test_run_command()
