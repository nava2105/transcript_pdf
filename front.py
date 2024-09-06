from flask import Flask, render_template, request, send_file
from src.pdf_reader.service.ReaderService import ReaderService
import os
from werkzeug.utils import secure_filename
from io import BytesIO
from docx import Document

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return 'Ruta no encontrada', 404

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/transcript', methods=['POST'])
def transcribir():
    if 'archivo' not in request.files:
        return '<br><br><center>No se ha seleccionado ningún archivo<br><br><center>'
    file = request.files['archivo']
    if file.filename == '':
        return '<br><br><center>No se ha seleccionado ningún archivo<br><br><center>'
    basePath = os.path.dirname(__file__)
    filename = secure_filename(file.filename)
    if os.path.splitext(filename)[1] == ".pdf":
        # Para cargar el archivo en la carpeta resources
        uploadPath = os.path.join(basePath, 'src/pdf_reader/resources', filename)
        file.save(uploadPath)
        analisisPath = os.path.join('src/pdf_reader/resources', filename)
        trascription = ReaderService.pdf2str(analisisPath)
        mostrar = True
        return render_template('home.html', trascription=trascription, mostrar=mostrar)
    return '<br><br><center>Debe ser formato pdf<br><br><center>'

@app.route('/download_txt', methods=['POST'])
def download_txt():
    text = request.form['transcription']
    return send_file(BytesIO(text.encode()), as_attachment=True, download_name='transcription.txt', mimetype='text/plain')

@app.route('/download_docx', methods=['POST'])
def download_docx():
    text = request.form['transcription']
    doc = Document()
    doc.add_paragraph(text)
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name='transcription.docx', mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
