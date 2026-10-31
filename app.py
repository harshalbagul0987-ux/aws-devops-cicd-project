
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Flask Website</title>
    </head>
    <body>
        <h1>Welcome to My Flask Website!</h1>
        <p>This is the home page. Deployed using Docker and AWS EC2 by GitHub Actions.</p>
        <a href="/about">Go to About Page</a>
    </body>
    </html>
    """

@app.route("/about")
def about():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>About Page</title>
    </head>
    <body>
        <h1>About My Project</h1>
        <p>This is an AWS DevOps CI/CD project.</p>
        <p>Technologies: Python, Flask, Docker, GitHub Actions and AWS EC2.</p>
        <a href="/">Go to Home Page</a>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
