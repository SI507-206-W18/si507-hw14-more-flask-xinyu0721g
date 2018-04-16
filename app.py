from flask import Flask, render_template, request, redirect
import model

app = Flask(__name__)


@app.route("/")
def index():
    # print the guestbook
    return render_template("index.html", entries=model.get_entries())


@app.route("/admin")
def admin():
    return render_template("admin.html", entries=model.get_entries())


@app.route("/add")
def addentry():
    # add a guestbook entry
    return render_template("addentry.html")


@app.route("/delete", methods=["POST"])
def delete_entry():
    delete_id = request.form["theid"]
    model.delete_entry(delete_id)
    return redirect("/")


@app.route("/edit", methods=["POST"])
def edit_entry():
    edit_id = request.form["theid"]
    new_text = request.form["message"]
    model.edit_entry(edit_id, new_text)
    return redirect("/")


@app.route("/postentry", methods=["POST"])
def postentry():
    name = request.form["name"]
    message = request.form["message"]
    model.add_entry(name, message)
    return redirect("/")


if __name__ == "__main__":
    model.init(app)
    app.run(debug=True)
