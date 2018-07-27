#!/bin/bash

if [ $# > 0 ]
then
    case "$1" in
        "جمع")
        if [ $# == 2 ]
        then
            python3 init.py "$2"
        else
            echo "ملف مفقود"
        fi
        ;;
        "نفذ")
        if [ $# == 2 ]
        then
            python3 "$2.py"
        else
            echo "ملف مفقود"
        fi
        ;;
        "حول")
        echo "القلب هو لغة برمجة"
        echo "إنه مفتوح المصدر"
        ;;
        *)
        echo $1 "خيار غير معترف بها"
        ;;
    esac
else
    echo "من فضلك ادخل الخيار"
fi
