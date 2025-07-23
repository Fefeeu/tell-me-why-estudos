import random
import matplotlib.pyplot as plt
import time
import numpy as np

def simulacao_cassino(prob_cassino_vencer_em_porcentagem=50.00,  
                     numero_de_linhas_no_grafico=2,
                      numero_de_rep_simulacao=100):
    """
    Simula múltiplas linhas com a lógica do cassino e plota em tempo real
    
    Parâmetros:
    prob_cassino_vencer_em_porcentagem (float): Probabilidade de ganhar (0-100)
    numero_de_rep_simulacao (int): Número total de iterações
    numero_de_linhas_no_grafico (int): Quantidade de linhas no gráfico
    """
    
    def cassino():
        x = random.randint(1, 10000) / 100
        return -1 if x <= prob_cassino_vencer_em_porcentagem else 1

    # Configuração inicial
    plt.ion()
    fig, ax = plt.subplots(figsize=(12, 7))

    # Cria as linhas com cores diferentes
    colors = plt.cm.tab10(np.linspace(0, 1, numero_de_linhas_no_grafico))
    lines = []
    data = []
    values = [0] * numero_de_linhas_no_grafico

    for i in range(numero_de_linhas_no_grafico):
        line, = ax.plot([], [], color=colors[i], label=f'Linha {i+1}', alpha=0.8)
        lines.append(line)
        data.append([])

    # Configurações do gráfico
    ax.set_title(f'Simulação do Cassino ({prob_cassino_vencer_em_porcentagem}% de chance)')
    ax.set_ylim(-50, 50)
    ax.set_xlim(0, 100)
    ax.grid(True)
    ax.axhline(0, color='gray', linestyle='--', alpha=0.5)
    ax.legend(loc='upper left')

    # Contador de interações
    counter = ax.text(0.02, 0.95, '', transform=ax.transAxes,
                     fontsize=12, bbox=dict(facecolor='white', alpha=0.7))

    # Loop principal
    for iteration in range(1, numero_de_rep_simulacao + 1):
        # Atualiza todas as linhas
        for i in range(numero_de_linhas_no_grafico):
            values[i] += cassino()
            data[i].append(values[i])
            
            if len(data[i]) > 100:
                data[i] = data[i][-100:]
            
            lines[i].set_data(range(len(data[i])), data[i])
        
        # Atualiza os limites
        ax.set_xlim(max(0, len(data[0])-100), len(data[0]))
        all_values = np.concatenate(data)
        ax.set_ylim(min(all_values)-5, max(all_values)+5)
        
        # Atualiza o contador
        counter.set_text(f'Interações: {iteration}/{numero_de_rep_simulacao}')
        
        # Redesenha
        fig.canvas.draw()
        fig.canvas.flush_events()
        time.sleep(0.001)

    # Finalização
    plt.ioff()
    plt.show()

# Exemplo de uso:
# simulacao_cassino(prob_cassino_vencer_em_porcentagem=48.0, 
#                  numero_de_rep_simulacao=500, 
#                  numero_de_linhas_no_grafico=5)

simulacao_cassino(80.00, 2, 100)
