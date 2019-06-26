import sys
import subprocess
import json
import yaml
from pip._internal.utils.misc import get_installed_distributions

venv = subprocess.Popen(["pyenv", "version"], stdout=subprocess.PIPE)
r = venv.stdout.read().strip()
piploc = subprocess.Popen(["which", "pip"], stdout=subprocess.PIPE)
s = piploc.stdout.read()
ppath = subprocess.Popen(["echo", "$PYTHONPATH"], stdout=subprocess.PIPE)
p = ppath.stdout.read()

ipkg = {}
mr = get_installed_distributions()
for i in mr:
    t = str(i).split()
    ipkg.update({t[0]: t[1]})

f = open("syslog.json", "w")
prints = json.dumps({
    "Version of python": sys.version, #version of python
    "Name of virt.env.": str(r)[2:],    #virtual environment (name)
    "Python exec. location": sys.executable,  #python executable location
    "Pip location": str(s)[2:],  #pip location
    "Installed packeges": ipkg, #installed packages: name, version
    "Site-packages location": sys.path, #site-packages location
    "$PYTHONPATH": str(p)[2:] #pip location
}, indent=4)
f.write(prints)

f = open("syslog.yml", "w")
prinls = yaml.dumps({"Information: "
    "Version of python": sys.version, #version of python
    "Name of virt.env.": str(r)[2:],    #virtual environment (name)
    "Python exec. location": sys.executable,  #python executable location
    "Pip location": str(s)[2:],  #pip location
    "Installed packeges": ipkg, #installed packages: name, version
    "Site-packages location": sys.path, #site-packages location
    "$PYTHONPATH": str(p)[2:] #pip location
}, default_flow_style=False, indent=4)
f.write(prinls)
