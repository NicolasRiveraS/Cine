print ()
print ("❢ ◤━━━━━ ¡Bienvenid@ al Sistema Integral de Gestión Cinematográfica! ━━━━━◥ ❢")
print ()

# Función para código de películas
def generaCode(codigo_peli):
    if (codigo_peli == 0):
        return 1
    else:
        return codigo_peli + 1

# Función para numero de función
def generaNumeroFuncion(numero_funcion):
    if (numero_funcion == 0):
        return 1
    else:
        return numero_funcion + 1

# Función para código de ventas
def generaVenta(codigo_venta):
    if (codigo_venta == 0):
        return 1
    else:
        return codigo_venta + 1

# Función para código de taquilla por película
def generaTaquillaPeli (codigo_taquilla_peli):
    if (codigo_taquilla_peli == 0):
        return 1
    else:
        return codigo_taquilla_peli + 1
    
# Función para código de taquilla por sala
def generaTaquillaSala (codigo_taquilla_sala):
    if (codigo_taquilla_sala == 0):
        return 1
    else:
        return codigo_taquilla_sala + 1
    
# Función para código de películas más populares
def generaMasPopulares (codigo_mas_populares):
    if (codigo_mas_populares == 0):
        return 1
    else:
        return codigo_mas_populares + 1
    
# Función para código de ventas por fecha
def generaVentaFecha (codigo_venta_fecha):
    if (codigo_venta_fecha == 0):
        return 1
    else:
        return codigo_venta_fecha + 1
    
# Función para código de funciones más vendidas
def generaMasVendidas (codigo_mas_vendidas):
    if (codigo_mas_vendidas == 0):
        return 1
    else:
        return codigo_mas_vendidas + 1
    
# Declaración de variables
codigo_peli = 0
numero_funcion = 0
codigo_venta = 0
codigo_taquilla_peli = 0
codigo_taquilla_sala = 0
codigo_venta_fecha = 0
codigo_mas_vendidas = 0
codigo_mas_populares = 0

opcion_principal = 0

cantidad_pelis = 0
cantidad_salas = 0
cantidad_funciones = 0
cantidad_ventas = 0

# Películas almacenadas
peliculas_matriz = []

# Salas almacenadas
salas_matriz = []

# Funciones almacenadas
funciones_matriz = []

# Ventas almacenadas
ventas_matriz = []

    # Menú Principal
