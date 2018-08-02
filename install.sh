#!/usr/bin/env bash

# Removing existing installation
rm -r $HOME/qalblang

# Creating directory
mkdir $HOME/qalblang
mkdir $HOME/qalblang/bin
mkdir $HOME/qalblang/qalb

# Copying file to the directory
cp -r bin/* $HOME/qalblang/bin
cp -r qalb/* $HOME/qalblang/qalb
cp start.py $HOME/qalblang

# Renaming file
mv $HOME/qalblang/bin/qalb.sh $HOME/qalblang/bin/قلب
chmod +x  $HOME/qalblang/bin/قلب