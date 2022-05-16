import smtplib
from email.mime.text import MIMEText

def send_mail(date, time, name, lastname, email, phone, nperson, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'c0e5a668ec9fc5'
    password = '6c762800635664'
    message = f"<h1>New reservation!</h1><ul><li>Date: {date}</li><li>Time: {time}</li><li>Name: {name}</li><li>Last Name: {lastname}</li><li>E-mail: {email}</li><li>Phone: {phone}</li><li>Guests: {nperson}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'CoffeShop@mysite.com'
    receiver_email = email
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Reservation'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())