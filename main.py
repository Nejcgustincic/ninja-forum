#!/usr/bin/env python
import webapp2
from handlers.base import MainHandler, CookieHandler, AboutHandler
from handlers.comments import CommentAdd, CommentList, CommentDelete
from handlers.topics import TopicCreateHandler, TopicDetails, TopicDelete
from workers.email_comment_worker import EmailNewCommentWorker

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/about', AboutHandler, name="about"),
    webapp2.Route('/set-cookie', CookieHandler, name="nastavi-cookie"),
    webapp2.Route('/topic/create', TopicCreateHandler, name="topic-create"),
    webapp2.Route('/topic/<topic_id:\d+>', TopicDetails, name="topic-details"),
    webapp2.Route('/topic/<topic_id:\d+>/comment/add', CommentAdd, name="comment-add"),
    webapp2.Route('/comment-list', CommentList, name="comment-list"),
    webapp2.Route('/topic/<topic_id:\d+>/delete', TopicDelete, name="topic-delete"),
    webapp2.Route('/comment/<comment_id:\d+>/delete', CommentDelete, name="comment-delete"),

    webapp2.Route("/task/email-new-comment", EmailNewCommentWorker)
], debug=True)
