# Writing tests

In the previous notebook you became familiar with the assert statement. 
Assert statements are a way of quickly checking if a certain snippet of code returns the expected output. 

Sometimes, you want to be able to quickly run a script to check if your code is working correctly. In such cases you will want to create some kind of test file. You have probably noticed that the PAs often have a `.py` file with some tests in it. We will flip the switch in this notebook. We have provided you with a corrected and updated version of the function `max_even_square` from last week. Now write a test for it!

It is helpful to read the book chapter on testing before attempting this notebook!

<div style="background-color:#AABAB2; color: black; width:95%; vertical-align: middle; padding:15px; margin: 10px; border-radius: 10px">
<p>

**Task 1:**
  
Create a test for the code below.
The test should:

- nothing happens if you pass a valid list with at least one even number in the function
- return an error when a list without any even numbers, such as `[1, 3, 5]`, are passed into the function
- return an error when when non-list objects, such as `'apple'`, are passed into the function
- return an error when lists with non-integer values, such as `[1, 3, 'apple']` are passed into the function
- retunr an error if an empty list is passed into the function

Make sure your test in the cell is underneath the code for the function `max_even_squared` and that your whole test is in this cell. 

</p>
</div>