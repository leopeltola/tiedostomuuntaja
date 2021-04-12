from PIL import Image
from io import BytesIO

def convert_to_pdf(img):
	f = BytesIO()
	img = img.convert("RGB")
	# img.save(f, format="png")
	img.save("files/temp.pdf")
	# f.seek(1)
	# img = Image.open(f)
	# return img
	return "files/temp.pdf"
