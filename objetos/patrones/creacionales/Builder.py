from abc import ABC, abstractmethod

# Clase que representa una pizza
class Pizza:
    def __init__(self):
        self.nombre = ""
        self.masa = ""
        self.salsa = ""
        self.queso = ""
        self.ingredientes = []

    def __str__(self):
        ingredientes = ", ".join(self.ingredientes) if self.ingredientes else "ninguno"
        return (f"Pizza {self.nombre}:\n"
                f"  Masa: {self.masa}\n"
                f"  Salsa: {self.salsa}\n"
                f"  Queso: {self.queso}\n"
                f"  Ingredientes adicionales: {ingredientes}")

# Builder abstracto para construir una pizza
class PizzaBuilder(ABC):
    def __init__(self):
        self.pizza = Pizza()

    def reset(self):
        self.pizza = Pizza()
        return self

    @abstractmethod
    def build_masa(self):
        pass

    @abstractmethod
    def build_salsa(self):
        pass

    @abstractmethod
    def build_queso(self):
        pass

    @abstractmethod
    def build_ingredientes(self):
        pass

    def get_pizza(self):
        return self.pizza

# Builder concreto para Pizza Mozzarella
class PizzaMozzarellaBuilder(PizzaBuilder):
    def build_masa(self):
        self.pizza.masa = "Masa fina y crujiente"
        return self

    def build_salsa(self):
        self.pizza.salsa = "Salsa de tomate tradicional"
        return self

    def build_queso(self):
        self.pizza.queso = "Mozzarella"
        return self

    def build_ingredientes(self):
        self.pizza.nombre = "Mozzarella"
        # En este caso, la pizza se caracteriza por su abundante queso
        return self

# Builder concreto para Pizza Fugazzeta
class PizzaFugazzetaBuilder(PizzaBuilder):
    def build_masa(self):
        self.pizza.masa = "Masa gruesa y esponjosa"
        return self

    def build_salsa(self):
        self.pizza.salsa = "Salsa de tomate ligera"
        return self

    def build_queso(self):
        self.pizza.queso = "Mozzarella y queso crema"
        return self

    def build_ingredientes(self):
        self.pizza.nombre = "Fugazzeta"
        self.pizza.ingredientes.append("Cebolla caramelizada")
        return self

# Builder concreto para Pizza Peperoni
class PizzaPeperoniBuilder(PizzaBuilder):
    def build_masa(self):
        self.pizza.masa = "Masa delgada y crujiente"
        return self

    def build_salsa(self):
        self.pizza.salsa = "Salsa de tomate picante"
        return self

    def build_queso(self):
        self.pizza.queso = "Queso mozzarella"
        return self

    def build_ingredientes(self):
        self.pizza.nombre = "Peperoni"
        self.pizza.ingredientes.append("Rodajas de peperoni")
        return self

# Builder concreto para Pizza Jamón y Morrón
class PizzaJamonMorronBuilder(PizzaBuilder):
    def build_masa(self):
        self.pizza.masa = "Masa clásica"
        return self

    def build_salsa(self):
        self.pizza.salsa = "Salsa de tomate suave"
        return self

    def build_queso(self):
        self.pizza.queso = "Queso mozzarella"
        return self

    def build_ingredientes(self):
        self.pizza.nombre = "Jamón y Morrón"
        self.pizza.ingredientes.extend(["Jamón", "Morrón en tiras"])
        return self

# Director que orquesta el proceso de construcción
class Director:
    @staticmethod
    def construir_pizza(builder: PizzaBuilder) -> Pizza:
        return (builder.reset()
                      .build_masa()
                      .build_salsa()
                      .build_queso()
                      .build_ingredientes()
                      .get_pizza())

    @staticmethod
    def construir_mozzarella() -> Pizza:
        return Director.construir_pizza(PizzaMozzarellaBuilder())

    @staticmethod
    def construir_fugazzeta() -> Pizza:
        return Director.construir_pizza(PizzaFugazzetaBuilder())

    @staticmethod
    def construir_peperoni() -> Pizza:
        return Director.construir_pizza(PizzaPeperoniBuilder())

    @staticmethod
    def construir_jamon_morron() -> Pizza:
        return Director.construir_pizza(PizzaJamonMorronBuilder())

# Ejemplo de uso
pizza1 = Director.construir_mozzarella()
pizza2 = Director.construir_fugazzeta()
pizza3 = Director.construir_peperoni()
pizza4 = Director.construir_jamon_morron()

print(pizza1)
print()
print(pizza2)
print()
print(pizza3)
print()
print(pizza4)
