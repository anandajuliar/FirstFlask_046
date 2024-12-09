from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Ambil data dari form
        nama = request.form.get("nama")
        email = request.form.get("email")
        return f"<h1>Halo, {nama}! Email Anda adalah {email}.</h1>"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
