# final-project
Create your own compiler for a given language in the handout. 


here's a file structure for how it can look

    /dir
      Part1.program
      Part2.program
      Part3.program
      /resources
        finalv1.txt
        finalv2.txt (generated from Part1.program)
        finalv3.txt (generated from Part2.program)
      results.txt (generated from Part3.program)
      program.bat
  
and then we can create a batch file or shell script (whatever OS the Professor is running) to run the programs in sequence.

--

Example Batch file:
    
    g++ Part1.program && java Part2.program && python Part3.program

