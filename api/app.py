from flask import Flask, render_template, request, abort, send_from_directory, url_for, redirect
import os

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/success/<name>')
def success(name):
    return f"<h2> Welcome to the page Chanp:{name}.</h2>"

@app.route('/login', methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form.get('nm')
        return redirect(url_for('success', name=user))
    else:
        
        return render_template('login.html') 



def home():
    return render_template('index.html')


@app.route('/skills')
def skills():
    return render_template('skills.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/projects/days')
def days():
    return render_template('days.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/about/resume', methods=["POST", "GET"])
def resume():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/img/'
    return send_from_directory(filepath, 'DeujaResume.pdf')


@app.route('/images')
def images():
    return render_template('images.html')


@app.route('/projects/game')
def game():
    return render_template('game.html')


if __name__ == '__main__':
    app.run(debug=True)
