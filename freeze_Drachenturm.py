# Convenience routine to freeze the requirements @ Drachenturm
import subprocess
subprocess.run("pip freeze > requirements_Drachenturm.txt", shell=True, check=True)

# To rebuild the environment use
# subprocess.run("pip install -r requirements_Drachenturm.txt", shell=True, check=True)