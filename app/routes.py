import os


# pyrefly: ignore[missing-import]
from flask import (
    Blueprint, render_template, redirect, url_for,
    flash, current_app, request
)

# Brevo HTTPS API — works on PythonAnywhere free tier (port 443)
# pyrefly: ignore[missing-import]
from brevo import Brevo
# pyrefly: ignore[missing-import]
from brevo.transactional_emails import (
    SendTransacEmailRequestSender,
    SendTransacEmailRequestToItem,
)

from app.forms import ContactForm

# Content data (editable by you)
from content.skills import SKILL_CATEGORIES
from content.services import SERVICES
from content.projects import PROJECTS
from content.catalogue_data import (
    FRAMEWORKS,
    SYSTEM_PROJECTS,
    FRONTEND_OPTIONS,
    DATABASE_OPTIONS,
    ADDON_MODULES,
    DEVOPS_OPTIONS,
    PALETTES,
    UI_STYLING_TIERS,
    CURRENCIES,
)


main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('index.html')


@main.route('/estimator')
def estimator():
    return render_template(
        'estimator.html',
        frameworks=FRAMEWORKS,
        projects=SYSTEM_PROJECTS,
        frontends=FRONTEND_OPTIONS,
        databases=DATABASE_OPTIONS,
        addons=ADDON_MODULES,
        devops=DEVOPS_OPTIONS,
        palettes=PALETTES,
        ui_tiers=UI_STYLING_TIERS,
        currencies=CURRENCIES,
    )


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/skills')
def skills():
    return render_template('skills.html', skill_categories=SKILL_CATEGORIES)


@main.route('/services')
def services():
    return render_template('services.html', services=SERVICES)


@main.route('/projects')
def projects():
    return render_template('projects.html', projects=PROJECTS)


@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    # Pre-fill message if redirected from project estimator
    if request.method == 'GET' and request.args.get('spec'):
        form.message.data = request.args.get('spec')

    if form.validate_on_submit():
        try:
            client = Brevo(api_key=os.environ.get('BREVO_API_KEY'))

            client.transactional_emails.send_transac_email(
                sender=SendTransacEmailRequestSender(
                    email=os.environ.get('MAIL_DEFAULT_SENDER'),
                    name=os.environ.get('MAIL_DEFAULT_SENDER_NAME', 'Portfolio Contact'),
                ),
                to=[
                    SendTransacEmailRequestToItem(
                        email=os.environ.get('CONTACT_RECEIVER_EMAIL'),
                        name=os.environ.get('MAIL_DEFAULT_SENDER_NAME', 'Laban Wanjala'),
                    ),
                ],
                reply_to=SendTransacEmailRequestToItem(
                    email=form.email.data,
                    name=form.name.data,
                ),
                subject=f"New contact from {form.name.data}",
                html_content=f"""
                    <h2>New Contact Form Submission</h2>
                    <p><strong>Name:</strong> {form.name.data}</p>
                    <p><strong>Email:</strong> {form.email.data}</p>
                    <hr>
                    <p><strong>Message:</strong></p>
                    <p style="white-space: pre-wrap;">{form.message.data}</p>
                """,
            )

            flash("Thanks! Your message was sent successfully.", "success")

        except Exception as e:
            flash("Sorry, something went wrong sending your message. Please try again.", "error")
            current_app.logger.exception(f"Brevo API send failed: {e}")

        return redirect(url_for('main.contact'))

    return render_template('contact.html', form=form)


# --- Error handlers ---
@main.app_errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def server_error(error):
    return render_template('500.html'), 500