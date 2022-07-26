from decouple import config
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email(destination, content):
	message = Mail(
		from_email='lucas.muoz@uc.cl',
		to_emails=destination,
		subject='Heroes API Simulation',
		plain_text_content=content
	)
	try:
		sg = SendGridAPIClient(config("SENDGRID_API_KEY"))
		response = sg.send(message)
		print("Email sent!")
	except Exception as e:
		print(e.message)