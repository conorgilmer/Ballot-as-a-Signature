// generate permutations nPr
import java.util.*;
 
public class permutations {
 
    static int fact(int n)
    {
        if (n <= 1)
            return 1;
        return n * fact(n - 1);
    }
 
    static int nPr(int n, int r)
    {
        return fact(n) / fact(n - r);
    }

    static void printPrefs(String cons, int n){
	System.out.println("Permutations for " + cons);
 	for (int r = 1; r <= n; r++) {
        System.out.println("Candidates = " + n + ", preferences = " + r + ". Permutations (nPr) = "
                           + nPr(n, r));}

    } 
    public static void main(String args[])
    {
	String cons = "Dublin West"; // constituency
        int n = 9;  // candidates

	printPrefs("\nDublin West", 9);
	printPrefs("\nDublin North", 12);
	printPrefs("\nMeath", 14);
    }
}
