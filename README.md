# <:blue_heart:/> لغة القلب 

**_QALB_** Language is a completely open source programming language in which you can code in arabic language.

It converts the arabic text into executable python code and execute it. In real you can code anything which you can code in python, but this is in starting phase and is not stable yet.

This is in completely basic and experimental phase.
 
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

Next Add `PATH=$HOME/qalblang/bin:$PATH` to your `.bash_profile`

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

As of now it has been tested on MacOS only. It might run linux as well but not tested yet.

On printing any arabic number it prints number.
