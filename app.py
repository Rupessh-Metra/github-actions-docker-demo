from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello from GitHub Actions!</h1>
    <p>This application was built and deployed using CI/CD.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
