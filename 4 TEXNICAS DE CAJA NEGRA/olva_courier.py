class OlvaCourier:
    def __init__(self):
        self.estado_actual = "Pedido recibido"

    # Prueba de Transición de Estado
    def transicion_estado(self):
        transiciones = {
            "Pedido recibido": "En preparación",
            "En preparación": "En tránsito",
            "En tránsito": ["Entregado", "Devuelto"]
        }
        if self.estado_actual in transiciones:
            next_state = transiciones[self.estado_actual]
            if isinstance(next_state, list):
                self.estado_actual = next_state[0]  # Simplicidad, se elige "Entregado"
            else:
                self.estado_actual = next_state
        else:
            self.estado_actual = "No se puede transitar más"
        print(f"Nuevo estado: {self.estado_actual}")

    # Prueba de Valor Límite
    def prueba_valor_limite(self, peso):
        if peso < 0 or peso > 30:
            print("Peso fuera de los límites permitidos (0-30 kg)")
        else:
            print("Peso dentro de los límites permitidos")

    # Prueba de Partición de Equivalencia
    def prueba_particion_equivalencia(self, zona):
        zonas_validas = ["Zona 1", "Zona 2", "Zona 3"]
        if zona in zonas_validas:
            print(f"Envío a {zona} es válido")
        else:
            print(f"Envío a {zona} no es válido")

    # Prueba de Tabla de Decisión
    def prueba_tabla_decision(self, tipo_paquete, prioridad_envio, seguro):
        print(f"Paquete: {tipo_paquete}, Prioridad: {prioridad_envio}, Seguro: {seguro}")
