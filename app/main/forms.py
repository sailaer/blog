# -*- coding: utf8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField,TextAreaField,SelectField
from flask.ext.pagedown.fields import PageDownField
from wtforms.validators import Required
from .. import config

class PostForm(Form):
    kind = SelectField(u'kind', choices = [('算法导论', '算法导论'),('CSAPP', 'CSAPP'), ('LISP', 'LISP'),  ('杂记', '杂记'),('编程相关','编程相关'),('填词', '填词')] )
    body = PageDownField("What's on your mind?", validators=[Required()])
    submit = SubmitField('发表')

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('发表')

class CommentForm(Form):
    name = StringField('昵称：', validators=[Required()])
    body = PageDownField("评论：", validators=[Required()])
    submit = SubmitField('发表')
