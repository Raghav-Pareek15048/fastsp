#include "tsp.h"
#include <vector>
#include <numeric>
#include <algorithm>
#include <climits>

int tsp_solver(const std::vector<int>& dist_matrix, int n) {
    if (n <= 1) {
        return 0;
    }
    if (n == 2) {
        return dist_matrix[0 * n + 1] + dist_matrix[1 * n + 0];
    }

    // Permute cities from 1 to n - 1 (keeping city 0 as fixed origin)
    std::vector<int> cities(n - 1);
    std::iota(cities.begin(), cities.end(), 1);

    int min_cost = INT_MAX;
    const int* matrix = dist_matrix.data();
    const size_t num_intermediate = cities.size() - 1;

    do {
        // Start from origin (node 0) to first city
        int current_cost = matrix[cities[0]];

        // Intermediate hops
        for (size_t i = 0; i < num_intermediate; ++i) {
            current_cost += matrix[cities[i] * n + cities[i + 1]];
        }

        // Return from last city back to origin (node 0)
        current_cost += matrix[cities.back() * n];

        if (current_cost < min_cost) {
            min_cost = current_cost;
        }
    } while (std::next_permutation(cities.begin(), cities.end()));

    return min_cost;
}
