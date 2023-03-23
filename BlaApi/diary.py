from BlaApi.client import Client

class Diary:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.client = Client(self.username, self.password)
        self.diary_list = self.client.diary_list()

    

    def search_by_student_id(self, student_id= None):
        #If student id is not passed, use the first one

        return f"student id is {student_id}"
    