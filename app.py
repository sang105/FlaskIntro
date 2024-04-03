from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)

@app.route("/")
def hello():
    job_list = load_jobs_from_db()
    return render_template("home.html", jobs=job_list)

@app.route("/api/jobs")
def list_jobs():
    job_list = load_jobs_from_db()
    return jsonify(job_list)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)


