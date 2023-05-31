import yaml
# pyyaml
import os
import shutil

folders = []
#make fancy loop 
#
for file in os.scandir(os.path.dirname(os.path.abspath(__file__))):
    if file.is_dir():
        folders.append(file)
for folder in folders:
    #if its not renamed
    if folder.name.isdigit():

        with open(folder.name +'/docker-compose.yml', 'r') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            services = data['services']
            folder_name = "/"+next(iter(services))
            shutil.move(folder.path, os.path.split(folder.path)[0]+folder_name)
    