"""
Test: send an email via gmail

"""
USER = 'dclynch123@gmail.com'
PWD = 'mhwhwmzwzpotmiza'
RECEIVER = 'mikeboris123@gmail.com'
SUB = 'dogs'
BOD = """
From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""



def send_email(user, pwd, recipient, subject, body):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    #create message container
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Link"
    msg['From'] = USER
    msg['To'] = RECEIVER

    html = """\
	<!DOCTYPE html>
	<html>
	<head>
	  <meta charset="utf-8">
	  <meta name="viewport" content="width=device-width">
	  <title>Dogs</title>
	  <link href="//netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.min.css" rel="stylesheet" type="text/css" />
	  <script src="https://code.jquery.com/jquery.min.js"></script>
	<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet" type="text/css" />
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
	</head>
	<body>
	<div class="container">
	  <div class="jumbotron">
	    <h1 class="text-center">
	      Dog Town
	    </h1>
	  </div>
	  <div class="text-center">
	    <figure class="figure">
	  <img src="http://cdn1.bloguin.com/wp-content/uploads/sites/85/2013/07/twitterminipony7runningminiponyconsolbaby.jpg" class="figure-img img-fluid rounded" alt="A generic square placeholder image with rounded corners in a figure.">
	  <figcaption class="figure-caption">Mini pony</figcaption>
	</figure>
	  </div>
	</div>
	</body>
	</html>	
	"""

    # record the MIME type of part2
    part2 = MIMEText(html, 'html')
    # attach part into message container
    msg.attach(part2)

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, msg.as_string())
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")

if __name__=='__main__':
	send_email(USER, PWD, RECEIVER, SUB, BOD)


