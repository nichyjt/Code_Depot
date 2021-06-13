// Select the largest/smallest element's index and build from there
void selectionsort(int* arr, int size){
	// Build from small implementation
	int smallest;
	int tmp;
	for(int i=0; i<size; ++i){
		smallest = i;
		for(int j=i; j<size; ++j){
			if(arr[j]<arr[smallest]){
				smallest = j;
			}
		}
		// Swap the smallest element with the i-th index
		tmp = arr[smallest];
		arr[smallest] =  arr[i];
		arr[i] = tmp;
	}
	printf("Selection sort completed!\n");
}