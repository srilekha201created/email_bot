import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
listener = sr.Recognizer()
engine=pyttsx3.init()
def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            return info.lower()
    except:
        pass


def send_email(receiver,subject,message):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('purposetesting51@gmail.com','grandma@')
    email=EmailMessage()
    email['from']='purposetesting51@gmail.com','grandma@'
    email['To']=receiver
    email['subject']=subject
    email.set_content(message)
    server.send_message(email)

email_list={
    'sri':'18131f0014@gvpce.ac.in',
    'Ramya:18131f0006@gmail.com',
    'koushi':'18131f0015@gvpce.ac.in'

}

def get_email_info()
    talk('To whome you want to send email')
    name=get_info()
    receiver=email_list[name]
    talk('what is the subject of your email...')
    subject=get_info()
    talk('Tell me the text in your email')
    message=get_info()
    send_email(receiver,subject,message)

get_email_info()