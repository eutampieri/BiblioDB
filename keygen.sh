#!/bin/sh
python randomkey.py
gcc key.c
rm key.c
mv a.out jsonvalidator.out
chmod +x jsonvalidator.out
rm randomkey.py