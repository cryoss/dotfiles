#!/usr/bin/env bash

cd ~/dev/venv
source bin/activate
jupyter notebook --no-browser --NotebookApp.token='' --NotebookApp.password=''
