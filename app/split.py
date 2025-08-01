from pypdf import PdfReader, PdfWriter
from io import BytesIO


def split_pdf(uploaded_file, split_page):
    reader = PdfReader(uploaded_file)
    total_pages = len(reader.pages)
    if not (1 <= split_page < total_pages):
        raise ValueError(f"Split page must be between 1 and {total_pages - 1}")

    writer1 = PdfWriter()
    writer2 = PdfWriter()

    for i, page in enumerate(reader.pages):
        if i < split_page:
            writer1.add_page(page)
        else:
            writer2.add_page(page)

    output1 = BytesIO()
    writer1.write(output1)
    output1.seek(0)

    output2 = BytesIO()
    writer2.write(output2)
    output2.seek(0)

    return output1, output2
