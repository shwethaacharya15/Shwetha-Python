# Import necessary modules from Flask
from flask import Flask, render_template, request
#render_template() is used to serve HTML files instead of just returning plain text.
#It helps separate frontend (HTML, CSS) from backend (Python logic).

#request is used to handle form submissions (GET, POST requests).
#It helps retrieve user input (e.g., username, password) from an HTML form.

# Create an instance of the Flask application
app = Flask(__name__)

# Define a route for the home page ("/") - This will display the login form
@app.route("/")
def home():
    # Renders the login.html file (frontend UI)
    return render_template("login.html")

# Define a route for handling the login form submission
@app.route("/login", methods=["POST"])  # Accepts only POST requests
def login():
    # Retrieve username and password entered by the user from the form
    username = request.form["username"]
    password = request.form["password"]

    # Validate the username and password (hardcoded for now)
    if username == "Shwetha Acharya" and password == "Shw@28":
        return "<h1>Login Successful!</h1>"  # Display success message if credentials are correct
    else:
        return "<h1>Invalid credentials, try again!</h1>"  # Display error message if incorrect

# Run the Flask application only if this script is executed directly (not imported as a module)
if __name__ == "__main__":
    # Start the Flask development server with debugging enabled
    app.run(debug=True)

