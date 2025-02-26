import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

# Parâmetros
dim = 50  # Tamanho da grade
taxa_regeneracao = 0.2  # chance de regeneração de uma célula vazia
taxa_queimada = 0.05  # chance de uma árvore pegar fogo

# 0: vazio, 1: vegetação, 2: fogo
def inicializar_grade(dim):
    return np.random.choice([0, 1], size=(dim, dim), p=[0.5, 0.5])

def atualizar_grade(grade):
    nova_grade = np.copy(grade)
    for i in range(dim):
        for j in range(dim):
            if grade[i, j] == 0:  # área vazia
                if np.random.rand() < taxa_regeneracao:
                    nova_grade[i, j] = 1  # vegetação cresce
            elif grade[i, j] == 1:  # vegetação
                if np.random.rand() < taxa_queimada:
                    nova_grade[i, j] = 2  # vegetação pega fogo
            elif grade[i, j] == 2:  # fogo
                nova_grade[i, j] = 0  # queima completamente e vira área vazia
    return nova_grade

# visualização
plt.ion()
fig, ax = plt.subplots()
grade = inicializar_grade(dim)
cmap = ListedColormap(["black", "green", "orange"])
img = ax.imshow(grade, cmap=cmap, vmin=0, vmax=2)
ax.set_title("Simulação do Autômato Celular")
step_text = ax.text(2, 2, 'Step: 0', color='white', fontsize=12, bbox=dict(facecolor='black', alpha=0.5))

def animar():
    global grade, step_text
    step = 0
    while True:
        grade = atualizar_grade(grade)
        img.set_array(grade)
        step_text.set_text(f'Step: {step}')
        step += 1
        plt.pause(0.2)

animar()
plt.ioff()
plt.show()
