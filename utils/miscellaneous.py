from PIL import Image
import io


class Miscellaneous:
    @staticmethod
    async def image_to_large_binary(image):
        image = Image.open(image)
        with io.BytesIO() as output:
            image.save(output, format="JPEG")
            binary_data = output.getvalue()
        return binary_data

    @staticmethod
    async def get_image_extension(image):
        image = Image.open(image)
        extension = image.format.lower()
        return extension
