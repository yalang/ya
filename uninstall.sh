#!/usr/bin/env bash

# Variable
PROJECT=ya
COMMAND=ya
COMMAND_AR=ي

# Removing existing installation
rm -rf $HOME/$PROJECT
rm -f /usr/local/bin/${COMMAND}
rm -f /usr/local/bin/${COMMAND_AR}
#if [ -f "/usr/local/bin/${COMMAND}" ];then
#    rm /usr/local/bin/${COMMAND}
#fi

#if [ -f "/usr/local/bin/${COMMAND_AR}" ];then
#    rm /usr/local/bin/${COMMAND_AR}
#fi
