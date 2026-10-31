
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
<title>Neon DevOps | AWS CI/CD Project</title>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: Arial, sans-serif;
    background: #070914;
    color: #f5f7ff;
    line-height: 1.6;
    overflow-x: hidden;
}

:root {
    --cyan: #00eaff;
    --purple: #a855f7;
    --card: #11182b;
    --muted: #a7b2cc;
}

nav {
    position: sticky;
    top: 0;
    z-index: 10;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 18px 8%;
    background: rgba(7, 9, 20, .92);
    border-bottom: 1px solid #1e3553;
    backdrop-filter: blur(12px);
}

.logo {
    font-size: 22px;
    font-weight: bold;
    color: var(--cyan);
    text-shadow: 0 0 12px var(--cyan);
}

nav a {
    color: white;
    text-decoration: none;
    margin-left: 22px;
    font-size: 14px;
    transition: .3s;
}

nav a:hover {
    color: var(--cyan);
}

.hero {
    min-height: 570px;
    padding: 110px 8% 90px;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background:
        radial-gradient(ellipse at 50% 30%,
        rgba(0, 234, 255, .14), transparent 55%),
        radial-gradient(ellipse at 80% 70%,
        rgba(168, 85, 247, .12), transparent 45%);
}

.tag {
    color: var(--cyan);
    border: 1px solid var(--cyan);
    padding: 7px 17px;
    border-radius: 30px;
    font-size: 13px;
    letter-spacing: 1px;
    box-shadow: 0 0 15px #00eaff33;
    animation: pulse 2s infinite;
}

.hero h1 {
    font-size: clamp(35px, 6vw, 65px);
    line-height: 1.15;
    margin: 25px 0;
    animation: fadeUp 1s ease;
}

.gradient {
    background: linear-gradient(90deg, #00eaff, #a855f7);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    text-shadow: none;
}

.hero p {
    color: var(--muted);
    max-width: 700px;
    font-size: 18px;
    margin-bottom: 28px;
}

.btn {
    display: inline-block;
    padding: 13px 27px;
    margin: 8px;
    border-radius: 8px;
    background: linear-gradient(90deg, #00bfff, #8b5cf6);
    color: white;
    text-decoration: none;
    font-weight: bold;
    transition: .3s;
    box-shadow: 0 0 18px #00eaff44;
}

.btn:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 30px #00eaff99;
}

.btn.secondary {
    background: transparent;
    border: 1px solid var(--cyan);
    box-shadow: none;
}

.section {
    padding: 75px 8%;
    text-align: center;
}

.section h2 {
    font-size: 32px;
    margin-bottom: 12px;
}

.subtitle {
    color: var(--muted);
    margin-bottom: 38px;
}

.cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
    gap: 20px;
}

