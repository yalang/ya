#!/bin/bash

if [ $# > 0 ]; then
    if [ -f "$1.قلب" ];then
        # Converting qalb to python
        python3 $HOME/qalblang/start.py "$1.قلب"
        # Removing any garbage file
        if [ -f "0" ];then
            rm "0"
        fi
        # Running python converted file
        if [ -f "$1.py" ];then
            python3 "$1.py"
        fi
    # For extension .qalb
    elif [ -f "$1.qalb" ];then
        # Converting qalb to python
        python3 $HOME/qalblang/start.py "$1.qalb"
        # Removing any garbage file
        if [ -f "0" ];then
            rm "0"
        fi
        # Running python converted file
        if [ -f "$1.py" ];then
            python3 "$1.py"
        fi
    # For extension .ql
    elif [ -f "$1.ql" ];then
        # Converting qalb to python
        python3 $HOME/qalblang/start.py "$1.ql"
        # Removing any garbage file
        if [ -f "0" ];then
            rm "0"
        fi
        # Running python converted file
        if [ -f "$1.py" ];then
            python3 "$1.py"
        fi
    else
        echo " ملف غير صالح $1"
    fi
else
    echo "من فضلك ادخل الخيار"
    echo "قلب <اسم الملف بلا .قلب>"
fi
