# Badges and Schedules

## Objectives

1. Define functions that use iteration and control the return values of those functions.
2. Define functions that call other functions.

## Instructions

In this lab you'll be learning how to iterate through a list and output the results in different ways. Write your code in the `conference_badges.py` file and you can run the test suite using the `learn` command.

You're hosting a conference and need to print badges for the speakers. Each badge should read: "Hello, my name is _____."

1. Write a `badge_maker` function that will create and return this message, given a person's name.
ex:

    ```python
    badge_maker("James")
    => "Hello, my name is James."
    ```

2. The list of speakers for your conference has been finalized. Your conference speakers are: Edsger, Ada, Charles, Alan, Grace, Linus, and Matz. How you scored these luminaries is beyond me, but way to go! Now you'll want to get their badges printed.

  * Write a `batch_badge_creator` function that takes a list of names as an argument and returns a list of badges (you can use your `badge_maker` function within this function if you want to start getting fancy).

3. You just realized that you also need to give each speaker a room assignment. Write a function called `assign_rooms` that takes the list of speakers and assigns each speaker to a room. Make sure that each room only has one speaker.
  * You have rooms 1-7.
  * return a list of room assignments in the form of: "Hello, _____! You'll be assigned to room _____!"
  *  *Hint*: Think about how you will assign a room number to each person. list items are indexed, meaning that you can access each element by its index number. Before opening a for loop, you may want to create a counter variable that increases each time the loop is run. An alternative is to use the [enumerate](https://docs.python.org/2/library/functions.html#enumerate) function.

Now you have to tell the printer what to print. Create a function called `printer` that will return one large string with the results of the `batch_badge_creator` function and the `assign_rooms` function.
  * *Hint*: Remember that functions can call other functions. If the return value of `assign_rooms` is a list of room assignments, how can you print out each assignment? You'll need to iterate over your list of room assignments in order to add each individual assignment to your final string.
  * *Hint:* Start with an empty string and keep adding to it by using the `+=` function.


