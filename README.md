# Uninformed-Search-using-Python
This repository contains Python implementations of two classic problems in artificial intelligence, namely "The wolf, the cabbage and the goat" and "Missionaries and Cannibals", solved using uninformed search algorithms. <br>
<h1>The wolf, the cabbage and the goat</h1> <br>
A farmer with his wolf, goat, and cabbage come to the edge of a river they wish to cross. 
There is a boat at the river's edge, but, of course, only the farmer can row. The boat can carry a maximum of the farmer and one other animal/vegetable. If the wolf is ever left alone with the goat, the wolf will eat the goat. Similarly, if the goat is left alone with the cabbage, the goat will eat the cabbage. Devise a sequence of crossings of the river so that all four of them arrive safely on the other side of the river. <br>
Formalization of WCG problem: <br>
State Space: tuple (wl, cl, gl, m, wr, cr, gr) with 0 ≤ wl, cl, gl, m,  wr, cr, gr ≤ 1 <br>
Initial State: (1, 1, 1, ‘STANGA’, 0, 0, 0) <br>
Successor Function(Actions): from each state, we can move across the man with the goat, the man with the cabbage or the man with the wolf. Note that not all states are legal. State
 (1, 0, 1, 1, 0, 0) is illegal. <br>
Goal State: (0, 0, 0, ‘DREAPTA’, 1, 1, 1) <br>
Path Costs: each action as a cost of 1 <br> <br>
Missionaries and Cannibals <br>
Three missionaries and three cannibals are on one side of a river that they wish to cross.  A boat is available that can hold at most two people and at least one. You must never leave a group of missionaries outnumbered by cannibals on the same bank. <br>
State Space: tuple(cl, ml, boat, cr, mr)<br>
Initial state: (3, 3, ‘STANGA’, 0, 0)<br>
Actions: from each state, we can move across two cannibals, a cannibal and a missionary or two missionaries. Note that not all states are legal. <br>
Goal:(0, 0, ‘DREAPTA’, 3, 3)
