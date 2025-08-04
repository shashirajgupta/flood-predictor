import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_alert_email(subject, body, to_email):
    """
    Sends an email alert using Gmail SMTP.
    
    Parameters:
        subject (str): The subject of the email.
        body (str): The message content.
        to_email (str): The recipient's email address.
    """
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = 'shashirajgupta7@gmail.com'      
    msg['To'] = to_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('shashirajgupta7@gmail.com', 'EMAIL_PASSWORD')  
            smtp.send_message(msg)
        print(f"✅ Alert sent to {to_email}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
