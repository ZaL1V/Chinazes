import subprocess
import minecraft_launcher_lib


version = input('Введіть версію')
username = input('')
minecraft_directory=minecraft_launcher_lib.utils.get_minecraft_directory().replace('minecraft', '.chinazes')

minecraft_launcher_lib.install.install_minecraft_version(versionid=version, minecraft_directory=minecraft_directory)

options = {
    'username': username,
    'uuid': '',
    'token': ''
}

subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version=version, minecraft_directory=minecraft_directory, options=options))