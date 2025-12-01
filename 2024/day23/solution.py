import networkx
import matplotlib.pyplot as plt

edges = []


def parse_input():
    with open("input.txt") as file:
        lines = file.readlines()
        for line in lines:
            _edge = line.split("-")
            edges.append((_edge[0], _edge[1].strip()))


def create_graph():
    G = networkx.Graph()
    G.add_edges_from(edges)
    return G


def draw_graph(G):
    plt.figure(figsize=(10, 8))
    networkx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray", node_size=3000, font_size=10)
    plt.show()


def find_triplets(G):
    return [c for c in networkx.enumerate_all_cliques(G) if len(c) == 3]


def find_max_clique(G):
    return max(networkx.find_cliques(G), key=len)


def filter_triplets(triplets):
    return [triplet for triplet in triplets if any(node.startswith("t") for node in triplet)]


def main():
    parse_input()
    G = create_graph()
    triplets = find_triplets(G)
    filtered_triplets = filter_triplets(triplets)
    # Part 1
    print(len(filtered_triplets))
    max_clique = find_max_clique(G)
    # Part 2
    print(",".join(sorted(max_clique)))


if __name__ == "__main__":
    main()
