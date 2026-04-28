from algs4.bag import Bag


class Graph:

    def __init__(self, v: int):
        if v < 0:
            raise ValueError("O número de vértices não pode ser negativo.")
        self._v = v
        self._e = 0
        self._adj = [Bag() for _ in range(v)]
        self._degree = [0] * v  # contador de grau por vértice

    @classmethod
    def from_file(cls, filename: str) -> "Graph":
        with open(filename, "r") as f:
            lines = [ln.strip() for ln in f if ln.strip()]

        if len(lines) < 2:
            raise ValueError(f"Arquivo '{filename}' está incompleto (faltam V e E).")

        v = int(lines[0])
        e = int(lines[1])
        g = cls(v)

        for i in range(2, 2 + e):
            if i >= len(lines):
                raise ValueError(
                    f"Arquivo '{filename}' declara {e} arestas, mas há menos linhas."
                )
            parts = lines[i].split()
            if len(parts) < 2:
                raise ValueError(f"Linha de aresta inválida: '{lines[i]}'")
            a, b = int(parts[0]), int(parts[1])
            g.add_edge(a, b)

        return g

    # ------------------------------------------------------------------ #
    #  Propriedades                                                        #
    # ------------------------------------------------------------------ #

    @property
    def v(self) -> int:
        """Número de vértices."""
        return self._v

    @property
    def e(self) -> int:
        """Número de arestas."""
        return self._e

    # ------------------------------------------------------------------ #
    #  Mutação                                                             #
    # ------------------------------------------------------------------ #

    def add_edge(self, v: int, w: int) -> None:
        """Adiciona a aresta não direcionada v-w."""
        self._validate_vertex(v)
        self._validate_vertex(w)
        self._adj[v].add(w)
        self._adj[w].add(v)
        self._degree[v] += 1
        self._degree[w] += 1
        self._e += 1

    # ------------------------------------------------------------------ #
    #  Consulta                                                            #
    # ------------------------------------------------------------------ #

    def adj(self, v: int):
        """Retorna o Bag de vizinhos de v."""
        self._validate_vertex(v)
        return self._adj[v]

    def degree(self, v: int) -> int:
        """Retorna o grau do vértice v."""
        self._validate_vertex(v)
        return self._degree[v]

    # ------------------------------------------------------------------ #
    #  Auxiliares                                                          #
    # ------------------------------------------------------------------ #

    def _validate_vertex(self, v: int) -> None:
        if not (0 <= v < self._v):
            raise ValueError(f"Vértice {v} fora do intervalo [0, {self._v - 1}].")

    def __str__(self) -> str:
        lines = [f"{self._v} vértices, {self._e} arestas"]
        for i in range(self._v):
            neighbors = " ".join(str(w) for w in self._adj[i])
            lines.append(f"  {i}: {neighbors}")
        return "\n".join(lines)