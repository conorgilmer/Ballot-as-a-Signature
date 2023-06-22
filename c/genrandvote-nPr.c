#include <stdio.h>
#include <stdlib.h>

void genvote(n,r) {
  int arr[n];
  
  int i;
  for (i = 0; i < n; ++i)
    arr[i] = i;

  for (i = 0; i < n; ++i) {
    int *a = &arr[ i ];
    int *b = &arr[ rand() % n ];
    
    int temp = *a;
    *a = *b;
    *b = temp;
  }

  for (i = 0; i < r; ++i)
    printf( "%d ", arr[i] );
}

int main(){
int n, r;

    printf("Enter a number to find candidates: ");

    scanf("%d",&n);

    printf("Enter a number to find preferences used: ");

    scanf("%d",&r);

    genvote(n,r);

}
