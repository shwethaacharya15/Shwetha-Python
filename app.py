# Import necessary modules from Flask
#This initializes the Flask application and allows you to define routes.
#It helps separate frontend (HTML, CSS) from backend logic, allowing you to return an HTML page instead of plain text
#Helps retrieve user input from forms or query parameters.
#Used after successful actions like form submission to send users to another page.
#Helps avoid hardcoding URLs and ensures routing works correctly across different environments.
from flask import Flask, render_template, request, redirect, url_for

# Create an instance of the Flask application
app = Flask(__name__)

# Define a route for the home page ("/") - Redirect to the registration page first
@app.route("/")
def home():
    return redirect(url_for("register"))

# Define a route for the registration page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Retrieve user details from the form
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        phone = request.form["phone"]

        # Redirect to login page after successful registration
        return redirect(url_for("login"))

    return render_template("register.html")  # Serve the registration form

# Define a route for the login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Retrieve username and password entered by the user from the form
        username = request.form["username"]
        password = request.form["password"]

        # Validate the username and password (hardcoded for now)
        if username == "Shwetha Acharya" and password == "Shw@28":
            return "<h1>Login Successful!</h1>"  # Display success message if credentials are correct
        else:
            return "<h1>Invalid credentials, try again!</h1>"  # Display error message if incorrect

    return render_template("login.html")  # Serve the login form

# Run the Flask application only if this script is executed directly (not imported as a module)
if __name__ == "__main__":
    # Start the Flask development server with debugging enabled
    app.run(debug=True)
