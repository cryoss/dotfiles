#!/usr/bin/env bash


if [ $# -eq 0 ]

then
        echo "Missing options!"
        echo "(run $0 -h for help)"
        echo ""
        exit 0
fi

ECHO="false"
while getopts "dt" OPTION; do
    case $OPTION in
        t)cd ~/dev/tensor
          source bin/activate
          jupyter notebook --no-browser --NotebookApp.token='' --NotebookApp.password='' &
          ;;
        d)cd ~/dev/venv
          source bin/activate
          jupyter notebook --no-browser --NotebookApp.token='' --NotebookApp.password='' &
          ;;
    esac
done
