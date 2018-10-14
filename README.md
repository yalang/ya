# <:blue_heart:/> لغة القلب 

> #### QalbLang is not related to the [قلب](https://github.com/nasser/---) (https://github.com/nasser/---) (https://en.wikipedia.org/wiki/Qalb_(programming_language)) (http://nas.sr/قلب/)
> _**Be sure to checkout this awesome repo as well.**_

**_QalbLang_** is an open source programming language where you can write python code in arabic language.

It takes the arabic text and convert it into python code and execute it. 
Which then can be used anywhere. You can code anything which you can code in python.

> It is recommended to use [IntelliJ IDEA](https://www.jetbrains.com/idea/) as it support RTL text direction and and it also support .قلب extension. 

- **Hello World** [Sample File اهلا.قلب](https://github.com/qalblang/qalblang-sample/blob/master/اهلا.قلب)
```python
اكتب("اهلا و سهلا يا عالم")؛
```
Output:
```bash
اهلا و سهلا يا عالم
```

- **Condition** [Sample File لو.قلب](https://github.com/qalblang/qalblang-sample/blob/master/لو.قلب)
```python
ع = ٧
لو ع ٪ ٢ == ٠:؛
    اكتب("ع الفردية")؛
ولو ٧ == ٠:؛
    اكتب("هذا صفر")؛
آخر:؛
    اكتب("ع الزوجية")؛
```
Output:
```bash
ع الزوجية
```

- **Function** [Sample File وظيفة.قلب](https://github.com/qalblang/qalblang-sample/blob/master/وظيفة.قلب)
```python
وظيفة جمع(اولا، ثاني):؛
    كل = اولا + ثاني؛
    إرجاع كل؛

اكتب("جمع = "، جمع(٢، ٣))؛
```
Output:
```bash
جمع =  ٥
```

**NOTE: `؛` is optional at the end of line**



For more sample code see (https://github.com/qalblang/qalblang-sample)


## Prerequisites
- macOS
- Python 3


## Getting Started
### Installation
- Clone this repo:
```bash
git clone https://github.com/qalblang/qalblang.git
cd qalblang
```
- Run install.sh:
```bash
./install.sh
```
- Add `export PATH=$HOME/qalblang/bin:$PATH` to `.bash_profile` or `.bashrc`


## Running

- Create a new file with name `اهلا.قلب` and open in any editor.

- Write this in the file

```vim
اكتب("اهلا و سهلا يا عالم")؛
```

- Save it

- Open a terminal and go to the folder where file is saved

- Run this command

```bash
قلب اهلا
```

- It will print 

```bash
اهلا و سهلا يا عالم
```

## Contributing

You are most welcome to contribute for qalblang.
For guidelines see CONTRIBUTING.md

To get started take a fork of this repository and clone it.

**Packages:** Python packages is required,
 with arabic names and functions with arabic names to call the 
 original and existing package functions.

For instance if we need to import tensorflow we can write

`استيراد tensorflow مثل تنسر`

If we have a package with name تنسر and having function names in arabic 
which calls the tensorflow actual functions we can write directly as

`استيراد تنسر مثل تنسر`

**Plugins:** Plugins for editors to support qalblang is required 
in order to write the code easily.
