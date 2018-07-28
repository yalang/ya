#<:blue_heart:/> لغة القلب 
**_QALB_** Language is a completely open source programming language in which you can code python in arabic language.

This is in completely basic and experimental phase.

Please see (https://github.com/qalblang/qalblang-sample) file for code samples.
 
> I apologize for any mistakes. And need your help in that.

`main.py` convert `احلاـوـسحلا`(arabic code) into `احلاـوـسحلا.py`(python code)

**مفيد** package contains few functions written in arabic which called python core functions.

As of now it contains only print function for the experiment purpose. 

This has been tested on macOS 10.13.2 and PyCharm 2018.1 (Community Edition) and Visual Studio Code (1.25.1)

## Requirements

Python3 is required to compile the code.


## Installing
Clone this repository in a folder.

`git init`

`git clone https://github.com/qalblang/qalblang.git`

Now go to the qalblang folder and run

`./install.sh`

Next Add `PATH=$HOME/qalblang/bin:$PATH` to your `.bash_profile`

## Known Issues

As of now it has been tested on MacOS only. It might run linux as well but not tested yet.

On printing any arabic number it prints number.
