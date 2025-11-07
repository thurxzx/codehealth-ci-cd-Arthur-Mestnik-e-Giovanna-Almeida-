# main.py
# Simulação do sistema CodeHealth - Agendamento Médico

def agendar_consulta(paciente, medico, horario):
    return f"Consulta agendada para {paciente} com o Dr(a). {medico} às {horario}."

if __name__ == "__main__":
    print("🏥 CodeHealth - Sistema de Agendamento Médico")
    resultado = agendar_consulta("Arthur", "Giovanna", "14:00")
    print(resultado)
