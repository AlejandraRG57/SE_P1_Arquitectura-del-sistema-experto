#Alejandra Rodriguez Guevara 21310127 7E1

# Clase que representa el Subsistema de Ejecución de Órdenes en un sistema experto
class OrderExecutionSubsystem:
    def __init__(self):
        """
        Constructor para inicializar el subsistema de ejecución de órdenes.
        
        Este subsistema se encarga de ejecutar las acciones correspondientes
        basadas en los hechos inferidos por el sistema experto.
        """
        self.actions = {}  # Diccionario para mapear hechos inferidos a acciones

    def add_action(self, inferred_fact, action_function):
        """
        Método para agregar una acción al subsistema de ejecución de órdenes.

        :param inferred_fact: Hecho inferido (ej. "posible infección") al que se asocia la acción.
        :param action_function: Función que define el comportamiento de la acción.
        """
        self.actions[inferred_fact] = action_function
        print(f"Acción para '{inferred_fact}' añadida al subsistema.")

    def execute_action(self, inferred_fact):
        """
        Método para ejecutar una acción específica basada en un hecho inferido.

        :param inferred_fact: Nombre del hecho inferido que desencadena una acción.
        """
        if inferred_fact in self.actions:
            print(f"Ejecutando acción para: {inferred_fact}")
            self.actions[inferred_fact]()  # Ejecutar la función correspondiente al hecho inferido
        else:
            print(f"No se encontró acción para el hecho inferido: {inferred_fact}")

    def execute_inferred_actions(self, inferred_facts):
        """
        Método para ejecutar las acciones que correspondan a los hechos inferidos.

        :param inferred_facts: Lista de hechos inferidos del motor de inferencia.
        """
        print("Ejecutando acciones basadas en los hechos inferidos...")
        for fact in inferred_facts:
            self.execute_action(fact)

# Clase que representa la base de conocimiento en el sistema experto
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

# Clase que representa el motor de inferencia en el sistema experto
class InferenceEngine:
    def __init__(self, knowledge_base):
        """
        Constructor para inicializar el motor de inferencia.

        :param knowledge_base: Base de conocimiento que contiene reglas y hechos.
        """
        self.knowledge_base = knowledge_base  # Base de conocimiento usada para las inferencias

    def infer(self, known_facts):
        """
        Método para realizar el proceso de inferencia.

        :param known_facts: Lista de hechos conocidos proporcionados al motor de inferencia.
        :return: Lista de nuevos hechos inferidos.
        """
        inferred_facts = known_facts.copy()  # Inicializar con hechos conocidos

        # Iterar sobre las reglas en la base de conocimiento
        for rule in self.knowledge_base.rules:
            antecedent, consequent = rule.split(' entonces ')  # Dividir la regla en antecedente y consecuente

            # Si el antecedente está en los hechos conocidos o inferidos, se infiere el consecuente
            if antecedent in inferred_facts:
                if consequent not in inferred_facts:
                    inferred_facts.append(consequent)

        return inferred_facts


# Definición de las acciones que se pueden ejecutar en el sistema
def administer_antibiotic():
    print("Acción: Administrando antibiótico al paciente.")

def recommend_rest():
    print("Acción: Recomendando descanso y mucho líquido.")

def administer_analgesic():
    print("Acción: Administrando analgésico para aliviar el dolor de cabeza.")

# Ejemplo de uso del Subsistema de Ejecución de Órdenes

# Crear la base de conocimiento y añadir reglas
knowledge_base = KnowledgeBase()
knowledge_base.add_rule("Si fiebre entonces posible infección")
knowledge_base.add_rule("Si tos entonces posible resfriado")
knowledge_base.add_rule("Si dolor de cabeza entonces posible migraña")

# Crear el motor de inferencia
inference_engine = InferenceEngine(knowledge_base)

# Crear el subsistema de ejecución de órdenes
order_execution_subsystem = OrderExecutionSubsystem()

# Añadir acciones al subsistema, pero ahora asociándolas a los hechos inferidos
order_execution_subsystem.add_action("posible infección", administer_antibiotic)
order_execution_subsystem.add_action("posible resfriado", recommend_rest)
order_execution_subsystem.add_action("posible migraña", administer_analgesic)

# Hechos conocidos proporcionados por el usuario
known_facts = ["fiebre"]

# Realizar la inferencia para deducir nuevos hechos
inferred_facts = inference_engine.infer(known_facts)

# Ejecutar las acciones correspondientes a los hechos inferidos
order_execution_subsystem.execute_inferred_actions(inferred_facts)