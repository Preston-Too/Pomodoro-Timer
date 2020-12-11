from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import UpdateProfile
from ..models import User
from flask_login import login_required,current_user
from .. import db,photos
import markdown2


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''


    title = 'Home - Welcome to pomodoro'
    content = "WELCOME TO POMODORO APP"

    return render_template('index.html', title = title,content = content)

@main.route('/about')
def about():
    return render_template('about.html', title = 'About')

@main.route('/pomodoro')
@login_required
def pomodoro():

    '''
    View root page function that returns the index page and its data
    '''


    title = 'Home - Welcome to pomodoro'
    content = "WELCOME TO POMODORO APP"

    return render_template('pomodoro.html', title = title,content = content)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/reason/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_reason(id):
    form = ReasonForm()
    reason = get_reason(id)
    if form.validate_on_submit():
        title = form.title.data
        reason = form.reason.data

        # Updated reason instance
        new_reason = Reason(reason_id=reason.id,reason_title=title,reason=reason,user=current_user)

        # save reason method
        new_reason.save_reason()
        return redirect(url_for('.reason',id = reason.id ))

    title = f'{reason.title} reason'
    return render_template('new_reason.html',title = title, reason_form=form, reason=reason)