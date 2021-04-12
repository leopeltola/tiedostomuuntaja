from flask import Flask, render_template, redirect, url_for, request, send_file
from werkzeug.utils import secure_filename
from convert import convert_to_pdf
from PIL import Image
from io import BytesIO
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired
from os import remove

class UploadForm(FlaskForm):
	file = FileField("file", validators=[DataRequired()])
	submit = SubmitField("submit")


app = Flask(__name__)
app.config["SECRET_KEY"] = "not-so-secret-key"

@app.route("/", methods=["GET", "POST"])
def index():
	form = UploadForm()
	if form.validate_on_submit():
		if 'file' not in request.files:
			flash('Tiedostoa ei löydetty')
			return render_template("main.html", form=form)
		file = request.files["file"]
		if file.filename == '':
			flash('Ei valittua tiedostoa')
			return render_template("main.html", form=form)
		f = BytesIO()
		file.save(f)
		img = Image.open(f)
		pdf = convert_to_pdf(img)
		img.close()
		pdf.seek(0)
		i = file.filename.find(".")
		name = file.filename[:i]
		return send_file(pdf, attachment_filename='{}.pdf'.format(name), as_attachment=True)

		# return render_template("main.html")
	return render_template("main.html", form=form)
