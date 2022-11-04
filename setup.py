import os
from pathlib import Path
def start():
  path = './env'
  if not os.path.exists(path):
      os.makedirs(path)
      os.system('python -m venv ./env')
      os.system('pip install -r requirements.txt')
start()

# print (str(Path.cwd()) + "\env\Scripts\\activate")
#file =str(Path.cwd()) + "\env\Scripts\\activate.bat"
#file = "/bin/bash --rcfile ./myScript.sh"
#os.system(file)
#activate_this = ".\env\Scripts\\activate.bat"
