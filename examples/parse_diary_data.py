from BlaApi import Client
from html2text import html2text as h2t #pip install html2text



username = 'my username'
password = 'my password'
c = Client(username=username, password=password)


#return diaries from this date

date = c.get_current_date()

#Select student on your account to return their diary.

student_id = c.students[0].get('student_id')
print(f"Attempting to get diaries for: {c.students[0].get('student_name')}")


def filter_diary(date=date, been_read=True):

    # sort by student, date, and been read then return the diary data by
    # sending notification ids to api endpoint.

    out = c.search_by_student(student_id=student_id)

    out  = c.search_by_date(date=date, passthru=out)

    out = c.search_been_read(been_read=been_read, passthru=out)

    return c.get_diary_data(notification_ids=out)

def format_diary():

    try:
        diary = filter_diary()
    except:
        print('No Diaries found.')
        return []

    output = []

    for d in diary:
        # parse html and convert into markdown.

        details = h2t(c.get('details'))

        # remove markdown tags to get plain text.

        details = details.replace('**', '')
        details = details.replace('\\', '')
        details = details.replace('   ', '')
        details = details.replace('_', '')

        # If 'subject' field is empty, then it's a notice.

        if c.get('subject'):
            subject = f"Subject: {c.get('subject')}"
        else:
            subject = f"Notice"

        # Append the attachment id to a link which redirects to the attachment.

        if c.get('attachmentId'):
            attachment_link = "https://beaconlightacademy.edu.pk/app/uploaded/"
            attachments = f"Attachments: {attachment_link}{d['attachmentId']}"
        else:
            attachments = ""
        
        output.append(f'{subject}\n{details}\n{attachments}')
    return output


diaries = format_diary()

for d in diaries:
    print(d)
