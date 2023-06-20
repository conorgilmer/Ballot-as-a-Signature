      ******************************************************************
      * Author:    Conor Gilmer
      * Date:      30/12/2022
      * Purpose:   permutations,combinations factorials etc.
      * Tectonics: cobc
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. STVPermutationsnPr.
       DATA DIVISION.
       FILE SECTION.

       WORKING-STORAGE SECTION.
       77 I PIC 9(12).
       77 F PIC 9(12) VALUE 1.
       77 N PIC 9(12).
       77 R PIC 9(12).
       77 U PIC 9(12).
       77 P PIC 9(12).
       77 Z PIC Z9(12)9.

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
           DISPLAY "Enter the number of Candidates N ".
           ACCEPT N.
           DISPLAY "Enter the number of Seats to allocate R ".
           ACCEPT R.
           DISPLAY OUTPUT-TITLE.
           PERFORM PERM-PARA.
      *     PERFORM DISPLAY-PARA.
           STOP RUN.

       PERM-PARA.
           MOVE 1 to F.
           PERFORM X-PARA VARYING I FROM 1 BY 1 UNTIL I > N.
           MOVE F TO P.
      *    DISPLAY "FACTORIAL OF n IS (n!) =  " P.
           COMPUTE U = N - R.
           move 1 to F
           PERFORM X-PARA VARYING I FROM 1 BY 1 UNTIL I > U.
      *    display "(n-r)!" F.
           COMPUTE U = P/F.
      *    DISPLAY "Permutations N!/(n-r)! = " U.
           PERFORM DISPLAY-PARA.
      *     STOP RUN.
       X-PARA.
      *    display F " " I.
           COMPUTE F = F * I.

       DISPLAY-PARA.
           move N to Z.
           MOVE Z to out-cand.
           MOVE R to out-pref
           move U to Z.
           MOVE Z to out-perm.
           DISPLAY OUTPUT-ROW.





       END PROGRAM STVPermutationsnPr.
