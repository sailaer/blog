# -*- coding: utf8 -*-
from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app
from . import main
from .forms import PostForm,CommentForm
from flask.ext.login import login_required, current_user
from .. import db
from ..models import User, Post, Comment


@main.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if current_user.is_administrator and \
            form.validate_on_submit():
        post = Post(body=form.body.data,
                    author=current_user._get_current_object(),
                    kind = form.kind.data)
        db.session.add(post)
        return redirect(url_for('.index'))
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    return render_template('index.html', form=form, posts=posts,
                           pagination=pagination)




@main.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    post = Post.query.get_or_404(id)
    if not current_user.is_administrator() :
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.body = form.body.data
        post.kind = form.kind.data
        db.session.add(post)
        flash('The post has been updated.')
        return redirect(url_for('.post', id=post.id))
    form.body.data = post.body
    return render_template('edit_post.html', form=form)

@main.route('/post/<int:id>', methods=['GET', 'POST'])
def post(id):
    post = Post.query.get_or_404(id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(body=form.body.data,
                          post=post,
                          name=form.name.data)
        db.session.add(comment)
        flash('Your comment has been published.')
        return redirect(url_for('.post', id=post.id, page=-1))
    page = request.args.get('page', 1, type=int)
    if page == -1:
        page = (post.comments.count() - 1) // \
            current_app.config['FLASKY_COMMENTS_PER_PAGE'] + 1
    pagination = post.comments.order_by(Comment.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_COMMENTS_PER_PAGE'],
        error_out=False)
    comments = pagination.items
    return render_template('post.html', posts=[post], form=form,
                           comments=comments, pagination=pagination)


@main.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    post = Post.query.get_or_404(id)
    if not current_user.is_administrator() :
        abort(403)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('.index'))

@main.route('/deleteCommit/<int:id>', methods=['GET', 'POST'])
def deleteComment(id):
    comment = Comment.query.get_or_404(id)
    if not current_user.is_administrator() :
        abort(403)
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('.post', id=comment.post_id))

@main.route('/about')
def about():
    return render_template('about.html')

