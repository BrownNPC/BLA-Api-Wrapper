import os
import json
import httpx
import datetime
from fake_useragent import UserAgent as ua

class Client():
	client = httpx.Client() # instanciate 
	#! BLA credentials must be passed in as string
	def __init__(self, username: str, password: str):
		# Random UserAgent
		self.headers = {'UserAgent': str(ua().chrome)}
		self.username = username
		self.password = password
		self.token = self.login().get('token')
		
	def login(self):
		# Construct API endpoint URL
		endpoint = "login"
		api_url = f"https://beaconlightacademy.edu.pk/app/restapi.php?endpoint={endpoint}&rnd=1667581678739&username={self.username}&password={self.password}"
		
		# Send POST request to API endpoint with headers
		response = self.client.post(api_url, headers=self.headers)
		#! Raise an error if POST fails
		response.raise_for_status()
		
		# Parse JSON response
		data = json.loads(response.content)['data']

		# Retrieve access token & student info from JSON response
		token = data.get('accessToken')
		if token is None:
			raise ValueError("Access token not found in response.")
		student_info = data.get('students')

		# Return student ids and student names as lists
		student_ids = [] #Initialize
		student_names = [] #Initialize

		for s in student_info:
			# Return student ids as list
			id = s.get('id')
			student_ids.append(id)

			# Return student name as list
			name = s.get('studentName')
			student_names.append(name)


		# Return retrieved data as dictionary
		output = {
			'token': token,
			'student_id': student_ids,
			'student_name': student_names

		}
		return output

	def diary_list(self):
		# Construct API endpoint URL
		endpoint = "diaryList"
		api_url = f"https://beaconlightacademy.edu.pk/app/restapi.php?endpoint={endpoint}&accessToken={self.token}&year=1"
		
		# Send POST request to API endpoint with headers
		response = self.client.post(api_url, headers=self.headers)

		#! Raise an error if POST fails
		response.raise_for_status()
		
		# Retreive diary list from JSON response
		data = json.loads(response.content)['data']
		
		return data


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
	
	def get_diary_data(self, notification_id):
		# Construct API endpoint URL
		endpoint = "diaryDetails"
		api_url = f"https://beaconlightacademy.edu.pk/app/restapi.php?endpoint={endpoint}&accessToken={self.token}&appUserNotificationId={notification_id}"

		# Send POST request to API endpoint with headers
		response = self.client.post(api_url, headers=self.headers)

		#! Raise an error if POST fails
		response.raise_for_status()

		# Retreive diary data from JSON response
		data = json.loads(response.content)['data']

		return data