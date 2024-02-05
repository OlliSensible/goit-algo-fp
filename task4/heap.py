import uuid
import networkx as nx
import matplotlib.pyplot as plt

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
            l = add_edges_to_graph(graph, node.left_child, position, x=l, y=y - 1, layer=layer + 1)
        if node.right_child:
            graph.add_edge(node.node_id, node.right_child.node_id)
            r = x + 1 / 2 ** layer
            position[node.right_child.node_id] = (r, y - 1)
            r = add_edges_to_graph(graph, node.right_child, position, x=r, y=y - 1, layer=layer + 1)
    return graph

def visualize_custom_heap(custom_heap_root):
    custom_heap_graph = nx.DiGraph()
    positions = {custom_heap_root.node_id: (0, 0)}
    custom_heap_graph = add_edges_to_graph(custom_heap_graph, custom_heap_root, positions)

    node_colors = [node[1]['color'] for node in custom_heap_graph.nodes(data=True)]
    node_labels = {node[0]: node[1]['label'] for node in custom_heap_graph.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(custom_heap_graph, pos=positions, labels=node_labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()

custom_heap_root = CustomHeapNode(1)
custom_heap_root.left_child = CustomHeapNode(2)
custom_heap_root.right_child = CustomHeapNode(6)
custom_heap_root.left_child.left_child = CustomHeapNode(3)
custom_heap_root.left_child.right_child = CustomHeapNode(5)
custom_heap_root.right_child.left_child = CustomHeapNode(7)
custom_heap_root.left_child.left_child.right_child = CustomHeapNode(4)

visualize_custom_heap(custom_heap_root)