# -*- coding: utf-8 -*-

"""
Clustering Using a Similarity Measure Based
on Shared Near Neighbors
R. A. JARVIS AND EDWARD A. PATRICK

A nonparametric clustering technique incorporating the
concept of similarity based on the sharing of near neighbors is presented.
In addition to being an essentially paraliel approach, the computational
elegance of the method is such that the scheme is applicable
to a wide class of practical problems involving large sample size and high
dimensionality. No attempt is made to show how a priori problem
knowledge can be introduced into the procedure.
"""


class JarvisPatrick(object):

    def __init__(self, dataset_elements, distance_function):
        self.dataset_elements = dataset_elements
        # initially each element is a cluster of 1 element
        self.cluster = {element: cluster_index for cluster_index, element in self.dataset_elements}
        self.distance_function = distance_function

    def __call__(self, number_of_neighbors, number_of_common_neighbors):
        """
        """

        neighbors = {}
        for element in self.dataset_elements:
            neighbors[element] = self.calculate_k_nearest_elements(element, number_of_neighbors)

        for element, neighbors in neighbors.items():
            for other_element, other_neighbors in neighbors.items():
                if element != other_element:
                    # we check both sides since the relation is not symmetric
                    if element in other_neighbors and other_element in neighbors:
                        if len(set(neighbors).intersection(other_neighbors)) >= number_of_common_neighbors:
                            self.reconfigure_clusters(element, other_element)

    def reconfigure_clusters(self, element, other_element):
        if self.cluster[element] != self.cluster[other_element]:
            # we keep the lowest index
            if self.cluster[other_element] > self.cluster[element]:
                for cluster_element in self.dataset_elements:
                    if self.cluster[cluster_element] == self.cluster[other_element]:
                        self.cluster[cluster_element] = self.cluster[element]
                self.cluster[other_element] = self.cluster[element]
            else:
                for cluster_element in self.dataset_elements:
                    if self.cluster[cluster_element] == self.cluster[element]:
                        self.cluster[cluster_element] = self.cluster[other_element]
                self.cluster[element] = self.cluster[other_element]

    def calculate_k_nearest_elements(self, element, k_value):
        res = []
        for neighbor in self.dataset_elements:
            res.append((neighbor, self.distance_function(element, neighbor)))
        return map(lambda element: element[1], sorted(res, key=lambda neighbor_tuple: neighbor_tuple[1]))[:k_value]
