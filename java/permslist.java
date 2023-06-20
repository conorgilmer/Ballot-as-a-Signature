import java.util.ArrayList;
 
public class permslist {
 
    static void printArrayList(ArrayList<String> arrL)
    {
        arrL.remove("");
        for (int i = 0; i < arrL.size(); i++)
            System.out.print(arrL.get(i) + "\n");
    }
 
    public static ArrayList<String> getPermutation(String str)
    {
 
        // If string is empty
        if (str.length() == 0) {
 
            // Return an empty arraylist
            ArrayList<String> empty = new ArrayList<>();
            empty.add("");
            return empty;
        }
 
        // Take first character of str
        char ch = str.charAt(0);
 
        // Take sub-string starting from the
        // second character
        String subStr = str.substring(1);
 
        // Recursive call
        ArrayList<String> prevResult = getPermutation(subStr);
 
        // Store the generated permutations
        // into the resultant arraylist
        ArrayList<String> Res = new ArrayList<>();
 
        for (String val : prevResult) {
            for (int i = 0; i <= val.length(); i++) {
                Res.add(val.substring(0, i) + ch + val.substring(i));
            }
        }
 
        // Return the resultant arraylist
        return Res;
    }
 
    public static void main(String[] args)
    {
        String str = "123456789";
        //String str = "123";
        printArrayList(getPermutation(str));
    }
}
