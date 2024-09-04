#Alejandra Rodriguez Guevara 21310127 7E1

# Clase que representa el motor de inferencia en un sistema experto
class InferenceEngine:
    def __init__(self, knowledge_base):
        """
        Constructor para inicializar el motor de inferencia.

        :param knowledge_base: Base de conocimiento que contiene reglas y hechos.
        """
        self.knowledge_base = knowledge_base  # Base de conocimiento usada para las inferencias
        self.inferred_facts = []  # Lista para almacenar los hechos inferidos

    def infer(self, known_facts):
        """
        Método para realizar el proceso de inferencia.

        :param known_facts: Lista de hechos conocidos proporcionados al motor de inferencia.
        :return: Lista de nuevos hechos inferidos.
        """
        self.inferred_facts = known_facts.copy()  # Inicializar con hechos conocidos

        # Iterar sobre las reglas en la base de conocimiento
        for rule in self.knowledge_base.rules:
            antecedent, consequent = rule.split(' entonces ')  # Dividir la regla en antecedente y consecuente

            # Si el antecedente está en los hechos conocidos o inferidos, se infiere el consecuente
            if antecedent in self.inferred_facts:
                if consequent not in self.inferred_facts:
                    self.inferred_facts.append(consequent)
                    print(f"Inferido: Dado '{antecedent}', se infiere '{consequent}'.")

        return self.inferred_facts

# Clase que representa la base de conocimiento en un sistema experto
class KnowledgeBase:
    def __init__(self):
        """
        Constructor para inicializar la base de conocimiento.

        Se inicializa con una estructura de datos que almacena reglas.
        """
        self.rules = []  # Lista para almacenar las reglas del sistema experto

    def add_rule(self, rule):
        """
        Método para añadir una regla a la base de conocimiento.

        :param rule: Regla que describe una relación entre hechos (e.g., "Si A entonces B").
        """
        self.rules.append(rule)
        print(f"Regla añadida: {rule}")

# Ejemplo de uso de la clase InferenceEngine y KnowledgeBase

# Crear una instancia de la base de conocimiento
knowledge_base = KnowledgeBase()

# Añadir reglas a la base de conocimiento
knowledge_base.add_rule("Si fiebre entonces posible infección")
knowledge_base.add_rule("Si tos entonces posible resfriado")
knowledge_base.add_rule("Si dolor de cabeza entonces posible migraña")

# Crear una instancia del motor de inferencia
inference_engine = InferenceEngine(knowledge_base)

# Proporcionar hechos conocidos al motor de inferencia
known_facts = ["fiebre", "dolor de cabeza"]

# Realizar inferencias
inferred_facts = inference_engine.infer(known_facts)
print(f"Hechos conocidos e inferidos: {inferred_facts}")