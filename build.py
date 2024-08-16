#!/usr/bin/python3

def read_file(path: str):
    with open(path, 'r') as file:
        return file.read()

def build_index():
    system = [
        "system/widgets",
        "system/taskbar",
    ]

    apps = [
        "apps/browser",
        "apps/terminal",
    ]

    ui = read_file("src/system/ui.html")
    start = read_file("src/system/start.html")

    menu_button = '<button id="@@APP_NAME" class="btn-some morp">@@APP_NAME</button>'
    menu_items = ""
    windows = ""

    for path in apps:
        name = path.replace("apps/", "").capitalize()
        component = read_file(f"src/{path}.html")
        component = component.replace("@@APP_NAME", name)
        item = menu_button.replace("@@APP_NAME", name)
        menu_items = f"{menu_items}\n{item}\n"
        windows = f"{windows}\n{component}\n"

    start_menu = start.replace("@@MENU_ITEMS", menu_items)

    for path in system:
        component = read_file(f"src/{path}.html")
        name = path.replace("system/", "")
        ui = ui.replace(f"@@{name.upper()}", component)

    ui = ui.replace("@@START", start_menu)
    index = ui.replace("@@APPS", windows)

    with open('src/index.html', 'w') as file:
        file.write(index)
        file.close()

build_index()
