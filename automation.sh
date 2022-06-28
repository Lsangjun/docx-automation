#!/bin/sh

which -s brew
if [[ $? != 0 ]] ; then
    # Install Homebrew
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    break
fi

brew list python3 || brew install python3

pip3 install -r requirements.txt && python3 app.py

