from flask import Flask, render_template, flash, redirect, url_for
from datetime import datetime
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# Configurations
app.config['SECRET_KEY'] = '4fe12cd24c82224cf6078407'

# Dummy blog post data
posts = [
    {
        'author': 'David Kinsley',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': datetime.now().strftime('%Y-%m-%d')
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': datetime.now().strftime('%Y-%m-%d')
    },
    {
        'author': 'Jane Smith',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': datetime.now().strftime('%Y-%m-%d')
    },
    {
        'author': 'Alice Brown',
        'title': 'Blog Post 4',
        'content': 'Fourth post content',
        'date_posted': datetime.now().strftime('%Y-%m-%d')
    },
    {
        'author': 'Charlie White',
        'title': 'Blog Post 5',
        'content': 'Fifth post content',
        'date_posted': datetime.now().strftime('%Y-%m-%d')
    }
]

# Route for the home page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

# Route for the about page
@app.route("/about")
def about():
    return render_template('about.html', title='About')

# Route for the registration page
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')  # Category is 'success'
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Welcome back, {form.username.data}!', 'success')  # Category is 'success'
        return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
