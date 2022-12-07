(new_env) C:\Users\sbyeg\django_projects\rship>python manage.py shell
  
  from rapport.models import Description

In [3]: Description.objects.all()
Out[3]: <QuerySet [<Description: Emmanuel's Birthday>, <Description: Ridely's Birthday>, <Description: Caleb's birthday>, <Description: Sam's Birthday>, <Description: My mum's Birthday>]>

In [4]: Description.objects.filter(id=1)
Out[4]: <QuerySet [<Description: Emmanuel's Birthday>]>

In [5]: all_entries = Description.objects.all()

In [6]: all_entries
Out[6]: <QuerySet [<Description: Emmanuel's Birthday>, <Description: Ridely's Birthday>, <Description: Caleb's birthday>, <Description: Sam's Birthday>, <Description: My mum's Birthday>]>

In [7]: one_entry = Entry.objects.get(pk=1)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-7-3569ec73d039> in <cell line: 1>()
----> 1 one_entry = Entry.objects.get(pk=1)

NameError: name 'Entry' is not defined

In [8]: one_entry = Description.objects.get(pk=1)

In [9]: one_entry
Out[9]: <Description: Emmanuel's Birthday>

In [10]: Description.objects.all()[:5]
Out[10]: <QuerySet [<Description: Emmanuel's Birthday>, <Description: Ridely's Birthday>, <Description: Caleb's birthday>, <Description: Sam's Birthday>, <Description: My mum's Birthday>]>

In [11]: Description.objects.all().values('description_text')
Out[11]: <QuerySet [{'description_text': "Info of my bro's birthday."}, {'description_text': "Info on my friend's birthday."}, {'description_text': "Info of my cousin's birthday."}, {'description_text': 'Info of my birthday.'}, {'description_text': "Info on my mum's birthday."}]>

 

In [12]: Description.objects.all().values_list('description_text')
Out[12]: <QuerySet [("Info of my bro's birthday.",), ("Info on my friend's birthday.",), ("Info of my cousin's birthday.",), ('Info of my birthday.',), ("Info on my mum's birthday.",)]>                   
