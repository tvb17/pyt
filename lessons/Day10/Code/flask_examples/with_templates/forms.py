# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError

__author__ = 'sobolevn'


class BlogPostForm(FlaskForm):
    title = StringField(label='Title', validators=[
        validators.Length(min=4, max=140),
    ])
    text = StringField(label='Article Text', validators=[
        validators.Length(min=10, max=3500),
    ])
