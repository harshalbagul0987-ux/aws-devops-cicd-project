from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return """
    <!doctype html>
    <html lang="en">
      <head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
      <title>DevOps Demo App</title>
      <style>
        body{font-family:Arial,sans-serif;max-width:760px;margin:60px auto;padding:0 20px;line-height:1.6;color:#172033}
        .card{padding:28px;border:1px solid #dbe3ef;border-radius:16px;background:#f7f9fc}
        code{background:#e8edf5;padding:3px 6px;border-radius:5px}
      </style></head>
      <body><div class="card">
        <h1>🚀 DevOps CI/CD Demo</h1>
        <p>Your Flask application is running in a Docker container.</p>
        <p>Pipeline: GitHub → GitHub Actions → Docker → AWS EC2</p>
        <p>Health endpoint: <a href="/health"><code>/health</code></a></p>
      </div></body>
    </html>
    """

@app.get("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    # Bind to all interfaces inside the container. Use a production WSGI server
    # for production deployments; this simple server is for a learning demo.
    app.run(host="0.0.0.0", port=5000)
