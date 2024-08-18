#!/usr/bin/python3
import os

def read_file(path: str) -> str:
    with open(path, 'r') as file:
        return file.read()


def create_app(app_name: str):
    base_path = f"src/apps/{app_name}"
    files = [
        f"{base_path}/{app_name}.html",
        f"{base_path}/scripts/app.{app_name}.js",
        f"{base_path}/styles/app.{app_name}.css",
    ]

    for file_path in files:
        directory = os.path.dirname(file_path)
        os.makedirs(directory, exist_ok=True)
        with open(file_path, 'w') as file:
            file.write("")

    print("Done!")

def read_files_paths(path: str) -> list:
    try:
        files = os.listdir(path)
        return files
    except FileNotFoundError as err:
        print(f"error {err}")
        return []

def mount_scripts(scripts: list) -> str:
    html_script = ""
    for sc in scripts:
        html_script = f'<script src="{sc}"></script>'
    return html_script

def mount_styles(scripts: list) -> str:
    html_css = ""
    for st in scripts:
        html_css = f'<link href="{st}" rel="stylesheet" />'
    return html_css


def build_index():
    system = [
        "system/widgets",
        "system/taskbar",
    ]

    apps = [
        "apps/browser",
        "apps/terminal",
        "apps/editor",
    ]

    ui = read_file("src/system/ui.html")
    start = read_file("src/system/start.html")

    menu_button = '''
    <script>
        $(document).ready(function () {
        $("#@@APP_NAME-btn").click(function () {
            $("#@@APP_NAME").toggle();
        });
        });
    </script>
    <button id="@@APP_NAME-btn" class="btn-some morp">@@APP_NAME</button>
    '''
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

def build():
    pass

create_app("desktop")
create_app("browser")
create_app("terminal")
create_app("editor")
