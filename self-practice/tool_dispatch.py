# A pretend filesystem: no actual files are read or changed.
files = {
    "hello.txt": "hello",
    "course.txt": "The harness executes the tool.",
}


def read_file(path):
    try:
        with open(path, encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: file not found: {path}"


# Map tool names (strings) to executable Python functions.
tools = {
    "read_file": read_file,
}


def dispatch(request):
    """Select and execute the requested tool."""
    name = request["name"]

    if name not in tools:
        return f"Error: unknown tool: {name}"

    function = tools[name]
    arguments = request["arguments"]

    # For example: read_file(path="hello.txt")
    return function(**arguments)


# Scripted requests stand in for requests from a model.
# This exercise tests dispatch; it doesn't call a model.
requests = [
    {
        "name": "read_file",
        "arguments": {"path": "hello.txt"},
    },
    {
        "name": "read_file",
        "arguments": {"path": "course.txt"},
    },
    {
        "name": "read_file",
        "arguments": {"path": "missing.txt"},
    },
    {
        "name": "delete_file",
        "arguments": {"path": "hello.txt"},
    },
]


for number, request in enumerate(requests, start=1):
    result = dispatch(request)
    print(f"{number}. {result}")


# Expected output:
# 1. hello
# 2. I am learning tool dispatch.
# 3. Error: file not found: missing.txt
# 4. Error: unknown tool: delete_file
