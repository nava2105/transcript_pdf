import fitz

class ReaderService:
    def __init__(self, archivo, npage):
        self.archivo = archivo
        self.npage = npage

    def pdf2txt(archivo):
        doc = fitz.open(archivo)
        salida = open(archivo + ".txt", "wb")

        for pagina in doc:
            texto = pagina.get_text().encode("utf8")
            """ .encode("utf8") solo permite que se ingrese información de
                tipo texto, esto excluye imagenes y saltos de linea """
            salida.write(texto)
            salida.write(b"\n-----\n")

        salida.close()

    def pdf2txt1page(archivo, npage) -> str:
        doc = fitz.open(archivo)
        page = doc.load_page(npage)
        return page.get_text()

    def pageN(archivo) -> int:
        doc = fitz.open(archivo)
        return doc.page_count

    def meta(archivo) -> str:
        doc = fitz.open(archivo)
        return doc.metadata