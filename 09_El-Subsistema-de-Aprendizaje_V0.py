#Alejandra Rodriguez Guevara 21310127 7E1

# Clase que representa el Subsistema de Aprendizaje en un sistema experto
class LearningSubsystem:
    def __init__(self, knowledge_base):
        """
        Constructor para inicializar el Subsistema de Aprendizaje.

        :param knowledge_base: Base de conocimiento del sistema experto.
        Este subsistema permite que el sistema experto aprenda nuevas reglas
        o mejore las reglas existentes en la base de conocimiento.
        """
        self.knowledge_base = knowledge_base  # Referencia a la base de conocimiento

    def learn_new_rule(self, new_rule):
        """
        Método para aprender una nueva regla y añadirla a la base de conocimiento.

        :param new_rule: Nueva regla a aprender (por ejemplo, "Si fiebre alta entonces posible infección grave").
        """
        # Verificar si la regla ya existe en la base de conocimiento
        if new_rule not in self.knowledge_base.rules:
            # Si la regla no existe, se añade a la base de conocimiento
            self.knowledge_base.add_rule(new_rule)
            print(f"Aprendida nueva regla: {new_rule}")
        else:
            # Si la regla ya existe, se notifica que no es necesario añadirla
            print(f"La regla '{new_rule}' ya existe en la base de conocimiento.")

    def improve_existing_rule(self, old_rule, improved_rule):
        """
        Método para mejorar una regla existente en la base de conocimiento.

        :param old_rule: Regla existente que se desea mejorar.
        :param improved_rule: Versión mejorada de la regla.
        """
        # Comprobar si la regla antigua está en la base de conocimiento
        if old_rule in self.knowledge_base.rules:
            # Reemplazar la regla antigua por la mejorada
            self.knowledge_base.rules.remove(old_rule)
            self.knowledge_base.add_rule(improved_rule)
            print(f"Regla mejorada: '{old_rule}' ha sido actualizada a '{improved_rule}'")
        else:
            # Notificar si la regla antigua no se encuentra en la base de conocimiento
            print(f"La regla '{old_rule}' no se encontró en la base de conocimiento para mejorarla.")

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

# Ejemplo de uso del Subsistema de Aprendizaje

# Crear la base de conocimiento y añadir una regla inicial
knowledge_base = KnowledgeBase()
knowledge_base.add_rule("Si fiebre entonces posible infección")

# Crear el Subsistema de Aprendizaje
learning_subsystem = LearningSubsystem(knowledge_base)

# Aprender una nueva regla
learning_subsystem.learn_new_rule("Si fiebre alta entonces posible infección grave")

# Intentar aprender una regla que ya existe
learning_subsystem.learn_new_rule("Si fiebre entonces posible infección")

# Mejorar una regla existente
learning_subsystem.improve_existing_rule("Si fiebre alta entonces posible infección grave", 
                                         "Si fiebre alta durante 3 días entonces posible infección grave")

# Intentar mejorar una regla que no existe
learning_subsystem.improve_existing_rule("Si tos entonces posible resfriado", 
                                         "Si tos persistente entonces posible bronquitis")