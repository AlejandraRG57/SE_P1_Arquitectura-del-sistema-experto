#Alejandra Rodriguez Guevara 21310127 7E1

# Clase que representa la base de conocimiento en un sistema experto
class KnowledgeBase:
    def __init__(self):
        """
        Constructor para inicializar la base de conocimiento.

        Se inicializa con una estructura de datos que almacena reglas y hechos.
        """
        self.rules = []  # Lista para almacenar las reglas del sistema experto
        self.facts = []  # Lista para almacenar los hechos conocidos

    def add_rule(self, rule):
        """
        Método para añadir una regla a la base de conocimiento.

        :param rule: Regla que describe una relación entre hechos (e.g., "Si A entonces B").
        """
        self.rules.append(rule)
        print(f"Regla añadida: {rule}")

    def add_fact(self, fact):
        """
        Método para añadir un hecho a la base de conocimiento.

        :param fact: Hecho conocido que puede ser utilizado en el proceso de inferencia.
        """
        self.facts.append(fact)
        print(f"Hecho añadido: {fact}")

    def infer(self):
        """
        Método para realizar inferencias basadas en las reglas y hechos en la base de conocimiento.

        Este método simula el proceso de razonamiento en un sistema experto.
        """
        inferred_facts = []

        # Proceso simple de inferencia: comparar hechos con reglas y deducir nuevos hechos
        for rule in self.rules:
            antecedent, consequent = rule.split(' entonces ')
            if antecedent in self.facts:
                inferred_facts.append(consequent)
                print(f"Inferencia: Dado '{antecedent}', se infiere '{consequent}'.")

        return inferred_facts

# Ejemplo de uso de la clase KnowledgeBase
# Crear una instancia de la base de conocimiento
knowledge_base = KnowledgeBase()

# Añadir reglas a la base de conocimiento
knowledge_base.add_rule("Si fiebre entonces posible infección")
knowledge_base.add_rule("Si tos entonces posible resfriado")

# Añadir hechos a la base de conocimiento
knowledge_base.add_fact("fiebre")

# Realizar inferencias basadas en las reglas y hechos
inferred_facts = knowledge_base.infer()
print(f"Hechos inferidos: {inferred_facts}")