# Deploy

Create Instance

SSH

## Dependencies

```
apt-get update && \
apt-get install -y build-essential && \
apt-get install -y git && \
apt-get install -y libprotobuf-dev && \
apt-get install -y libssl-dev && \
apt-get install -y software-properties-common && \
add-apt-repository ppa:deadsnakes/ppa && \
apt-get install -y python3.11 && \
apt-get install -y python3-pip
```

### Virtual Env Wrapper

`pip3 install virtualenv virtualenvwrapper`

Make Virtual env directory

`mkdir ~/.virtualenvs`

Find paths for python

`which virtualenv` -> [VENV_PATH]
`which virtualenvwrapper.sh` -> [VENV_WRAPPER_PATH]
`which python3` -> [PYTHON_PATH]

Add Virtual Env to paths

`sudo nano ~/.zshrc` # Mac OS
`sudo nano ~/.bashrc` # Ubuntu

Add following paths:

Where you see `VENV_PATH` and `PYTHON_PATH` you want to insert the result from the  `which` command.

```
# Configuration for virtualenv
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=[PYTHON_PATH]
export VIRTUALENVWRAPPER_VIRTUALENV=[VENV_PATH]
source [VENV_WRAPPER_PATH]
```

Add Changes to system

`source ~/.zshrc` # Mac OS
`source ~/.bashrc` # Ubuntu

### Supervisord

`sudo apt-get install supervisor`

`service supervisor restart`

```
[program:xrpl-gpt3]
directory=/home/dangell/xrpl-gpt3
command=/bin/bash -c  'source /home/dangell/.virtualenvs/xrpl-gpt3/bin/activate && python3 main.py'
autostart=true
autorestart=true
```

`sudo supervisorctl reread && sudo supervisorctl update`

`supervisorctl`