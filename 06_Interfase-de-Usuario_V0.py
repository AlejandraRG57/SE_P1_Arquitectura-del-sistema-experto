#Alejandra Rodriguez Guevara 21310127 7E1

import tkinter as tk
from tkinter import messagebox

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

# Clase que representa la Interfaz Gráfica de Usuario (GUI)
class ExpertSystemGUI:
    def __init__(self, root, inference_engine):
        """
        Constructor para inicializar la interfaz gráfica de usuario.

        :param root: Ventana principal de Tkinter.
        :param inference_engine: El motor de inferencia que proporcionará respuestas.
        """
        self.root = root
        self.inference_engine = inference_engine

        self.root.title("Sistema Experto de Diagnóstico Médico")

        # Etiqueta para el título
        self.title_label = tk.Label(root, text="Sistema Experto de Diagnóstico Médico", font=("Arial", 16))
        self.title_label.pack(pady=10)

        # Etiqueta para la entrada de síntomas
        self.input_label = tk.Label(root, text="Ingrese sus síntomas separados por comas:")
        self.input_label.pack(pady=5)

        # Caja de texto para que el usuario introduzca los síntomas
        self.symptoms_entry = tk.Entry(root, width=50)
        self.symptoms_entry.pack(pady=5)

        # Botón para realizar la inferencia
        self.infer_button = tk.Button(root, text="Obtener Diagnóstico", command=self.get_diagnosis)
        self.infer_button.pack(pady=10)

        # Etiqueta para mostrar el diagnóstico
        self.diagnosis_label = tk.Label(root, text="Diagnóstico:", font=("Arial", 12))
        self.diagnosis_label.pack(pady=10)

        # Caja de texto para mostrar los resultados inferidos
        self.result_text = tk.Text(root, height=10, width=60, state=tk.DISABLED)
        self.result_text.pack(pady=10)

    def get_diagnosis(self):
        """
        Método para obtener el diagnóstico basado en los síntomas del usuario.
        """
        # Obtener los síntomas del usuario
        symptoms = self.symptoms_entry.get()
        known_facts = [symptom.strip() for symptom in symptoms.split(",")]

        # Realizar la inferencia usando el motor de inferencia
        inferred_facts = self.inference_engine.infer(known_facts)

        # Mostrar los resultados inferidos en el cuadro de texto
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)  # Limpiar el cuadro de texto antes de mostrar los resultados

        if inferred_facts:
            self.result_text.insert(tk.END, "Diagnóstico basado en los síntomas proporcionados:\n")
            for fact in inferred_facts:
                self.result_text.insert(tk.END, f"- {fact}\n")
        else:
            self.result_text.insert(tk.END, "No se pudo inferir un diagnóstico basado en los síntomas proporcionados.")

        self.result_text.config(state=tk.DISABLED)  # Deshabilitar el cuadro de texto para que no se edite

# Ejemplo de uso de las clases InferenceEngine, KnowledgeBase y ExpertSystemGUI

# Crear la ventana principal de Tkinter
root = tk.Tk()

# Crear una instancia de la base de conocimiento
knowledge_base = KnowledgeBase()

# Añadir reglas a la base de conocimiento
knowledge_base.add_rule("Si fiebre entonces posible infección")
knowledge_base.add_rule("Si tos entonces posible resfriado")
knowledge_base.add_rule("Si dolor de cabeza entonces posible migraña")

# Crear una instancia del motor de inferencia
inference_engine = InferenceEngine(knowledge_base)

# Crear la interfaz gráfica de usuario y pasar el motor de inferencia
gui = ExpertSystemGUI(root, inference_engine)

# Ejecutar el bucle principal de Tkinter
root.mainloop()