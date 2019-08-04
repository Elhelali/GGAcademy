import requests

def welcome_message(usermail):
	return requests.post(
		"https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
		auth=("api", "40468c83e0feff81b25ebc89f56e8b14-16ffd509-f94a9ba3"),
		data={"from": "Excited User <mailgun@ggacademy.vegas>",
			"to": [usermail, "ali@ggacademy.vegas"],
			"subject": "Hello",
			"text": "Welcome to GGAcademy!"})