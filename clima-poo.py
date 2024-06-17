class ClimaSemanal:
    def __init__(self):
        """
        Inicializa la instancia con una lista vacía para las temperaturas.
        """
        self.temperaturas = []

    def ingresar_temperaturas(self):
        """
        Método para ingresar las temperaturas diarias.
        """
        for i in range(7):
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
                    self.temperaturas.append(temp)
                    break
                except ValueError:
                    print("Por favor, ingrese un valor numérico.")
    
    def calcular_promedio(self):
        """
        Método para calcular el promedio semanal de temperaturas.
        """
        if not self.temperaturas:
            return 0
        suma = sum(self.temperaturas)
        promedio = suma / len(self.temperaturas)
        return promedio

    def mostrar_resultados(self):
        """
        Método para mostrar las temperaturas ingresadas y el promedio semanal.
        """
        print(f"Las temperaturas ingresadas son: {self.temperaturas}")
        promedio_semanal = self.calcular_promedio()
        print(f"El promedio semanal de las temperaturas es: {promedio_semanal:.2f}°C")

def main():
    """
    Función principal que organiza el flujo del programa.
    """
    print("Programa para calcular el promedio semanal de temperaturas.")
    
    clima = ClimaSemanal()
    
    # Ingresar las temperaturas diarias
    clima.ingresar_temperaturas()
    
    # Mostrar los resultados
    clima.mostrar_resultados()

# Ejecutar la función principal
if __name__ == "__main__":
    main()
