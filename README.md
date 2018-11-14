# ي : لغة البرمجة 

> NOTE: We have changed the name of this project to ya or (ي : لغة البرمجة) (yā: The programming language).
> The last character.
> Previously it was called qalblang. 
> You may find some footprint for the same in here. 
> Please let me know at quadrixm@gmail.com. 
> Happy to see your suggestions or any feedback.

**_Ya (ي)_** is an open source programming language where you can write python code in arabic language.

It takes the arabic text and convert it into python code and execute it. 
Which then can be used anywhere. You can code anything which you can code in python.

> It is recommended to use [IntelliJ IDEA](https://www.jetbrains.com/idea/) as it support RTL text direction and and it also support .ي extension. 

- **Hello World** [Sample File اهلا.ي](https://github.com/yalang/examples/blob/master/اهلا.ي)
```python
اكتب("اهلا و سهلا يا عالم")؛
```
Output:
```bash
اهلا و سهلا يا عالم
```

- **Condition** [Sample File لو.ي](https://github.com/yalang/examples/blob/master/لو.ي)
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

- **Function** [Sample File وظيفة.ي](https://github.com/yalang/examples/blob/master/وظيفة.ي)
```python
وظيفة جمع(اولا، ثاني):؛
    كل = اولا + ثاني؛
    إرجع كل؛

اكتب("جمع = "، جمع(٢، ٣))؛
```
Output:
```bash
جمع =  ٥
```

**NOTE: `؛` is optional at the end of line**



For more sample code see (https://github.com/yalang/examples)


## Prerequisites
- macOS
- Python 3


## Getting Started
### Installation
- Clone this repo:
```bash
git clone https://github.com/yalang/ya.git
cd ya
```
- Run install.sh:
```bash
./install.sh
```
- Add `export PATH=$HOME/ya/bin:$PATH` to `.bash_profile` or `.bashrc`


## Running

- Create a new file with name `اهلا.ي` and open in any editor.

- Write this in the file

```vim
اكتب("اهلا و سهلا يا عالم")؛
```

- Save it

- Open a terminal and go to the folder where file is saved

- Run this command

```bash
ي اهلا
```

- It will print 

```bash
اهلا و سهلا يا عالم
```

## Contributing

You are most welcome to contribute for ya.
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

**Plugins:** Plugins for editors to support Ya is required 
in order to write the code easily.
