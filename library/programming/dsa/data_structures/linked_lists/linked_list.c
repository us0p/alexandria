#include <stdlib.h>
#include <stdio.h>

typedef struct Node {
    int data;
    struct Node *next;
    struct Node *prev;
} Node;

typedef struct LinkedList {
    int len;
    Node *head;
    Node *tail;
} LinkedList;

LinkedList *create_list(void) {
    LinkedList *ll = malloc(sizeof(LinkedList));
    if (!ll) exit(1);
    ll->len = 0;
    ll->head = NULL;
    ll->tail = NULL;
    return ll;
}

Node *create_node(int data) {
    Node *n = malloc(sizeof(Node));
    if (!n) exit(1);
    n->data = data;
    n->next = NULL;
    n->prev = NULL;
    return n;
}

void append(LinkedList *ll, int data) {
    Node *n = create_node(data);
    if (!ll->head) {
	ll->head = n;
	ll->tail = n;
    } else {
	ll->tail->next = n;
	n->prev = ll->tail;
	ll->tail = n;
    }
    ll->len++;
}

void prepend(LinkedList *ll, int data) {
    Node *n = create_node(data);
    if (!ll->head) {
	ll->head = n;
	ll->tail = n;
    } else {
	ll->head->prev = n;
	n->next = ll->head;
	ll->head = n;
    }
    ll->len++;
}

Node *pop(LinkedList *ll) {
    Node *n = ll->head;
    if (!n) {
	return NULL;
    }
    if (ll->head == ll->tail) {
	ll->head = NULL;
	ll->tail = NULL;
    } else {
	ll->head = ll->head->next;
	ll->head->prev = NULL;
    }
    ll->len--;
    return n;
}

Node *remove_node(LinkedList *ll) {
    Node *n = ll->tail;
    if (!n) {
	return NULL;
    }
    if (ll->head == ll->tail) {
	ll->head = ll->tail = NULL;
    } else {
	ll->tail = ll->tail->prev;
	ll->tail->next = NULL;
    }
    ll->len--;
    return n;
}

Node *get_node_at(LinkedList *ll, int idx) {
    if (idx >= ll->len || idx < 0) return NULL;
    if (idx == 0) return ll->head;
    if (idx == ll->len) return ll->tail;

    Node *el = ll->head->next;
    for (int i = 1; i < idx; i++) {
	el = el->next;
    }

    return el;
}

void insert_node_at(LinkedList *ll, int idx, int data) {
    Node *n = create_node(data);
    Node *node_at = get_node_at(ll, idx);
    if (!node_at) return;

    n->next = node_at;
    n->prev = node_at->prev;
    node_at->prev->next = n;
    node_at->prev = n;
    ll->len++;
}

Node *remove_node_at(LinkedList *ll, int idx) {
    Node *node_at = get_node_at(ll, idx);
    node_at->next->prev = node_at->prev;
    node_at->prev->next = node_at->next;
    node_at->next = NULL;
    node_at->prev = NULL;
    ll->len--;
    return node_at;
}

void clear_list(LinkedList *ll) {
    Node *tail = ll->tail;
    while (tail) {
	Node *tmp = tail;
	tail = tmp->prev;
	free(tmp);
    }
    free(ll);
}

int main(void) {
    LinkedList *ll = create_list();
    for (int i = 0; i < 10; i++) {
	if (i % 2) append(ll, i);
	else prepend(ll, i);
    }
    for(int i = 0; i < ll->len; i++) {
	printf("idx %d, value: %d\n", i, get_node_at(ll, i)->data);
    }
    puts("----");
    insert_node_at(ll, 5, 10);
    for(int i = 0; i < ll->len; i++) {
	printf("idx %d, value: %d\n", i, get_node_at(ll, i)->data);
    }
    puts("----");
    remove_node_at(ll, 5);
    for(int i = 0; i < ll->len; i++) {
	printf("idx %d, value: %d\n", i, get_node_at(ll, i)->data);
    }
    clear_list(ll);
}
