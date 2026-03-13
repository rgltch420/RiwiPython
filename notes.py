import os
print("Bienvenido a notas")
students = {}
orderNotes=[]

  
def notes(id_st, nombre):
    noteDesarrollo = float(input("Ingresa tu nota de desarrollo: "))
    if noteDesarrollo <= 50:
        print("Debe reforzar el frente técnico principal.")
    noteIngles = float(input("Ingresa tu nota de ingles: "))
    noteSkilss = float(input("Ingresa tu nota de habilidades blandas: "))
    noteDesarrolloFina = float(noteDesarrollo * 0.60)
    noteInglesFina = float(noteIngles * 0.20)
    noteSkilssFina= float(noteSkilss * 0.20)
    ponderado = float(noteDesarrolloFina + noteSkilssFina + noteInglesFina)
    students [id_st] ={"Nombre": nombre, "ponderado": ponderado}
    return noteInglesFina, noteSkilssFina, noteDesarrolloFina, ponderado

def order():

    ranking = sorted(students.values(), key=lambda x: x['ponderado'], reverse = True)
    print("Estudiantes de mayor a menor")
    for stu in ranking:
        print(f"Nombre: {stu['Nombre']} | Ponderado: {stu['ponderado']:.2f}")




try:
    while True:
          id_st = int(input("Ingresa el ID del usuario: ")) 
          nombre = input("Nombre del estudiante: ")
          print(f"Estudiante {nombre} agregado con éxito.")

          os.system('clear')


          _, _, _, ponderado = notes(id_st, nombre)

          if ponderado < 50:
              
              print(order())
          elif ponderado < 80:
              print(order())
          elif ponderado <= 100:
              print(order())
          else:
              print("Revisa tus notas no son validas")
except ValueError:
     print("Ingresa un valor correcto")    
