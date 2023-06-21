      ******************************************************************
      * Author:    Conor Gilmer
      * Date:      30/12/2022
      * Purpose:   Cobol to calculate factorial n!
      *             using an intrinsic library
      *            e.g. cobc -x -fintrinsics=FACTORIAL MyProg.cob

      * Tectonics: GNUCobol Compiler. cobc -x
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. FactC.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
       77 I PIC 9(8).
       77 F PIC 9(8) VALUE 1.
       77 N PIC 9(8).
       77 P PIC Z(7)9.

       PROCEDURE DIVISION.

       MAIN-PROCEDURE.

       MAIN-PARA.
           DISPLAY "ENTER ANY NUMBER".
           ACCEPT N.
           MOVE FACTORIAL(N) TO F.
           MOVE F TO P.
           DISPLAY "FACTORIAL OF GIVEN NUMBER IS" P.
           STOP RUN.

       END PROGRAM FactC.
