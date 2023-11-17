from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def pagehome():
    return render_template("home.html")

@app.route("/cv")
def pagecv():
    return render_template("cv.html")

@app.route("/profile")
def pageprofile():
    return render_template("profile.html")

@app.route("/artikel")
def pagearticle():
    return render_template("artikel.html")

@app.route("/cat")
def pagecat():
    return render_template("cat.html")

@app.route("/fibonacci")
def pagefibonacci():
    return render_template("fibonacci.html")

@app.route("/csvtojson")
def pagejson():
    return render_template("csvtojson.html")

@app.route("/post", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("post.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"
