# from flask import Flask

# # This creates our web application
# # _name_ is just a Python thing - don't worry about it for now
# app = Flask(_name_)

# # This is a "route" - it tells Flask what to show when someone visits our website
# @app.route('/')
# def home():
#     return '<h1>Hello World! My first website! 🎉</h1>'

# @app.route('/about')
# def about():
#     return '<h1>About Me</h1><p>I am learning Flask!</p>'

# # This starts our website
# if _name_ == '_main_':
#     app.run(debug=True)

from flask import Flask, render_template

# Create our app
app = Flask(__name__)

# Sample data about you (change this to your info!)
ABOUT_ME = {
    'name': 'alinda',
    'age': 22,
    'school': 'Makerere University',
    'hobbies': ['Watching', 'Gaming', 'Music', 'Travelling', 'Reading novels'],
    'bio': 'I am just a chill girl!'
}

# Sample projects (add your own!)
PROJECTS = [
    {
        'title': 'My Personal Website',
        'description': 'This portfolio website built with Flask! It shows some of the basic details one should know about me. ',
        'technologies': ['Python', 'Flask', 'HTML', 'CSS'],
        'link': '#'
    },
    {
        'title': 'Glamazon',
        'description': "This is an online salon app, where one can make appointments with the saloon owner, chat with them privately, reschedule or cancel bookings according to the person's proram, and choose a service based the way tey are grouped for easier use.",
        'technologies': ['Flutter'],
        'link': '#'
    },
    {
        'title' : "Conershop",
        'description' : "this is a group project we did with five other collegues. it is an online shopping app withh all kinds of otems you could search for, including electronics, clothes for both men and women, shoes, and many more.",
        'technologies' : ['Django'],
        'link' : '#'
    },
]

# Routes (the pages of our website)
@app.route('/')
def home():
    """This is the main page"""
    return render_template('index.html', about=ABOUT_ME, projects=PROJECTS[:3])

@app.route('/about')
def about():
    """This is the about page"""
    return render_template('about.html', about=ABOUT_ME)

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route("/contact")
def contact():
    return render_template("contacts.html")

# Start the website
if __name__ == '__main__':
    app.run(debug=True)