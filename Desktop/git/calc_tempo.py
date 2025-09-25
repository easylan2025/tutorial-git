# este programa vai ler a hora inicial e final de algum projeto , depois de somar quantos minutos ele fez o projeto vai informar a quantidade de tempo gasta naquela tarefa
from datetime import datetime, timedelta

def calcular_minutos(hora_inicial_h, hora_inicial_m, hora_final_h, hora_final_m) -> int:
    inicio = datetime(2000, 1, 1, int(hora_inicial_h), int(hora_inicial_m))
    fim = datetime(2000, 1, 1, int(hora_final_h), int(hora_final_m))

    # Se a hora final for menor que a inicial, considera que passou da meia-noite
    if fim < inicio:
        fim += timedelta(days=1)

    diferenca = fim - inicio
    return int(diferenca.total_seconds() / 60)

def separar_hora_minuto(entrada):
    """
    Detecta se a entrada usa ':' ou ',' e retorna hora e minuto como inteiros
    """
    if ":" in entrada:
        partes = entrada.split(":")
    elif "," in entrada:
        partes = entrada.split(",")
    else:
        raise ValueError("Formato inválido! Use HH:MM ou HH,MM")
    
    hora, minuto = int(partes[0]), int(partes[1])
    
    # Validação de hora e minuto
    if not (0 <= hora <= 23):
        raise ValueError("Hora inválida! Deve estar entre 0 e 23.")
    if not (0 <= minuto <= 59):
        raise ValueError("Minuto inválido! Deve estar entre 0 e 59.")
    
    return hora, minuto

total_minutos = 0

print("Registro de tarefas (aperte Enter sem digitar hora inicial para sair)")

while True:
    print("\n--- Novo intervalo ---")
    
    # Entrada da hora inicial com validação
    while True:
        entrada_inicial = input("Hora inicial (HH:MM ou HH,MM): ")
        if entrada_inicial == "":
            print("Encerrando registro...")
            break
        try:
            hora_inicial_h, hora_inicial_m = separar_hora_minuto(entrada_inicial)
            break
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")

    if entrada_inicial == "":
        break
    
    # Entrada da hora final com validação
    while True:
        entrada_final = input("Hora final (HH:MM ou HH,MM): ")
        try:
            hora_final_h, hora_final_m = separar_hora_minuto(entrada_final)
            break
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")

    minutos = calcular_minutos(hora_inicial_h, hora_inicial_m, hora_final_h, hora_final_m)
    total_minutos += minutos

    horas_acumuladas = total_minutos // 60
    minutos_acumulados = total_minutos % 60

    print(f"Intervalo registrado: {minutos} minutos.")
    print(f"Tempo total acumulado: {horas_acumuladas} horas e {minutos_acumulados} minutos.")

# Mostra o total final
horas = total_minutos // 60
minutos = total_minutos % 60
print(f"\nTempo total registrado: {horas} horas e {minutos} minutos.")
