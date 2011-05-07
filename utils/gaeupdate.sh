#!/bin/sh
EMAIL=

sed -i 's/debug=True/debug=False/' dispatch.py

appcfg.py $EMAIL update .

git checkout dispatch.py
