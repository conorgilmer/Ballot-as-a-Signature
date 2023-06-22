#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* Calculate the quota for a PR-STV Election
 The Droop Quota is
 Q = (n/r+1) + 1
 The Hare Quota is
 Q = (n/r) 
*/

/* DroopQuota Calculate */
int droopQuota ( n, r){
int quota;
quota = round(((n/(r+1))+1));

return quota;
}

/* Hare Quota Calculate */
int hareQuota ( n, r){
int quota;
quota = round(n/r);

return quota;
}

/* Main Function */
int main(){
int n, r;

    /* get number of votes */
    printf("Enter a number votes : ");
    scanf("%d",&n);

    printf("Enter a number seats to allocate : ");
    scanf("%d",&r);
    
    printf(" The Droop Quota would be %d\n", droopQuota(n,r));
    printf(" The Hare Quota would be %d\n", hareQuota(n,r));

}
