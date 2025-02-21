#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

typedef struct DynamicArray {
    int len;
    int cap;
    int *data;
} DynamicArray;

DynamicArray *makeDA(int cap) {
    DynamicArray *da = (DynamicArray*)malloc(sizeof(DynamicArray));
    da->len = 0;
    da->cap = cap;
    da->data = (int *)malloc(da->cap * sizeof(int));
    return da;
}

void append(DynamicArray *da, int item) {
    if (da->len < da->cap) {
	da->data[da->len] = item;
	da->len++;
	return;
    }
    int *currArr = da->data;
    da->cap *= 2;
    da->data = (int *)malloc(da->cap * sizeof(int));
    memcpy(da->data, currArr, da->len * sizeof(int));
    free(currArr);
    append(da, item);
}

void pop(DynamicArray *da) {
    if (da->len > 0) {
	da->len -= 1;
	da->data[da->len] = 0;
    }
}

void shift(DynamicArray *da, int item) {
    if (da->len < da->cap) {
	for(int i = da->len - 1; i >= 0; i--) {
	    da->data[i + 1] = da->data[i];
	}
	da->data[0] = item;
	da->len++;
	return;
    }
    int *currArr = da->data;
    da->cap *= 2;
    da->data = (int *)malloc(da->cap * sizeof(int));
    memcpy(da->data, currArr, da->len * sizeof(int));
    free(currArr);
    shift(da, item);
}

void unshift(DynamicArray *da) {
    if (da->len > 0) {
	for(int i = 0; i < da->len; i++) {
	    da->data[i] = da->data[i + 1];
	}
	da->len--;
    }
}

void printArr(int *arr, int arrSize) {
    printf("[");
    for (int i = 0; i < arrSize; i++) {
	printf("%d", arr[i]);	
	if (i + 1 < arrSize) printf(", ");
    }
    printf("]\n");
}

double getTimeMS(struct timespec s, struct timespec e) {
    double sDiff = e.tv_sec - s.tv_sec;
    double sNDiff = e.tv_nsec - s.tv_nsec;
    return sDiff * 1000 + sNDiff / 1000000;
}

double getAverageDurationInsertFn(
    void (appendFn)(DynamicArray *da, int item),
    DynamicArray *da,
    int cap
) {
    struct timespec s, e;
    double ms = 0;
    for(int i = 0; i < cap; i++) {
	clock_gettime(CLOCK_MONOTONIC, &s);
	appendFn(da, i);
	clock_gettime(CLOCK_MONOTONIC, &e);
	ms += getTimeMS(s, e);
    }

    return ms / cap;
}

double getAverageDurationRemoveFn(
    void (removeFn)(DynamicArray *da),
    DynamicArray *da,
    int cap
) {
    struct timespec s, e;
    double ms = 0;
    for(int i = 0; i < cap; i++) {
	clock_gettime(CLOCK_MONOTONIC, &s);
	removeFn(da);
	clock_gettime(CLOCK_MONOTONIC, &e);
	ms += getTimeMS(s, e);
    }

    return ms / cap;
}

int main(void) {
    int cap = 100000;
    DynamicArray *da = makeDA(cap);

    double avg1 = getAverageDurationInsertFn(append, da, cap);
    printf("average duration append %d items: %.2fms\n", cap, avg1);
    free(da);
    da = makeDA(cap);

    double avg2 = getAverageDurationInsertFn(shift, da, cap);
    printf("average duration shift %d items: %.2fms\n", cap, avg2);

    double avg3 = getAverageDurationRemoveFn(pop, da, cap);
    printf("average duration pop %d itesm: %.2fms\n", cap, avg1);

    getAverageDurationInsertFn(append, da, cap);
    double avg4 = getAverageDurationRemoveFn(unshift, da, cap);
    printf("average duration unshift %d items: %.2fms\n", cap, avg2);
    free(da);
}
