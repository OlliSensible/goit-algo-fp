import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq

class CustomHeapNode:
    def __init__(self, key, color="skyblue"):
        self.left_child = None
        self.right_child = None
        self.value = key
        self.node_color = color
        self.node_id = str(uuid.uuid4())

def add_edges_to_graph(graph, node, position, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.node_id, color=node.node_color, label=node.value)
        if node.left_child:
            graph.add_edge(node.node_id, node.left_child.node_id)
            l = x - 1 / 2 ** layer
            position[node.left_child.node_id] = (l, y - 1)
            add_edges_to_graph(graph, node.left_child, position, x=l, y=y - 1, layer=layer + 1)
        if node.right_child:
            graph.add_edge(node.node_id, node.right_child.node_id)
            r = x + 1 / 2 ** layer
            position[node.right_child.node_id] = (r, y - 1)
            add_edges_to_graph(graph, node.right_child, position, x=r, y=y - 1, layer=layer + 1)

def visualize_custom_heap(custom_heap_root):
    custom_heap_graph = nx.DiGraph()
    positions = {custom_heap_root.node_id: (0, 0)}
    add_edges_to_graph(custom_heap_graph, custom_heap_root, positions)

    node_colors = [node[1]['color'] for node in custom_heap_graph.nodes(data=True)]
    node_labels = {node[0]: node[1]['label'] for node in custom_heap_graph.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(custom_heap_graph, pos=positions, labels=node_labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()

def build_heap_tree(array):
    if not array:
        return None

    def build_node(index):
        if index >= len(array):
            return None
        node = CustomHeapNode(array[index])
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        node.left_child = build_node(left_index)
        node.right_child = build_node(right_index)
        return node

    return build_node(0)

heap_array = [1, 3, 5, 7, 9, 2, 4, 8, 6, 10, 2]
heapq.heapify(heap_array)

heap_tree_root = build_heap_tree(heap_array)

visualize_custom_heap(heap_tree_root)