#!/bin/sh

sed -i 's/debug=True/debug=False/' dispatch.py

appcfg.py update .

git checkout dispatch.py