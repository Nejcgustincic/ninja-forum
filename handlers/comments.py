from webapp2_extras import users

from handlers.base import BaseHandler
from models.comment import Comment
from models.topic import Topic
from google.appengine.api import users


class CommentAdd(BaseHandler):
    def post(self, topic_id):
        user = users.get_current_user()

        if not user:
            return self.write("Please log in ")

        text = self.request.get("comment-text")
        topic = Topic.get_by_id(int(topic_id))

        comment= Comment(content=text,author_email= user.email(), topic_id=topic.key.id(),topic_title = topic.title)
        comment.put()

        return self.redirect_to("topic-details", topic_id=topic.key.id())



