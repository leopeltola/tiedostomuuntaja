from flask import Flask, render_template, redirect, url_for, request, send_file
from werkzeug.utils import secure_filename
from convert import convert_to_pdf
from PIL import Image
from io import BytesIO
from flask_wtf import FlaskForm
from wtforms import FileField
from os import remove

class FileUploadForm(FlaskForm):
	file = FileField()


app = Flask(__name__)
app.config["SECRET_KEY"] = "super-secret-key"

@app.route("/", methods=["GET", "POST"])
def index():
	form = FileUploadForm()
	if request.method == "POST":
		file = request.files["file"]
		file.save("files/{}".format(file.filename))
		img = Image.open("files/{}".format(file.filename))
		pdf_path = convert_to_pdf(img)
		img.close()
		remove("files/{}".format(file.filename))
		return send_file(pdf_path, attachment_filename='converted_file.pdf', as_attachment=True)

		# return render_template("main.html")
	return render_template("main.html")
