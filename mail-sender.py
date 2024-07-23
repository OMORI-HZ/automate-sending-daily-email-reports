import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # e.g., 'smtp.gmail.com' for Gmail
SMTP_PORT = 587  # For TLS
SMTP_USER = 'your_email@example.com'
SMTP_PASSWORD = 'your_password'

# Function to send the email
def send_email():
    # Create the email content
    from_address = SMTP_USER
    to_address = 'recipient@example.com'
    subject = 'Daily Report'
    body = 'This is your daily report.'

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # Create server object with SSL option
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    # Perform operations via server
    server.login(from_address, SMTP_PASSWORD)
    text = msg.as_string()
    server.sendmail(from_address, to_address, text)
    server.quit()

    print("Email sent successfully!")

# Schedule the email to be sent daily
schedule.every().day.at("08:00").do(send_email)  # Set the time you want to send the email

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
