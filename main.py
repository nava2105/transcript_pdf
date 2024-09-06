# from src.pdf_reader.service.ReaderService import ReaderService
#
# if __name__ == '__main__':
#     # Definimos un nombre para nuestra clase de lectura
#     reader = ReaderService
#     # Definimos el nombre del archivo pdf en la carpeta resources
#     archivo = "src/pdf_reader/resources/Archivo.pdf"
#     # Llamamos a la función que nos dice el número de páginas del pdf
#     npages = reader.pageN(archivo)
#     # Llamamos a la función que nos dice la metadata de páginas del pdf
#     # print(reader.meta(archivo))
#     # Llamamos a la función que extrae la informacion del pdf a txt
#     # reader.pdf2txt(archivo)
#     # Llamamos a la función que imprime la informacion de todas las paginas del pdf
#     i = 0
#     for i in range(npages):
#         print(reader.pdf2txt1page(archivo,i))