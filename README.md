# BLA-API-Wrapper.


## Description

##### Reverse engineering of [Beacon Light Academy's Homework App.](https://beaconlightacademy.edu.pk/app/)


### Archived
This was my first ever programming project. I had absolutely zero coding experience prior.
I used this code to make a whatsapp bot to update my classmates on homework (the school's app did not have push notifications). The bot had around 30 users the time. I polished this library up to make a better app than what my school had, halfway through said app's development I ended up leaving the school. I am archiving this project to add some context, and also because I did not end up using this. 

### Table of Contents

- [Installation](#Installation)



- [Quick-Start](#Quick-Start)



- [Documentation](#Documentation)



- [Examples](https://github.com/Omer-Farooqui/BLA-Api-Wrapper/tree/master/examples)


- Useful Links:
  
  - [PyPI](https://pypi.org/project/BlaApi/)
  
  - [Github Repo](https://github.com/Omer-Farooqui/BLA-Api-Wrapper)

## Installation

The library is available on [PyPI](https://pypi.org/project/BlaApi/), install using pip.

```shell
pip install BlaApi
```

Or update it.

```shell
pip install BlaApi --upgrade
```

## Quick Start

The code below returns a list of **'notification_ids'** The date needs to be in the format; **'Abbreviated_Day, DD/MM/YYYY'**

```python
from BlaApi import Client
username = 'my username'
password = 'my password'

notification_ids = c.search_by_date("Thu, 13/04/2023")
print(notification_ids)
```

###### Output:

```shell
['3049357', '3049213', '3038795', '3038038', '3036497', '3036305']
```

We can use **'notification ids'** to make api calls and retrieve useful information.

```python
from BlaApi import Client
c = Client(username, password)
diary_data = c.get_diary_data(notification_ids)
print(diary_data)
```

The output consists of a list of dictionaries which contain details for the corresponding notification id.

###### Output:

```python
[{
        "studentId": "8326",
        "id": "3049213",
        "appDiaryId": "64980",
        "title": "Class work - 13th April",
        "details": "**Book: TBS**\n\
**Unit 06: Setting up a company**\n
**Chapter 01: Gathering information**\n\n
Chapter completed; discussed all activities. 'Sharpen your skills' also covered.\n\n",
        "bRead": "1",
        "created": "2023-04-13 10:05:25",
        "diaryType": "cw",
        "dateDue": None,
        "attachment": None,
        "attachment2": None,
        "dateSubmitted": None,
        "subject": "ENGLISH LANGUAGE",
        "currentTimestamp": "2023-04-15 15:25:21",
        "assignmentId": "64980",
        "gr_no": "12266",
        "comments": [],
},
]
```

*The html is converted to markdown.* 

>Check out some [examples](https://github.com/Omer-Farooqui/BLA-Api-Wrapper/tree/master/examples) or read the [documentation.](#Documentation)

## Documentation

This is some boilerplate code you should be familiar with.

```python
from BlaApi import Client
username = 'my username'
password = 'my password'

c = Client(username, password)
```

> Keep in mind that In the api, the 'notificationId' and 'id' variables are used interchangeably.

The **'login()'** method allows you to retrieve information such as: auth token and student information such as class, section student_name, gr_number, student_id.

The **'get_diary_list()'** method will return a list of all the diaries available in the app's database, which allows you to retrieve information such as: date posted, subject name, assignment id, notification id (id), title, description, diary type (cw/hw), if the diary has been read (bRead) and the student id which the diary corresponds to.

The **'get_diary_data()'** method allows you to get the content of the diary itself, by passing a list of notification ids. it has options such as: student id, app diary id (assignment id), attachment id, comments and the rest is the same as **get_diary_list()**

The there are methods to parse and sort through the diary list, and return notification ids for the entries. The methods inside it also allow you to also pass in a list of notification ids as a second argument using its **'passthru'** variable.

The **'get_current_date()'** method from **'Diary'** returns today's date in a format that the api needs to function. (Abbreviated_Day, DD/MM/YYYY)

The **'search_by_student'** method from **'Diary'** returns the notification_ids for one of the students registered on your account. By default it sets student_number = 0, meaning it will return diaries for the first student by default.

The other methods from **'Diary'** are: **'search_by_date(date)'**, and **'search_been_read(True/False)'**. They are self explanatory.

## To-Do

- [ ] Add methods for interacting with more features
  
  - [ ] Comments
  
  - [ ] Description

  - [ ] Student info
  
  - [ ] Attachments

- [ ] Make better doccumentation

### My motivation to create this

Simply put, I found my school's app to be subpar, so I'm attempting to create a better one.




Feel free to open an [issue](https://github.com/Omer-Farooqui/BLA-Api-Wrapper/issues) if you have any questions, and star the [repo](https://github.com/Omer-Farooqui/BLA-Api-Wrapper) if you're cool
