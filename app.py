
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AWS DevOps CI/CD Project</title>
        <style>
            * { box-sizing: border-box; }
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #0b1120;
                color: #e5e7eb;
                line-height: 1.6;
            }
            nav {
                padding: 20px 8%;
                display: flex;
                justify-content: space-between;
                background: #111827;
                border-bottom: 1px solid #263449;
            }
            nav a { color: #60a5fa; text-decoration: none; margin-left: 20px; }
            .hero { padding: 85px 8%; text-align: center; }
            .hero h1 { font-size: 42px; color: white; }
            .hero h1 span { color: #38bdf8; }
            .hero p { color: #aebbd0; font-size: 18px; }
            .btn {
                display: inline-block;
                margin-top: 20px;
                padding: 12px 24px;
                background: #2563eb;
                color: white;
                border-radius: 8px;
                text-decoration: none;
            }
            .section { padding: 35px 8% 70px; text-align: center; }
            .cards {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
                gap: 18px;
                margin-top: 30px;
            }
            .card {
                background: #172235;
                padding: 25px;
                border: 1px solid #2b405c;
                border-radius: 12px;
            }
            .card h3 { color: #38bdf8; }
            footer {
                text-align: center;
                padding: 25px;
                background: #111827;
                color: #9ca3af;
            }
        </style>
    </head>
    <body>
        <nav>
            <strong>🚀 AWS DevOps Project</strong>
            <div>
                <a href="/">Home</a>
                <a href="/about">About</a>
                <a href="/health">Health</a>
            </div>
        </nav>

        <section class="hero">
            <h1>Welcome to <span>My DevOps Project</span></h1>
            <p>Automated CI/CD Pipeline using GitHub Actions, Docker and AWS EC2.</p>
            <p>Build • Test • Deploy • Monitor</p>
            <a class="btn" href="/about">Explore Project</a>
        </section>

        <section class="section">
            <h2>Technologies Used</h2>
            <div class="cards">
                <div class="card"><h3>Python</h3><p>Application development</p></div>
                <div class="card"><h3>Flask</h3><p>Web framework</p></div>
                <div class="card"><h3>Docker</h3><p>Containerization</p></div>
                <div class="card"><h3>GitHub Actions</h3><p>CI/CD automation</p></div>
                <div class="card"><h3>AWS EC2</h3><p>Cloud deployment</p></div>
            </div>
        </section>

        <footer>
            AWS DevOps CI/CD Demo | Deployed with GitHub Actions 🚀
        </footer>
    </body>
    </html>
    """

@app.route("/about")
def about():
    return """
    <!DOCTYPE html>
    <html>
    <head><title>About Project</title></head>
    <body style="font-family:Arial;background:#0b1120;color:white;padding:40px">
        <h1>About My AWS DevOps Project</h1>
        <p>This project demonstrates an automated CI/CD pipeline.</p>
        <p>Technologies: Python, Flask, Docker, GitHub Actions and AWS EC2.</p>
        <a href="/" style="color:#38bdf8">Go to Home Page</a>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
