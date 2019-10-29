import platform
import os
import sys
import pkg_resources
import json
import yaml
from distutils.sysconfig import get_python_lib

python_info = {}
python_info['version'] = platform.python_version()
python_info['path'] = os.environ['PYTHONPATH']

if 'VIRTUAL_ENV' in os.environ:
    python_info['virtual environment'] = os.environ['VIRTUAL_ENV']
else:
    python_info['virtual environment'] = 'None'

python_info['executable location'] = sys.executable
python_info['site-packages location'] = get_python_lib()
python_info['pip location'] = get_python_lib() + '/pip'

installed_packages = {}
print(pkg_resources.working_set)
for d in pkg_resources.working_set:
    installed_packages[d.project_name] = d.version


python_info['installed packages'] = installed_packages

with open('pyinfo.json', 'w') as json_file:
    json.dump(python_info, json_file, indent=4)

with open('pyinfo.yml', 'w') as outfile:
    yaml.dump(python_info, outfile, default_flow_style=False)