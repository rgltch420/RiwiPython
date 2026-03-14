# 📦 Sistema de Inventario en Python
![alt text](images.png)
## 📖 Descripción del Proyecto

Este proyecto es un **programa simple de gestión de inventario desarrollado en Python**.
El objetivo del programa es permitir que un usuario **registre productos**, indicando:

* El **nombre del producto**
* El **precio del producto**
* La **cantidad disponible**

Con esta información, el programa **calcula automáticamente el costo total** de cada producto (precio × cantidad).

Finalmente, el programa muestra **todo el inventario registrado** de una forma organizada.

Este programa funciona **en la terminal** y utiliza interacción con el usuario mediante texto.

---

# 🎯 Objetivo del Programa

El objetivo principal del programa es aprender y demostrar algunos **conceptos fundamentales de programación en Python**, como:

* Uso de **variables**
* Uso de **diccionarios**
* Creación de **funciones**
* Uso de **bucles (loops)**
* Manejo de **errores**
* Entrada de datos por el usuario
* Validación de datos
* Operaciones matemáticas básicas

---

# 🧠 Explicación Conceptual (Muy Sencilla)

Imagina que tienes una **tienda** 🏪.

En tu tienda necesitas saber:

* Qué productos tienes
* Cuánto cuestan
* Cuántos hay disponibles

Este programa funciona como **una libreta digital** donde puedes escribir todos los productos que tienes.

Cada vez que agregas un producto, el programa lo guarda dentro de una estructura llamada **diccionario** en Python.

Ese diccionario se llama:

```
inventory
```

Dentro de ese diccionario se guarda la información de cada producto.

Por ejemplo:

```
{
 "Manzana": {
   "precio": 2,
   "cantidad": 10,
   "costo_total": 20
 }
}
```

Esto significa:

* Manzana cuesta 2
* hay 10 unidades
* el costo total es 20

---

# 🛠 Tecnologías Utilizadas

Este proyecto utiliza:

* **Python 3**

Librerías estándar de Python:

* `os`
* `pprint`

No se necesitan instalar librerías adicionales.

---

# 📚 Librerías Utilizadas

## 1️⃣ Librería `os`

```python
import os
```

La librería `os` permite que Python **interactúe con el sistema operativo**.

En este programa se usa para **limpiar la pantalla de la terminal**.

Código utilizado:

```python
os.system("cls" if os.name == "nt" else "clear")
```

Explicación:

* Si el sistema es **Windows**, ejecuta `cls`
* Si el sistema es **Linux o Mac**, ejecuta `clear`

Esto hace que la terminal **no se vea llena de texto** y sea más fácil leer.

---

## 2️⃣ Librería `pprint`

```python
import pprint
```

`pprint` significa **pretty print**, es decir, **impresión bonita**.

Sirve para mostrar estructuras complejas como diccionarios de forma **más organizada y fácil de leer**.

Ejemplo:

```python
pprint.pprint(inventory)
```

En lugar de imprimir todo en una sola línea desordenada, lo muestra estructurado.

---

# 📦 Variable Global

```python
inventory = {}
```

Aquí se crea un **diccionario vacío**.

Un diccionario es como **una caja donde guardamos información**.

En este caso guardaremos **todos los productos registrados**.

Cada producto se guarda de esta forma:

```python
inventory[nombre_producto] = {
    "precio": price,
    "cantidad": quantity,
    "costo_total": total_cost
}
```

---

# 🔧 Función `create_product()`

Esta función se encarga de **crear un producto y guardarlo en el inventario**.

```python
def create_product():
```

Una función es un **bloque de código que realiza una tarea específica**.

En este caso la tarea es **registrar un producto**.

---

# 🔁 Bucle Infinito

Dentro de la función existe un bucle:

```python
while True:
```

Esto significa:

El programa **seguirá pidiendo datos hasta que el usuario ingrese información válida**.

Si el usuario comete un error, el programa **no se rompe**, simplemente vuelve a preguntar.

---

# ⌨️ Entrada de Datos del Usuario

El programa solicita tres datos:

```python
name_product = input("Enter the name of product: ").strip()
price_input = input("Enter the price of product: ").strip()
quantity_input = input("Enter the quantity of product: ").strip()
```

Explicación:

`input()` permite que el usuario escriba información.

`.strip()` elimina espacios innecesarios.

Por ejemplo:

Si el usuario escribe:

```
   manzana
```

`.strip()` lo convierte en:

