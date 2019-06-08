# Python Internship Task - 0/1 Knapsack Problem

#### Dynamic Programming

## General info:

The function takes 2 arguments `usb_size` and `memes` each with a size and a price.

General task was to write a Python function which calculates the best set of memes which can be sold for the highest price.
This is an example of a knapsack problem. In this our problem, we are given a set of items (memes) and backpack (USB stick) 
capacity. Each item has it's value and weight. The task is to find a collection of memes that the total weight does not 
exceed capacity of the USB stick and the total value (price) is maximized.

Problem has been solved using dynamic programming with bottom-up method. 
The function generates an array where the maximum value that can be optained is stored.
Then we choose the elements that will fit in the USB stick and for which the sum of the memes values will be the highest. 
Next, our function returns a tuple with the first element being a total value of all memes on the USB stick, and the
second being a set of names of the memes that should be copied onto the USB.

## Setup:

```
clone the repository
pip install -r requirements.txt
```
