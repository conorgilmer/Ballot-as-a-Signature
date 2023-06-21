      ******************************************************************
      * Author:    Conor Gilmer
      * Date:      30/12/2022
      * Purpose:   permutations,combinations factorials etc.
      * Tectonics: cobc -x -fintrinsics=FACTORIAL
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. STVPermutationsC.
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
       SELECT OUTPUT-FILE
           ASSIGN TO 'permutations_output.dat'
           ORGANIZATION IS LINE SEQUENTIAL
           ACCESS MODE IS SEQUENTIAL.
       DATA DIVISION.
       FILE SECTION.
       FD  OUTPUT-FILE         RECORD CONTAINS 50 CHARACTERS.
       01  OUTPUT-RECORD.
         05 OUT-REC-ROW          PIC X(50).

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
       display '*** Starting ***'.
       START-ROUTINE.
           display 'Opening files'.
      *     OPEN INPUT INPUT-FILE.
           display "open file for output".
           OPEN OUTPUT OUTPUT-FILE.

       OUTPUT-TITLE-ROUTINE.
           move OUTPUT-TITLE to OUT-REC-ROW.
           write OUTPUT-RECORD.


       MAIN-PROCEDURE.
           DISPLAY "Enter the number of Candidates N ".
           ACCEPT N.
           DISPLAY OUTPUT-TITLE.
           PERFORM PERM-PARA varying R FROM 1 BY 1 UNTIL R > N.
           display "closing output file".
           close OUTPUT-FILE.
           display '*** The End ***'.
           STOP RUN.

       PERM-PARA.
           COMPUTE U = FACTORIAL(N)/FACTORIAL(N - R).
      *    DISPLAY "Permutations N!/(n-r)! = " U.
           PERFORM DISPLAY-PARA.

       DISPLAY-PARA.
           move N to Z.
           MOVE Z to out-cand.
           MOVE R to out-pref
           move U to Z.
           MOVE Z to out-perm.
           DISPLAY OUTPUT-ROW.
           MOVE OUTPUT-ROW to OUT-REC-ROW.
           write OUTPUT-RECORD.


       END PROGRAM STVPermutationsC.
