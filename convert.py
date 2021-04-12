from PIL import Image
from io import BytesIO

def convert_to_pdf(img):
	f = BytesIO()
	img = img.convert("RGB")
	img = img.transpose(Image.ROTATE_270)
	img.save(f, format="pdf")
	f.seek(0)
	return f
