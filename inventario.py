# AQUI NOSOTROS SOLO TOMAMOS EL NOMBRE DE EL CLIENTE Y LE DAMOS UNA BIENVENIDA A NUESTRO SISTEMA.
# HERE WE ONLY GET THE CUSTOMER NAME AND WE GIVE AN WELCOME TO OUR SYSTEM.
nombre_cliente = input("\nINDICANOS CUAL ES TU NOMBRE: ")
print(f"\nBIENVENIDO {nombre_cliente} A NUESTRO SISTEMA DE INVENTARIO")

# INVENTARIO INICIAL CON 5 PRODUCTOS
inventario_tienda = [
    {"nombre": "LAMPARA DE ESCRITORIO", "precio": 25.99, "cantidad": 10},
    {"nombre": "LAMPARA DE TECHO", "precio": 45.50, "cantidad": 5},
    {"nombre": "BOMBILLO LED", "precio": 3.75, "cantidad": 50},
    {"nombre": "LAMPARA DE PIE", "precio": 60.00, "cantidad": 7},
    {"nombre": "APLIQUE DE PARED", "precio": 30.25, "cantidad": 12}
]

# ESTE EL EL MENU QUE PUEDE VER EL CLIENTE.
# THIS IS THE MENU THAT CAN SEE THE CUSTOMER.

def menu_tienda():
    print("\n----INVENTARIO ACTUAL DE PRODUCTOS DE NUESTRA TIENDA----")
    print("1. AÑADIR UN NUEVO PRODUCTO A NUESTRO INVENTARIO")
    print("2. BUSCAR UN PRODUCTO EN EL INVENTARIO DE LA TIENDA")
    print("3. ACTUALIZAR NUESTRO CATALOGO")
    print("4. VER TODO EL INVENTARIO")
    print("5. CALCULAR EL VALOR TOTAL DEL INVENTARIO")
    print("6. ELIMINAR UN PRODUCTO DE NUESTRO INVENTARIO")
    print("7. SALIR")

# AQUI EL CLIENTE PUEDE AÑADIR CUALQUIER PRODUCTO EN NUESTRO SISTEMA.
# HERE THE CUSTOMER CAN ADD ANY PRODUCT IN OUR SYSTEM.

def agg_producto():
    print("\n--- AÑADIR UN PRODUCTO A NUESTRO INVENTARIO ---")
    nombre = input("INDIQUENOS EL NOMBRE DE EL NUEVO PRODUCTO: ").strip()
    while nombre == "":
        nombre = input("ERROR: INDIQUENOS UN NOMBRE VALIDO: ").strip()

    try:
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
    except ValueError:
        print("Error: INDIQUENOS LA CANTIDAD Y EL PRECIO EN NUMEROS:")
        return

    inventario_tienda.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })
    print("¡SU PRODUCTO FUE AGREGADO EXITOSAMENTE!")

# AQUI EL CLIENTE PUEDE VER LOS PRODUCTOS LOS CUALES AÑADIO EN NUESTRO SISTEMA.
# HERE THE CUSTOMER CAN SEE THE PRODUCTS THAT ARE ADD IN OUR SYSTEM.

def buscar_producto():
    print("\n--- BUSCAR UN PRODUCTO EN NUESTRO INVENTARIO DE LA TIENDA---")
    nombre = input("INDICANOS QUE PRODUCTO ESTAS BUSCANDO: ").strip().lower()
    for p in inventario_tienda:
        if p["nombre"].lower() == nombre:
            print(f"Nombre: {p['nombre']}")
            print(f"Precio: ${p['precio']}")
            print(f"Cantidad: {p['cantidad']}")
            return
    print("ESTE PRODUCTO NO HAS SIDO ENCONTRADO")

# AQUI EL CLIENTE PUEDE ACTUALIZAR LOS PRODUCTOS LOS CUALES TENEMOS EN NUESTRO INVENTARIO CON INFORMACION NUEVA.
# HERE THE CUSTOMER CAN UPDATE THE PRODUCTS THAT WE HAVE IN OUR INVENTORY WHIT NEW INFORMATION.

