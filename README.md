# Depth First Search


Depth First Search Algorithm : 
A standard DFS implementation puts each vertex of the graph into one of two categories:

*   Visited
*   Not Visited

The purpose of the algorithm is to mark each vertex as visited while avoiding cycles.

The DFS algorithm works as follows:

* Start by putting any one of the graph's vertices on top of a stack.
* Take the top item of the stack and add it to the visited list.
* Create a list of that vertex's adjacent nodes. Add the ones which aren't in the visited list to the top of the stack.
* Keep repeating steps 2 and 3 until the stack is empty.

## Output:

![image](https://user-images.githubusercontent.com/73773202/156792626-43be357b-b940-46d7-9c6f-978c55c15665.png)



---
