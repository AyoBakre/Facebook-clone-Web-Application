from facebook import app
from flask_login import current_user
import os
from PIL import Image
import secrets


def save_post_image(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/img/posts', picture_fn)
    output_size = (800, 350)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


def save_cover_image(form_picture):
    if form_picture is None:
        picture_fn = current_user.cover_image
        return picture_fn
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/img/cover', picture_fn)
    output_size = (950, 350)
    i = Image.open(form_picture)
    i.resize(output_size)
    i.save(picture_path)
    return picture_fn


def save_profile_picture(form_picture):
    if form_picture is None:
        picture_fn = current_user.profile_image
        return picture_fn
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/img/avatar', picture_fn)
    output_size = (225, 225)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    prev_picture = os.path.join(app.root_path, 'static/img/avatar', current_user.profile_image)
    if current_user.profile_image != 'default.jpg' and os.path.exists(prev_picture):
        os.remove(prev_picture)
    return picture_fn
