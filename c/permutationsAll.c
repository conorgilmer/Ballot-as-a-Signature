//Program to find the number of permutations nPr of a given number
#include<stdio.h>


/* Factorial function */
int fact(int n){
int fact = 1, x;
    for(x=1;x<=n;x++)
        fact=fact*x; 

    return(fact);
}

int main(){

    int x,perm,n,r;

    printf("Enter a number of candidates: ");

    scanf("%d",&n); 

    printf("n\tr\tPermutations\n");
    for(r=1;r<=n;r++){
    
       perm = fact(n)/fact(n-r);
       printf("%d\t%d\t%d\n", n, r, perm);
    }
//    printf("fact (n) %d\n", fact(n));
//    printf("fact (n-r) %d\n", fact(n-r));
//    printf("Permutations of %dP%d is: %d",n,r,perm);

    printf("\n");
    return 0;

}
