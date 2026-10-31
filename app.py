
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

GITHUB_URL = "https://github.com/harshalbagul0987-ux/aws-devops-cicd-project"

STYLE = """
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }

html { scroll-behavior: smooth; }

body {
    font-family: Arial, sans-serif;
    background: #070914;
    color: #f5f7ff;
    line-height: 1.7;
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
    padding: 18px 7%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 15px;
    flex-wrap: wrap;
    background: rgba(7,9,20,.94);
    border-bottom: 1px solid #263449;
    backdrop-filter: blur(12px);
}

.logo {
    color: var(--cyan);
    font-size: 20px;
    font-weight: bold;
}

nav a, .back {
    color: var(--cyan);
    text-decoration: none;
    margin-left: 18px;
}

nav a:hover, .back:hover { color: white; }

.hero {
    padding: 100px 8%;
    text-align: center;
    background:
      radial-gradient(circle at 20% 20%, #06334266, transparent 35%),
      radial-gradient(circle at 80% 30%, #42165d55, transparent 35%);
}

.tag {
    display: inline-block;
    padding: 9px 20px;
    border: 1px solid var(--cyan);
    border-radius: 30px;
    color: var(--cyan);
    letter-spacing: 2px;
    font-size: 13px;
}

.hero h1 {
    font-size: clamp(38px, 6vw, 68px);
    line-height: 1.15;
    margin: 28px 0;
}

.gradient {
    background: linear-gradient(90deg, #00eaff, #a855f7);
    -webkit-background-clip: text;
    color: transparent;
}

.hero p {
    color: var(--muted);
    font-size: 19px;
    max-width: 850px;
    margin: auto;
}

.btn {
    display: inline-block;
    margin: 25px 8px 0;
    padding: 13px 25px;
    border-radius: 10px;
    background: linear-gradient(100deg, #00bce8, #8855f5);
    color: white;
    text-decoration: none;
    font-weight: bold;
    transition: .3s;
}

.btn:hover {
    transform: translateY(-4px);
    box-shadow: 0 0 25px #00eaff66;
}

.btn-outline {
    background: transparent;
    border: 1px solid var(--cyan);
}

section {
    padding: 65px 7%;
    max-width: 1500px;
    margin: auto;
}

.section-title {
    text-align: center;
    font-size: 34px;
    margin-bottom: 12px;
}

.subtitle {
    text-align: center;
    color: var(--muted);
    margin-bottom: 35px;
}

.cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
    gap: 20px;
}

.card {
    background: var(--card);
    border: 1px solid #29435e;
    border-radius: 15px;
    padding: 25px;
    transition: .3s;
}

.card:hover {
    transform: translateY(-6px);
    border-color: var(--cyan);
    box-shadow: 0 0 22px #00eaff22;
}

.card h3 { color: var(--cyan); margin-bottom: 12px; }
.card p, .card li { color: var(--muted); }

.icon { font-size: 30px; margin-bottom: 12px; }

.panel {
    background: var(--card);
    border: 1px solid var(--cyan);
    border-radius: 18px;
    padding: 35px;
    box-shadow: 0 0 25px #00eaff12;
}

.panel h2 { color: var(--cyan); margin-bottom: 18px; }
.panel p { color: var(--muted); margin-bottom: 14px; }

.pipeline {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 14px;
}

.step {
    background: #14243a;
    border: 1px solid var(--cyan);
    border-radius: 12px;
    padding: 20px 10px;
    text-align: center;
    transition: .3s;
}

.step:hover {
    box-shadow: 0 0 20px #00eaff55;
    transform: scale(1.04);
}

.step strong { display: block; color: var(--cyan); }
.step span { color: var(--muted); font-size: 13px; }

ul { padding-left: 20px; }
li { margin: 8px 0; }

.repo-link {
    color: var(--cyan);
    overflow-wrap: anywhere;
}

footer {
    text-align: center;
    padding: 30px;
    border-top: 1px solid #263449;
    color: var(--muted);
}

.reveal {
    animation: appear .8s ease both;
}

@keyframes appear {
    from { opacity: 0; transform: translateY(18px); }
    to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 768px) {
    nav { justify-content: center; }
    nav a { margin: 5px 8px; }
    .hero { padding: 65px 5%; }
    section { padding: 45px 5%; }
    .section-title { font-size: 27px; }
    .panel { padding: 22px; }
    .cards { grid-template-columns: 1fr; }
    .pipeline { grid-template-columns: 1fr 1fr; }
}

@media (max-width: 420px) {
    .pipeline { grid-template-columns: 1fr; }
    .btn { margin: 12px 0 0; }
}
</style>
"""

