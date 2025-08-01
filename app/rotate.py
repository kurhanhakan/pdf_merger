from pypdf import PdfReader, PdfWriter
from io import BytesIO


def rotate_pdf(uploaded_file, rotation_degree):
    if rotation_degree not in [90, 180, 270]:
        raise ValueError("Rotation degree must be one of 90, 180, 270")

    reader = PdfReader(uploaded_file)
    writer = PdfWriter()

    for page in reader.pages:
        page.rotate(rotation_degree)
        writer.add_page(page)

    output = BytesIO()
    writer.write(output)
    output.seek(0)
    return output
