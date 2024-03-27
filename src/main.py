import streamlit as st
from langchain_community.document_loaders import PyPDFLoader


def preprocessing_document(pdf_path:str):

    """
    1. Load PDF
    2. Split into "pages"
    3. For each page: preprocess text (spaces, new lines etc)
    4. return the cleaned up pages
    """
    loader = PyPDFLoader(pdf_path)
    pages = loader.load_and_split()
    return pages




def main():
    st.header("SkipperBot :)")
    st.subheader("Answers questions based on what knowledge I possess")

    input_query = st.text_input("Enter a question",key = "textbox1")
    if len(input_query) < 5:
        st.warning("Enter a question to proceed further")
    else:
        button = st.button("Ask away", key="button1")
        if button:
            st.success('Input submitted successfully!')
            

        





if __name__ == "__main__":
    main()