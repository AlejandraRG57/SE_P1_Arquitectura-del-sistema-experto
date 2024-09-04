#Alejandra Rodriguez Guevara 21310127 7E1

# Clase que representa el subsistema de adquisición de conocimiento en un sistema experto
class KnowledgeAcquisitionSubsystem:
    def __init__(self):
        """
        Constructor para inicializar el subsistema de adquisición de conocimiento.

        Se inicializa con una lista para almacenar el conocimiento adquirido.
        """
        self.acquired_knowledge = []  # Lista para almacenar el conocimiento adquirido

    def acquire_knowledge(self, source, knowledge):
        """
        Método para adquirir conocimiento de una fuente específica.

        :param source: La fuente de donde proviene el conocimiento (e.g., experto humano, documentos).
        :param knowledge: El conocimiento adquirido (e.g., reglas, hechos, procedimientos).
        """
        acquisition_entry = {
            "source": source,
            "knowledge": knowledge
        }
        self.acquired_knowledge.append(acquisition_entry)
        print(f"Conocimiento adquirido de {source}: {knowledge}")

    def display_acquired_knowledge(self):
        """
        Método para mostrar todo el conocimiento adquirido.

        Muestra una lista de todo el conocimiento almacenado en el subsistema.
        """
        print("Conocimiento adquirido hasta ahora:")
        for entry in self.acquired_knowledge:
            print(f"Fuente: {entry['source']}, Conocimiento: {entry['knowledge']}")

# Ejemplo de uso de la clase KnowledgeAcquisitionSubsystem
# Crear una instancia del subsistema de adquisición de conocimiento
acquisition_subsystem = KnowledgeAcquisitionSubsystem()

# Adquirir conocimiento de diferentes fuentes
acquisition_subsystem.acquire_knowledge("Experto Dr. García", "Regla: Si fiebre entonces posible infección")
acquisition_subsystem.acquire_knowledge("Documentación médica", "Hecho: La fiebre es un síntoma común de infecciones virales")
acquisition_subsystem.acquire_knowledge("Base de datos de casos", "Hecho: 80% de los pacientes con fiebre tienen infección")

# Mostrar todo el conocimiento adquirido
acquisition_subsystem.display_acquired_knowledge()