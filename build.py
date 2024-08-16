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

    ui = read_file("/src/system/ui")
    apps = ""

    for path in apps:
        name = path.replace("apps/", "").capitalize()
        component = read_file(f"src/{path}.html")
        component = component.replace("@@APP_NAME", name)
        app = f"{component}\n\n"


    for path in system:
        component = read_file(f"src/{path}.html")
        name = path.replace("system/", "")
        ui.replace(f"@@{name.upper}", component)

    index = ui.replace("@@APPS", apps)

    with open('src/index.html', 'rw') as file:
        file.write(index)
        file.close()

    print(len(index))


build_index()
