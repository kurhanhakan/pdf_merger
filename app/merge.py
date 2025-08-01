from pypdf import PdfReader, PdfWriter
from io import BytesIO


def merge_pdfs(uploaded_files):
    writer = PdfWriter()
    for uploaded_file in uploaded_files:
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            writer.add_page(page)
    output = BytesIO()
    writer.write(output)
    output.seek(0)
    return output
