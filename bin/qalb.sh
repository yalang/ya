#!/bin/bash

if [ $# > 0 ]; then
    if [ -f "$1.قلب" ];then
        python3 $HOME/qalblang/start.py "$1.قلب"
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
