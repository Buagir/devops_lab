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
    "Version of python": sys.version,
    "Name of virt.env.": str(r)[2:],
    "Python exec. location": sys.executable,
    "Pip location": str(s)[2:],
    "Installed packeges": ipkg,
    "Site-packages location": sys.path,
    "$PYTHONPATH": str(p)[2:]
}, indent=4)
f.write(prints)

f = open("syslog.yml", "w")
prinls = yaml.dumps({"Information: "
    "Version of python": sys.version,
    "Name of virt.env.": str(r)[2:],
    "Python exec. location": sys.executable,
    "Pip location": str(s)[2:],
    "Installed packeges": ipkg,
    "Site-packages location": sys.path,
    "$PYTHONPATH": str(p)[2:]
}, default_flow_style=False, indent=4)
f.write(prinls)
