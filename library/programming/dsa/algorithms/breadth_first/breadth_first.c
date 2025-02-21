#include <stdlib.h>
#include <stdio.h>

typedef struct node{
    int value;
    struct node *left;
    struct node *right;
} node;

typedef struct queue_node {
    node *value;
    struct queue_node *next;
} queue_node;

typedef struct queue {
    queue_node *head;
    queue_node *tail;
} queue;

void breadth_first(node *root) {
    queue_node qn = {root};
    queue q = {&qn, &qn};
    while (q.head->value != NULL) {
	node *n = q.head->value;
	printf("%d\n", n->value);
	queue_node *qnl= malloc(sizeof(queue_node));
	qnl->value = n->left;
	q.tail->next = qnl;
	q.tail = qnl;
        queue_node *qnr = malloc(sizeof(queue_node));
	qnr->value = n->right;
        q.tail->next = qnr;
        q.tail = qnr;
	q.head = q.head->next;
    }
}

int main(void) {
    node node7 = {7};
    node node6 = {6};
    node node5 = {5};
    node node4 = {4};
    node node3 = {3, &node6, &node7};
    node node2 = {2, &node4, &node5};
    node node1 = {1, &node2, &node3};
    breadth_first(&node1);
}
