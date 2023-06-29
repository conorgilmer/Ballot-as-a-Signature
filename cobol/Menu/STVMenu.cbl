      ******************************************************************
      * Author:
      * Date:
      * Purpose:
      * Tectonics: cobc
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. STVMenu.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
       01 WS-WORKING-STORAGE.
           05 WS-USER-RESPONSE       PIC X.
           05 ARE-THERE-MORE-RECORDS PIC XXX VALUE 'YES'.

       PROCEDURE DIVISION.

       0100-MAIN.
           DISPLAY "MAIN".
           PERFORM 0200-MENU.
       0100-EXIT.
      *
      *
       0200-MENU.
       DISPLAY " ".
       DISPLAY "================================= "
       DISPLAY " STV Permutation Tools            ".
       DISPLAY " ".
       DISPLAY " 1 Permutations nPr".
       DISPLAY " 2 Generate Vote ".
       DISPLAY " 3 List Generated Votes   ".
       DISPLAY " 0 QUIT".
       DISPLAY " ".
       DISPLAY " Select Option".
       DISPLAY " ".
       DISPLAY "================================= "
       DISPLAY " ".
       ACCEPT WS-USER-RESPONSE
       IF WS-USER-RESPONSE =1
             PERFORM 0300-PERMUTATIONS
       ELSE IF WS-USER-RESPONSE =2
             PERFORM 0400-GENERATE-VOTE
       ELSE IF WS-USER-RESPONSE =3
             PERFORM 0500-LIST-VOTES
       ELSE IF WS-USER-RESPONSE =0
            PERFORM 0900-QUIT
       ELSE PERFORM 0900-QUIT.
       0200-END.

       0300-PERMUTATIONS.
           DISPLAY "Calculating...Permutations"
           CALL 'SubSTVPermnPr'
           PERFORM 0200-MENU.
       0300-EXIT.

       0400-GENERATE-VOTE.
           DISPLAY "GENERATE VOTE."
           CALL 'SubSTVGenVote'
           PERFORM 0200-MENU.
       0400-EXIT.

       0500-LIST-VOTES.
           DISPLAY "List Votes"
           CALL 'SubSTVListVotes'
           PERFORM 0200-MENU.
       0500-EXIT.

       0900-QUIT.
       DISPLAY "================================= "
       DISPLAY "       QUITTING PROGRAM           ".
       DISPLAY "================================= "
       STOP RUN.
