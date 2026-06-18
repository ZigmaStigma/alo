
def menu():
    print("Sistema de gestión de peliculas")
    print("1.Agregar Pelicula")
    print("2.Listar Peliculas")
    print("3.Buscar Pelicula")
    print("4.Actualizar Pelicula")
    print("5.Eliminar Pelicula")
    print("6.Salir")

def agregar_pelicula(lista_peliculas):
    print("Agrega una pelicula")

    nombre = input("Ingrese el nombre de la pelicula: ").strip().lower()
    if not nombre:
        print("El nombre de la pelicula no puede estar vacio.")
        return
    
    for pelicula in lista_peliculas:
        if pelicula["nombre"].lower() == nombre.lower():
            print(f"La pelicula '{nombre}' ya se encuentra registrada")
            return
    try:
        año = int(input("Ingrese el año de estreno: "))
        if año < 1888 and año > 2026:
            print("Año fuera del rango valido (1888-2026).")
            return

    except ValueError:
        print("Entrada invalida, debe ser un número entero.")
        return
    
    categoria = input("Ingrese la categoría de la pelicula: ").strip().lower()
    if not categoria:
        print("La categoría no puede estar vacía.")
        return
    
    nueva_pelicula = {
        "nombre": nombre,
        "año": año,
        "categoria": categoria,
    }

    lista_peliculas.append(nueva_pelicula)
    print(f"Pelicula '{nombre}' guardada exitosamente.")

def listar_peliculas(lista_peliculas):
    if not lista_peliculas:
        print("La base de datos se encuentra vacía.")
        return
    
    print(f"Inventarío actual ({len(lista_peliculas)}) registros.")
    for i, pelicula in enumerate(lista_peliculas, start=1):
        print(f"{i}. {pelicula['nombre'].title()} - ({pelicula['año']}) - {pelicula['categoria'].capitalize()}")

def buscar_pelicula(lista_peliculas):
    if not lista_peliculas:
        print("Directorio vacio.")
        return
    
    termino = input("Ingrese el nombre de la pelicula a buscar: ").strip().lower()
    if not termino:
        print("El termino de la busqueda no puede estar vacio.")

    coincidencias = [p for p in lista_peliculas if termino in p["nombre"].lower()]

    if not coincidencias:
        print("No se puede encontrar la pelicula.")
    else:
        print(f"Se hallaron {len(coincidencias)} resultados(s): ")
        for i, pelicula in enumerate(coincidencias, start=1):
            print(f"{i}. {pelicula["nombre"].title()} ({pelicula["año"]})")

def actualizar_pelicula(lista_peliculas):
    if not listar_peliculas:
        print("Directorio vacio")
        return
    
    nombre_buscado = input("Ingrese le nombre de la pelicula exacta a modificar: ").strip().lower()
    indice_encontrado = -1

    for i, pelicula in enumerate(lista_peliculas):
        if pelicula["nombre"].lower() == nombre_buscado:
            indice_encontrado = i
            break
    
    if indice_encontrado == -1:
        print("Pelicula no localizada.")
        return
    
    ref_pelicula = lista_peliculas[indice_encontrado]
    print(f"Modificando {ref_pelicula['nombre'].title()}")
    print("Nota: Presione enter sin escribir nada para mantener el valor actual.")
    
    nuevo_nombre = input(f"Ingrese el nuevo nombre de la pelicula [{ref_pelicula['nombre']}]: ").strip()
    if nuevo_nombre:
        ref_pelicula["nombre"] = nuevo_nombre

    nuevo_año_str = input(f"Nuevo año [{ref_pelicula['año']}]: ").strip()
    if nuevo_año_str:
        try:
            nuevo_año = int(nuevo_año_str)
            ref_pelicula["año"] = nuevo_año
        except ValueError:
            print("Año invalido ignorado, se conservara el originial.")
    
    nueva_categoria = input(f"Nueva categoria [{ref_pelicula['categoria']}]: ").strip()
    if nueva_categoria:
        ref_pelicula["categoria"] = nueva_categoria

    print("Registro actualizado con exito.")

def eliminar_pelicula(lista_peliculas):
    if not lista_peliculas:
        print("Directorio vacio.")
        return
    
    nombre_eliminar = input("Ingrese el nombre exacto de la pelicula a eliminar: ").strip().lower()

    for i, pelicula in enumerate(lista_peliculas):
        if pelicula["nombre"].lower() == nombre_eliminar:
            print(f"Se eliminara definitivamente : {pelicula["nombre"].title()}")
            confirmacion = input("Confirmación de la eliminación (S/N): ").strip().lower()

            if confirmacion in ['s','si','y','yes']:
                del lista_peliculas[i]
                print("Eliminación completada.")
            else:
                print("Operación abortada.")
            return
        
def ejecutar_sistema():

    inventario_peliculas = []
    print("Inicializando Sistema Core...")
    while True:
        try:
            menu()
            opcion = input("Seleccione una operación [1-6]: ").strip()
            if opcion == "1":
                agregar_pelicula(inventario_peliculas)
            elif opcion == "2":
                listar_peliculas(inventario_peliculas)
            elif opcion == "3":
                buscar_pelicula(inventario_peliculas)
            elif opcion == "4":
                actualizar_pelicula(inventario_peliculas)
            elif opcion == "5":
                eliminar_pelicula(inventario_peliculas)
            elif opcion == "6":
                print("Cerrando sesión...")
                break
        except KeyboardInterrupt:
            print("Interrupción forzada por el usuario, cerrando programa.")
            break
        except Exception as e:
            print("Se produjo un fallo del sistema.")

##aloalo