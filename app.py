from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello_world():
    return render_template("index.html", title="Home", active_nav_link="home")

@app.route("/services")
def service():
    return render_template("services.html", title="Services", active_nav_link="services")

@app.route("/about")
def about():
    return render_template("about.html", title="About Us", active_nav_link="about")

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact Us", active_nav_link="contact")


if __name__ == '__main__':
    app.run()
