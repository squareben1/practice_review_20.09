# Practice Review Kata

Quick, easy practice Kata in Python to prep for tomorrow's observed review. 

### Notes From Initial Requirements Gathering Session:
Features:

Sound wave taken in, check if any frequencies above or below thresholds

Remove them outside of: 
User supplied - provide defaults
limits: 40 lower 1000 upper 
Inputs supplied in arrays of frequencies 

Examples: 
10, 20
Array input [11, 12, 15, 20, 21] - output = exactly the same except last number 20 

[9, 10, 11] = [10, 10, 11]

Array takes 2 numbers and an array 
Outputs the array with any numbers outside of limit returned maximum or minimum limit 

Plan: 

Input / output 
[10, 11] > [10, 11]
[9, 10] > [10, 10]
[10, 21] > [10, 20]
