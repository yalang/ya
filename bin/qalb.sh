#!/bin/bash

if [ $# > 0 ]; then
    if [ $# == "جمع" ]; then
        if [ $# == 2 ]; then
            python3 $HOME/qalblang/start.py "$2"
        else
            echo "ملف مفقود"
        fi
    elif [ $# == "نفذ" ]; then
        if [ $# == 2 ]; then
            python3 "$2.py"
        else
            echo "ملف مفقود"
        fi
    elif [ $# == "حول" ]; then
        echo "القلب هو لغة برمجة"
        echo "إنه مفتوح المصدر"
    else
        if [ -s "$1.قلب" ];then
            python3 $HOME/qalblang/start.py "$1.قلب"
            python3 "$1.py"
        else
            echo "ملف مفقود"
        fi
    fi
else
    echo "من فضلك ادخل الخيار"
    echo "قلب <اسم الملف بلا .قلب>"
    echo "قلب جمع <اسم الملف مع .قلب>"
    echo "قلب نفذ <اسم الملف مع .قلب>"
    echo "قلب حول"
fi
