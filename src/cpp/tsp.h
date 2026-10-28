#ifndef TSP_H
#define TSP_H

#include <vector>

/**
 * Calculates the shortest path tour cost through a fully connected graph
 * represented by a flattened 1D distance matrix using std::next_permutation.
 *
 * @param dist_matrix 1D vector of length n * n containing distances where
 *                    distance from node i to node j is at index [i * n + j].
 * @param n           Number of nodes in the graph.
 * @return            The minimum tour cost visiting each node once and returning to origin node 0.
 */
int tsp_solver(const std::vector<int>& dist_matrix, int n);

#endif // TSP_H
