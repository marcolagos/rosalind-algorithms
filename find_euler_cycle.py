"""
    https://rosalind.info/problems/ba3f/

    Find an Eulerian cycle in a graph.
    Given: An Eulerian directed graph, in the form of an adjacency list.
    Return: An Eulerian cycle in this graph.

    Synopsis:
    Pick a random start node.
    Run a depth first search on the node.
    Append the node to the cycle.
    Rerun the depth first search on the next node.
"""
from collections import defaultdict

def read_input(file_path: str) -> list[str]:
    """Reads the input file and returns the list of lines."""
    with open(file_path, "r") as input_file:
        return input_file.readlines()

def find_euler_cycle(graph: dict) -> list[str]:
    # Initialize the cycle.
    def dfs(node):
        # If the node has no neighbors, append it to the cycle.
        while graph[node]:
            # Pick a neighbor.
            neighbor = graph[node].pop()
            dfs(neighbor)
        cycle.append(node)

    # Pick a random start node.
    start_node = list(graph.keys())[0]
    cycle = []
    # `dfs` will append the nodes to `cycle` in reverse order.
    dfs(start_node)

    return cycle[::-1]
    

def main():
    """Main call. Parses, runs, and saves problem specific data."""
    # Reading the input file
    graph_str = read_input('datasets/rosalind_ba3f.txt')

    graph = {}
    for line in graph_str:
        line = line.strip()
        key, values = line.split(' -> ')
        values = values.split(',')
        graph[key] = values

    cycle = find_euler_cycle(graph)
    # Printing and saving answer
    with open('solutions/rosalind_ba3f.txt', 'w') as output_file:
        cycle_str = '->'.join(cycle)
        output_file.write(cycle_str)

if __name__ == "__main__":
    main()
