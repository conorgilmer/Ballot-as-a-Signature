//Program to find the number of permutations nPr of a given number
#include<stdio.h>


/* Factorial function */
int fact(int n){
int fact = 1, x;
    for(x=1;x<=n;x++)
        fact=fact*x; 

    return(fact);
}

/* Permutations function */
int permutations(int n, int r){
    int perm;
       perm = fact(n)/fact(n-r);

    return(perm);
}

/* Combinations function */
int combinations(int n, int r){
    int combi;
       combi = (fact(n)/fact(n-r)) * fact(r);

    return(combi);
}

/* main function */
int main(){

    int x,perm,combi,n,r;

    printf("Enter a number of candidates: ");

    scanf("%d",&n); 

    printf("n\tr\tPermutations\tCombinations\n");
    for(r=1;r<=n;r++){
       perm = permutations(n,r);
       combi = combinations(n,r);
       printf("%d\t%d\t%d\t\t%d\n", n, r, perm, combi);
    }
//    printf("fact (n) %d\n", fact(n));
//    printf("fact (n-r) %d\n", fact(n-r));
//    printf("Permutations of %dP%d is: %d",n,r,perm);

    printf("\n");
    return 0;

}
