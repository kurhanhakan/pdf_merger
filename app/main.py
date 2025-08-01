import streamlit as st
from merge import merge_pdfs
from split import split_pdf
from rotate import rotate_pdf
from delete_pages import delete_pages_pdf


st.set_page_config(page_title="PDF Tools", page_icon="📄", layout="centered")
st.title("📄 PDF Merger, Splitter, Rotator & Deleter")

tab1, tab2, tab3, tab4 = st.tabs(
    ["🔗 Merge PDFs", "✂️ Split PDF", "🔄 Rotate PDF", "🗑️ Delete Pages"]
)

# Merge Tab
with tab1:
    uploaded_files = st.file_uploader(
        "Upload PDF files", type="pdf", accept_multiple_files=True, key="merge"
    )
    if uploaded_files:
        if st.button("Merge PDFs"):
            try:
                output = merge_pdfs(uploaded_files)
                st.success("✅ PDFs merged successfully!")
                st.download_button(
                    label="⬇️ Download Merged PDF",
                    data=output,
                    file_name="merged_output.pdf",
                    mime="application/pdf",
                )
            except Exception as e:
                st.error(f"❌ Error merging PDFs: {e}")

# Split Tab
with tab2:
    split_file = st.file_uploader(
        "Upload a single PDF file to split", type="pdf", key="split"
    )
    if split_file:
        try:
            from pypdf import PdfReader

            reader = PdfReader(split_file)
            total_pages = len(reader.pages)
            st.info(f"Total pages: {total_pages}")

            split_page = st.number_input(
                f"Split after page number (1–{total_pages - 1})",
                min_value=1,
                max_value=total_pages - 1,
                value=1,
                step=1,
            )

            if st.button("Split PDF"):
                output1, output2 = split_pdf(split_file, split_page)
                st.success("✅ PDF split successfully!")
                col1, col2 = st.columns(2)
                with col1:
                    st.download_button(
                        label="⬇️ Download Part 1",
                        data=output1,
                        file_name="part1.pdf",
                        mime="application/pdf",
                    )
                with col2:
                    st.download_button(
                        label="⬇️ Download Part 2",
                        data=output2,
                        file_name="part2.pdf",
                        mime="application/pdf",
                    )
        except Exception as e:
            st.error(f"❌ Error splitting PDF: {e}")

# Rotate Tab
with tab3:
    rotate_file = st.file_uploader(
        "Upload a single PDF file to rotate", type="pdf", key="rotate"
    )
    rotation_degree = st.selectbox(
        "Select rotation angle", options=[90, 180, 270], index=0
    )
    if rotate_file and st.button("Rotate PDF"):
        try:
            output = rotate_pdf(rotate_file, rotation_degree)
            st.success(f"✅ PDF rotated by {rotation_degree} degrees!")
            st.download_button(
                label="⬇️ Download Rotated PDF",
                data=output,
                file_name=f"rotated_{rotation_degree}.pdf",
                mime="application/pdf",
            )
        except Exception as e:
            st.error(f"❌ Error rotating PDF: {e}")

# Delete Pages Tab
with tab4:
    delete_file = st.file_uploader("Upload a single PDF file", type="pdf", key="delete")
    if delete_file:
        try:
            from pypdf import PdfReader

            reader = PdfReader(delete_file)
            total_pages = len(reader.pages)
            st.info(f"Total pages: {total_pages}")

            pages_to_delete_str = st.text_input(
                "Enter page numbers or ranges to delete (e.g. 1,3,5-7):"
            )

            if st.button("Delete Pages") and pages_to_delete_str.strip():
                output = delete_pages_pdf(delete_file, pages_to_delete_str)
                st.success(f"✅ Deleted pages: {pages_to_delete_str}")
                st.download_button(
                    label="⬇️ Download PDF after deletion",
                    data=output,
                    file_name="deleted_pages.pdf",
                    mime="application/pdf",
                )
        except Exception as e:
            st.error(f"❌ Error deleting pages: {e}")