HOME = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AWS DevOps CI/CD Project</title>
""" + STYLE + """
</head>
<body>
<nav>
  <div class="logo">⚡ DevOps Project</div>
  <div>
    <a href="/">Home</a>
    <a href="/about">About</a>
    <a href="/health">Health</a>
    <a href="{{ repo }}" target="_blank" rel="noopener">GitHub ↗</a>
  </div>
</nav>

<header class="hero reveal">
  <span class="tag">AWS CLOUD • DEVOPS • AUTOMATION</span>
  <h1>Welcome to<br><span class="gradient">My DevOps Project</span></h1>
  <p>
    Building and deploying applications through an automated CI/CD
    pipeline using GitHub Actions, Docker and AWS EC2.
  </p>
  <a class="btn" href="#pipeline">Explore Pipeline ↗</a>
  <a class="btn btn-outline" href="/about">About Project</a>
</header>

<section id="pipeline">
  <h2 class="section-title">🚀 CI/CD Pipeline</h2>
  <p class="subtitle">From source code to cloud deployment</p>
  <div class="pipeline">
    <div class="step">📁 <strong>Build</strong><span>Source code</span></div>
    <div class="step">🧪 <strong>Test</strong><span>Python unit tests</span></div>
    <div class="step">🐳 <strong>Package</strong><span>Docker image</span></div>
    <div class="step">☁️ <strong>Deploy</strong><span>AWS EC2 + SSM</span></div>
    <div class="step">📊 <strong>Monitor</strong><span>Health endpoint</span></div>
  </div>
</section>

<section>
  <h2 class="section-title">🛠 Technologies Used</h2>
  <p class="subtitle">Tools that power this project</p>
  <div class="cards">
    <div class="card"><div class="icon">🐍</div><h3>Python & Flask</h3><p>Backend application and web routes.</p></div>
    <div class="card"><div class="icon">🐳</div><h3>Docker</h3><p>Application containerization.</p></div>
    <div class="card"><div class="icon">⚙️</div><h3>GitHub Actions</h3><p>Automated build, testing and deployment workflow.</p></div>
    <div class="card"><div class="icon">☁️</div><h3>AWS EC2</h3><p>Cloud hosting for the Flask application.</p></div>
    <div class="card"><div class="icon">🔐</div><h3>IAM OIDC & SSM</h3><p>Secure AWS authentication and remote deployment.</p></div>
  </div>
</section>

<footer>
  AWS DevOps CI/CD Project | Built with Python, Flask, Docker and AWS
