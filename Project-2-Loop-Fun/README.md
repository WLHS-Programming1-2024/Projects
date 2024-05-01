# Loop Fun
Loops programming project

The purpose of this assignment is to get some experience working with repetition structures (loops).

## Details

This program will allow you to get some practice using repetition structures (for and while loops).  It will consist of 4 parts.

Part 1 - Get two integer values (a box height and width) from the user.
- The box height should be between between 3 and 10 (inclusive).  If the user enters a number that is out of bounds (less than 3 or greater than 10), continue to prompt them until they enter an appropriate number (use a while loop).
- The box width should be greater than the height, but no larger than 20. If the user enters a number that is out of bounds (<= the box height or greater than 20), continue to prompt them until they enter an appropriate number (use a while loop).

Part 2 - Use a for loop to print out all the numbers (on one line, space delimited) between the 
height and width (inclusive), and then print the average (mean) of those numbers.  

Part 3 - Print a hollow box made of * as shown in the example below. (this could require multiple
loops or one loop and use of some formatting functions). The width and height of the box should be the values entered by the user in part 1.

Part 4 - Use nested loops to print out the triangular shape shown in the example below. The height will be the number entered for the box height.  The first row of the triangle is two asterisks, and each subsequent row should be two asterisks bigger than the previous row. (see example below)

## Sample Output

Output should look *exactly* like this output:

*Enter a box height(between 3 and 10): 2*

*That number is out of bounds: Try again: 5*

*Enter a box width between (6 and 20): 42*

*That number is out of bounds: Try again: 3*

*That number is out of bounds: Try again: 12* 

*The integers from 5 to 12 are:*

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; 5 6 7 8 9 10 11 12 

*and the average of those numbers is 8.5.*
```
************
*          *
*          *
*          *
************
```
```
**
****
******
********
**********
```

## Technical Details
As with all programs written in this course, maintainability is as important as functionality, so your code should be clear and easy to follow. Make sure it follows the class coding conventions, and double check your code against this checklist before submitting.
- PEP-8: [https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/) - use the VS Code extension

## Submitting
* Submit loop_fun.py in Google Classroom
