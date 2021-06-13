// Sorting integers with bubble sort
void printarr(int*, int);

void bubblesort(int* arr, int size){
	// 'Bubble' up the largest element to the last position
	for(int i = size-1; i>=0; --i){
		int tmp;
		for(int j=1; j<=i; ++j){
			// Swap
			if(arr[j]<arr[j-1]){
				tmp = arr[j-1];
				arr[j-1] = arr[j];
				arr[j] = tmp;
			}
		}
	}
	printf("Bubblesort done!\n");
}
