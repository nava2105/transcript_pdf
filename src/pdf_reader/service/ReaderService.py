import fitz

class ReaderService:
    def __init__(self, archivo, npage, route):
        self.archivo = archivo
        self.npage = npage

    def pdf2txt(archivo):
        doc = fitz.open(archivo)
        salida = open(archivo + ".txt", "wb")

        for pagina in doc:
            texto = pagina.get_text().encode("utf8")
            salida.write(texto)
            salida.write(b"\n-----\n")

        salida.close()

    def pdf2str (archivo):
        doc = fitz.open(archivo)
        salida = ""
        for numPagina in range(doc.page_count):
            pagina = doc.load_page(numPagina)
            textPagina = pagina.get_text("text")
            salida += textPagina
        return salida

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
