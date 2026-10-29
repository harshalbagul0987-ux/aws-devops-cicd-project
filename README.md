# Automated Cloud Deployment Using Docker, GitHub Actions, and AWS EC2

A beginner-friendly DevOps portfolio project. It packages a small Flask application into Docker, tests it automatically with GitHub Actions, and documents how to run it on AWS EC2.

## Architecture

Developer → GitHub repository → GitHub Actions (tests + Docker build) → AWS EC2 (Docker container)

> The included workflow performs continuous integration (tests and image build). The AWS deployment is a separate, manual first deployment so you can learn the server setup safely. Add automated deployment only after the app works on EC2.

## Requirements

- Python 3.12+
- Git
- Docker Desktop or Docker Engine
- GitHub account
- Optional: AWS account for the cloud deployment section

## Run locally without Docker

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python -m unittest discover -s tests -v
python app.py
```

Open http://127.0.0.1:5000 and http://127.0.0.1:5000/health.

## Build and run with Docker

```bash
docker build -t devops-demo .
docker run --rm -p 5000:5000 devops-demo
```

Open http://localhost:5000. Stop with Ctrl+C.

## Set up GitHub Actions

1. Create a new GitHub repository named `aws-devops-cicd-project`.
2. Upload or push all project files to the `main` branch.
3. Open the repository's **Actions** tab.
4. The workflow in `.github/workflows/ci.yml` runs tests and builds the Docker image on pushes and pull requests to `main`.
5. Make a small change to `app.py`, commit it, and confirm the workflow passes.

## Deploy to AWS EC2 (learning deployment)

1. In AWS, launch a small Amazon Linux EC2 instance. Review current pricing and Free Tier eligibility before launching; eligibility varies by account and offer.
2. Create or select a key pair and store the private key securely. Never upload it to GitHub.
3. In the EC2 security group, allow SSH (TCP 22) only from your own public IP. Allow TCP 5000 from your IP for testing; do not expose it to everyone unnecessarily.
4. Connect to the instance using the SSH instructions shown by AWS.
5. Install Docker using the current Amazon Linux documentation for your instance version, then start and enable the Docker service.
6. Copy the project to the instance using Git or SCP, then run:

```bash
docker build -t devops-demo .
docker run -d --name devops-demo --restart unless-stopped -p 5000:5000 devops-demo
docker ps
```

7. Visit `http://EC2-PUBLIC-IP:5000` and `http://EC2-PUBLIC-IP:5000/health` while the test port is allowed by your security group.
8. For a more production-like setup, put Nginx or an Application Load Balancer in front, use HTTPS, restrict inbound access, and use a production WSGI server.

## Security and cost notes

- AWS resources can incur charges. Set a budget alert and terminate the EC2 instance and delete unused resources when finished.
- Never commit AWS access keys, private SSH keys, passwords, or `.env` files.
- Do not use root credentials for routine work. Prefer IAM roles and least-privilege permissions.
- This demo uses Flask's development server; do not treat it as a production deployment.
- Before opening public access, understand security groups, patching, logs, and HTTPS.

## Resume bullet (use only after you complete and test it)

**Built a containerized Flask application and automated CI checks using GitHub Actions; created a repeatable Docker deployment workflow and deployed the app to AWS EC2.**

## Interview explanation

- **Git:** version control for source code.
- **GitHub Actions:** runs repeatable automated workflow steps after code changes.
- **CI:** automatically tests and builds the application.
- **Docker:** packages the app and dependencies into an image.
- **EC2:** virtual server used to host the container.
- **Health endpoint:** simple URL that returns the service status.
- **Next improvement:** publish the image to Amazon ECR and deploy it through a secured workflow using OIDC/IAM rather than long-lived AWS keys.
