from flask import (
            Flask,
            render_template,
            request,
            redirect,
            url_for,
            flash
        )


app = Flask(__name__)
app.secret_key = "********123456"


@app.route('/')
def index():
    return render_template('awatax/index.html',home='active')

@app.route('/about-us')
def about_us():
    return render_template('awatax/about.html',about_us = "active")

@app.route('/meet-our-team')
def meet_our_team():
    return render_template('awatax/team.html',about_us = "active")

@app.route('/gallery')
def gallery():
    return render_template('awatax/gallery.html',gallery = "active")

@app.route('/projects-completed')
def projects():
    return render_template('awatax/projects.html',projects = "active")

@app.route('/contact-us')
def contact_us():
    return render_template('awatax/contact.html',contact_us = "active")

@app.route('/job-opportunities')
def job_opportunities():
    return render_template('awatax/jobs.html',careers = "active")

@app.route('/internship-opportunities')
def internship_opportunities():
    return render_template('awatax/intern.html',careers = "active")

@app.route('/services')
def services():
    return render_template('awatax/services.html',services = "active")


if __name__ == '__main__':
    app.run(debug = True,port=8070)