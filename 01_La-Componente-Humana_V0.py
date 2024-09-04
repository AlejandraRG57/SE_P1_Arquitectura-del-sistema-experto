#Alejandra Rodriguez Guevara 21310127 7E1

# Clase que representa la componente humana en un sistema experto
class HumanComponent:
    def __init__(self, name, role, expertise_level):
        """
        Constructor para inicializar la componente humana.

        :param name: Nombre de la persona.
        :param role: Rol de la persona en el sistema experto (e.g., experto, usuario final).
        :param expertise_level: Nivel de expertise de la persona en una escala de 1 a 10.
        """
        self.name = name
        self.role = role
        self.expertise_level = expertise_level

    def provide_knowledge(self, knowledge):
        """
        Método para que la persona aporte conocimiento al sistema experto.

        :param knowledge: Conocimiento que la persona proporciona (e.g., reglas, hechos).
        :return: Mensaje confirmando la recepción del conocimiento.
        """
        return f"{self.name} (Rol: {self.role}) ha proporcionado conocimiento: {knowledge}"

    def make_decision(self, input_data):
        """
        Método para que la persona tome decisiones basadas en la información proporcionada por el sistema experto.

        :param input_data: Datos o recomendaciones proporcionadas por el sistema experto.
        :return: Decisión tomada por la persona.
        """
        # Ejemplo de cómo se podría tomar una decisión en función del nivel de expertise
        if self.expertise_level > 7:
            decision = "Decisión avanzada basada en experiencia y conocimiento profundo."
        else:
            decision = "Decisión basada en conocimiento básico o intermedio."
        
        return f"{self.name} (Rol: {self.role}) ha tomado la siguiente decisión: {decision}"

# Ejemplo de uso de la clase HumanComponent
# Crear una instancia de un experto humano en el sistema experto
human = HumanComponent(name="Dr. García", role="Experto", expertise_level=9)

# El experto proporciona conocimiento al sistema
knowledge_response = human.provide_knowledge("Regla: Si fiebre y tos, entonces posible infección.")
print(knowledge_response)

# El experto toma una decisión basada en datos proporcionados
decision_response = human.make_decision("Recomendación: Realizar pruebas adicionales.")
print(decision_response)