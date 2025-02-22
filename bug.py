def function_with_unclosed_file(filename):
    try:
        file = open(filename, 'r')
        # ... some code that processes the file ...
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    # This is the bug: the file is not closed even if an error occurs
    # ... more code that might also raise exceptions ...

function_with_unclosed_file('my_file.txt')