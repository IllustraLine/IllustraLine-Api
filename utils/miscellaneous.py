from PIL import Image
import io
import difflib


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

    @staticmethod
    async def search_course_by_title(inputan, data, threshold=0.4):
        result = []
        for d in data:
            judul = d.title.lower()
            similarity_ratio = difflib.SequenceMatcher(
                None, inputan.lower(), judul
            ).ratio()
            if similarity_ratio >= threshold:
                result.append(d)
        return result
