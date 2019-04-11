from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///memes.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_like(meme_id):
	to_like = session.query(meme).filter_by(meme_id=meme_id).first()
	to_like.likes = to_like.likes+1

def add_comment(comment_poster, comment_rating , comment_content,on_post):
	comment_object = comment(
		comment_poster = comment_poster,
		comment_rating = comment_rating,
		comment_content = comment_content,
		on_post = on_post)
	session.add(comment_object)
	session.commit()
	return comment_object


def query_comments_by_post(on_post):
	comments = session.query(comment).filter_by(on_post = on_post).all()
	return comments




