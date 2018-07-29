# <:blue_heart:/> لغة القلب 

**_QALB_** Language is a completely open source programming language in which you can code in arabic language.

It is a [transcompiler](https://en.wiktionary.org/wiki/transcompiler). It means that is it takes the arabic text and convert it into python code and execute it. You can use the python code anywhere. In real you can code anything which you can code in python, but this is in starting phase and is not stable yet.

> It is recommended to use [IntelliJ IDEA](https://www.jetbrains.com/idea/) It support RTL text direction and you can see .قلب extension easily. The development for plugin to support qalblang is in progress.  

As of now it has support for MacOS only.

## Requirements

Python3 is required to compile the code.


## Installing
Clone this repository in a folder.

`git init`

`git clone https://github.com/qalblang/qalblang.git`

Now go to the qalblang folder and run

`./install.sh`

Next Add "PATH=$HOME/qalblang/bin:$PATH" to your `.bash_profile`

## Running

Open terminal and create a *.قلب file.

`vi احلا.قلب`

Lets write some code to print "احلا و سهلا يا عالم"

`اكتب("احلا و سهلا يا عالم")`

Save file and exit

And now run

`قلب احلا`

It will print 

`احلا و سهلا يا عالم`

For more sample code see (https://github.com/qalblang/qalblang-sample)

## Known Issues

As of now it has been tested on MacOS only. It might run on linux as well but not tested yet.

On printing any arabic number it prints number.

## Contributing

You are most welcome to contribute for qalblang.
For guidelines see CONTRIBUTING.md

To get started take a fork of this repository and clone it. Now go to the `start.py` 


There are few things which requires for immediate changes.

**Keywords:** Keywords for qalblang are need to be refined and standarized. As I am not a native arabic speaker, I have tried it to more accurate as possible. It is not all complete and need work. Please take a look at these files if you are a native arab.

- qalblang/qalb/py/ar/functions.json
- qalblang/qalb/py/ar/keywords.json
- qalblang/qalb/py/ar/literals.json

**Packages:** One could import a package by writing in arabic. But one needs to type the name in english to import the package. If we have packages with name in arabic it will be all arabic.

For instance if we need to import tensorflow we can write

`استيراد tensorflow مثل تنسر`

Now if we have a package name with تنسرتدفق which will have function names written in arabic which will call the tensorflow actual functions we can write the code as

`استيراد تنسرتدفق مثل تنسر`

See مفيد package in this repository for example

**Plugins:** Plugins for editor is must in order to write the code. And it needed to be developed.
