(new_env) C:\Users\sbyeg\django_projects\rship>python manage.py shell
  
  from rapport.models import Description

>>>  Description.objects.all()
>>>  <QuerySet [<Description: Emmanuel's Birthday>, <Description: Ridely's Birthday>, <Description: Caleb's birthday>, <Description: Sam's Birthday>, <Description: My mum's Birthday>]>

>>>  Description.objects.filter(id=1)
>>>  <QuerySet [<Description: Emmanuel's Birthday>]>

>>>  all_entries = Description.objects.all()

>>>  all_entries
>>>  <QuerySet [<Description: Emmanuel's Birthday>, <Description: Ridely's Birthday>, <Description: Caleb's birthday>, <Description: Sam's Birthday>, <Description: My mum's Birthday>]>

>>>  one_entry = Entry.objects.get(pk=1)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-7-3569ec73d039> in <cell line: 1>()
----> 1 one_entry = Entry.objects.get(pk=1)

NameError: name 'Entry' is not defined

>>>  one_entry = Description.objects.get(pk=1)

>>>  one_entry
>>>  <Description: Emmanuel's Birthday>

>>>  Description.objects.all()[:5]
>>>  <QuerySet [<Description: Emmanuel's Birthday>, <Description: Ridely's Birthday>, <Description: Caleb's birthday>, <Description: Sam's Birthday>, <Description: My mum's Birthday>]>

>>>  Description.objects.all().values('description_text')
>>>  <QuerySet [{'description_text': "Info of my bro's birthday."}, {'description_text': "Info on my friend's birthday."}, {'description_text': "Info of my cousin's birthday."}, {'description_text': 'Info of my birthday.'}, {'description_text': "Info on my mum's birthday."}]>

 

>>> Description.objects.all().values_list('description_text')
>>> <QuerySet [("Info of my bro's birthday.",), ("Info on my friend's birthday.",), ("Info of my cousin's birthday.",), ('Info of my birthday.',), ("Info on my mum's birthday.",)]>                   
12


#To get the list of usernames:

>>> User.objects.all().values('username')
>>> [{'username': u'u1'}, {'username': u'u2'}]

>>> User.objects.all().values_list('username')
>>> [(u'u1',), (u'u2',)]
#If you want just strings, a list comprehension can do the trick:

>>> usr_names = User.objects.all().values('username')
>>> [u['username'] for u in usr_names]
>>> [u'u1', u'u2']
Using values_list:

>>> usr_names = User.objects.all().values_list('username')
>>> [u[0] for u in usr_names]
>>> [u'u1', u'u2']
                
>>> discr_items = Description.objects.all().values_list('description_text')

>>>  discr_items
>>>  <QuerySet [("Info of my bro's birthday.",), ("Info on my friend's birthday.",), ("Info of my cousin's birthday.",), ('Info of my birthday.',), ("Info on my mum's birthday.",)]>
                
>>> discr_items = Description.objects.all().values('description_text')
>>>  <QuerySet [{'description_text': "Info of my bro's birthday."}, {'description_text': "Info on my friend's birthday."}, {'description_text': "Info of my cousin's birthday."}, {'description_text': 'Info of my birthday.'}, {'description_text': "Info on my mum's birthday."}]>

                # Getting all the field objects in django querying               
>>>  items = Description.objects.all().values('description_text','reminder_date', 'event_date')
>>> items
>>> <QuerySet [{'description_text': "Info of my bro's birthday.", 'reminder_date': datetime.datetime(2023, 1, 24, 9, 0, tzinfo=datetime.timezone.utc), 'event_date': datetime.datetime(2023, 2, 3, 21, 0, tzinfo=datetime.timezone.utc)}, {'description_text': "Info on my friend's birthday.", 'reminder_date': datetime.datetime(2023, 3, 1, 9, 0, tzinfo=datetime.timezone.utc), 'event_date': datetime.datetime(2023, 3, 5, 5, 0, tzinfo=datetime.timezone.utc)}, {'description_text': "Info of my cousin's birthday.", 'reminder_date': datetime.datetime(2023, 6, 5, 9, 0, tzinfo=datetime.timezone.utc), 'event_date': datetime.datetime(2023, 6, 15, 3, 0, tzinfo=datetime.timezone.utc)}, {'description_text': 'Info of my birthday.', 'reminder_date': datetime.datetime(2023, 7, 1, 15, 0, tzinfo=datetime.timezone.utc), 'event_date': datetime.datetime(2023, 7, 12, 5, 0, tzinfo=datetime.timezone.utc)}, {'description_text': "Info on my mum's birthday.", 'reminder_date': datetime.datetime(2023, 7, 31, 9, 0, tzinfo=datetime.timezone.utc), 'event_date': datetime.datetime(2023, 8, 3, 5, 0, tzinfo=datetime.timezone.utc)}]>
                
