#!/usr/bin/bash

# dependencies 
sudo yum install -y libffi-devel zlib-devel bzip2-devel readline-devel \
 sqlite-devel wget curl llvm ncurses-devel openssl-devel lzma-sdk-devel redhat-rpm-config 

# pyenv
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
echo '
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
' >> ~/.bashrc
source ~/.bashrc

pyenv install 2.7.17
pyenv install 3.7.4
	
# pyenv-virtualenv 
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv  

yum install -y python-virtualenv python-pip python3-pip

#
make environments
pyenv virtualenv 2.7.17 
pyenv virtualenv 3.7.4 

virtualenv --prompt="2.7.17" venv2.7
virtualenv --prompt="3.7.4" venv3.7
