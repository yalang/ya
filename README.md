# <:blue_heart:/> لغة القلب 

**_QALB_** Language is an open source programming language where you can write python code in arabic language.

It is a [transcompiler](https://en.wiktionary.org/wiki/transcompiler). 
It means that is it takes the arabic text and convert it into python code and execute it. 
Which then can be used anywhere. You can code anything which you can code in python.

> It is recommended to use [IntelliJ IDEA](https://www.jetbrains.com/idea/) as it support RTL text direction and and it also support .قلب extension. 

**Supports MacOS only.**

## Requirements

Python3


## Installation
Clone this repository in a folder.

`git init`

`git clone https://github.com/qalblang/qalblang.git`

Now go to the qalblang folder and run

`./install.sh`

Next Add this `export PATH=$HOME/qalblang/bin:$PATH` to your `.bash_profile`

## Running

Create a new file with name `اهلا.قلب` and open in any editor.

Now write this in the file

`اكتب("اهلا و سهلا يا عالم")؛`

Save file and exit

Run this command in terminal from the directory where file exist

`قلب اهلا`

It will print 

`اهلا و سهلا يا عالم`

For more sample code see (https://github.com/qalblang/qalblang-sample)

## Known Issues

As of now it has been tested on MacOS only. It might run on linux.

## Contributing

You are most welcome to contribute for qalblang.
For guidelines see CONTRIBUTING.md

To get started take a fork of this repository and clone it.

**Packages:** Python packages with arabic names and having function with arabic names to call the origin and existing package functions are required.

For instance if we need to import tensorflow we can write

`استيراد tensorflow مثل تنسر`

If we have a package with name تنسر and having function names in arabic 
which calls the tensorflow actual functions we can write directly as

`استيراد تنسر مثل تنسر`

**Plugins:** Plugins for editors to support qalblang is required in order to write the code easily.
