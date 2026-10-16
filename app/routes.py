from flask import (
    Blueprint, render_template, redirect, url_for,
    flash, request, current_app
)
from flask_mail import Message

from app.forms import ContactForm
from app import mail 

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('index.html')


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/skills')
def skills():
    return render_template('skills.html')


@main.route('/services')
def services():
    return render_template('services.html')


@main.route('/projects')
def projects():
    return render_template('projects.html')


@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        # Build the email
        msg = Message(
            subject=f"New contact from {form.name.data}",
            recipients=[current_app.config['CONTACT_RECEIVER_EMAIL']],
            reply_to=form.email.data,
        )
        msg.body = (
            f"Name: {form.name.data}\n"
            f"Email: {form.email.data}\n\n"
            f"Message:\n{form.message.data}"
        )

        try:
            mail.send(msg)
            flash("Thanks! Your message was sent successfully.", "success")
        except Exception as e:
            flash("Sorry, something went wrong sending your message. Please try again.", "error")
            # Log the real error for debugging
            current_app.logger.exception(f"Mail send failed: {e}")

        return redirect(url_for('main.contact'))

    return render_template('contact.html', form=form)


# --- Error handlers ---
@main.app_errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def server_error(error):
    return render_template('500.html'), 500