#Alejandra Rodriguez Guevara 21310127 7E1

# Clase que representa el Subsistema de Explicación en un sistema experto
class ExplanationSubsystem:
    def __init__(self):
        """
        Constructor para inicializar el subsistema de explicación.
        
        Este subsistema se encarga de proporcionar explicaciones detalladas sobre cómo 
        el sistema experto llegó a una determinada conclusión o recomendación.
        """
        self.explanation_log = []  # Lista para almacenar el historial de inferencias y reglas aplicadas

    def log_rule_application(self, rule, fact_inferred):
        """
        Método para registrar la aplicación de una regla en el proceso de inferencia.

        :param rule: Regla que fue aplicada (por ejemplo, "Si fiebre entonces posible infección").
        :param fact_inferred: Hecho que se dedujo a partir de la regla (por ejemplo, "posible infección").
        """
        explanation = f"Aplicando la regla: '{rule}' para inferir el hecho: '{fact_inferred}'"
        self.explanation_log.append(explanation)

    def explain_inference(self):
        """
        Método para proporcionar una explicación detallada del proceso de inferencia.
        
        Este método imprime todas las reglas que se aplicaron para llegar a los hechos inferidos.
        """
        if self.explanation_log:
            print("Explicación del proceso de inferencia:")
            for log_entry in self.explanation_log:
                print(log_entry)
        else:
            print("No se ha registrado ninguna inferencia hasta el momento.")

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
    def __init__(self, knowledge_base, explanation_subsystem):
        """
        Constructor para inicializar el motor de inferencia.

        :param knowledge_base: Base de conocimiento que contiene reglas y hechos.
        :param explanation_subsystem: Subsistema de explicación para registrar y proporcionar explicaciones.
        """
        self.knowledge_base = knowledge_base  # Base de conocimiento usada para las inferencias
        self.explanation_subsystem = explanation_subsystem  # Subsistema de explicación

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
            if antecedent in inferred_facts and consequent not in inferred_facts:
                inferred_facts.append(consequent)
                # Registrar la aplicación de la regla en el subsistema de explicación
                self.explanation_subsystem.log_rule_application(rule, consequent)

        return inferred_facts


# Ejemplo de uso del Subsistema de Explicación

# Crear la base de conocimiento y añadir reglas
knowledge_base = KnowledgeBase()
knowledge_base.add_rule("Si fiebre entonces posible infección")
knowledge_base.add_rule("Si tos entonces posible resfriado")
knowledge_base.add_rule("Si dolor de cabeza entonces posible migraña")

# Crear el subsistema de explicación
explanation_subsystem = ExplanationSubsystem()

# Crear el motor de inferencia con el subsistema de explicación
inference_engine = InferenceEngine(knowledge_base, explanation_subsystem)

# Hechos conocidos proporcionados por el usuario
known_facts = ["fiebre", "tos"]

# Realizar la inferencia para deducir nuevos hechos
inferred_facts = inference_engine.infer(known_facts)

# Mostrar los hechos inferidos
print("Hechos inferidos:", inferred_facts)

# Proporcionar una explicación del proceso de inferencia
explanation_subsystem.explain_inference()