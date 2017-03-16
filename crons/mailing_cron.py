from handlers.base import BaseHandler
from models.mail import Mail
from models.topic import Topic
import datetime
from google.appengine.api import mail



class MailingCron(BaseHandler):
    def get(self):
        mails = Mail.query(Mail.subscribed == True).fetch()
        topics = Topic.query(Topic.created > datetime.datetime.now() - datetime.timedelta(hours=24)).fetch()

        for mail in mails:
            for topic in topics:
                mail.send_mail(sender="nejcgustincic@gmail.com", to = mail.email(),subject="Check out the latest topics",
                               body = """Hi These are the latest topics on our forum : <a href"/topic/{0}">{1}<a>""" .format(topic.key.id(),topic.title())
                               )

