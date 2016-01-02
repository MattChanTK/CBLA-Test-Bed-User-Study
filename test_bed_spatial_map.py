__author__ = 'Matthew'

import math

class NodeSpatialMap(object):

    def __init__(self):

        self.node_dict = dict()

    def add_node(self, node_name, x, y, z=0):

        if isinstance(node_name, str) and \
            isinstance(x, (int, float)) and \
            isinstance(y, (int, float)) and \
                isinstance(z, (int, float)):

            self.node_dict[node_name] = (x, y, z)

        else:
            raise ValueError('Invalid node_name or coordinates.')

    def get_position(self, node_name):

        if node_name in self.node_dict:
            return self.node_dict[node_name]
        else:
            return None

    def get_displacement(self, from_node, to_node):

        if isinstance(from_node, (tuple, list)) and len(from_node) == 3:
            pos_1 = tuple(from_node)
        else:
            pos_1 = self.get_position(from_node)

        if isinstance(to_node, (tuple, list)) and len(to_node) == 3:
            pos_2 = tuple(to_node)
        else:
            pos_2 = self.get_position(to_node)

        if isinstance(pos_1, (tuple, list)) and \
                isinstance(pos_2, (tuple, list))\
                and (len(pos_1) == len(pos_2)):

            displacement = []
            for i in range(len(pos_1)):
                displacement.append(pos_2[i] - pos_1[i])

            return tuple(displacement)
        else:
            return None

    def get_distance(self, node_1, node_2):

        displacement = self.get_displacement(node_1, node_2)

        if displacement:
            return math.sqrt(sum([x**2 for x in displacement]))

        return None

    def build_cbla_test_bed_node_map(self):

        # Cluster 1
        self.add_node('c1.cbla_light_0', 2.0, 0, 0)
        self.add_node('c1.cbla_light_1', 3.0, 1.74, 0)
        self.add_node('c1.cbla_light_2', 1.0, 1.74, 0)

        self.add_node('c1.cbla_halfFin_0-l', 2.0, 0.84, 0)
        self.add_node('c1.cbla_halfFin_1-l', 2.34, 1.37, 0)
        self.add_node('c1.cbla_halfFin_2-l', 1.74, 1.37, 0)

        self.add_node('c1.cbla_halfFin_0-r', 2.0, 0.84, 0)
        self.add_node('c1.cbla_halfFin_1-r', 2.34, 1.37, 0)
        self.add_node('c1.cbla_halfFin_2-r', 1.74, 1.37, 0)

        self.add_node('c1.cbla_reflex_0-l', 2.0, 0.84, 0)
        self.add_node('c1.cbla_reflex_1-l', 2.34, 1.37, 0)
        self.add_node('c1.cbla_reflex_2-l', 1.74, 1.37, 0)

        self.add_node('c1.cbla_reflex_0-m', 2.0, 0.84, 0)
        self.add_node('c1.cbla_reflex_1-m', 2.34, 1.37, 0)
        self.add_node('c1.cbla_reflex_2-m', 1.74, 1.37, 0)

        # Cluster 2
        self.add_node('c2.cbla_light_0', 4.1, 3.55, 0)
        self.add_node('c2.cbla_light_1', 3.0, 5.34, 0)
        self.add_node('c2.cbla_light_2', 5.11, 5.34, 0)

        self.add_node('c2.cbla_halfFin_0-l', 4.1, 4.35, 0)
        self.add_node('c2.cbla_halfFin_1-l', 4.4, 4.9, 0)
        self.add_node('c2.cbla_halfFin_2-l', 3.8, 4.9, 0)

        self.add_node('c2.cbla_halfFin_0-r', 4.1, 4.35, 0)
        self.add_node('c2.cbla_halfFin_1-r', 4.4, 4.9, 0)
        self.add_node('c2.cbla_halfFin_2-r', 3.8, 4.9, 0)

        self.add_node('c2.cbla_reflex_0-l', 4.1, 4.35, 0)
        self.add_node('c2.cbla_reflex_1-l', 4.4, 4.9, 0)
        self.add_node('c2.cbla_reflex_2-l', 3.8, 4.9, 0)

        self.add_node('c2.cbla_reflex_0-m', 4.1, 4.35, 0)
        self.add_node('c2.cbla_reflex_1-m', 4.4, 4.9, 0)
        self.add_node('c2.cbla_reflex_2-m', 3.8, 4.9, 0)

        # Cluster 3
        self.add_node('c3.cbla_light_0', 6.15, 0, 0)
        self.add_node('c3.cbla_light_1', 7.15, 1.74, 0)
        self.add_node('c3.cbla_light_2', 5.12, 1.74, 0)

        self.add_node('c3.cbla_halfFin_0-l', 6.15, 0.84, 0)
        self.add_node('c3.cbla_halfFin_1-l', 6.47, 1.37, 0)
        self.add_node('c3.cbla_halfFin_2-l', 5.78, 1.37, 0)

        self.add_node('c3.cbla_halfFin_0-r', 6.15, 0.84, 0)
        self.add_node('c3.cbla_halfFin_1-r', 6.47, 1.37, 0)
        self.add_node('c3.cbla_halfFin_2-r', 5.78, 1.37, 0)

        self.add_node('c3.cbla_reflex_0-l', 6.15, 0.84, 0)
        self.add_node('c3.cbla_reflex_1-l', 6.47, 1.37, 0)
        self.add_node('c3.cbla_reflex_2-l', 5.78, 1.37, 0)

        self.add_node('c3.cbla_reflex_0-m', 6.15, 0.84, 0)
        self.add_node('c3.cbla_reflex_1-m', 6.47, 1.37, 0)
        self.add_node('c3.cbla_reflex_2-m', 5.78, 1.37, 0)

        # Cluster 4
        self.add_node('c4.cbla_light_0', 8.20, 3.55, 0)
        self.add_node('c4.cbla_light_1', 9.21, 5.34, 0)
        self.add_node('c4.cbla_light_2', 7.15, 5.34, 0)

        self.add_node('c4.cbla_halfFin_0-l', 8.20, 4.35, 0)
        self.add_node('c4.cbla_halfFin_1-l', 8.56, 4.9, 0)
        self.add_node('c4.cbla_halfFin_2-l', 7.80, 4.9, 0)

        self.add_node('c4.cbla_halfFin_0-r', 8.20, 4.35, 0)
        self.add_node('c4.cbla_halfFin_1-r', 8.56, 4.9, 0)
        self.add_node('c4.cbla_halfFin_2-r', 7.80, 4.9, 0)

        self.add_node('c4.cbla_reflex_0-l', 8.20, 4.35, 0)
        self.add_node('c4.cbla_reflex_1-l', 8.56, 4.9, 0)
        self.add_node('c4.cbla_reflex_2-l', 7.80, 4.9, 0)

        self.add_node('c4.cbla_reflex_0-m', 8.20, 4.35, 0)
        self.add_node('c4.cbla_reflex_1-m', 8.56, 4.9, 0)
        self.add_node('c4.cbla_reflex_2-m', 7.80, 4.9, 0)

    def build_cbla_test_bed_grid_map(self):

        self.add_node('box_1', 1.3, 0, 0)
        self.add_node('box_2', 3.9, 0, 0)
        self.add_node('box_3', 6.5, 0, 0)
        self.add_node('box_4', 9.1, 0, 0)
        self.add_node('box_5', 1.3, 2.33, 0)
        self.add_node('box_6', 3.9, 2.33, 0)
        self.add_node('box_7', 6.5, 2.33, 0)
        self.add_node('box_8', 9.1, 2.33, 0)
        self.add_node('box_9', 1.3, 2.33, 0)
        self.add_node('box_10', 3.9, 4.66, 0)
        self.add_node('box_11', 6.5, 4.66, 0)
        self.add_node('box_12', 9.1, 4.66, 0)

