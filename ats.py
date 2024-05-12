from flask import Flask, render_template, request
import PyPDF2
import os

app = Flask(__name__)

# Ensure there is a folder to save uploaded files
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def parse_resume(file_stream):
    reader = PyPDF2.PdfReader(file_stream)
    text = ""
    for page in reader.pages:
        current_txt = page.extract_text()
        if current_txt:
            current_txt = current_txt.replace("\n", " ").replace("●", " ")
            text += current_txt
    return text

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.pdf'):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            with open(filepath, "rb") as file_stream:
                content = parse_resume(file_stream)
            os.remove(filepath)  # Remove file after processing
            return render_template('result.html', content=content)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
