#!/bin/sh

echo starting compilation..
touch ./.compiled.py
python3 translate.py $1
echo compiled

echo running
python3 ./.compiled.py
echo exit
# rm ./.compiled.py
