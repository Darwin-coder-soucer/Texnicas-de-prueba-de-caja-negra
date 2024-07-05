from olva_courier import OlvaCourier

olva = OlvaCourier()

# Pruebas de Transición de Estado
print("Pruebas de Transición de Estado:")
olva.transicion_estado()  # De "Pedido recibido" a "En preparación"
olva.transicion_estado()  # De "En preparación" a "En tránsito"
olva.transicion_estado()  # De "En tránsito" a "Entregado"
olva.transicion_estado()  # No se puede transitar más
print()

# Pruebas de Valor Límite
print("Pruebas de Valor Límite:")
olva.prueba_valor_limite(0)    # Límite inferior
olva.prueba_valor_limite(30)   # Límite superior
olva.prueba_valor_limite(-1)   # Fuera del límite inferior
olva.prueba_valor_limite(31)   # Fuera del límite superior
print()

# Pruebas de Partición de Equivalencia
print("Pruebas de Partición de Equivalencia:")
olva.prueba_particion_equivalencia("Zona 1")
olva.prueba_particion_equivalencia("Zona 2")
olva.prueba_particion_equivalencia("Zona 3")
olva.prueba_particion_equivalencia("Zona 4")  # Zona inválida
print()

# Pruebas de Tabla de Decisión
print("Pruebas de Tabla de Decisión:")
olva.prueba_tabla_decision("Frágil", "Alta", "Sí")
olva.prueba_tabla_decision("Frágil", "Alta", "No")
olva.prueba_tabla_decision("Frágil", "Baja", "Sí")
olva.prueba_tabla_decision("Frágil", "Baja", "No")
olva.prueba_tabla_decision("No frágil", "Alta", "Sí")
olva.prueba_tabla_decision("No frágil", "Alta", "No")
olva.prueba_tabla_decision("No frágil", "Baja", "Sí")
olva.prueba_tabla_decision("No frágil", "Baja", "No")
