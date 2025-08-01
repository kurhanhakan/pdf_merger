from pypdf import PdfReader, PdfWriter
from io import BytesIO


def parse_pages(text):
    pages = set()
    parts = [p.strip() for p in text.split(",") if p.strip()]
    for part in parts:
        if "-" in part:
            start, end = part.split("-")
            pages.update(range(int(start), int(end) + 1))
        else:
            pages.add(int(part))
    return pages


def delete_pages_pdf(uploaded_file, pages_to_delete_str):
    reader = PdfReader(uploaded_file)
    total_pages = len(reader.pages)
    pages_to_delete = parse_pages(pages_to_delete_str)

    invalid_pages = [p for p in pages_to_delete if p < 1 or p > total_pages]
    if invalid_pages:
        raise ValueError(f"Invalid page numbers: {invalid_pages}")

    writer = PdfWriter()
    for i, page in enumerate(reader.pages, start=1):
        if i not in pages_to_delete:
            writer.add_page(page)

    output = BytesIO()
    writer.write(output)
    output.seek(0)
    return output
