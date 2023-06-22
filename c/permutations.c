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

    printf("Enter a number to find candidates: ");

    scanf("%d",&n); 

    printf("Enter a number to find preferences used: ");

    scanf("%d",&r); 


    perm = fact(n)/fact(n-r);
//    printf("fact (n) %d\n", fact(n));
//    printf("fact (n-r) %d\n", fact(n-r));
    printf("Permutations of %dP%d is: %d",n,r,perm);

    printf("\n");
    return 0;

}
