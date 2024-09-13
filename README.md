# optimal-rectangle-placement-algo

## Problem: 
Choose five rectangles of random width and height. Place the rectangles in the space of 100x100 units optimally so that the solution area is minimal 

## Rules: 
1. Rectangles cannot overlap and have a seperation of one unit.
2. 2. rectangles can be rotated.
3. No sorting of rectangles beforehand.
4. If placement is not possible then error should be generated.
5. Use python to code the problem.
6. Share your math plot results which show the rectangle (width and height) along with rotation if any and its placement.

Algorithm: 1. use Recursive Partitioning (Divide and Conquer) The space is divided into smaller regions, and each subregion is recursively divided again until you find an appropriate place for each rectangle. Your code should work by splitting the available space into two parts and placing rectangles within those parts.
