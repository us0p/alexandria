#include <stdio.h>

typedef struct node {
    int value;
    struct node *left;
    struct node *right;
} node;

void inorder(node *root) {
    if (root == NULL) {
	return;
    }

    inorder(root->left);
    printf("%d\n", root->value);
    inorder(root->right);
}

void postorder(node *root) {
    if (root == NULL) {
	return;
    }

    postorder(root->left);
    postorder(root->right);
    printf("%d\n", root->value);
}

int main(void) {
    node node7 = {21};
    node node6 = {18};
    node node5 = {4};
    node node4 = {5};
    node node3 = {3, &node6, &node7};
    node node2 = {23, &node4, &node5};
    node node1 = {7, &node2, &node3};
    inorder(&node1);
    printf("-----\n");
    postorder(&node1);
}