```
manzana
```

---

# 🧹 Limpieza de Pantalla

Después de ingresar los datos se limpia la pantalla:

```python
os.system("cls" if os.name == "nt" else "clear")
```

Esto hace que la terminal **se vea más ordenada**.

---

# ⚠️ Validación de Campos Vacíos

El programa verifica que el usuario **no deje campos vacíos**.

```python
if not (name_product and price_input and quantity_input):
```

Si algún campo está vacío se muestra el mensaje:

```
No dejes campos vacios
```

y el programa vuelve a pedir los datos.

---

# 🔢 Conversión de Datos

Los datos ingresados por el usuario son **texto**.

Por eso deben convertirse a números.

```python
price = float(price_input)
quantity = int(quantity_input)
```

Esto permite realizar cálculos.

Ejemplo:

| Entrada | Tipo convertido |
| ------- | --------------- |
| "10.5"  | float           |
| "3"     | int             |

---

# 🚫 Validación de Números Negativos

El programa evita valores negativos.

```python
if price < 0 or quantity < 0:
```

Ejemplo de valor incorrecto:

```
precio: -5
```

El programa mostrará:

```
Ingresa solo numeros positivos
```

---

# 🧮 Cálculo del Costo Total

El costo total se calcula así:

```python
total_cost = price * quantity
```

Ejemplo:

```
precio = 10
cantidad = 5
```

Resultado:

```
costo_total = 50
```

---

# 💾 Guardar el Producto en el Inventario

El producto se guarda dentro del diccionario `inventory`.

```python
inventory[name_product] = {
    "precio": price,
    "cantidad": quantity,
    "costo_total": total_cost
}
```

Ejemplo del resultado:

```
{
 "Laptop": {
   "precio": 500,
   "cantidad": 2,
   "costo_total": 1000
 }
}
```

---

# 🔙 Retorno del Nombre del Producto

La función devuelve el nombre del producto:

```python
return name_product
```

Esto permite mostrar el mensaje de confirmación.

---

# ⚠️ Manejo de Errores

El programa utiliza:

```python
except ValueError:
```

Esto ocurre cuando el usuario escribe algo que **no es un número**.

Ejemplo:

```
precio: diez
```

El programa mostrará:

```
Error: ID, Precio y Cantidad deben ser números.
```

---

# 🔁 Bucle Principal del Programa

El programa principal también usa un bucle:

```python
while True:
```

Este bucle controla todo el flujo del programa.

---

# 📥 Cantidad de Productos

El usuario debe ingresar cuántos productos desea registrar.

```python
num_products = int(input("enter the quantity of products required: "))
```

Ejemplo:

```
3
```

El programa pedirá **3 productos**.

---

# 🚫 Validación de Cantidad

El programa evita valores menores a 1.

```python
if num_products < 1:
```

Esto evita entradas como:

```
0
-2
```

---

# 🔁 Registro de Productos

Se usa un bucle `for`:

```python
for _ in range(num_products):
```

Si el usuario ingresó:

```
3
```

El programa registrará **3 productos**.

---

# 📢 Mensaje de Confirmación

Después de registrar cada producto se muestra:

```
Producto 'nombre' añadido con éxito
```

Ejemplo:

```
Producto 'Manzana' añadido con éxito
```

---

# 🧹 Limpieza Antes del Resultado Final

Antes de mostrar el inventario final se limpia la pantalla nuevamente.

---

# 📊 Inventario Final

Finalmente se muestra el inventario completo:

```python
pprint.pprint(inventory)
```

Ejemplo de salida:

```
{
 'Manzana': {'precio': 2.0, 'cantidad': 10, 'costo_total': 20.0},
 'Leche': {'precio': 3.5, 'cantidad': 4, 'costo_total': 14.0}
}
```

---

# ▶️ Ejemplo de Ejecución

Ejemplo de uso del programa:

```
enter the quantity of products required: 2

--- Registro de producto 1 ---
Enter the name of product: Manzana
Enter the price of product: 2
Enter the quantity of product: 10

Producto 'Manzana' añadido con éxito!

--- Registro de producto 2 ---
Enter the name of product: Leche
Enter the price of product: 3
Enter the quantity of product: 5
```

Resultado final:

```
--- inventario final ---

{
 'Manzana': {'precio': 2.0, 'cantidad': 10, 'costo_total': 20.0},
 'Leche': {'precio': 3.0, 'cantidad': 5, 'costo_total': 15.0}
}
```

