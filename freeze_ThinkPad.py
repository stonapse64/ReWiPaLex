# Convenience routine to freeze the requirements @ ThinkPad
import subprocess
subprocess.run("pip freeze > requirements_ThinkPad.txt", shell=True, check=True)

# To rebuild the environment use
# subprocess.run("pip install -r requirements_ThinkPad.txt", shell=True, check=True)