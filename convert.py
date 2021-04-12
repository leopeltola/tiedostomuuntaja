from PIL import Image
from io import BytesIO

def convert_to_pdf(img):
	f = BytesIO()
	img = img.convert("RGB")
	img = img.rotate(-90)
	img.save(f, format="pdf")
	# img.save("files/temp.pdf")
	f.seek(1)
	# img = Image.open(f)
	return f
	# return "files/temp.pdf"
