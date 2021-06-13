// Insertion sort works like sorting a deck of cards
void insertionsort(int* arr, int size){
	for(int i=0; i<size; ++i){
		// Pull a new 'card' from the array deck
		// Check the built hand and swap if necessary
		for(int j=i; j>0; --j){
			// NOTE: i := 'new' card's initial index
			if(*(arr+j-1) > *(arr+j)){
				int tmp = *(arr+j);
				*(arr+j) = *(arr+j-1);
				*(arr+j-1) = tmp;
			}
		}
	}
	printf("Insertion sort completed!\n");
}