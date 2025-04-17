from menu import mostrar_menu
from utils import aguardar_horario
from agendamento import executar_agendamentos


if __name__ == "__main__":
    quadra, horarios, inicio = mostrar_menu()
    aguardar_horario(inicio)
    executar_agendamentos(quadra, horarios)
