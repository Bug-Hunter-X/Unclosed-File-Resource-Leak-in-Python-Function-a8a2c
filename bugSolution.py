def function_with_closed_file(filename):
    try:
        file = open(filename, 'r')
        # ... some code that processes the file ...
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure file is closed even if exceptions occur
        if 'file' in locals() and file:  #Check if file exists before closing
            file.close()

function_with_closed_file('my_file.txt')
    