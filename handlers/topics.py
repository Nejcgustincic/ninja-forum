
from handlers.base import BaseHandler
from models.comment import Comment
from models.topic import Topic
from google.appengine.api import users, memcache
import uuid



class TopicCreateHandler (BaseHandler):
    def get(self):
        user= users.get_current_user()

        csrf_token= str(uuid.uuid4())
        memcache.add(key=csrf_token, value=user.email(), time=600)

        params = {"csrf_token" : csrf_token}
        return self.render_template("topic_create.html",params=params)

    def post(self):
        title= self.request.get("title")
        content= self.request.get("content")
        user = users.get_current_user()
        if not user:
            return self.write("you are not logged in")

        #CSRF protection
        csrf_token = self.request.get("csrf_token")
        csrf_value=memcache.get(csrf_token)
        if not csrf_value or str(csrf_value) != user.email():
            return self.write("You are a hacker")

        new_topic = Topic(title=title, content=content, author_email= user.email())
        new_topic.put()
        return self.redirect_to("topic-details", topic_id=new_topic.key.id())

class TopicDetails(BaseHandler):
    def get(self, topic_id):


        topic = Topic.get_by_id(int(topic_id))
        comments = Comment.query(Comment.topic_id == topic.key.id(), Comment.deleted == False).order(Comment.created).fetch()

        params = {"topic": topic,"comments":comments}

        return self.render_template("topic_details.html", params=params)

class TopicDelete(BaseHandler):
    def post(self, topic_id):

        topic = Topic.get_by_id(int(topic_id))
        user = users.get_current_user()

        if topic.author_email == user.email() or users.is_current_user_admin():
            topic.deleted=True
            topic.put()


        params = {"topic":topic, "user":user}
        return self.redirect_to("main-page",params=params)