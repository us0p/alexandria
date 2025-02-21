#include <stdbool.h>
#include <math.h>
#include <stdio.h>

typedef struct vertice {
    int to;
    int dist;
} vertice;

// is used to check if all edges have been already seen.
bool has_unvisited(bool seen[5], double dists[5]) {
    for (int i = 0; i < 5; i++) {
	if (dists[i] < INFINITY && !seen[i]) {
	    return true;
	}
    }

    return false;
}

// is used to retrieve the nearest unseen edge.
int get_lowest_unvisited(bool seen[5], double dists[5]) {
    for (int i = 0; i < 5; i++) {
	if (dists[i] < INFINITY && !seen[i]) {
	    return i;
	}
    }

    return -1;
}

void dijkstra_shortest_path(
    int source,
    int destination,
    vertice graph[5][4]
) {
    // you can think of it as a stack, it's used to track the edges you 
    // visited.
    int prev[5] = {-1, -1, -1, -1, -1};

    // it has the same number of edges in your graph, it's used to mark 
    // which edges you alread visited.
    bool seen[5] = {false, false, false, false, false};

    // it has the sae number of edges in your graph, it's used to 
    // represent the distance between each edge. the source is always at 
    // distance 0. it's not possible to have negative distances.
    double dists[5] = {0,INFINITY,INFINITY,INFINITY,INFINITY,};

    while (has_unvisited(seen, dists)) {
	int lo = get_lowest_unvisited(seen, dists);
	seen[lo] = true; // mark edge as seen.

	// loops over every vertice of the current edge.
	for (int edge = 0; edge < 4; edge++) {
	    vertice v = graph[lo][edge];
	    // doesn't check the edge the vertice points to, if edge is
	    // already seen.
	    if (seen[v.to]) continue;
	    // get distance to edge which the vertice points to, the
	    // distance is equal to the current distance plus the vertice
	    // distance.
	    int dist = dists[lo] + v.dist;
	    // is the distance is lower than the current registered
	    // distance (starts at INFINITY), update dist to the shortest
	    // one.
	    if (dist < dists[v.to]) {
		// mark vertice destination edge as being pointed to by
		// the current edge.
		prev[v.to] = lo;
		dists[v.to] = dist;
	    }
	}
    }

    // will becone the reversed edge list of the shortest path from source
    // to destination.
    int out[5] = {};
    int curr = destination;
    int out_index = 0;
    while (prev[curr] != -1) {
	out[out_index] = curr;
	curr = prev[curr];
	out_index++;
    }
    out[out_index] = source;

    // printing out in reversed order, will produce the ordered list of
    // edges that leads to the shortest path from source to destination.
    for (int i = 4; i >= 0; i--) {
	printf("%d\n", out[i]);
    }
}

int main(void) {
    vertice adjacent_list[5][4] = {
	{{1, 1}, {2, 5}, {0, 0}, {0, 0}},
	{{2, 7}, {3, 6}, {0, 0}, {0, 0}},
	{{4, 1}, {0, 0}, {0, 0}, {0, 0}},
	{{2, 1}, {0, 0}, {0, 0}, {0, 0}},
	{{0, 0}, {0, 0}, {0, 0}, {0, 0}},
    };

    dijkstra_shortest_path(0, 4, adjacent_list);
}
