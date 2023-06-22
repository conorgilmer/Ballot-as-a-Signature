//Program to find the number of combinations nCr of a given number
//nCr = ((n!)/(n-r)!)r!


#include<stdio.h>


/* Factorial function */
int fact(int n){
int fact = 1, x;
    for(x=1;x<=n;x++)
        fact=fact*x; 

    return(fact);
}

int main(){

    int x,comb,n,r;

    printf("Enter a number for n : ");

    scanf("%d",&n); 

    printf("Enter a number: for r : ");

    scanf("%d",&r); 


    comb = (fact(n)/fact(n-r)) * fact(r);
//    printf("fact (n) %d\n", fact(n));
//    printf("fact (n-r) %d\n", fact(n-r));
    printf("Combinations of %dC%d is: %d",n,r,comb);

    printf("\n");
    return 0;

}
