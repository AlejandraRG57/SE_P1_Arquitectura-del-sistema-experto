#Alejandra Rodriguez Guevara 21310127 7E1

# Clase que representa el control de la coherencia en un sistema experto
class CoherenceControl:
    def __init__(self):
        """
        Constructor para inicializar el control de coherencia.

        Se inicializa con listas para almacenar las reglas y hechos, y detectar inconsistencias.
        """
        self.rules = []  # Lista para almacenar las reglas del sistema experto
        self.facts = []  # Lista para almacenar los hechos conocidos

    def add_rule(self, rule):
        """
        Método para añadir una regla y verificar su coherencia con las reglas existentes.

        :param rule: Regla que se desea añadir.
        :return: Mensaje indicando si la regla es coherente o si presenta inconsistencias.
        """
        # Verificar si la nueva regla es coherente con las reglas existentes
        if self.check_inconsistency(rule):
            print(f"Inconsistencia detectada al añadir la regla: {rule}")
        else:
            self.rules.append(rule)
            print(f"Regla añadida: {rule}")

    def add_fact(self, fact):
        """
        Método para añadir un hecho y verificar su coherencia con los hechos existentes.

        :param fact: Hecho que se desea añadir.
        :return: Mensaje indicando si el hecho es coherente o si presenta inconsistencias.
        """
        # Verificar si el nuevo hecho es coherente con los hechos existentes
        if self.check_inconsistency(fact, fact_check=True):
            print(f"Inconsistencia detectada al añadir el hecho: {fact}")
        else:
            self.facts.append(fact)
            print(f"Hecho añadido: {fact}")

    def check_inconsistency(self, new_entry, fact_check=False):
        """
        Método para verificar inconsistencias con las reglas o hechos existentes.

        :param new_entry: Nueva regla o hecho a verificar.
        :param fact_check: Indica si se está verificando un hecho (True) o una regla (False).
        :return: True si se detecta una inconsistencia, False en caso contrario.
        """
        if fact_check:
            # Verificar inconsistencias entre hechos
            for fact in self.facts:
                if self.is_contradictory(fact, new_entry):
                    return True
        else:
            # Verificar inconsistencias entre reglas
            for rule in self.rules:
                if self.is_contradictory(rule, new_entry):
                    return True
        return False

    def is_contradictory(self, existing_entry, new_entry):
        """
        Método para determinar si dos reglas o hechos son contradictorios.

        :param existing_entry: Regla o hecho existente.
        :param new_entry: Nueva regla o hecho que se desea añadir.
        :return: True si son contradictorios, False en caso contrario.
        """
        # Esta función es un ejemplo simplificado. Aquí podrías implementar la lógica específica
        # para detectar contradicciones en base al formato de tus reglas y hechos.
        return existing_entry == new_entry[::-1]  # Ejemplo de contradicción simplificada

# Ejemplo de uso de la clase CoherenceControl
# Crear una instancia del control de coherencia
coherence_control = CoherenceControl()

# Añadir reglas y hechos, verificando su coherencia
coherence_control.add_rule("Si fiebre entonces posible infección")
coherence_control.add_rule("Si no fiebre entonces no posible infección")  # Ejemplo de inconsistencia

coherence_control.add_fact("fiebre")
coherence_control.add_fact("no fiebre")  # Ejemplo de inconsistencia