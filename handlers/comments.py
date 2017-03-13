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

        Comment.create(content=text,author=user, topic= topic)

        return self.redirect_to("topic-details", topic_id=topic.key.id())

class CommentList(BaseHandler):
    def get(self):
        user = users.get_current_user()
        comments = Comment.query(Comment.deleted == False).order(Comment.topic_title).fetch()
        params = {"user" : user, "comments":comments}

        return self.render_template("comment_list.html",params=params)

class CommentDelete(BaseHandler):
    def post(self,comment_id):
        user= users.get_current_user()
        comment = Comment.get_by_id(int(comment_id))
        if comment.author_email == user.email() or users.is_current_user_admin():
            comment.deleted = True
            comment.put()
        return self.redirect_to("topic-details", topic_id= comment.topic_id)



