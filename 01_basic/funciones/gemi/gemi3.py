"""
Ejercicio 3: Ordenamiento multicriterio para un dashboard

En el backend de una plataforma de cursos online, estás generando un
reporte de rendimiento de estudiantes. Quieres ordenar la lista de estudiantes
primero de forma descendente por su nota final, y en caso de empate, de forma
ascendente por su tiempo de entrega (en minutos)

Tarea:

Utiliza la función sorted() pasando una función lambda en el parametro key
para lograr este ordenamiento múltiple.
""" 

estudiantes = [
    {"nombre": "Sofía", "nota": 85, "tiempo": 45},
    {"nombre": "Mateo", "nota": 95, "tiempo": 50},
    {"nombre": "Valentina", "nota": 95, "tiempo": 30},
    {"nombre": "Lucas", "nota": 70, "tiempo": 20}
]

reporte_rendimiento = sorted(estudiantes, key=lambda estudiante: (-estudiante.get("nota"), estudiante.get("tiempo")))

print(reporte_rendimiento)
