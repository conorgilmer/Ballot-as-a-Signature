      ******************************************************************
      * Author:    Conor Gilmer
      * Date:      30/12/2022
      * Purpose:   permutations,combinations factorials etc.
      * Tectonics: cobc
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. PermutationsC.
       DATA DIVISION.
       FILE SECTION.

       WORKING-STORAGE SECTION.
       77 I PIC 9(8).
       77 F PIC 9(8) VALUE 1.
       77 N PIC 9(8).
       77 R PIC 9(8).
       77 U PIC 9(8).
       77 P PIC 9(8).
       77 Z PIC Z9(11)9.

       01  OUTPUT-TITLE.
           05 filler         PIC XX.
           05 out-cand-t     PIC X(10) VALUE "Candidates".
           05 filler         PIC XX.
           05 out-pref-t     PIC X(12) VALUE "Preferences".
           05 filler         PIC XX.
           05 out-perm-t     PIC X(12) VALUE "Permutations".

       01  OUTPUT-ROW.
           05 filler         PIC XX.
           05 out-cand       PIC Z(9)9.
           05 filler         PIC XX.
           05 out-pref       PIC Z(11)9.
           05 filler         PIC XX.
           05 out-perm       PIC Z(11)9.

       PROCEDURE DIVISION.
       MAIN-PROCEDURE.

       MAIN-PARA.
           DISPLAY "Enter the number of Candidates (n)  ".
           ACCEPT N.
           DISPLAY "Enter a number preferences used (r) ".
           ACCEPT R.
           COMPUTE U = FACTORIAL(N)/FACTORIAL(N - R).

           DISPLAY "Permutations = " U.
      *     STOP RUN.

       DISPLAY-PARA.
           DISPLAY "Output".
           DISPLAY " ".
           move N to Z.
           MOVE Z to out-cand.
           MOVE R to out-pref
           move U to Z.
           MOVE Z to out-perm.
           DISPLAY OUTPUT-TITLE.
           DISPLAY OUTPUT-ROW.


       END PROGRAM PermutationsC.
