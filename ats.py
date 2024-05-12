pip install PyPDF2
import streamlit as st
import PyPDF2

def parsed_resume(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page_num in range(len(reader.pages)):
        current_txt = reader.pages[page_num].extract_text()
        current_txt = current_txt.replace("\n", " ")
        current_txt = current_txt.replace("●", " ")
        text += current_txt
    return text

def main():
    st.title("PDF to Text Converter")

    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    if uploaded_file is not None:
        try:
            text = parsed_resume(uploaded_file)
            st.success("PDF successfully converted to text!")
            st.write(text)
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()