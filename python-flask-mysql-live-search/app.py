from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "course_coupons"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/livesearch", methods=["POST"])
def livesearch():
    searchbox = request.form.get("text")
    cursor = mysql.connection.cursor()
    query = "SELECT title FROM courses WHERE title LIKE %s ORDER BY title"
    cursor.execute(query, (searchbox + '%',))
    result = cursor.fetchall()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
