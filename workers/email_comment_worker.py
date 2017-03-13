from handlers.base import BaseHandler
from google.appengine.api import mail


class EmailNewCommentWorker(BaseHandler):
    def post(self):
        topic_author_email = self.request.get("topic_author_email")
        topic_title = self.request.get("topic_title")
        comment_content= self.request.get("comment_content")
        mail.send_mail(sender="nejcgustincic@gmail.com", to=topic_author_email,
                       subject="You have new comment in topic %s" % topic_title,
                       body="nov komentar: {0} ".format(comment_content))