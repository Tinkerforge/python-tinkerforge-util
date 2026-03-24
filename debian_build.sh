#!/bin/sh -e
python prepare.py
dpkg-buildpackage --no-sign
