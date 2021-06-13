#include <iostream>
#include "bubblesort.c"
#include "selectionsort.c"
#include "insertionsort.c"
#include "mergesort.c"

void printarr(int* arr, int size){
	for(int i=0; i<size; ++i){
		printf("%d ", *(arr+i));
	}
}

int main(){
	int nums[7] = {2,4,1,5,7,6,3};
	// bubblesort(nums, 7);
	// selectionsort(nums, 7);
	// insertionsort(nums, 7);
	mergesort(nums, 0, 6);
	printarr(nums, 7);
	return 0;
}