while opcion_principal != 6:

    print ("\t   1 - Gestión de Películas")
    print ("\t   2 - Gestión de Salas de Cine")
    print ("\t   3 - Gestión de Funciones")
    print ("\t   4 - Gestión de Ventas")
    print ("\t   5 - Reportes y Estadísticas")
    print ("\t   6 - Salir")
    print ()
    opcion_principal = int(input("\t   Por favor, ingrese una opción: "))
    print ()

    # Gestión de Películas
    if opcion_principal == 1:
        
        while True:
            opcion_peli = 0
            print ("◣━━━ Gestión de Películas ━━━◢")
            print ()
            print ("1 - Agregar una Película")
            print ("2 - Mostrar Películas")
            print ("3 - Buscar una Película")
            print ("4 - Modificar una Película")
            print ("5 - Eliminar una Película")
            print ("6 - Volver al menú anterior")
            print ()
            opcion_peli = int(input("Por favor, ingrese una opción: "))
            print ()

            # Agregar Película
            if opcion_peli == 1:
                print ("━ Agregar Película ━")
                print ()
                print ("Por favor ingrese la información de la película solicitada a continuación")
                codigo_peli = generaCode (codigo_peli)
                nombre_peli = str(input("Nombre: "))
                año_peli = int(input("Año de lanzamiento: "))
                genero_peli = str(input("Género: "))
                director_peli = str(input("Director: "))
                actor_peli = str(input("Actor principal: "))
                duracion_peli = int(input("Duración (minutos): "))
                sinopsis_peli = str(input("Sinopsis: "))
                print ()

                # Posición      0               1           2           3               4           5               6               7
                pelicula = [codigo_peli , nombre_peli , año_peli , genero_peli , director_peli , actor_peli , duracion_peli , sinopsis_peli]
                
                peliculas_matriz.append (pelicula)

                cantidad_pelis += 1

                print ("¡Gracias!")
                print ()

            # Mostrar Películas
            elif opcion_peli == 2:
                print ("━ Catálogo de Películas ━")
                print ()
                
                if cantidad_pelis > 0:
                    print ("Películas disponibles:")
                    print ()

                    for i in range (cantidad_pelis):
                        print ("► Código: CP - 0", peliculas_matriz [i] [0])
                        print ("Nombre:", peliculas_matriz [i] [1])
                        print ("Año de lanzamiento:", peliculas_matriz [i] [2])
                        print ("Género:", peliculas_matriz [i] [3])
                        print ("Director:", peliculas_matriz [i] [4])
                        print ("Actor principal:", peliculas_matriz [i] [5])
                        print ("Duración:", peliculas_matriz [i] [6], "minutos")
                        print ("Sinopsis:", peliculas_matriz [i] [7])
                        print ()
                else:
                    print ("Por el momento no hay películas disponibles.")
                    print ()

            # Buscar Película
            elif opcion_peli == 3:

                while True:
                    print ("━ Buscador de Películas ━")
                    print ()
                    print ("1 - Buscar película por código")
                    print ("2 - Buscar película por nombre")
                    print ("3 - Regresar")
                    print ()
                    opcion_buscar_peli = int(input("Por favor, ingrese una opción: "))
                    print ()

                    # Buscar por código
                    if opcion_buscar_peli == 1:
                        print (">> Buscar por código <<")
                        print ()
                        buscar_codigo = int(input("Ingrese el número final del código de la película (CP - 0#): "))
                        indexCodigo = -1
                        print ()

                        for i in range (cantidad_pelis):
                            if peliculas_matriz [i] [0] == buscar_codigo:
                                indexCodigo = i

                        if indexCodigo == -1:
                            print ("No hay una película con el código introducido. Intente nuevamente.")
                            print ()
                        else:
                            print ("La película encontrada es la siguiente:")
                            print ()
                            print ("► Código: CP - 0", peliculas_matriz [indexCodigo] [0])
                            print ("Nombre:", peliculas_matriz [indexCodigo] [1])
                            print ("Año de lanzamiento:", peliculas_matriz [indexCodigo] [2])
                            print ("Género:", peliculas_matriz [indexCodigo] [3])
                            print ("Director:", peliculas_matriz [indexCodigo] [4])
                            print ("Actor principal:", peliculas_matriz [indexCodigo] [5])
                            print ("Duración:", peliculas_matriz [indexCodigo] [6], "minutos")
                            print ("Sinopsis:", peliculas_matriz [indexCodigo] [7])
                            print ()
                    
                    # Buscar por nombre
                    elif opcion_buscar_peli == 2:
                        print (">> Buscar por nombre <<")
                        print ()
                        buscar_nombre = str(input("Ingrese el nombre de la película: "))
                        indexNombre = -1
                        print ()

                        for i in range (cantidad_pelis):
                            if peliculas_matriz [i] [1] == buscar_nombre:
                                indexNombre = i

                        if indexNombre == -1:
                            print ("No hay una película con el nombre introducido. Intente nuevamente.")
                            print ()
                        else:
                            print ("La película encontrada es la siguiente:")
                            print ()
                            print ("► Código: CP - 0", peliculas_matriz [indexNombre] [0])
                            print ("Nombre:", peliculas_matriz [indexNombre] [1])
                            print ("Año de lanzamiento:", peliculas_matriz [indexNombre] [2])
                            print ("Género:", peliculas_matriz [indexNombre] [3])
                            print ("Director:", peliculas_matriz [indexNombre] [4])
                            print ("Actor principal:", peliculas_matriz [indexNombre] [5])
                            print ("Duración:", peliculas_matriz [indexNombre] [6], "minutos")
                            print ("Sinopsis:", peliculas_matriz [indexNombre] [7])
                            print ()

                    elif opcion_buscar_peli == 3:
                        print ("►► Regresando al menú anterior...")
                        print ()
                        break

                    else:
                        print ("Opción no disponible, intente nuevamente.")
                        print ()

            # Modificar Película
            elif opcion_peli == 4:
                print ("━ Modificar Película ━")
                print ()
                modificar_codigo = int(input("Ingrese el número final del código de la película que desea modificar (CP - 0#): "))
                indexModificar = -1
                print ()

                for i in range (cantidad_pelis):
                    if peliculas_matriz [i] [0] == modificar_codigo:
                        indexModificar = i
                
                if indexModificar == -1:
                    print ("No hay una película asociada que sea modificable con el código introducido.")
                    print ("Por favor intente nuevamente.")
                    print ()
                else:
                    print ("La película encontrada es la siguiente:")
                    print ()
                    print ("► Código: CP - 0", peliculas_matriz [indexModificar] [0])
                    print ("Nombre:", peliculas_matriz [indexModificar] [1])
                    print ("Año de lanzamiento:", peliculas_matriz [indexModificar] [2])
                    print ("Género:", peliculas_matriz [indexModificar] [3])
                    print ("Director:", peliculas_matriz [indexModificar] [4])
                    print ("Actor principal:", peliculas_matriz [indexModificar] [5])
                    print ("Duración:", peliculas_matriz [indexModificar] [6], "minutos")
                    print ("Sinopsis:", peliculas_matriz [indexModificar] [7])
                    print ()

                    print ("Ingrese a continuación los datos nuevos:")
                    nombre_peli = str(input("Nombre: "))
                    año_peli = int(input("Año de lanzamiento: "))
                    genero_peli = str(input("Género: "))
                    director_peli = str(input("Director: "))
                    actor_peli = str(input("Actor principal: "))
                    duracion_peli = int(input("Duración (minutos): "))
                    sinopsis_peli = str(input("Sinopsis: "))
                    print ()

                    modificacion_peli = [peliculas_matriz [indexModificar] [0] , nombre_peli , año_peli , genero_peli , director_peli , actor_peli , duracion_peli , sinopsis_peli]

                    peliculas_matriz [indexModificar] = (modificacion_peli)

                    print ("¡Película modificada correctamente!")
                    print ()

            # Eliminar Película
            elif opcion_peli == 5:
                print ("━ Eliminar Película ━")
                print ()
                eliminar_codigo = int(input("Ingrese el número final del código de la película que desea eliminar (CP - 0#): "))
                indexEliminar = -1
                print ()

                for i in range (cantidad_pelis):
                    if peliculas_matriz [i] [0] == eliminar_codigo:
                        indexEliminar = i
                
                if indexEliminar == -1:
                    print ("No hay una película asociada que sea eliminable con el código introducido.")
                    print ("Por favor intente nuevamente.")
                    print ()
                else:
                    print ("La película encontrada es la siguiente:")
                    print ()
                    print ("► Código: CP - 0", peliculas_matriz [indexEliminar] [0])
                    print ("Nombre:", peliculas_matriz [indexEliminar] [1])
                    print ("Año de lanzamiento:", peliculas_matriz [indexEliminar] [2])
                    print ("Género:", peliculas_matriz [indexEliminar] [3])
                    print ("Director:", peliculas_matriz [indexEliminar] [4])
                    print ("Actor principal:", peliculas_matriz [indexEliminar] [5])
                    print ("Duración:", peliculas_matriz [indexEliminar] [6], "minutos")
                    print ("Sinopsis:", peliculas_matriz [indexEliminar] [7])
                    print ()

                    print (">> ¿Está seguro que desea eliminar esta película? <<")
                    print ("1 - Si")
                    print ("2 - No")
                    print ()
                    opcion_borrar = int(input("Ingrese una opción: "))
                    print ()

                    if opcion_borrar == 1:

                        peliculas_matriz.pop (indexEliminar)

                        cantidad_pelis -= 1

                        print ("Película asociada con el código CP - 0", eliminar_codigo, "eliminada correctamente.")
                        print ("Para consultar las películas restantes, puede revisarlas en el menú anterior.")
                        print ()
                    else:
                        print ("Ninguna película eliminada.")
                        print ()

            elif opcion_peli == 6:
                print ("►► Regresando al menú anterior...")
                print ()
                break

            else:
                print ("Opción no disponible. Intente nuevamente.")
                print ()


    # Gestión de Salas de Cine
    elif opcion_principal == 2:

        while True:
            opcion_salas = 0
            print ("◣━━━ Gestión de Salas de Cine ━━━◢")
            print ()
            print ("1 - Agregar Sala")
            print ("2 - Mostrar Salas")
            print ("3 - Modificar una Sala")
            print ("4 - Eliminar una Sala")
            print ("5 - Volver al menú anterior")
            print ()
            opcion_salas = int(input("Ingrese una opción: "))
            print ()

            # Agregar Sala
            if opcion_salas == 1:
                print ("━ Agregar Sala ━")
                print ()
                print ("Por favor ingrese la información solicitada a continuación:")
                numero_sala = int(input("Identificación única de la sala dentro del cine: "))
                ubicacion_sala = str(input("Dirección del cine donde se encuentra: "))
                capacidad_sala = int(input("Número máximo de personas que pueden ocuparla: "))
                tecnologia_sala = str(input("Tipo de proyección que ofrece (2D, 3D o IMAX): "))
                print ()

                # Posición    0               1               2                3
                sala = [numero_sala , ubicacion_sala , capacidad_sala , tecnologia_sala]

                salas_matriz.append (sala)

                cantidad_salas += 1

                print ("¡Gracias!")
                print ()

            # Mostrar Salas
            elif opcion_salas == 2:
                print ("━ Salas Registradas ━")
                print ()
                
                if cantidad_salas > 0:
                    print ("Actualmente hay", cantidad_salas, "salas registradas:")
                    print ()
                
                    for s in range (cantidad_salas):
                        print ("Número de sala:", salas_matriz [s] [0])
                        print ("Ubicada en:", salas_matriz [s] [1])
                        print ("Con una capacidad de:", salas_matriz [s] [2], "personas.") 
                        print ("Cuenta con tecnología:", salas_matriz [s] [3])              
                        print ()
                else:
                    print ("Por el momento no hay salas registradas.")
                    print ()

            # Modificar Sala
            elif opcion_salas == 3:
                print ("━ Modificar Sala ━")
                print ()
                modificar_sala = int(input("Ingrese el número de sala que desea modificar: "))
                indexModificar = -1
                print ()

                for i in range (cantidad_salas):
                    if salas_matriz [i] [0] == modificar_sala:
                        indexModificar = i
                
                if indexModificar == -1:
                    print ("No se ha encontrado una sala asociada al número indicado.")
                    print ("Por favor intente nuevamente.")
                    print ()
                else:
                    print ("La sala encontrada es la siguiente:")
                    print ()
                    print (" Número de sala:", salas_matriz [indexModificar] [0])
                    print (" Ubicada en:", salas_matriz [indexModificar] [1])
                    print (" Con una capacidad de:", salas_matriz [indexModificar] [2], "personas.") 
                    print (" Cuenta con tecnología :", salas_matriz [indexModificar] [3]) 
                    print ()

                    print ("Ingrese a continuación los datos nuevos:")
                    numero_sala = int(input("Identificación única de la sala dentro del cine: "))
                    ubicacion_sala = str(input("Dirección del cine donde se encuentra: "))
                    capacidad_sala = int(input("Número máximo de personas que pueden ocuparla: "))
                    tecnologia_sala = str(input("Tipo de proyección que ofrece (2D, 3D o IMAX): "))
                    print ()

                    modificacion_sala = [numero_sala , ubicacion_sala , capacidad_sala , tecnologia_sala]

                    salas_matriz [indexModificar] = (modificacion_sala)
                    
                    print ("¡La sala ha sido modificada correctamente!")
                    print ()

            # Eliminar Sala
            elif opcion_salas == 4:         
                print ("━ Eliminar Sala ━")
                print ()
                eliminar_sala = int(input("Ingrese el número de sala a eliminar: "))
                indexEliminar = -1
                print ()

                for i in range (cantidad_salas):
                    if salas_matriz [i] [0] == eliminar_sala:
                        indexEliminar = i
                
                if indexEliminar == -1:
                    print ("No se encontró el número de sala:", eliminar_sala)
                    print ()
                else:
                    print ("La sala encontrada es la siguiente:")
                    print ()
                    print ("Número de sala:", salas_matriz [indexEliminar] [0])
                    print ("Ubicada en:", salas_matriz [indexEliminar] [1])
                    print ("Con una capacidad de:", salas_matriz [indexEliminar] [2], "personas.") 
                    print ("Cuenta con tecnología:", salas_matriz [indexEliminar] [3])
                    print ()

                    print (">> ¿Está seguro que desea eliminar esta sala? <<")
                    print ("1 - Si")
                    print ("2 - No")
                    print ()
                    opcion_borrar = int(input("Ingrese una opción: "))
                    print ()

                    if opcion_borrar == 1:

                        salas_matriz.pop (indexEliminar) 

                        cantidad_salas -= 1

                        print ("La sala número", eliminar_sala, "ha sido eliminada correctamente.")
                        print ("Para consultar las salas restantes, puede revisarlas en el menú anterior.")
                        print ()
                    else:
                        print ("Ninguna sala ha sido eliminada.")
                        print ()

            elif opcion_salas == 5:
                print ("►► Regresando al menú anterior...")
                print ()
                break

            else:
                print ("Opción no disponible. Intente nuevamente.")
                print ()       


    # Gestión de Funciones
    elif opcion_principal == 3:

        while True:
            opcion_funciones = 0
            print ("◣━━━ Gestión de Funciones ━━━◢")
            print ()
            print ("1 - Programar Función")
            print ("2 - Mostrar Funciones")
            print ("3 - Modificar una Función")
            print ("4 - Eliminar una Función")
            print ("5 - Volver al menú anterior")
            print ()
            opcion_funciones = int(input("Ingrese una opción: "))
            print ()

            # Programar Función
            if opcion_funciones == 1:
                print ("━ Programar Función ━")
                print ()
                print ("Por favor introduzca los datos a continuación para crear una función:")
                numero_funcion = generaNumeroFuncion (numero_funcion)
                cod_peli_funcion = int(input("Ingrese el número final del código de la película (CP - 0#): "))
                sala_funcion = int(input("Ingrese el número de sala donde se proyectará: "))
                horario_funcion = str(input("Ingrese el horario de la función (día y hora): "))
                idioma_funcion = str(input("Ingrese si la película es doblada o subtitulada: "))
                indexPeliFuncion = -1
                indexSalaFuncion = -1
                print ()

                for i in range (cantidad_pelis):
                    if peliculas_matriz [i] [0] == cod_peli_funcion:
                        indexPeliFuncion = i
                
                for j in range (cantidad_salas):
                    if salas_matriz [j] [0] == sala_funcion:
                        indexSalaFuncion = j

                if indexPeliFuncion == -1:
                    print ("Lo sentimos, la película solicitada no se encuentra en el sistema.")
                    print ()

                elif indexSalaFuncion == -1:
                    print ("Lo sentimos, la sala solicitada no se encuentra en el sistema.")
                    print ()
                
                else:
                    # Posición       0                               1                                   2                            3                 4                          5
                    funcion = [numero_funcion , peliculas_matriz [indexPeliFuncion] [1] , salas_matriz [indexSalaFuncion] [0] , horario_funcion , idioma_funcion , salas_matriz [indexSalaFuncion] [3]]

                    funciones_matriz.append (funcion)

                    cantidad_funciones += 1

                    print ("¡Función añadida con éxito!")
                    print ()

            # Mostrar Funciones
            elif opcion_funciones == 2:
                print ("━ Funciones Registradas ━")
                print ()
                
                if cantidad_funciones > 0:
                    print ("Actualmente hay", cantidad_funciones, "funciones registradas:")
                    print ()
                
                    for i in range (cantidad_funciones):
                        print ("► Función", funciones_matriz [i] [0])
                        print ("Película:", funciones_matriz [i] [1])
                        print ("Sala:", funciones_matriz [i] [2])
                        print ("Horario:", funciones_matriz [i] [3])
                        print ("Idioma:", funciones_matriz [i] [4])
                        print ("Tecnología:", funciones_matriz [i] [5])
                        print ()

                else:
                    print ("Por el momento no hay funciones registradas.")
                    print ()

            # Modificar una Función
            elif opcion_funciones == 3:
                print ("━ Modificar una Función ━")
                print ()
                modificar_función = int(input("Ingrese el número de función que desea modificar: "))
                indexModificar = -1
                print ()

                for i in range (cantidad_funciones):
                    if funciones_matriz [i] [0] == modificar_función:
                        indexModificar = i
                
                if indexModificar == -1:
                    print ("No se ha encontrado una función asociada al número indicado.")
                    print ("Por favor intente nuevamente.")
                    print ()
                else:
                    print ("La función encontrada es la siguiente:")
                    print ()
                    print ("► Función", funciones_matriz [indexModificar] [0])
                    print ("Película:", funciones_matriz [indexModificar] [1])
                    print ("Sala:", funciones_matriz [indexModificar] [2])
                    print ("Horario:", funciones_matriz [indexModificar] [3])
                    print ("Idioma:", funciones_matriz [indexModificar] [4])
                    print ("Tecnología:", funciones_matriz [indexModificar] [5])
                    print ()

                    print ("Ingrese a continuación los datos nuevos:")
                    sala_funcion = int(input("Ingrese el número de sala donde se proyectará: "))
                    horario_funcion = str(input("Ingrese el horario de la función (fecha y hora): "))
                    idioma_funcion = str(input("Ingrese si la película es doblada o subtitulada: "))
                    indexSalaFuncion = -1
                    print ()

                    for j in range (cantidad_salas):
                        if salas_matriz [j] [0] == sala_funcion:
                            indexSalaFuncion = j

                    if indexSalaFuncion == -1:
                        print ("Lo sentimos, la función solicitada no se encuentra en el sistema.")
                        print ()

                    else:
                        modificacion_funcion = [funciones_matriz [indexModificar] [0] , funciones_matriz [indexModificar] [1] , salas_matriz [indexSalaFuncion] [0] , horario_funcion , idioma_funcion , salas_matriz [indexSalaFuncion] [3]]
                        
                        funciones_matriz [indexModificar] = (modificacion_funcion)
                    
                        print ("¡La función ha sido modificada correctamente!")
                        print ()

            # Eliminar Función
            elif opcion_funciones == 4:
                print ("━ Eliminar una Función ━")
                print ()
                eliminar_funcion = int(input("Ingrese el número de la función a eliminar: "))
                indexEliminar = -1
                print ()

                for i in range (cantidad_funciones):
                    if funciones_matriz [i] [0] == eliminar_funcion:
                        indexEliminar = i
                
                if indexEliminar == -1:
                    print ("No se encontró el número de función:", eliminar_funcion)
                    print ()
                else:
                    print ("La función encontrada es la siguiente:")
                    print ()
                    print ("► Función", funciones_matriz [indexEliminar] [0])
                    print ("Película:", funciones_matriz [indexEliminar] [1])
                    print ("Sala:", funciones_matriz [indexEliminar] [2])
                    print ("Horario:", funciones_matriz [indexEliminar] [3])
                    print ("Idioma:", funciones_matriz [indexEliminar] [4])
                    print ("Tecnología:", funciones_matriz [indexEliminar] [5])
                    print ()

                    print (">> ¿Está seguro que desea eliminar esta función? <<")
                    print ("1 - Si")
                    print ("2 - No")
                    print ()
                    opcion_borrar = int(input("Ingrese una opción: "))
                    print ()

                    if opcion_borrar == 1:
                        funciones_matriz.pop (indexEliminar)

                        cantidad_funciones -= 1

                        print ("La función número", eliminar_funcion, "ha sido eliminada correctamente.")
                        print ("Para consultar las funciones restantes, puede revisarlas en el menú anterior.")
                        print ()
                    else:
                        print ("Ninguna función ha sido eliminada.")
                        print ()

            elif opcion_funciones == 5:
                print ("►► Regresando al menú anterior...")
                print ()
                break
            
            else:
                print ("Opción no disponible. Intente nuevamente.")
                print ()

    # Gestión de Ventas
    elif opcion_principal == 4:

        while True:
            opcion_ventas = 0
            print ("◣━━━ Gestión de Ventas ━━━◢")
            print ()
            print ("1 - Venta de Boletos")
            print ("2 - Mostrar Ventas")
            print ("3 - Volver al menú anterior")
            print ()
            opcion_ventas = int(input("Ingrese una opción: "))
            print ()

            # Venta de Boletos
            if opcion_ventas == 1:
                print ("━ Venta de Boletos ━")
                print ()
                print ("Por favor ingrese la información solicitada a continuación")
                codigo_venta = generaCode (codigo_venta)
                funcion_venta = int(input("Ingrese el número de función de la venta: "))
                cantidad_boletos = int(input("Ingrese la cantidad de boletos vendidos en dicha función: "))
                indexFuncionVenta = -1
                print ()

                for i in range (cantidad_funciones):
                    if funciones_matriz [i] [0] == funcion_venta:
                        indexFuncionVenta = i
                
                if indexFuncionVenta == -1:
                    print ("No hay una función registrada con la información introducida. Intente nuevamente.")
                    print ()
                
                else:
                    if funciones_matriz [indexFuncionVenta] [5] == "2d" or funciones_matriz [indexFuncionVenta] [5] == "2D":
                        precio_boleto = 2700
                    elif funciones_matriz [indexFuncionVenta] [5] == "3d" or funciones_matriz [indexFuncionVenta] [5] == "3D":
                        precio_boleto = 3400
                    else:
                        precio_boleto = 4800

                    total = (precio_boleto * cantidad_boletos)

                    cantidad_ventas += 1

                    # Posición     0              1           2                       3
                    venta = [codigo_venta , funcion_venta , total , funciones_matriz [indexFuncionVenta] [1]]

                    ventas_matriz.append (venta)

                    print ("Tipo de tecnología:", funciones_matriz [indexFuncionVenta] [5])
                    print ("Precio de la entrada:", precio_boleto, "colones.")
                    print ()
                    print ("El monto total de la venta es de", total, "colones.")
                    print ()

            # Mostrar Ventas
            elif opcion_ventas == 2:
                print ("━ Ventas Registradas ━")
                print ()

                if cantidad_ventas > 0:
                    print ("Actualmente hay", cantidad_ventas, "ventas registradas:")
                    print ()
                
                    for i in range (cantidad_ventas):
                        print ("► Código de venta: V - 0 0", ventas_matriz [i] [0])
                        print ("Función", ventas_matriz [i] [1])
                        print ("Total vendido:", ventas_matriz [i] [2], "colones.")
                        print ()

                else:
                    print ("Por el momento no hay ventas registradas.")
                    print ()

            elif opcion_ventas == 3:
                print ("►► Regresando al menú anterior...")
                print ()
                break
            
            else:
                print ("Opción no disponible. Intente nuevamente.")
                print ()

    # Reportes y Estadísticas
    elif opcion_principal == 5:
        while True:
            opcion_reportes = 0
            print ("◣━━━ Reportes y Estadísticas ━━━◢")
            print ()
            print ("1 - Taquilla por Película")
            print ("2 - Taquilla por Sala")
            print ("3 - Películas más Populares")
            print ("4 - Ventas por Fecha")
            print ("5 - Funciones más Vendidas")
            print ("6 - Volver al menú anterior")
            print ()
            opcion_reportes = int(input("Ingrese una opción: "))
            print ()

            # Taquilla por Película
            if opcion_reportes == 1:
                print ("▬ Taquilla por Película ▬")
                print ()
                print ("Películas disponibles y sus ingresos:")
                print ()
                indexTaquillaPeli = -1

                for i in range (cantidad_funciones):
                    if ventas_matriz [i] [3] == funciones_matriz [i] [1]:
                        indexTaquillaPeli = i

                        if indexTaquillaPeli == -1:
                            print ("No existe registro de taquilla por el momento.")
                            print ()

                        else:
                            codigo_taquilla_peli = generaTaquillaPeli (codigo_taquilla_peli)

                            file = open ("TaquillaPelículaRE0" + (str(codigo_taquilla_peli)) + ".txt", "w")

                            print ("► Película:" , ventas_matriz [indexTaquillaPeli] [3])
                            print ("►► Ingreso total:" , ventas_matriz [indexTaquillaPeli] [2] , "colones.")
                            print ()

                            file.write ("Película: " + (ventas_matriz [indexTaquillaPeli] [3]) + "\n")
                            file.write ("Ingreso total: " + (str(ventas_matriz [indexTaquillaPeli] [2])) + " colones." + "\n")
                            file.write ("\n")

                            file.close ()
            
            # Taquilla por Sala
            elif opcion_reportes == 2:
                print ("▬ Taquilla por Sala ▬")
                print ()
                print ("Salas registradas y sus ingresos:")
                print ()

                indexTaquillaSala = -1
                total_tec_2d = 0
                total_tec_3d = 0
                total_tec_imax = 0
                
                for i in range (cantidad_salas):
                    if salas_matriz [i] [3] == funciones_matriz [i] [5]:
                        indexTaquillaSala = i

                        if indexTaquillaSala == -1:
                            print ("No existe registro de taquilla por el momento.")
                            print ()

                        else:

                            if salas_matriz [i] [3] == "2D" or salas_matriz [i] [3] == "2d":
                                total_tec_2d += ventas_matriz [indexTaquillaSala] [2]

                            elif salas_matriz [i] [3] == "3D" or salas_matriz [i] [3] == "3d":
                                total_tec_3d += ventas_matriz [indexTaquillaSala] [2]

                            else:
                                total_tec_imax += ventas_matriz [indexTaquillaSala] [2]

                print ("► Tecnología de sala: 2D")
                print ("►► Ingreso total:" , total_tec_2d , "colones.")
                print ()
                print ("► Tecnología de sala: 3D")
                print ("►► Ingreso total:" , total_tec_3d , "colones.")
                print ()
                print ("► Tecnología de sala: IMAX")
                print ("►► Ingreso total:" , total_tec_imax , "colones.")
                print ()

                codigo_taquilla_sala = generaTaquillaSala (codigo_taquilla_sala)

                file = open ("TaquillaSalaRE0" + (str(codigo_taquilla_sala)) + ".txt", "w")

                file.write ("Tecnología de sala: 2D \n")
                file.write ("Ingreso total: " + str(total_tec_2d) + " colones. \n")
                file.write ("\n")
                file.write ("Tecnología de sala: 3D \n")
                file.write ("Ingreso total: " + str(total_tec_3d) + " colones. \n")
                file.write ("\n")
                file.write ("Tecnología de sala: IMAX \n")
                file.write ("Ingreso total: " + str(total_tec_imax) + " colones. \n")
                file.write ("\n")

                file.close ()

            # Películas más Populares
            elif opcion_reportes == 3:
                print ("▬ Películas más Populares ▬")
                print ()
                indexPeliPopular = -1

                if cantidad_funciones > 0:
                    print ("Películas más proyectadas:")
                    print ()
                
                    for i in range (cantidad_funciones):
                        for j in range (cantidad_funciones):
                            if funciones_matriz [i] [1] == funciones_matriz [j] [1]:
                                indexPeliPopular = i

                    if indexPeliPopular == -1:
                        print ("Por el momento no hay películas registradas.")
                        print ()

                    else:
                        print ("► Función", funciones_matriz [indexPeliPopular] [0])
                        print ("Película:", funciones_matriz [indexPeliPopular] [1])
                        print ("Sala:", funciones_matriz [indexPeliPopular] [2])
                        print ("Horario:", funciones_matriz [indexPeliPopular] [3])
                        print ("Idioma:", funciones_matriz [indexPeliPopular] [4])
                        print ("Tecnología:", funciones_matriz [indexPeliPopular] [5])
                        print ()

                        codigo_mas_populares = generaMasPopulares (codigo_mas_populares)

                        file = open ("PeliculasPopularesRE0" + (str(codigo_mas_populares)) + ".txt", "w")

                        file.write ("Función " + str(funciones_matriz [indexPeliPopular] [0]) + "\n")
                        file.write ("Película: " + str(funciones_matriz [indexPeliPopular] [1]) + "\n")
                        file.write ("Sala: " + str(funciones_matriz [indexPeliPopular] [2]) + "\n")
                        file.write ("Horario: " + str(funciones_matriz [indexPeliPopular] [3]) + "\n")
                        file.write ("Idioma: " + str(funciones_matriz [indexPeliPopular] [4]) + "\n")
                        file.write ("Tecnología: " + str(funciones_matriz [indexPeliPopular] [5]) + "\n")
                        file.write ("\n")

                        file.close ()

                else:
                    print ("Por el momento no hay películas registradas.")
                    print ()

            # Ventas por Fecha
            elif opcion_reportes == 4:
                print ("▬ Ventas por Fecha ▬")
                print ()
                fecha = str(input("Ingrese el horario de la función (día y hora): "))
                print ()
                indexFechaFunción = -1
                indexFechaVenta = -1

                for i in range (cantidad_funciones):
                    if fecha == funciones_matriz [i] [3]:
                        indexFechaFunción = i

                        if indexFechaFunción == -1:
                            print ("Por el momento no hay función registrada con ese horario.")
                            print ()
                        
                        else:
                            for i in range (cantidad_funciones):
                                if funciones_matriz [indexFechaFunción] [0] == ventas_matriz [i] [1]:
                                    indexFechaVenta = i

                                    print ("► Función" , funciones_matriz [indexFechaFunción] [0])
                                    print ("Horario:" , funciones_matriz [indexFechaFunción] [3])
                                    print ("Código de venta: V - 0 0", ventas_matriz [indexFechaVenta] [0])
                                    print ("Ventas generadas:" , ventas_matriz [indexFechaVenta] [2], "colones.")
                                    print ()

                                    codigo_venta_fecha = generaVentaFecha (codigo_venta_fecha)

                                    file = open ("VentasFechaRE0" + (str(codigo_venta_fecha)) + ".txt", "w")

                                    file.write ("Función " + str(funciones_matriz [indexFechaFunción] [0]) + "\n")
                                    file.write ("Horario: " + str(funciones_matriz [indexFechaFunción] [3]) + "\n")
                                    file.write ("Código de venta: V - 0 0" + str(ventas_matriz [indexFechaVenta] [0]) + "\n")
                                    file.write ("Ventas generadas: " + str(ventas_matriz [indexFechaVenta] [2]) + "colones.\n")
                                    file.write ("\n")

                                    file.close ()

            # Funciones más Vendidas
            elif opcion_reportes == 5:
                print ("▬ Funciones más Vendidas ▬")
                print ()
                mayor_venta = 0
                menor_venta = 0
                indexMasVendidasMax = -1
                indexMasVendidasMin = -1
                indexFuncionMax = -1
                indexFuncionMin = -1

                if cantidad_funciones > 0:

                    for i in range ((cantidad_funciones - 1)):
                        if ventas_matriz [i] [2] > ventas_matriz [i + 1] [2]:
                            mayor_venta = ventas_matriz [i] [2]
                            menor_venta = ventas_matriz [i + 1] [2]
                        else:
                            mayor_venta = ventas_matriz [i + 1] [2]
                            menor_venta = ventas_matriz [i] [2]

                    for i in range (cantidad_funciones):
                        if ventas_matriz [i] [2] == mayor_venta:
                            indexMasVendidasMax = i

                    for i in range (cantidad_funciones):
                        if ventas_matriz [i] [2] == menor_venta:
                            indexMasVendidasMin = i

                    for i in range (cantidad_funciones):
                        if funciones_matriz [i] [0] == ventas_matriz [indexMasVendidasMax] [1]:
                            indexFuncionMax = i

                            print ("Función más vendida: Función" , funciones_matriz [indexFuncionMax] [0])
                            print ("Película:" , funciones_matriz [indexFuncionMax] [1])
                            print ("Sala:" , funciones_matriz [indexFuncionMax] [2])
                            print ("Horario:" , funciones_matriz [indexFuncionMax] [3])
                            print ()

                    for i in range (cantidad_funciones):
                        if funciones_matriz [i] [0] == ventas_matriz [indexMasVendidasMin] [1]:
                            indexFuncionMin = i

                            print ("Función menos vendida: Función" , funciones_matriz [indexFuncionMin] [0])
                            print ("Película:" , funciones_matriz [indexFuncionMin] [1])
                            print ("Sala:" , funciones_matriz [indexFuncionMin] [2])
                            print ("Horario:" , funciones_matriz [indexFuncionMin] [3])
                            print ()
                    
                    codigo_mas_vendidas = generaMasVendidas (codigo_mas_vendidas)

                    file = open ("FuncionesMasVendidasRE0" + (str(codigo_mas_vendidas)) + ".txt", "w")

                    file.write ("Función más vendida: Función " + str(funciones_matriz [indexFuncionMax] [0]) + "\n")
                    file.write ("Película: " + str(funciones_matriz [indexFuncionMax] [1]) + "\n")
                    file.write ("Sala: " + str(funciones_matriz [indexFuncionMax] [2]) + "\n")
                    file.write ("Horario: " + str(funciones_matriz [indexFuncionMax] [3]) + "\n")
                    file.write ("\n")
                    file.write ("Función menos vendida: Función " + str(funciones_matriz [indexFuncionMin] [0]) + "\n")
                    file.write ("Película: " + str(funciones_matriz [indexFuncionMin] [1]) + "\n")
                    file.write ("Sala: " + str(funciones_matriz [indexFuncionMin] [2]) + "\n")
                    file.write ("Horario: " + str(funciones_matriz [indexFuncionMin] [3]) + "\n")
                    file.write ("\n")

                    file.close ()


                else:
                    print ("Por el momento no existe registro de funciones. Intente nuevamente.")
                    print ()

            elif opcion_reportes == 6:
                print ("►► Regresando al menú anterior...")
                print ()
                break

            else:
                print ("Opción no disponible. Intente nuevamente.")
                print ()

    # Salir
    elif opcion_principal == 6:
        print ("❢ ◥ ▬▬▬ ¡Muchas gracias por visitarnos! ¡Vuelva pronto! ▬▬▬ ◤ ❢")
        print ()

    # Opción inválida
    else:
        print ("Opción no disponible. Intente nuevamente.")
        print ()
