import PyPDF2

def extract_text_from_pdf(pdf_file):
    text = ''
    pdf = PyPDF2.PdfReader(pdf_file)
    for page in range(len(pdf.pages)):
        text += pdf.pages[page].extract_text()
    return text

def main():
    pdf_file = 'front-end.pdf'
    extracted_text = extract_text_from_pdf(pdf_file)
    print(extracted_text)

if __name__ == "__main__":
    main()
