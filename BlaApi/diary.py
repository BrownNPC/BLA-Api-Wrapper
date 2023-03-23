from BlaApi.client import Client

class Diary:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.client = Client(self.username, self.password)
        self.diary_list = self.client.diary_list()

    
    def search_by_student_id(self, student_id):
        diary = self.client.diary_list()

        # make a POST to diary data endpoint 
        # if student id is a match and return
        # the diaries as a list

        output = [] # initialize

        for d in diary:
            if d["studentId"] == student_id:
                notification_id = d['id']
                response = self.client.get_diary_data(notification_id=notification_id)
                output.append(response)

        return output
    