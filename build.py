#!/usr/bin/python3

def read_file(path):
    with open(path, 'r') as file:
        return file.read()

def build_index():
    system = [
        "system/widgets",
        "system/taskbar",
        "system/start",
    ]

    apps = [
        "apps/browser",
        "apps/terminal",
    ]

    ui = read_file("src/system/ui.html")
    windows = ""

    for path in apps:
        name = path.replace("apps/", "").capitalize()
        component = read_file(f"src/{path}.html")
        component = component.replace("@@APP_NAME", name)
        windows = f"{windows}\n\n{component}"


    for path in system:
        component = read_file(f"src/{path}.html")
        name = path.replace("system/", "")
        ui = ui.replace(f"@@{name.upper()}", component)
        # print(f"@@{name.upper()}", component)

    index = ui.replace("@@APPS", windows)

    with open('src/index.html', 'w') as file:
        file.write(index)
        file.close()

    # print(index)


build_index()
