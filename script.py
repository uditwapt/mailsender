import smtplib
from email.mime.text import MIMEText


recipients = ["uditwapt@gmail.com","uditg1989@gmail.com","yashpatodia.yash@gmail.com","motasimkazmi333@gmail.com"  ]

mailSubject = "LetsPy Delhi BootCamp at IIIT Delhi"
mailBody = """Hello Tribe, 
LetsPy, an initiative of,  GirlScript Foundation presents to you a two days Python boot-camp

What is this LetsPy about?

LetsPy is India's Biggest Python Programming Boot-camp. The 2 days Boot-camp tells an overview of getting started with Python from Scratch to the extend of building applications using it.

Interesting! Whats the format?

The boot-camp aims to kick-start your dev journey from Scratch to Pro. It consist of hands on experience and making cool projects out of it. The Boot-camp will be conducted by industry mentors and professionals.

Nice! But why should I attend it?
- Learn Python from Scratch to Pro Level.
- Get Expert Guidance and Support
- Food and Beverage is on us
- Certificates
- Kits with tons of Swags
- Networking with Like-Minded People.

Super! When is it being Held?

March 30-31, 2019
Venue: IIIT Delhi
Timings: 10:00 AM to 5:00 PM

Woah! I want to join in! How to proceed further?
Register at the given link before 27th March to be a part of it.

Registration link - http://bit.ly/letspyreg
Registration Charges: ₹599 only.

Facebook Event:
https://www.facebook.com/events/334835250477207/

Join our WhatsApp Community: 
https://chat.whatsapp.com/HzGq5sKf5F06zuqhk03EEf

For any queries, contact at: 
Motasim: 8804223700
letspydelhi@gmail.com

Happy Coding! 

    """

for i in recipients:

    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    print "Connected"

        
    msg = MIMEText(mailBody)
    
    smtpserver.ehlo()
    smtpserver.starttls()
    #smtpserver.set_debuglevel(1)

    sender = 'girlscript2@gmail.com'
    passwrd = "girlscript2@321"
    smtpserver.login(sender,passwrd)
    print "Logged in"
    msg['Subject'] = mailSubject
    msg['From'] = sender
    msg['To'] = i
    
    try:
        smtpserver.sendmail(sender, [i], msg.as_string()) 
        print "Sent to " + i + "\n\n"
    except(e):
        print "Mail Failed for" + i    
    del msg
    smtpserver.quit()