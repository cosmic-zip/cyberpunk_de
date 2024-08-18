#!/usr/bin/python3
import os


def read_file(path: str) -> str:
    with open(path, "r") as file:
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
        with open(file_path, "w") as file:
            file.write("")

    print("Done!")


def read_files_paths(path: str) -> list:
    try:
        files = os.listdir(path)
        return files
    except FileNotFoundError as err:
        print(f"error {err} {path}")
        return []


def build_apps() -> str:
    # List all apps
    app_list = read_files_paths("src/apps/")

    # Open app boxed container
    app_container = read_file("src/system/app.html")
    final_app_list = ""
    for app in app_list:

        ## Build JS tags
        html_script = ""
        scripts = read_files_paths(f"src/apps/{app}/scripts")
        for sc in scripts:
            file_content = read_file(f"src/apps/{app}/scripts/{sc}")
            html_script = f"{html_script}<script>\n{file_content}\n</script>\n"

        ## Build window buttons
        html_script = f"{html_script}<script>\n{read_file('src/system/window_toggle.js')}\n</script>\n"

        ## Build CSS tags
        html_css = ""
        styles = read_files_paths(f"src/apps/{app}/styles")
        for st in styles:
            file_content = read_file(f"src/apps/{app}/styles/{st}")
            html_css = f"{html_css}<style>\n{file_content}\n</style>\n"

        app_content = read_file(f"src/apps/{app}/{app}.html")

        final_app = app_container.replace("@@APP_CONTAINER", app_content)
        final_app = final_app.replace("@@APP_SCRIPTS", html_script)
        final_app = final_app.replace("@@APP_STYLES", html_css)
        final_app = final_app.replace("@@APP_NAME", app)

        final_app_list = f"{final_app_list}\n{final_app}\n"

    return final_app_list


def build_base_window() -> str:
    window = read_file("src/system/ui.html")

    fixed_items = [
        f'<script>\n{read_file("src/scripts/jquery.js")}\n</script>\n',
        f'<script>\n{read_file("src/scripts/ui.js")}\n</script>\n',
        f'<style>\n{read_file("src/styles/ui.css")}\n</style>\n',
        f'<style>\n{read_file("src/styles/apps.css")}\n</style>\n',
    ]

    final_fixed_items = ""
    for item in fixed_items:
        final_fixed_items = f"{final_fixed_items}{item}\n"

    return window.replace("@@FIXED_ITEMS", final_fixed_items)


def build_desktop() -> str:

    app_list = read_files_paths("src/apps/")
    desktop = read_file("src/system/ui.html")

    ## Build start menu
    start_menu = read_file("src/system/start.html")
    start_menu_item = read_file("src/system/start_items.html")
    menu_items = ""
    for app_name in app_list:
        menu_btn = start_menu_item.replace("@@APP_NAME", app_name)
        menu_items = f"{menu_items}{menu_btn}\n"

    ## Build start_menu
    final_start_menu = start_menu.replace("@@MENU_ITEMS", menu_items)
    desktop = desktop.replace("@@START", final_start_menu)

    ## Build taskbar
    taskbar = read_file("src/system/taskbar.html")
    desktop = desktop.replace("@@TASKBAR", taskbar)

    ## Build apps
    apps = build_apps()
    desktop = desktop.replace("@@APPS", apps)

    return desktop


def build_cyberpunk_desktop() -> str:
    try:
        desktop = build_desktop()
        with open("src/index.html", "w+") as file:
            file.write(desktop)
            file.close()
        return "done"

    except Exception as err:
        print(f"$$$ ERROR :: {err}")
        return "error"


print(build_cyberpunk_desktop())
