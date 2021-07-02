// Partition: For a pivot, p, throw all < p to its left and all > p to its right then return p's sorted index
int partition(int* arr, int startindex, int endindex){
	int pivotIndex = endindex;
	// Initialise builder/scanner index
	int curr = startindex;
	while(curr < pivotIndex){
		if(arr[curr]>arr[pivotIndex]){
			// Swap curr with pivotIndex's left neighbour
			int tmp = arr[curr];
			arr[curr] = arr[pivotIndex-1]; //swap neighbours
			arr[pivotIndex-1] = arr[pivotIndex];
			arr[pivotIndex--] = tmp; //inline decrement
		}else{
			// arr[curr] is correctly partitioned
			++curr; 
		}
	}
	return pivotIndex;
}

void quicksort(int* arr, int startindex, int endindex){
	// If size <= 1, the array is already sorted
	if(startindex >= endindex) return;
	int partitionIndex = partition(arr, startindex, endindex);
	quicksort(arr, startindex, partitionIndex-1); // left sort
	quicksort(arr, partitionIndex+1, endindex); // right sort
}