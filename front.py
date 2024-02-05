from flask import Flask, render_template, request
import main as m
from src.pdf_reader.service.ReaderService import ReaderService
import os
from dotenv import load_dotenv
from src.nlp.service.InterferenceService import InferenceService
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.errorhandler
def nor_foud(error):
    return 'Ruta no encontrada'

@app.route('/', methods= ['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/registrar-archivo', methods= ['GET', 'POST'])
def registrarArchivo():
    if request.method == 'POST':
        file = request.files['archivo']
        basePath = os.path.dirname(__file__)
        filename = secure_filename(file.filename)
        if os.path.splitext(filename)[1] == ".pdf":
            # Para cargar el archivo en la carpeta resources
            uploadPath = os.path.join(basePath, 'src/pdf_reader/resources', filename)
            file.save(uploadPath)
            analisisPath = os.path.join('src/pdf_reader/resources', filename)
            # return '<br><br><center>El registro fue un exito<br><br><center>'
            return (f'<h1>{ReaderService.pageN(analisisPath)}</h1>')
        return '<br><br><center>Debe ser formato pdf<br><br><center>'
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='localhost',port=5000,debug=True);