
**_Insertion sort _**

**is a sorting algorithm that places an unsorted element at its suitable place in each iteration. Insertion sort works similarly as we sort cards in our hand in a card game. We assume that the first card is already sorted then, we select an unsorted card**

## To trace the array [8, 4, 23, 42, 16, 15] using the Insertion Sort algorithm, I will follow these steps:

- Initialize the sorted array: sorted = []

1. Iteration 1:

Insert 8 into sorted, Since sorted is empty, append 8 to it 
Updated sorted: [8]

2. Iteration 2:

Insert 4 into sorted, Compare 4 with 8 in sorted and find that 4 is smaller. Insert 4 before 8
Updated sorted: [4, 8]

3. Iteration 3:

Insert 23 into sorted, Compare 23 with 8 in sorted and find that 23 is greater. Move on to the next element, Compare 23 with 4 and find that 23 is greater. Insert 23 after 4 and before 8
Updated sorted: [4, 8, 23]

4. Iteration 4:

Insert 42 into sorted, Compare 42 with 23 in sorted and find that 42 is greater , Move on to the next element Compare 42 with 8 and find that 42 is greater, Move on to the next element, Compare 42 with 4 and find that 42 is greater. Insert 42 after 4, 8, and 23
Updated sorted: [4, 8, 23, 42]

5. Iteration 5:

Insert 16 into sorted, Compare 16 with 42 in sorted and find that 16 is smaller. Move on to the next element. Compare 16 with 23 and find that 16 is smaller. Move on to the next element. Compare 16 with 8 and find that 16 is greater. Insert 16 after 8 and before 23.
Updated sorted: [4, 8, 16, 23, 42]

6. Iteration 6:

Insert 15 into sorted, Compare 15 with 42 in sorted and find that 15 is smaller, Move on to the next element Compare 15 with 23 and find that 15 is smaller, Move on to the next element Compare 15 with 16 and find that 15 is smaller then Move on to the next element will Compare 15 with 8 and find that 15 is greater. Insert 15 after 8 and before 16

Updated sorted: [4, 8, 15, 16, 23, 42]
After going through all iterations and comparing the elements with the existing elements in the sorted array, the final sorted array is [4, 8, 15, 16, 23, 42].

The Insertion Sort algorithm creates a sorted array by inserting elements one by one into their correct positions. It uses the Insert function to determine where each element should be placed within the sorted array.