</footer>
</body>
</html>
"""

ABOUT = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>About | AWS DevOps Project</title>
""" + STYLE + """
</head>
<body>
<nav>
  <div class="logo">⚡ DevOps Project</div>
  <div>
    <a href="/">Home</a>
    <a href="/about">About</a>
    <a href="/health">Health</a>
    <a href="{{ repo }}" target="_blank" rel="noopener">GitHub ↗</a>
  </div>
</nav>

<header class="hero">
  <span class="tag">PROJECT DOCUMENTATION</span>
  <h1>About <span class="gradient">My DevOps Project</span></h1>
  <p>A practical demonstration of automated software delivery
  using cloud and DevOps technologies.</p>
</header>

<section>
  <div class="panel">
    <h2>⚡ Project Overview</h2>
    <p>
      This project demonstrates an automated AWS DevOps CI/CD pipeline.
      It tests a Python Flask application, builds a Docker image and
      deploys the application to an AWS EC2 instance using GitHub Actions
      and AWS Systems Manager.
    </p>
    <p>
      The workflow uses IAM OIDC federation for GitHub Actions
      authentication instead of storing long-lived AWS access keys
      in GitHub repository secrets.
    </p>
    <a class="btn" href="{{ repo }}" target="_blank" rel="noopener">
      View GitHub Repository ↗
    </a>
  </div>
</section>

<section>
  <h2 class="section-title">🎯 Project Objectives</h2>
  <div class="cards">
    <div class="card"><h3>Automation</h3><p>Reduce repetitive manual build, test and deployment tasks.</p></div>
    <div class="card"><h3>Reliability</h3><p>Run automated tests before allowing deployment.</p></div>
    <div class="card"><h3>Security</h3><p>Use OIDC and IAM roles for controlled AWS access.</p></div>
    <div class="card"><h3>Monitoring</h3><p>Provide a health endpoint to check application availability.</p></div>
  </div>
</section>

<section>
  <h2 class="section-title">🛠 Technologies & Their Roles</h2>
  <div class="cards">
    <div class="card"><h3>Python</h3><p>Programming language used to develop the application.</p></div>
    <div class="card"><h3>Flask</h3><p>Lightweight Python web framework for application routes.</p></div>
    <div class="card"><h3>GitHub</h3><p>Source code management and version control.</p></div>
    <div class="card"><h3>GitHub Actions</h3><p>Automates testing, image building and deployment.</p></div>
    <div class="card"><h3>Docker</h3><p>Packages the application and its dependencies in a container.</p></div>
    <div class="card"><h3>AWS EC2</h3><p>Runs the deployed application on a cloud virtual server.</p></div>
    <div class="card"><h3>AWS SSM</h3><p>Runs deployment commands on the EC2 instance remotely.</p></div>
    <div class="card"><h3>IAM OIDC</h3><p>Allows GitHub Actions to assume an AWS IAM role securely.</p></div>
  </div>
</section>

<section>
  <h2 class="section-title">🔄 Deployment Workflow</h2>
  <p class="subtitle">How code moves from a developer's computer to AWS</p>
  <div class="pipeline">
    <div class="step">👨‍💻<strong>Developer</strong><span>Push code</span></div>
    <div class="step">🐙<strong>GitHub</strong><span>Store source</span></div>
    <div class="step">🧪<strong>Test</strong><span>Run unit tests</span></div>
    <div class="step">🐳<strong>Docker</strong><span>Build image</span></div>
    <div class="step">🔐<strong>OIDC</strong><span>AWS role access</span></div>
    <div class="step">☁️<strong>AWS SSM</strong><span>Send commands</span></div>
    <div class="step">🖥️<strong>EC2</strong><span>Run application</span></div>
    <div class="step">💚<strong>Health Check</strong><span>Verify service</span></div>
  </div>
</section>

<section>
  <h2 class="section-title">🌟 Benefits for Different Users</h2>
  <div class="cards">
    <div class="card">
      <div class="icon">🎓</div>
      <h3>Students & Beginners</h3>
      <ul>
        <li>Learn practical DevOps concepts.</li>
        <li>Understand CI/CD pipelines.</li>
        <li>Practice Docker and AWS deployment.</li>
        <li>Build a portfolio project.</li>
      </ul>
    </div>
    <div class="card">
      <div class="icon">👨‍💻</div>
      <h3>Developers</h3>
      <ul>
        <li>Automate repetitive deployment steps.</li>
        <li>Catch errors with automated tests.</li>
        <li>Use consistent application packaging.</li>
        <li>Maintain version-controlled releases.</li>
      </ul>
    </div>
    <div class="card">
      <div class="icon">🏢</div>
      <h3>Teams & Organizations</h3>
      <ul>
        <li>Standardize deployment workflows.</li>
        <li>Reduce manual operational work.</li>
        <li>Apply controlled cloud permissions.</li>
        <li>Improve deployment traceability.</li>
      </ul>
    </div>
    <div class="card">
      <div class="icon">🔍</div>
      <h3>Recruiters & Reviewers</h3>
      <ul>
        <li>See practical cloud skills.</li>
        <li>Review source code on GitHub.</li>
        <li>Inspect automated workflow runs.</li>
        <li>Understand the deployment architecture.</li>
      </ul>
    </div>
  </div>
</section>

<section>
  <h2 class="section-title">🌍 Real-World Use Cases</h2>
  <div class="cards">
    <div class="card"><h3>Web Applications</h3><p>Automate releases of Python-based websites and APIs.</p></div>
    <div class="card"><h3>Development Teams</h3><p>Test code changes before deploying new versions.</p></div>
    <div class="card"><h3>Learning Environments</h3><p>Practice cloud infrastructure and deployment workflows.</p></div>
    <div class="card"><h3>Small Projects</h3><p>Create a repeatable deployment process for lightweight applications.</p></div>
  </div>
</section>

<section>
  <h2 class="section-title">🔐 Security & Monitoring</h2>
  <div class="panel">
    <h2>Security practices</h2>
    <ul>
      <li>GitHub Actions uses AWS IAM OIDC federation.</li>
      <li>IAM roles control which AWS actions are permitted.</li>
      <li>AWS Systems Manager is used for remote deployment.</li>
      <li>No long-lived AWS access keys are required in the workflow.</li>
    </ul>
    <h2 style="margin-top:25px">Application health check</h2>
    <p>Endpoint: <a class="repo-link" href="/health">/health</a></p>
    <p>Expected response: {"status":"healthy"}</p>
    <a class="btn btn-outline" href="/health">Check Application Health</a>
  </div>
</section>

<section>
  <h2 class="section-title">🚀 Getting Started</h2>
  <div class="panel">
    <h2>Requirements</h2>
    <ul>
      <li>Python 3 and pip</li>
      <li>Git and a GitHub account</li>
      <li>Docker</li>
      <li>AWS account with configured EC2 and IAM permissions</li>
    </ul>
    
    <p style="margin-top:20px">
      <a class="repo-link" href="/">← Back to Home</a>
    </p>
  </div>
</section>

<footer>
  AWS DevOps CI/CD Project | Python • Flask • Docker • GitHub Actions • AWS
</footer>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HOME, repo=GITHUB_URL)


@app.route("/about")
def about():
    return render_template_string(ABOUT, repo=GITHUB_URL)


@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

@app.route("/api/status")
def api_status():
    return jsonify({
        "application": "AWS DevOps CI/CD Project",
        "status": "online",
        "health": "healthy",
        "framework": "Flask",
        "monitoring": "Application health endpoint"
    }), 200


MONITOR = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Monitoring Dashboard</title>
""" + STYLE + """
</head>
<body>
<nav>
  <div class="logo">⚡ DevOps Monitoring</div>
  <div>
    <a href="/">Home</a>
    <a href="/about">About</a>
    <a href="/health">Health</a>
    <a href="{{ repo }}" target="_blank" rel="noopener">GitHub ↗</a>
  </div>
</nav>

<section class="hero">
  <span class="tag">APPLICATION MONITORING</span>
  <h1>Live <span class="gradient">Monitoring Dashboard</span></h1>
  <p>Check your Flask application health and monitoring status.</p>
</section>

<section>
  <div class="cards">
    <div class="card">
      <h3>Application Status</h3>
      <p id="appStatus">Checking...</p>
    </div>
    <div class="card">
      <h3>Health Check</h3>
      <p id="healthStatus">Checking...</p>
    </div>
    <div class="card">
      <h3>Framework</h3>
      <p>Python Flask</p>
    </div>
    <div class="card">
      <h3>CI/CD Workflow</h3>
      <p><a class="repo-link" href="{{ repo }}/actions" target="_blank" rel="noopener">View GitHub Actions ↗</a></p>
    </div>
  </div>

  <div class="panel" style="margin-top:30px;text-align:center">
    <h2>Monitoring Controls</h2>
    <p id="lastUpdated">Not checked yet</p>
    <button class="btn" onclick="checkStatus()">↻ Refresh Status</button>
  </div>
</section>

<footer>AWS DevOps CI/CD Project | Monitoring Dashboard</footer>

<script>
async function checkStatus() {
  const appStatus = document.getElementById("appStatus");
  const healthStatus = document.getElementById("healthStatus");
  const lastUpdated = document.getElementById("lastUpdated");

  appStatus.textContent = "Checking...";
  healthStatus.textContent = "Checking...";

  try {
    const response = await fetch("/api/status", {cache: "no-store"});
    if (!response.ok) throw new Error("Status check failed");

    const data = await response.json();
    appStatus.textContent = data.status.toUpperCase();
    healthStatus.textContent = data.health.toUpperCase();
    lastUpdated.textContent = "Last checked: " + new Date().toLocaleString();
  } catch (error) {
    appStatus.textContent = "OFFLINE / ERROR";
    healthStatus.textContent = "UNAVAILABLE";
    lastUpdated.textContent = "Unable to reach application";
  }
}

checkStatus();
</script>
</body>
</html>
"""


@app.route("/monitor")
def monitor():
    return render_template_string(MONITOR, repo=GITHUB_URL)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
