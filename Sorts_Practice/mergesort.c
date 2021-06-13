void merge(int *arr, int start, int end, int mid){
	// Create copy of the array
	int leftlen = mid-start+1;
	int rightlen = end-mid;
	int left[leftlen];
	int right[rightlen];
	for(int i=0; i<leftlen; ++i){
		left[i] = arr[start+i];
	}
	for(int i=0; i<rightlen; ++i){
		right[i] = arr[mid+1+i];
	}
	// Most fun part
	int lptr = 0, rptr = 0;
	while(lptr < leftlen && rptr < rightlen){
		if(left[lptr]<right[rptr]){
			arr[start++] = left[lptr++];
		}else{
			arr[start++] = right[rptr++];
		}
	}
	while(lptr<leftlen){
		arr[start++] = left[lptr++];
	}
	while(rptr<rightlen){
		arr[start++] = right[rptr++];
	}
}

void mergesort(int* arr, int start_index, int end_index){
	if(start_index>=end_index) return;
	// WARNING: End 
	int mid = (start_index+end_index)/2;
	// Sort left
	mergesort(arr, start_index, mid);
	// Sort right
	mergesort(arr, mid+1, end_index);
	// Merge left and right
	merge(arr, start_index, end_index, mid);
}