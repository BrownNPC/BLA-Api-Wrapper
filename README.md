# BLA-API-Wrapper.

---

### Description

This is a wrapper I made to interact with my school's web application, using python.
The app itself is used to view homework assignments.

### Table of Contents

- [Installation](#Installation)
  
- [Getting Started](#Getting Started)
  

### Installation

```shell
pip install BlaApi
```

### Getting Started

The code below returns a list of **'notification_ids'**
The date needs to be in the format **'Abbreviated_Day, DD/MM/YYYY'**

```python
from BlaApi.diary import Diary
username = # Bla username
password = # Bla password

d = Diary(username=username, password=password)
notification_ids = d.search_by_date("Thu, 13/04/2023")
print(notification_ids)
```

**Output:**

```shell
['3049357', '3049213', '3038795', '3038038', '3036497', '3036305']
```

The output is a list of notification ids, we can use to make api calls and retrieve useful information

```python
#from BlaApi.client import Client
#c = Client(username, password)
c = d.client
diary_data = c.get_diary_data(out)
print(diary_data)
```

The output would be a list of dictionaries corresponding to the notification id provided.
