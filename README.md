# Generating all permutations

Now that you understand recursion you can use this idea together with what you have learned in the previous tasks to generate all the permutations of a list of `n` distinguishable objects.  Your task in this exercise is thus to complete the function called permutations in the cell on the left.   This function takes a single natural number, `n`, in input.  It should return a list of all possible permutations of the set of natural numbers that are less than or equal to `n`.   (recall that 0 is not a natural number).  For example, if `n=3` then permutations should return. 

````
[ [3,1,2], [1,3,2], [1,2,3], [3,2,1], [2,3,1] , [2,1,3] ]
````

Notice that I have used a recursive call to permutations within the function to generate all the distinct lists of symbols for `n-1`.

___

## A couple of notes on this exercise

The code we have written to generate all the permutations is rather slow.  There are certainly faster algorithms for completing this task out there, which you should use if you need to generate permutations in a project.  The reason we are doing it this way here is to illustrate the proof that was explained in the video.

Notice also that you do not need to use recursion to complete this task.  You can write the code to generate all the permutations using a for loop instead.  When I was designing this exercise, however, I felt that the code was easier to understand if recursion was used.  You do need recursion to write some algorithms so it is useful to know about.  I apologise if adding this in here has caused confusion, however.
