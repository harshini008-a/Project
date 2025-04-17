from flask import Flask, render_template, request, send_file
import qrcode
import os

app = Flask(__name__)
OUTPUT_FOLDER = "static/qrcodes"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_path = None
    if request.method == "POST":
        data = request.form.get("qrdata")
        if data:
            img = qrcode.make(data)
            qr_filename = os.path.join(OUTPUT_FOLDER, "qr.png")
            img.save(qr_filename)
            qr_path = "/" + qr_filename
    return render_template("index.html", qr_path=qr_path)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
