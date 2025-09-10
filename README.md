<p align="center">
    <img loading="lazy" src="https://files.engaged.com.br/5db0810e95b4f900077e887e/account/5db0810e95b4f900077e887e/xMCS8NFKTMqwhefy8WLd_catolica-horizontal.png" width="300">
</p>

# The Longer Path Problem
Projeto da disciplina de **Algoritmos Avançados**: cálculo do **caminho simples de maior peso** em um **grafo dirigido acíclico (DAG)** com **pesos** (inclusive **negativos**).

## Situação do Projeto
![Status](https://img.shields.io/badge/Status-Em%20Progresso-yellow)

![Etapa](https://img.shields.io/badge/Etapa-N1-green)

## Abordagem

- **Ordenação topológica (Kahn, 1962)** + **Programação Dinâmica**.
- Em ordem topológica, **relaxamos** as arestas maximizando `dist[v] = max(dist[v], dist[u] + w)`.
- Suporta **pesos negativos** (não há ciclos em DAG, portanto não há “ganho infinito”).
- **Matriz de adjacência** como entrada (0 = **ausência** de aresta).

## Estrutura

```
.
├── main.py        # script principal
├── entrada.txt    # exemplo de entrada (modelo abaixo)
└── README.md
```

## Formato de entrada

Exemplo (`entrada.txt`):

```txt
# Número de vértices
5

# Matriz de adjacência, onde 0 significa ausência de aresta
0 1 2 0 0
0 0 3 5 0
0 0 0 1 2
0 0 0 0 6
0 0 0 0 0

# Origem e destino (índices começando em 0)
0 4
```

> **Observação:** `0` significa **ausência de aresta**. Logo, arestas de **peso zero** não são suportadas neste formato.

## Como executar

### Replit
1. Crie um projeto Python.
2. Envie `main.py` e `entrada.txt`.
3. Clique em **Run** (ou execute `python3 main.py` no console).

### VSCode / Terminal
```bash
python main.py                    # usa 'entrada.txt' por padrão
python main.py meu_arquivo.txt    # para usar outro arquivo em específico
```

## Saída esperada

No exemplo acima, o programa imprime:
```
Caminho máximo: [0, 1, 3, 4]
Peso total: 12
```

Se não houver caminho `origem → destino`, a mensagem será:
```
Não existe caminho de O até D.
```

## Validações e Limitações

- Verificação de **DAG** (Kahn). Se houver ciclo, o programa aborta com mensagem.
- Se `destino` não for alcançável a partir de `origem`, informa que **não existe caminho**.
- Como a entrada é **matriz de adjacência**, a complexidade é `O(n^2)`. Para grafos muito esparsos/grandes, listas de adjacência seriam preferíveis (`O(V+E)`).
- **Peso 0** não é representável (0 já indica “sem aresta”).

## Contribuidores
A equipe envolvida nesta atividade é constituída por alunos da 7ª Fase (20252) do curso de Engenharia de Software do Centro Universitário Católica SC de Jaraguá do Sul.

<div align="center">
<table>
  <tr>
    <td align="center"><a href="https://github.com/HigorAz"><img loading="lazy" src="https://avatars.githubusercontent.com/u/141787745?v=4" width="115"><br><sub>Higor Azevedo</sub></a></td>
    <td align="center"><a href="https://github.com/AoiteFoca"><img loading="lazy" src="https://avatars.githubusercontent.com/u/141975272?v=4" width="115"><br><sub>Nathan Cielusinski</sub></a></td>
    <td align="center"><a href="https://github.com/MrNicolass"><img loading="lazy" src="https://avatars.githubusercontent.com/u/80847876?v=4" width="115"><br><sub>Nicolas Gustavo 
  </tr>
</div>
