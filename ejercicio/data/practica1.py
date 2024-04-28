# Acceder al archivo CSV
archivo = open('Listado-Instituciones-Educativas-distribuidas-por-zona-distrito-y-circuito.csv', "r")

# Obtener las líneas del archivo
lineas = archivo.readlines()

# Cerrar el archivo CSV
archivo.close()

# Obtener los encabezados del CSV y separarlos por el separador "|"
encabezados = lineas[0].strip().split("|")

# Iterar sobre cada línea del CSV, comenzando desde la segunda línea
for linea in lineas[1:]:
    # Separar la línea por el separador "|"
    valores = linea.strip().split("|")

    # Obtenemos los valores que nos interesa mostrar en patalla usando su posicion en la lista
    codigo_amie = valores[0]
    nombre_institucion = valores[1]
    provincia = valores[2]
    canton = valores[3]
    parroquia = valores[4]
    zona_administrativa = valores[5]
    codigo_distrito = valores[6]
    sostenimiento = valores[7]
    regimen_escolar = valores[8]
    modalidad = valores[9]
    numero_estudiantes = valores[13]
    numero_docentes = valores[14]
    estado = valores[15]
    
    # Crear el contenido HTML con los valores obtenidos
    pagina = """
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8">
        <title>%s</title>
      </head>
      <body>
        <h1>Información de la institución</h1>
        <p><b>Código AMIE:</b> %s</p>
        <p><b>Nombre de la Institución:</b> %s</p>
        <p><b>Provincia:</b> %s</p>
        <p><b>Cantón:</b> %s</p>
        <p><b>Parroquia:</b> %s</p>
        <p><b>Zona Administrativa:</b> %s</p>
        <p><b>Código de Distrito:</b> %s</p>
        <p><b>Sostenimiento:</b> %s</p>
        <p><b>Régimen Escolar:</b> %s</p>
        <p><b>Modalidad:</b> %s</p>
        <p><b>Número de Estudiantes:</b> %s</p>
        <p><b>Número de Docentes:</b> %s</p>
        <p><b>Estado:</b> %s</p>
      </body>
    </html>
    """ % (nombre_institucion, codigo_amie, nombre_institucion, provincia, canton, parroquia, zona_administrativa,
           codigo_distrito, sostenimiento, regimen_escolar, modalidad, numero_estudiantes, numero_docentes, estado)
    #Usando la concatenacion de cadenas asignamos valores a cada "%s"(string) con su dato correspondiente

    # Crear el nombre del archivo HTML usando el primer valor de la línea
    nombre_archivo = f"html/{valores[0]}.html"

    # Guardar el contenido HTML en el archivo correspondiente
    with open(nombre_archivo, "w") as archivo_html:
        archivo_html.write(pagina)

    print(f'Se ha creado el archivo HTML "{nombre_archivo}"')
