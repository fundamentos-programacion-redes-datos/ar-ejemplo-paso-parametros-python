
def obtener_estudiantes(numero=1):
    # Inicialización de variables
    reporte_estudiantes = "\nListado de Estudiantes\n"  # Cadena para almacenar la lista de estudiantes
    contador = 0  # Contador para numeración de estudiantes
    bandera = True  # Variable de control para el ciclo while
    
    contador = 1  # Se inicializa el contador en 1

    # Uso de lista para almacenar la información de los estudiantes
    lista_estudiantes = []  # Lista donde cada estudiante se almacenará como una sublista
    
    # Bucle para ingreso de datos de los estudiantes
    while contador <= numero:  # Se ejecuta hasta que se ingresen la cantidad de estudiantes solicitados
        print("\nIngrese la información del estudiante:")
        nombre = input("Nombre del estudiante: ")  # Se solicita el nombre del estudiante
        apellido = input("Apellidos del estudiante: ")  # Se solicita el apellido del estudiante
        correo = input("Correo del estudiante: ")  # Se solicita el correo electrónico del estudiante
        edad = input("Edad del estudiante: ")  # Se solicita la edad del estudiante
        edad = int(edad)  # Conversión de la edad a entero

        # Se almacena la información en una lista temporal
        lista = [nombre, apellido, correo, edad]  
        lista_estudiantes.append(lista)  # Se agrega la lista del estudiante a la lista principal
    
        contador = contador + 1  # Se incrementa el contador para controlar el número de registros
    
    # Construcción del reporte de estudiantes a partir de la lista de estudiantes
    for i in lista_estudiantes:
        reporte_estudiantes = f"{reporte_estudiantes}{i[0]} {i[1]} -correo:{i[2]}-, edad:{i[3]}\n"
    
    # Impresión del reporte final de estudiantes
    print(reporte_estudiantes)  # Se muestra el listado de estudiantes


def obtener_docentes(numero=1):
    # Inicialización de variables
    reporte = "\nListado de Docentes\n"  # Cadena para almacenar la lista de docentes
    contador = 0  # Contador para numeración de docentes
    bandera = True  # Variable de control para el ciclo while
    
    contador = 1  # Se inicializa el contador en 1

    # Uso de lista para almacenar la información de los docentes
    lista_docentes = []  # Lista donde cada docente se almacenará como una sublista
    
    # Bucle para ingreso de datos de los docentes
    while contador <= numero:  # Se ejecuta hasta que se ingresen la cantidad de docentes solicitados
        print("\nIngrese la información del docente:")
        nombre = input("Nombre del docente: ")  # Se solicita el nombre del docente
        apellido = input("Apellidos del docente: ")  # Se solicita el apellido del docente
        ciudad = input("Ciudad de residencia: ")  # Se solicita la ciudad de residencia del docente

        # Se almacena la información en una lista temporal
        lista = [nombre, apellido, ciudad]  
        lista_docentes.append(lista)  # Se agrega la lista del docente a la lista principal
    
        contador = contador + 1  # Se incrementa el contador para controlar el número de registros
    
    # Construcción del reporte de docentes a partir de la lista de docentes
    for i in lista_docentes:
        reporte = f"{reporte}{i[0]} {i[1]} -ciudad de residencia:{i[2]}\n"
    
    # Impresión del reporte final de docentes
    print(reporte)  # Se muestra el listado de docentes


# Menú principal del programa
if __name__ == "__main__":
    bandera = True  # Variable de control para mantener el programa en ejecución

    while bandera:  # Se ejecuta hasta que el usuario decida salir
        mensaje = "Menú\nIngrese 1 para generar estudiantes; 2 para generar docentes; 3 para generar un estudiante y un docente: "
        opcion = input(mensaje)  # Se solicita al usuario que elija una opción del menú
        opcion = int(opcion)  # Conversión a entero para procesar la elección
        
        if opcion == 1:
            # Solicitar el número de estudiantes a registrar
            elementos = input("Ingrese el número de estudiantes a generar: ")  
            elementos = int(elementos)  # Conversión a entero
            obtener_estudiantes(elementos)  # Se llama a la función para registrar estudiantes
        else:
            if opcion == 2:
                # Solicitar el número de docentes a registrar
                elementos = input("Ingrese el número de docentes a generar: ")  
                elementos = int(elementos)  # Conversión a entero
                obtener_docentes(elementos)  # Se llama a la función para registrar docentes
            else:
                # Se ejecuta la opción por defecto, generando un estudiante y un docente
                # pues en cada función existe un parámetro con un valor por defecto
                obtener_estudiantes()
                obtener_docentes()

        # Se solicita al usuario si desea salir del programa
        salida = input("Ingrese 'si' para salir del proceso, caso contrario use cualquier valor para seguir: ")
        
        if salida.lower() == "si":  # Si el usuario ingresa "si", se termina el bucle
            bandera = False  # Se cambia la variable de control para salir del programa
