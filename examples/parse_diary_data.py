from BlaApi.diary import Diary
from html2text import html2text as h2t #pip install html2text


load_dotenv()
username = # your bla username
password = # your bla password
d = Diary(username=username, password=password)


#return diaries from this date

date = 'Thu, 13/04/2023'

#Select student on your account to return their diary.

student_number = 0


def filter_diary(date=date, been_read=True, student_number=student_number):

    # sort by student, date, and been read then return the diary data by
    # sending notification ids to api endpoint.

    out = d.search_by_student(student_number=student_number)

    out  = d.search_by_date(date=date, passthru=out)

    out = d.search_been_read(been_read=been_read, passthru=out)

    return d.client.get_diary_data(notification_ids=out)

def format_diary():
    diary = filter_diary()

    if diary:
        output = []

        for d in diary:
            # parse html and convert into markdown.

            details = h2t(d.get('details'))

            # remove markdown tags to get plain text.

            details = details.replace('**', '')
            details = details.replace('\\', '')
            details = details.replace('   ', '')
            details = details.replace('_', '')

            # If 'subject' field is empty, then it's a notice.

            if d.get('subject'):
                subject = f"Subject: {d.get('subject')}"
            else:
                subject = f"Notice"

            # Append the attachment id to a link which redirects to the attachment.

            if d.get('attachmentId'):
                attachment_link = "https://beaconlightacademy.edu.pk/app/uploaded/"
                attachments = f"Attachments: {attachment_link}{d['attachmentId']}"
            else:
                attachments = ""
            
            output.append(f'{subject}\n{details}\n{attachments}')
        return output
    else:
        print('No diaries found.')
        return None



diaries = filter_diary()

for d in diaries:
    print(d)
