# ASCII trees

## 1. My very own tree!
   Make a program that prints a pine tree

   * Desired output:
     ```
         #
        ###
       #####
      #######
     #########
         #
     ```

## 2. A forrest?
   Modify the previous program to allow the user specify the 
   number of layers (`n`) and the number of trees (`m`) from
   the standard input (`stdin`).

   Make sure `n` and `m` are valid **numbers** and are greater than 0.

   There is a single space between the trees.

   * Desired output for `n = 3` and `m = 1`:
     ```
       #
      ###
     #####
       #
     ```

   * Desired output for `n = 7` and `m = 3`:
     ```
           #             #             #
          ###           ###           ###
         #####         #####         #####
        #######       #######       #######
       #########     #########     #########
      ###########   ###########   ###########
     ############# ############# #############
           #             #             #
     ```

## 3. A new way to grow trees
   Modify the previous program to also allow the user to specify `n` and `m`
   as command line arguments (use `sys.argv`).  
   * If the user specifies no arguments, the program should behave as described
     in the previous assignment.

   * If the user specifies 1 argument, the program should fail (exit with
     non-zero value).

   * If the user specifies 2 arguments, both of which are valid values for `n`
     and `m`, the program should **NOT** ask for input from `stdin` and
     should use the arguments for `n` and `m` respectively. Any input prompt
     should **NOT** be present in the output.

   * If the user specifies 2 arguments and more than 1 is not a valid value for
     `n` or `m` then the program should fail (exit with non-zero value)

   * If the user specifies more than 2 arguments then the program should also
     fail.

## 4. Let's make a difference!
   Modify the previous program to print each tree using a different character.

   The characters can be hardcoded in the source file. If `m > len(chars)` the
   characters should 'loop'.
   
   * Desired output for `n = 7`, `m = 5` and `chars = ['A', 'B', 'C']`:
     ```
           A             B             C             A             B
          AAA           BBB           CCC           AAA           BBB
         AAAAA         BBBBB         CCCCC         AAAAA         BBBBB
        AAAAAAA       BBBBBBB       CCCCCCC       AAAAAAA       BBBBBBB
       AAAAAAAAA     BBBBBBBBB     CCCCCCCCC     AAAAAAAAA     BBBBBBBBB
      AAAAAAAAAAA   BBBBBBBBBBB   CCCCCCCCCCC   AAAAAAAAAAA   BBBBBBBBBBB
     AAAAAAAAAAAAA BBBBBBBBBBBBB CCCCCCCCCCCCC AAAAAAAAAAAAA BBBBBBBBBBBBB
           A             B             C             A             B
     ```

   * Desired output for `n = 5`, `m = 6` and `chars = ['#', '%']`:
     ```
         #         %         #         %         #         %
        ###       %%%       ###       %%%       ###       %%%
       #####     %%%%%     #####     %%%%%     #####     %%%%%
      #######   %%%%%%%   #######   %%%%%%%   #######   %%%%%%%
     ######### %%%%%%%%% ######### %%%%%%%%% ######### %%%%%%%%%
         #         %         #         %         #         %
     ```
