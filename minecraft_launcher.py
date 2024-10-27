import os
import json
import shutil
import subprocess
import minecraft_launcher_lib
from PyQt5 import QtCore, QtGui, QtWidgets
from uuid import uuid1

def launch_minecraft(callback):
    from design import Ui_MainWindow
    minecraft_version = "1.12.2"
    forge_version = "1.12.2-14.23.5.2858"

    with open('options.json', 'r') as f:
        person_option = json.load(f)

    username = person_option['username']
    minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory().replace('minecraft', '.chinazes')
    custom_mods_path = os.path.join(os.path.dirname(__file__), "custom_mods_path")

    minecraft_launcher_lib.install.install_minecraft_version(versionid=minecraft_version, minecraft_directory=minecraft_directory, callback=callback )

    minecraft_launcher_lib.forge.install_forge_version(forge_version, minecraft_directory)

    mods_path = os.path.join(minecraft_directory, "mods")
    if not os.path.exists(mods_path):
        os.makedirs(mods_path) 

    for mod in os.listdir(custom_mods_path):
        mod_path = os.path.join(custom_mods_path, mod)
        if os.path.isfile(mod_path):
            shutil.copy2(mod_path, os.path.join(mods_path, mod))

    options = {
        'username': username,
        'uid': str(uuid1()),
        'token': '',
        'gameDirectory': minecraft_directory,
        'jvmArguments': ["-Duser.language=uk", "-Duser.country=UA", "-Duser.variant=UA"]
    }

    command = minecraft_launcher_lib.command.get_minecraft_command(
        version=f"1.12.2-forge-{forge_version.split('-')[1]}",
        minecraft_directory=minecraft_directory,
        options=options
    )

    subprocess.call(command)
