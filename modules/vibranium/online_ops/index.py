import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib

# create a class called OnlineOps


class OnlineOps:
    def __init__(self):
        pass

    def search_wikipedia(self, query):
        # search wikipedia for the query
        result = wikipedia.summary(query, sentences=2)
        return result

    # create a method called search_google
    def search_google(self, query):
        # search google for the query
        kit.search(query)

    def play_on_youtube(self, video):
        kit.playonyt(video)

    def send_whatsapp_message(self, number, message):
        kit.sendwhatmsg_instantly(f"+91{number}", message)

    # create a method called send_email
    # def send_email(self, to, subject, content):
    #     # create an EmailMessage object
    #     msg = EmailMessage()
    #     # set the email content
    #     msg.set_content(content)
    #     # set the email subject
    #     msg['Subject'] = subject
    #     # set the email sender
    #     msg['From'] = config('EMAIL')
    #     # set the email receiver
    #     msg['To'] = to
    #     # create a smtplib.SMTP object
    #     server = smtplib.SMTP('smtp.gmail.com', 587)
    #     # start the smtp server
    #     server.starttls()
    #     # login to the smtp server
    #     server.login(config('EMAIL'), config('PASSWORD'))
    #     # send the email
    #     server.send_message(msg)
    #     # close the smtp server
    #     server.quit()
