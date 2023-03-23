import os
import json
import httpx
import datetime
from fake_useragent import UserAgent as ua

class bla():
	client = httpx.Client()
	
	def __init__(self, username: str, password: str):
		if not isinstance(username, str) or not isinstance(password, str) or not username.strip() or not password.strip(): 
			raise ValueError("Invalid input, please pass in BLA credentials as string.")
		
		self.headers = {'UserAgent': str(ua().chrome)}
		self.username = username
		self.password = password
		self.token = self.login()

	def login(self):
		# Construct API endpoint URL
		endpoint = "login"
		api_url = f"https://beaconlightacademy.edu.pk/app/restapi.php?endpoint={endpoint}&rnd=1667581678739&username={self.username}&password={self.password}"
		
		# Send POST request to API endpoint with headers
		response = self.client.post(api_url, headers=self.headers)
		response.raise_for_status()
		
		# Retrieve authentication token from response JSON data
		data = json.loads(response.content)['data']
		token = data.get('accessToken')
		
		# Raise an error if authentication token is not found in response
		if not token:
			raise ValueError("Authentication token not found in response, request possibly failed.")
		
		return token
	
	def diary_list(self):
		endpoint = "diaryList"
		api_url = f"https://beaconlightacademy.edu.pk/app/restapi.php?endpoint={endpoint}&accessToken={self.token}&year=1"
		
		# Send POST request to API endpoint with headers
		response = self.client.post(api_url, headers=self.headers)
		response.raise_for_status()
		
		# Retrieve authentication token from response JSON data
		data = json.loads(response.content)['data']
		
		return data


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
	