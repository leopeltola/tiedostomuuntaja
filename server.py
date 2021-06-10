from io import BytesIO

from flask import Flask, flash, render_template, request, send_file
from flask_wtf import FlaskForm
from PIL import Image
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired

from convert import FileConverter


class UploadForm(FlaskForm):
    file = FileField("file", validators=[DataRequired()])
    submit = SubmitField("submit")


app = Flask(__name__)
app.config["SECRET_KEY"] = "not-so-secret-key"


@app.route("/", methods=["GET", "POST"])
def index():
    form = UploadForm()
    if form.validate_on_submit():
        if "file" not in request.files:
            flash("Tiedostoa ei löydetty 😕")
            return render_template("main.html", form=form)
        file = request.files["file"]
        if file.filename == "":
            flash("Ei valittua tiedostoa 😞👺")
            return render_template("main.html", form=form)
        f = BytesIO()
        file.save(f)
        img = Image.open(f)
        pdf = FileConverter.img_to_pdf(img)
        img.close()
        i = file.filename.find(".")
        name = file.filename[:i]
        return send_file(
            pdf, attachment_filename="{}.pdf".format(name), as_attachment=True
        )

        # return render_template("main.html")
    return render_template("main.html", form=form)
