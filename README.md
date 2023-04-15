# BLA-API-Wrapper.

---

#### Description

This is a wrapper I made to interact with my school's web application, using python.
The app itself is used to view homework assignments.

#### Table of Contents

- [Installation](#Installation)
  
- [Getting Started](#Getting Started)
  

#### Installation

```shell
pip install BlaApi
```

## Getting Started

The code below returns a list of 'notification_ids' which match the passed date
The Date needs to be in the format: 'Abbreviated Day, DD,MM,YYYY'

```python
from BlaApi.diary import Diary
username = #user
password = #pass

d = Diary(username=username, password=password)
out = d.search_by_date("Thu, 13/04/2023")
print(out)

'''
```
