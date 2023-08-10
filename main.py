from  productos import Producto
from utilitarios import input_int

menu = """
    CAFETIN SENATI 
___________________
      opciones

    1. ALMUERZO
    2. DESAYUNO
    3. CENA
    4. EXTRAS
"""
jp = Producto("JUGO DE QUINUA", 2, 50)
# lista_cafetin = [
#    {"desayuno":[]},
#    {"almuerzo":[]},
#    {"cena":[]},
#     {"extras":[]},
# ]
lista_productos = []
lista_almuerzo = []
lista_cena = []
lista_extras = []
def crear_producto(list_product):
    nombre_p = input("Nombre del producto: ")
    precio_p = input_int("Precio del producto: ", "no ingresaste bien el precio")
    stock_p = input_int("Cantidad del producto: ", "no ingresaste bien el stock")
    item_p =Producto(nombre_p, precio_p, stock_p) 
    list_product.append(item_p)

p = Producto("JUGO DE QUINUA", 2, 50)
c = Producto("PAN CON PALTA", 2, 50)
lista_productos.append(p)
lista_productos.append(c)


s = Producto("SECO DE POLLO", 7, 50)
b = Producto("CHIFA", 10, 50)
lista_productos.append(s)
lista_productos.append(b)

f = Producto("POLLO", 15, 50)
z = Producto("SEVICHE", 13, 50)
lista_productos.append(f)
lista_productos.append(z)

h = Producto("pollo dorado", 8, 50)
m = Producto("caldo", 4, 50)
lista_productos.append(h)
lista_productos.append(m)

def lista_prodcutos(list_product):
     contador = 0
     for item in list_product:
          contador +=1
          print(f"{contador}. {item.get_info_completa()}")

def vender_producto(product_selected, cantidad):
  product_selected.actualizar_stock(cantidad)



# lista_prodcutos(lista_productos)
  print(menu)

opcion = input_int("eleja un opcion: ", "No existe esa opcion")
if opcion == 1:
   lista_productos(lista_productos)
   opcion_desayuno = input_int("elija un desayuno: ", "No existe esa opcion")
   Producto_seleccionado = lista_productos[opcion_desayuno -1]
   pregunta = input_int("cual es la cantidad que desea: ", "No existe esta opcion")
   vender_producto(Producto_seleccionado, pregunta)
   subtotal = Producto_seleccionado.get_precio() * pregunta 
#    print(Producto_seleccionado.get_nombre())
#    print(pregunta)
#    print(subtotal)
     print(tiket_venta(Producto_seleccionado.get_nombre(), pregunta, sudtotal))
#    print(Producto_seleccionado.get_info_conpleta())


elif opcion == 2:
   lista_productos(lista_almuerzo)
elif opcion == 3:   
   lista_productos(lista_cena)
elif opcion == 4:
   lista_productos(lista_extras)


   eleccion_desayuno = input_int("Elija unba opcion: ", "no existe esta opcion")
   print(eleccion_desayuno)
   if eleccion_desayuno ==1:
         print("pan con cafe")
