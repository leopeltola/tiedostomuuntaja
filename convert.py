from io import BytesIO

from PIL import Image


class FileConverter:
    @staticmethod
    def img_to_pdf(img):
        f = BytesIO()
        img = img.convert("RGB")
        img = img.transpose(Image.ROTATE_270)
        img.save(f, format="pdf")
        f.seek(0)
        return f
