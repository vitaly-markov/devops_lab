#!/usr/bin/bash

# dependencies
yyum install -y libffi-devel zlib-devel bzip2-devel readline-devel sqlite-devel wget llvm ncurses-devel openssl-devel lzma-sdk-devel epel-release redhat-rpm-config  vim wget git

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
#
make environments
pyenv virtualenv 2.7.17 PyEnv2.7
pyenv virtualenv 3.7.4 PyEnv3.7

pyenv activate PyEnv3.7

