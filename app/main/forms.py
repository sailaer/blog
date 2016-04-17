from flask.ext.wtf import Form
from wtforms import StringField, SubmitField,TextAreaField,SelectField
from flask.ext.pagedown.fields import PageDownField
from wtforms.validators import Required
from .. import config

class PostForm(Form):
    kind = SelectField(u'kind', choices = [('csapp', 'CSAPP'), ('lisp', 'LISP'), ('acm', '算法导论'), ('every', '杂记'),('program','编程相关'),('lrc', '填词')] )
    body = PageDownField("What's on your mind?", validators=[Required()])
    submit = SubmitField('发表')

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('发表')

class CommentForm(Form):
    name = StringField('昵称：', validators=[Required()])
    body = PageDownField("评论：", validators=[Required()])
    submit = SubmitField('发表')
