from handlers.base import BaseHandler
from models.mail import Mail


class Mailing(BaseHandler):
    def post(self):
        email = self.request.get("email")
        name = self.request.get("name")
        mail = Mail(email=email, name=name)
        mail.put()

        return self.redirect_to("main-page")

