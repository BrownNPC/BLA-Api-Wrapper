import datetime
from BlaApi.client import Client

class Diary:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.client = Client(self.username, self.password)
        self.diary_list = self.client.diary_list()
    
    def search_by_student_id(self, student_id):

        diary = self.client.diary_list()

        # parse output from diary list function
        # if student id is a match then
        # return the diaries as a list

        output = [] # initialize

        for d in diary:
            if d["studentId"] == student_id:
                notification_id = d['id']
                response = self.client.get_diary_data(notification_id)
                output.append(response)
                
        return output
    
        #Retreive current date in a format that the api requires. 
        #EXAMPLE: "Tue, 9/11/2001"
    def get_current_date(self):

        # Get current date and day of week
        current_date = datetime.datetime.today()
        day_of_week = current_date.strftime("%A")

        # Format day of week to abbreviated format (e.g. 'Mon')
        abbreviated_day_of_week = day_of_week[:3]

        # Get current day and month
        current_day = str(current_date.day).zfill(2)
        current_month = str(current_date.month).zfill(2)

        # Format date string
        formatted_date = f"{abbreviated_day_of_week}, {current_day}/{current_month}/{current_date.year}"
        
        return formatted_date

    def search_by_date(self, date):

        diary = self.client.diary_list()
        # parse output from diary list function
        # if student id is a match then
        # return the diaries as a list

        output = []
        for d in diary:
            if d['date'] == date:
                notification_id = d['id']   
                response = self.client.get_diary_data(notification_id)
                output.append(response)
        return output