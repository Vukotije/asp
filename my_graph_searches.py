from primeri_graf import *


def dfs(g, u, discovered):
    """ Primenjuje DFS na neotkriven deo grafa(Graph) g počevši od čvora(Vertex) u.

    discovered je rečnik koji mapira svaki čvor na ivicu koja je koriščen za njegovo pronalaženje
    prilikom DFS.
    Nove ivice se dodaju u ovaj rečnik.
    """
    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v not in discovered:
            discovered[v] = e
            dfs(g, v, discovered)


def dfs_complete(g):
    """Primenjuje DFS nad celim grafom i vraća šumu kao rečnik.

    Rezultat mapira svaki čvor v na ivicu koja je korišćena za njegovo otkrivanje.
    (Čvorovi koji su koreni DFS stabla su mapirani na None.)
    """
    forest = {}

    for v in g.vertices():
        if v not in forest:
            forest[v] = None
            dfs(g, v, forest)

    return forest


def bfs(g, s, discovered):
    """Primenjuje DFS za neotkriven deo grafa(Graph) g počevši od čvora(Vertex) s.

        discovered je rečnik koji mapira svaki čvor na ivicu koja je koriščen za njegovo pronalaženje
        prilikom BFS (prvobitno treba da bude mapiran na None).
        Nove ivice se dodaju u ovaj rečnik.
    """
    level = [s]
    while level:
        next_level = []
        for v in level:
            for e in g.incident_edges(v):
                u = e.opposite(v)
                if u not in discovered:
                    next_level.append(u)
                    discovered[u] = e
        level = next_level



def bfs_complete(g):
    """Primenjuje DFS nad celim grafom i vraća šumu kao rečnik.

        Rezultat mapira svaki čvor v na ivicu koja je korišćena za njegovo otkrivanje.
        (Čvorovi koji su koreni BFS stabla su mapirani na None.)
    """
    forest = {}

    for vertex in g.vertices():
        if vertex not in forest:
            forest[vertex] = None
            bfs(g, vertex, forest)

    return forest


if __name__ == '__main__':
    graph = figure_14_14()
    print('-------------- DFS --------------')
    forest = dfs_complete(graph)
    for vertex in forest.keys():
        print('Vertex: ' + str(vertex))
        if forest[vertex]:
            print('Edge: ' + str(forest[vertex]))
        else:
            print('Edge: None')

    print('\n\n-------------- BFS --------------')
    forest = bfs_complete(graph)
    for vertex in forest.keys():
        print('Vertex: ' + str(vertex))
        if forest[vertex]:
            print('Edge: ' + str(forest[vertex]))
        else:
            print('Edge: None')


