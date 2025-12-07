# BinarySearchVisualizer
Binary Search Visualizer built with Python and Gradio




Decomposition
Binary search is divided into smaller tasks:
1.	Accept input list and target from the user.
2.	Validate and convert the list into integers; ensure it is sorted.
3.	Set low, high, and repeatedly calculate mid.
4.	Compare the middle value and decide to move left, move right, or return found.
5.	Record each step for display.
6.	Output all steps and a summary (found/not found).
________________________________________
Pattern Recognition
The algorithm repeats the same cycle:
•	Check the middle element.
•	If equal → stop.
•	If smaller → discard the right half.
•	If larger → discard the left half.
This repeated "halve the list and compare" pattern continues until the target is found or the interval is empty.
________________________________________
Abstraction
Shown to the user:
•	The list with the current middle element highlighted,
•	low, mid, high,
•	Plain-language explanation: move left / move right / found.
Hidden:
•	Python loops, index math, error handling, and internal data types.
The user sees the thinking of the algorithm, not the code details.
________________________________________
Algorithm Design (Input → Process → Output + GUI)
•	Input: Two text fields — a comma-separated list and a target number.
•	Processing: Validate input → binary search loop → build step-by-step trace.
•	Output: A textbox showing each step, and a summary result message.
•	GUI: Gradio handles input boxes, button click, and displaying the results.
