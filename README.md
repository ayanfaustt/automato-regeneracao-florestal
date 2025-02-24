# Simulação de Autômato Celular para Propagação de Fogo

Este projeto implementa um autômato celular para simular a propagação de fogo em uma vegetação. A simulação ocorre em uma grade bidimensional onde cada célula pode assumir três estados:

- **Preto** (0): Área vazia
- **Verde** (1): Vegetação
- **Laranja** (2): Fogo

A cada iteração, células vazias podem regenerar vegetação com uma determinada probabilidade, enquanto células de vegetação podem pegar fogo e eventualmente se tornarem vazias novamente.

## Como Executar

### Pré-requisitos
Para executar o código, é necessário ter o Python instalado, juntamente com as seguintes bibliotecas:

- `matplotlib`
- `numpy`

Caso ainda não tenha essas bibliotecas, instale-as com o comando:
```sh
pip install numpy matplotlib
```

### Execução
Para rodar a simulação, basta executar o script Python:
```sh
python program.py
```

Isso abrirá uma janela com a simulação em tempo real, onde as células mudam de estado conforme as regras definidas.

## Funcionamento do Código
1. **Inicialização da grade**: Uma matriz `dim x dim` é criada aleatoriamente com valores 0 (vazio) ou 1 (vegetação).
2. **Regras de atualização**:
   - Células vazias podem regenerar vegetação com uma probabilidade `taxa_regeneracao`.
   - Células de vegetação podem pegar fogo com uma probabilidade `taxa_queimada`.
   - Células em chamas queimam completamente e se tornam vazias na próxima iteração.
3. **Exibição**: O `matplotlib` é utilizado para exibir a simulação com atualização contínua.

## Parâmetros
Você pode ajustar os seguintes parâmetros no código para testar diferentes cenários:
- `dim`: Tamanho da grade (padrão: 50)
- `taxa_regeneracao`: Probabilidade de regeneração da vegetação (padrão: 0.1)
- `taxa_queimada`: Probabilidade de pegar fogo (padrão: 0.05)
