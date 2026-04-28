# T6 — Isomorfismo em Árvores por Codificação Canônica

## Vídeo explicativo

> 🎥 **Link do vídeo:** https://youtu.be/kpE4kO9NhwU?si=EPij3Xr_05HwF1DR

---

## Descrição

Este projeto implementa um verificador de isomorfismo entre duas árvores não
direcionadas usando **codificação canônica**.  
Duas árvores são isomorfas se e somente se produzirem a mesma representação
textual canônica após o processo de enraizamento pelo centro.

---

## Estrutura do projeto

```
T6/
├── README.md
├── T6.md
├── dados/
│   ├── iso-path4-a.txt                  
│   ├── iso-path4-b.txt               
│   ├── nao-iso-estrela5.txt 
│   ├── nao-iso-path5.txt       
│   ├── tree_dois_centros_a.txt    
│   ├── tree_dois_centros_b.txt  
│   └── invalid-ciclo3.txt   
└── src/
    ├── main.py                    
    ├── graph.py                   
    └── tree_isomorphism.py        
```

---

## Como executar

```bash
python src/main.py <arquivo1.txt> <arquivo2.txt>
```

### Exemplos

```bash
# Árvores isomorfas
python src/main.py dados/iso-path4-a.txt dados/iso-path4-b.txt

# Árvores NÃO isomorfas
python src/main.py dados/iso-path4-a.txt dados/nao-iso-path5.txt

# Dois centros — isomorfas
python src/main.py dados/tree_dois_centros_a.txt dados/tree_dois_centros_a.txt

# Entrada inválida (ciclo)
python src/main.py dados/grafo_invalido_ciclo.txt dados/tree1.txt
```

---

## Formato de entrada (padrão algs4)

```
V          ← número de vértices
E          ← número de arestas
v1 w1      ← aresta entre v1 e w1
v2 w2
...
```

Os vértices devem ser indexados de **0** até **V − 1**.

---

## Saída do programa

O programa exibe, em ordem:

1. Lista de adjacência de cada árvore (vértices, arestas)
2. Validação de cada entrada (árvore válida ou motivo de invalidade)
3. Centro(s) encontrado(s) em cada árvore válida
4. Codificação canônica de cada árvore válida
5. **Veredito final**: isomorfas ou não isomorfas

---

## Algoritmo

### 1. Validação

Uma árvore com *V* vértices tem exatamente *V − 1* arestas e é conexa.  
O programa verifica ambas as condições antes de prosseguir.

### 2. Centros (remoção iterativa de folhas)

Remove-se camadas de folhas repetidamente até restar 1 ou 2 vértices.  
Esses vértices são os **centros** da árvore.

### 3. Codificação canônica

- A árvore é enraizada no centro encontrado.
- Para cada nó, calculam-se recursivamente os códigos dos filhos.
- Os códigos são **ordenados lexicograficamente** e concatenados entre `(` e `)`.
- Uma folha tem código `()`.
- Com **dois centros**, calculam-se as duas codificações possíveis e adota-se a menor, garantindo unicidade independentemente da ordem de leitura.

### 4. Comparação

Se as codificações canônicas forem iguais → **isomorfas**; caso contrário → **não isomorfas**.
