#include <stdio.h>
#include <stdlib.h>

/* generate random vote - permutation - nPr */
/* it does this by randomising elements in an array[n] */
/* then selecting the first r of them */ 
void genvote(n,r) {
  int arr[n];
  
  int i;
  /* populate the array with values 1 to n */
  for (i = 0; i < n; ++i)
    arr[i] = i;

  /* randomise the elements in the array */
  for (i = 0; i < n; ++i) {
    int *a = &arr[ i ];
    int *b = &arr[ rand() % n ];
    
    int temp = *a;
    *a = *b;
    *b = temp;
  }

  /* select r number of elements from the ranomised array */
  for (i = 0; i < r; ++i)
    printf( "%d ", arr[i] );
}

/* Main Function */
int main(){
int n, r;

    /* get values of n and r */
    printf("Enter a number to find candidates: ");
    scanf("%d",&n);

    printf("Enter a number to find preferences used: ");
    scanf("%d",&r);
    
    /* generate a vote a permutaiton from an array */
    genvote(n,r);

}