def act_producto():
    print("\n--- ACTUALIZAR NUESTRO CATALOGO---")
    nombre = input("¿QUE PRODUCTO DESEA ACTUALIZAR? ").strip().lower()
    for p in inventario_tienda:
        if p["nombre"].lower() == nombre:
            try:
                nuevo_precio = float(input("INTRODUZCA EL NUEVO PRECIO: "))
                p["precio"] = nuevo_precio
                print("¡FELICIDADES SU PRECIO HA SIDO ACTUALIZADO EXITOSAMENTE!")
                return
            except ValueError:
                print("ERROR: DEBE INTRODUCIR UN PRECIO QUE SEA UN NUMERO:")
                return
    print("ESTE PRODUCTO NO HA SIDO ENCONTRADO")

# EN ESTA SECCION EL CLIENTE PUEDE ELIMINAR LOS PRODUCTOS QUE SE ENCUENTRAN EN EL INVENTARIO.
# ON THIS SECTION THE CUSTOMER CAN DELETE THE PRODUCTS THAT ARE IN OUR INVENTORY.

def eliminar_producto():
    print("\n--- ELIMINAR UN PRODUCTO DE NUESTRO CATALOGO")
    nombre = input("INDIQUENOS QUE PRODUCTO DE NUESTRO CATALOGO DESEAS ELIMINAR: ").strip().lower()
    for i, p in enumerate(inventario_tienda):
        if p["nombre"].lower() == nombre:
            inventario_tienda.pop(i)
            print("¡ESTE PRODUCTO HA SIDO ELIMINADO EXITOSAMENTE!")
            return
    print("ESTE PRODUCTO NO HA SIDO ENCONTRADO")

# EN ESTA SECCION NUESTRO SISTEMA HACE UN CALCULO DE LOS ARTICULOS QUE TENEMOS EN NUESTRO INVENTARIO
# Y NOS MUESTRA LAS EXISTENCIAS Y PRECIO DE TODO LO QUE TENEMOS EN NUESTRO INVENTARIO.
# ON THIS SECTION OUR SYSTEM DO AN CALCULATION OF THE ARTICLES THAT WE HAVE IN OUR INVENTORY AND SHOW US
# THE EXISTENCES AND THE PRICE OF ALL THAT WE HAVE IN OUR INVENTORY.

def calcular_total():
    print("\n--- CALCULAR EL VALOR TOTAL DEL INVENTARIO ---")
    if not inventario_tienda:
        print("ACTUALMENTE NO SE ENCUENTRAN PRODUCTOS EN NUESTRO INVENTARIO PRUEBA AGREGAR ALGUNO")
        return
    total = sum(p["precio"] * p["cantidad"] for p in inventario_tienda)
    print(f"NUESTRO VALOR TOTAL DE INVENTARIO ACTUALMENTE ES ${total:.2f}")

# HERE WE CAN SEE ALL THE ARTICLES THAT WE HAVE IN OUR INVENTORY.
#AQUI PODREMOS VER TODOS LOS ARTICULO QUE TENEMOS EN NUESTRO INVENTARIO.

def ver_inventario():
    print("\n--- VER TODO NUESTRO INVENTARIO---")
    if not inventario_tienda:
        print("ACTUALMENTE NO CONTAMOS CON NINGUN ARTICULO EN NUESTRO INVENTARIO")
        return
    for idx, p in enumerate(inventario_tienda, start=1):
        print(f"{idx}. Nombre: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

# MENU FUNCIONAL
def main():
    print("\n ¿QUE DESEA HACER EL DIA DE HOY?")
    while True:
        menu_tienda()
        option = input("SELECCIONA UNA OPCION (1-7): ").strip()
        if option == "1":
            agg_producto()
        elif option == "2":
            buscar_producto()
        elif option == "3":
            act_producto()
        elif option == "4":
            ver_inventario()
        elif option == "5":
            calcular_total()
        elif option == "6":
            eliminar_producto()
        elif option == "7":
            print(f"¡ESPERAMOS VERTE DE NUEVO {nombre_cliente}!") 
            break
        else:
            print("DEBE SELECCIONAR UNA OPCION VALIDA INTENTE DE NUEVO")

if __name__ == "__main__":
    main()