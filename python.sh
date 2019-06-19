#!/bin/bash
#If your OS is CentOS ==> then install dependends packages
#sudo yum install zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel libffi-devel openssl-devel



curl -L https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
echo "export PATH=\"~/.pyenv/bin:$PATH\"" >> .bash_profile
echo "export PYENV_VIRTUALENV_DISABLE_PROMPT=1" >> .bash_profile
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
exec "$SHELL"
pyenv install 3.7.0
pyenv install 2.7.16
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
python get-pip.py
pip install virtualenv
pyenv local 2.7.16
pyenv virtualenv 2.7.16 2
pyenv local 3.7.0
pyenv virtualenv 3.7.0 3