.card {
    background: linear-gradient(145deg, #151f36, #0d1425);
    padding: 28px 20px;
    border: 1px solid #263c5d;
    border-radius: 14px;
    transition: .35s;
}

.card:hover {
    transform: translateY(-9px);
    border-color: var(--cyan);
    box-shadow: 0 0 22px #00eaff30;
}

.card .symbol {
    font-size: 30px;
    margin-bottom: 12px;
}

.card h3 {
    color: var(--cyan);
    margin-bottom: 10px;
}

.card p {
    color: var(--muted);
    font-size: 14px;
}

.pipeline {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 18px;
}

.step {
    padding: 25px 15px;
    background: #101a30;
    border: 1px solid #314b70;
    border-radius: 12px;
    position: relative;
    animation: glow 3s infinite alternate;
}

.step h3 {
    color: var(--cyan);
    margin: 10px 0;
}

.step span {
    font-size: 28px;
}

.architecture {
    max-width: 950px;
    margin: auto;
    padding: 35px 20px;
    border: 1px solid #284766;
    border-radius: 18px;
    background: #0d1425;
    box-shadow: 0 0 30px #00eaff18;
}

.arch-row {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
}

.arch-box {
    padding: 17px 20px;
    min-width: 145px;
    border: 1px solid var(--cyan);
    border-radius: 10px;
    color: var(--cyan);
    background: #10233a;
    box-shadow: 0 0 15px #00eaff22;
}

.arrow {
    color: var(--purple);
    font-size: 25px;
    font-weight: bold;
}

.about-box {
    max-width: 800px;
    margin: auto;
    padding: 35px;
    background: var(--card);
    border: 1px solid #314b70;
    border-radius: 15px;
}

.about-box p {
    color: var(--muted);
    margin-top: 12px;
}

footer {
    text-align: center;
    padding: 30px 15px;
    border-top: 1px solid #263c5d;
    color: var(--muted);
}

footer span {
    color: var(--cyan);
}

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(25px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes pulse {
    50% { box-shadow: 0 0 25px #00eaff77; }
}

@keyframes glow {
    from { box-shadow: 0 0 5px #00eaff15; }
    to { box-shadow: 0 0 18px #00eaff44; }
}

@media (max-width: 650px) {
    nav {
        flex-direction: column;
        gap: 12px;
    }

    nav a {
        margin: 0 7px;
        font-size: 12px;
    }

    .hero {
        min-height: 480px;
        padding: 75px 6%;
    }

    .hero p {
        font-size: 15px;
    }

    .section {
        padding: 55px 6%;
    }

    .arch-row {
        flex-direction: column;
    }

    .arrow {
        transform: rotate(90deg);
    }
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation: none !important;
        transition: none !important;
        scroll-behavior: auto !important;
    }
}
</style>
</head>

<body>

<nav>
    <div class="logo">⚡ NEON DEVOPS</div>
    <div>
        <a href="/">Home</a>
        <a href="#technologies">Tech</a>
        <a href="#pipeline">Pipeline</a>
        <a href="#architecture">Architecture</a>
        <a href="/about">About</a>
    </div>
</nav>

<section class="hero">
    <div class="tag">AWS CLOUD • DEVOPS • AUTOMATION</div>

    <h1>
        Welcome to<br>
        <span class="gradient">My DevOps Project</span>
    </h1>

    <p>
        Building and deploying applications through an
        automated CI/CD pipeline using GitHub Actions,
        Docker and AWS EC2.
    </p>

    <div>
        <a href="#pipeline" class="btn">Explore Pipeline ↗</a>
        <a href="/about" class="btn secondary">About Project</a>
    </div>
</section>

<section class="section" id="technologies">
    <h2>⚙ Technologies Used</h2>
    <p class="subtitle">Tools powering this cloud deployment</p>

    <div class="cards">
        <div class="card">
            <div class="symbol">🐍</div>
            <h3>Python</h3>
            <p>Application development</p>
        </div>

        <div class="card">
            <div class="symbol">🌐</div>
            <h3>Flask</h3>
            <p>Lightweight web framework</p>
        </div>

        <div class="card">
            <div class="symbol">🐳</div>
            <h3>Docker</h3>
            <p>Application containerization</p>
        </div>

        <div class="card">
            <div class="symbol">⚙</div>
            <h3>GitHub Actions</h3>
            <p>CI/CD workflow automation</p>
        </div>

        <div class="card">
            <div class="symbol">☁</div>
            <h3>AWS EC2</h3>
            <p>Cloud hosting and deployment</p>
        </div>
    </div>
</section>

<section class="section" id="pipeline">
    <h2>🚀 CI/CD Pipeline</h2>
    <p class="subtitle">From source code to cloud deployment</p>

    <div class="pipeline">
        <div class="step">
            <span>📁</span>
            <h3>Build</h3>
            <p>Source code pushed to GitHub</p>
        </div>

        <div class="step">
            <span>🧪</span>
            <h3>Test</h3>
            <p>Automated Python unit tests</p>
        </div>

        <div class="step">
            <span>🐳</span>
            <h3>Package</h3>
            <p>Docker image build</p>
        </div>

        <div class="step">
            <span>☁</span>
            <h3>Deploy</h3>
            <p>AWS EC2 deployment using SSM</p>
        </div>

        <div class="step">
            <span>📊</span>
            <h3>Monitor</h3>
            <p>Application health endpoint</p>
        </div>
    </div>
</section>

<section class="section" id="architecture">
    <h2>🏗 Project Architecture</h2>
    <p class="subtitle">How the deployment components connect</p>

    <div class="architecture">
        <div class="arch-row">
            <div class="arch-box">👨‍💻 Developer</div>
            <div class="arrow">→</div>
            <div class="arch-box">GitHub</div>
            <div class="arrow">→</div>
            <div class="arch-box">GitHub Actions</div>
        </div>

        <div class="arrow">↓</div>

        <div class="arch-row">
            <div class="arch-box">Automated Tests</div>
            <div class="arrow">→</div>
            <div class="arch-box">Docker Build</div>
            <div class="arrow">→</div>
            <div class="arch-box">AWS IAM OIDC</div>
        </div>

        <div class="arrow">↓</div>

        <div class="arch-row">
            <div class="arch-box">AWS Systems Manager</div>
            <div class="arrow">→</div>
            <div class="arch-box">AWS EC2</div>
            <div class="arrow">→</div>
            <div class="arch-box">Flask Application</div>
        </div>
    </div>
</section>

<section class="section">
    <h2>💡 About This Project</h2>
    <p class="subtitle">Learning by building real cloud workflows</p>

    <div class="about-box">
        <h3 class="gradient">Automated AWS DevOps CI/CD Project</h3>
        <p>
            This project demonstrates automated application
            testing, Docker containerization and deployment
            to AWS EC2 using GitHub Actions and AWS Systems Manager.
        </p>
        <p>
            Secure AWS authentication is configured using
            IAM OIDC federation.
        </p>
        <a href="/about" class="btn">View Project Details</a>
    </div>
</section>

<footer>
    <p>⚡ AWS DevOps CI/CD Project</p>
    <p>Built with Python, Flask, Docker & GitHub Actions</p>
    <p>Deployed on <span>AWS EC2</span> 🚀</p>
</footer>

</body>
</html>
"""


@app.route("/about")
def about():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>About | Neon DevOps</title>
<style>
body {
    margin: 0;
    padding: 35px 20px;
    font-family: Arial, sans-serif;
    background: #070914;
    color: white;
    line-height: 1.7;
}
main {
    max-width: 800px;
    margin: 50px auto;
    padding: 35px;
    background: #11182b;
    border: 1px solid #00eaff;
    border-radius: 16px;
    box-shadow: 0 0 25px #00eaff33;
}
h1 { color: #00eaff; }
p { color: #b6c2dc; }
a { color: #00eaff; }
</style>
</head>
<body>
<main>
    <h1>⚡ About My DevOps Project</h1>
    <p>This project demonstrates an automated AWS CI/CD pipeline.</p>
    <h2>Technologies</h2>
    <p>Python, Flask, Docker, GitHub Actions, AWS EC2, AWS SSM and IAM OIDC.</p>
    <h2>Deployment Flow</h2>
    <p>GitHub → GitHub Actions → Tests → Docker → AWS SSM → EC2.</p>
    <a href="/">← Back to Home</a>
</main>
</body>
</html>
"""


@app.route("/health")
def health():
    return jsonify(status="healthy"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
