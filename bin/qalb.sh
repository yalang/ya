#!/bin/bash

if [ $# > 0 ]; then
    if [ -s "$1.قلب" ];then
        python3 $HOME/qalblang/start.py "$1.قلب"
        python3 "$1.py"
    else
        echo "ملف مفقود"
    fi
else
    echo "من فضلك ادخل الخيار"
    echo "قلب <اسم الملف بلا .قلب>"
fi
