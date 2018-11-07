# ي : لغة البرمجة 

ي : لغة البرمجة هي لغة برمجة مفتوحة المصدر

هنا يمكنك كتابة باللغة العربية python code

> من المستحسن استخدام [IntelliJ IDEA](https://www.jetbrains.com/idea/). 

- **اهلا** [ملف عينة اهلا.ي](https://github.com/qalblang/qalblang-sample/blob/master/اهلا.قلب)
```python
اكتب("اهلا و سهلا يا عالم")؛
```
انتاج:
```bash
اهلا و سهلا يا عالم
```

- **شرط** [ملف عينة لو.ي](https://github.com/qalblang/qalblang-sample/blob/master/لو.قلب)
```python
ع = ٧
لو ع ٪ ٢ == ٠:؛
    اكتب("ع الفردية")؛
ولو ٧ == ٠:؛
    اكتب("هذا صفر")؛
آخر:؛
    اكتب("ع الزوجية")؛
```
انتاج:
```bash
ع الزوجية
```

- **وظيفة** [ملف عينة وظيفة.ي](https://github.com/qalblang/qalblang-sample/blob/master/وظيفة.قلب)
```python
وظيفة جمع(اولا، ثاني):؛
    كل = اولا + ثاني؛
    إرجاع كل؛

اكتب("جمع = "، جمع(٢، ٣))؛
```
انتاج:
```bash
جمع =  ٥
```

**ملحوظة: `؛` هو اختياري في نهاية السطر**



لمزيد من عينة رمز انظر (https://github.com/qalblang/qalblang-sample)


## المتطلبات الأساسية
- macOS
- Python 3


## ابدء
### تعليمات التحميل
- انسخ هذا:
```bash
git clone https://github.com/qalblang/qalblang.git
cd qalblang
```
- تنفيذ هذا install.sh:
```bash
./install.sh
```
- اضف `export PATH=$HOME/qalblang/bin:$PATH` إلى `.bash_profile` أو `.bashrc`


## Running

- قم بإنشاء ملف جديد بالاسم `اهلا.قلب` 

- فتح في المحرر

- اكتب هذا في الملف

```vim
اكتب("اهلا و سهلا يا عالم")؛
```

- احفظها

- افتح terminal 

- اذهب إلى المجلد حيث يتم حفظ الملف

- تنفيذ هذا

```bash
ي اهلا.ي
```

- انتاج 

```bash
اهلا و سهلا يا عالم
```
