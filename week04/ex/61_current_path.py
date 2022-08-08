def current_path():
    import os
    cwd = os.getcwd()
    return str(cwd)



print(current_path())