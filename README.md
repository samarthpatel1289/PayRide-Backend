# PayRide PreRequisite. 

# Installing Pyenv : Python Version Manager
```
brew install pyenv
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
exec "$SHELL"
pyenv install 3.9.1
```

# Installing Pyenv-virtualenv : Pyenv VirtualEnv manager
```
brew install pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
```

# Creating Virtualenv name ride. 
```
pyenv virtualenv 3.9.1 ride
```

# Activating virtualenv
```
source activate ride
```

# Installing Requirements 
```
pip3 install -r requirements.txt
```

# Migrating Database
```
python3 manage.py makemigrations
python3 manage.py migrate
```

# Running Server
```
python3 manage.py runserver
```
