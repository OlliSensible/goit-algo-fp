import uuid
import networkx as nx
import matplotlib.pyplot as plt

class CustomHeapNode:
    def __init__(self, key, color="#1296F0"):
        self.left_child = None
        self.right_child = None
        self.value = key
        self.node_color = color
        self.node_id = str(uuid.uuid4())
        self.visit_order = None

def random_color(start_color, end_color, fraction):
    return tuple(start + (end - start) * fraction for start, end in zip(start_color, end_color))

def generate_color(visit_order, total_nodes):
    start_color = (26, 71, 101)  # Dark color
    end_color = (175, 223, 255)  # Light color
    fraction = visit_order / total_nodes
    interpolated_color = random_color(start_color, end_color, fraction)
    return '#{:02x}{:02x}{:02x}'.format(*map(int, interpolated_color))

def dfs_visit_order(node, visit_order=[0], total_nodes=6):
    if node is not None:
        visit_order[0] += 1
        node.visit_order = visit_order[0]
        node.node_color = generate_color(node.visit_order, total_nodes)
        dfs_visit_order(node.left_child, visit_order, total_nodes)
        dfs_visit_order(node.right_child, visit_order, total_nodes)

def bfs_visit_order(root, total_nodes=6):
    queue = [root]
    order = 0
    while queue:
        node = queue.pop(0)
        if node is not None:
            order += 1
            node.visit_order = order
            node.node_color = generate_color(node.visit_order, total_nodes)
            queue.append(node.left_child)
            queue.append(node.right_child)

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
    return graph, position

def visualize_custom_heap(custom_heap_root, total_nodes, traversal_method):
    if traversal_method == 'DFS':
        dfs_visit_order(custom_heap_root, total_nodes=total_nodes)
    elif traversal_method == 'BFS':
        bfs_visit_order(custom_heap_root, total_nodes=total_nodes)
    
    custom_heap_graph = nx.DiGraph()
    positions = {custom_heap_root.node_id: (0, 0)}
    custom_heap_graph, positions = add_edges_to_graph(custom_heap_graph, custom_heap_root, positions)

    node_colors = [node[1]['color'] for node in custom_heap_graph.nodes(data=True)]
    node_labels = {node[0]: node[1]['label'] for node in custom_heap_graph.nodes(data=True)}

    plt.figure(figsize=(10, 8))
    nx.draw(custom_heap_graph, pos=positions, with_labels=True, labels=node_labels, arrows=False, node_size=2500, node_color=node_colors, font_weight='bold', font_color='white')
    plt.show()

custom_heap_root = CustomHeapNode(1)
custom_heap_root.left_child = CustomHeapNode(2)
custom_heap_root.right_child = CustomHeapNode(6)
custom_heap_root.left_child.left_child = CustomHeapNode(3)
custom_heap_root.left_child.right_child = CustomHeapNode(5)
custom_heap_root.right_child.left_child = CustomHeapNode(7)
custom_heap_root.left_child.left_child.right_child = CustomHeapNode(4)

#visualize_custom_heap(custom_heap_root, 7, 'DFS')

visualize_custom_heap(custom_heap_root, 7, 'BFS')