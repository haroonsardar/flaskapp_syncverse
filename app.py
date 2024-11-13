# Import necessary modules and libraries
from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

#Deploy App on ng-rok
from pyngrok import ngrok
from flask import Flask, request, render_template
ngrok.set_auth_token("2oNiPImS0sQ4kx4bqftIb18UmPG_5rYh1sjeC4BDQv9VvTCVw")
public_url = ngrok.connect(5000)
print("Ngrok URL:", public_url)
# Initialize the Flask application with specific folders for templates and static files
app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = 'your_secret_key'  # Set a secret key for session management and flash messages

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the app
db = SQLAlchemy(app)

# Define the User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each user
    name = db.Column(db.String(150), nullable=False)  # User's name
    email = db.Column(db.String(150), unique=True, nullable=False)  # User's unique email
    password = db.Column(db.String(200), nullable=False)  # Hashed password

# Route for the home page, redirects to login by default
@app.route('/')
def index():
    return redirect(url_for('auth', action='login'))

# Route for authentication (login and signup)
@app.route('/auth', methods=['GET', 'POST'])
def auth():
    action = request.args.get('action', 'login')  # Determine if login or signup

    if request.method == 'POST':
        # Get form data for email and password
        email = request.form.get('email')
        password = request.form.get('password')

        # Login process
        if action == 'login':
            user = User.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                session['user_id'] = user.id  # Store user ID in session
                flash("Login successful!")
                return redirect(url_for('dashboard'))
            else:
                flash("Invalid credentials, please try again.")

        # Signup process
        elif action == 'signup':
            name = request.form.get('name')
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                flash("Email already registered. Please log in.")
                return redirect(url_for('auth', action='login'))

            # Hash the password and create a new user
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            new_user = User(name=name, email=email, password=hashed_password)
            try:
                db.session.add(new_user)
                db.session.commit()
                flash("User registered successfully!")  # Success message on signup
                return redirect(url_for('auth', action='login'))
            except Exception as e:
                db.session.rollback()
                flash(f"An error occurred: {e}")
                return redirect(url_for('auth', action='signup'))

    # Render the authentication page with login or signup action
    return render_template('auth.html', action=action)

# Route for the dashboard, accessible only if logged in
@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        return render_template('dashboard.html', user=user)
    else:
        flash("Please log in to access the dashboard.")
        return redirect(url_for('auth', action='login'))

# Route for the profile page, accessible only if logged in
@app.route('/profile')
def profile():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        return render_template('profile.html', user=user)
    else:
        flash("Please log in to access the profile.")
        return redirect(url_for('auth', action='login'))

# Route for a results page (e.g., displaying some generated content)
@app.route('/result')
def result():
    return render_template('result.html')  # Ensure this template exists

# Route for logging out the user
@app.route('/logout')
def logout():
    session.clear()  # Clear the session data
    flash("You have been logged out.")
    return redirect(url_for('auth', action='login'))

# Run the app
if __name__ == '__main__':
    # Create the database if it doesn't exist
    if not os.path.exists("users.db"):
        with app.app_context():
            db.create_all()
            print("Database created successfully!")
    app.run()  # Start the Flask server in debug mode
