import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP server configuration
smtp_server = "smtp.gmail.com"
port = 587
context = ssl.create_default_context()

def connect():
    # Get sender and recipient details from user
    sender_email = input("Enter your email: ")  # Your email
    receiver_email = input("Enter recipient's email: ")  # Recipient's email
    sender_password = input("Enter your password: ")

    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = input("Enter the subject: ")  # Subject of the email

    # Add body to the email
    body = input("Enter the body of the email: ")
    message.attach(MIMEText(body, "plain"))

    try:
        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)  # Secure the connection
            servermessage.login(sender_email, sender_password)  # Log in to the server
            server.sendmail(sender_email, receiver_email, .as_string())  # Send the email
            print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("Failed to log in. Please check your email and password.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to send the email
connect()
