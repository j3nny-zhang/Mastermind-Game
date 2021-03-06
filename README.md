# Mastermind-Game
As a beginner in coding, I've decided to teach myself Python through small projects, hopefully learning the fundamentals of the language on the way.<br/><br/>
**But why choose Python as my language of choice?** <br/>
Well, I've always had in interest in Machine Learning and AI (which primarly uses Python as it focuses on Data Science), and it is in general a widely used language by some of the biggest companies to date. Furthermore, I believe that by understanding the logic behind script languages, I will be able to easily adapt to other programming languages as well.<br/><br/>
**My Mastermind-Game project plan**<br/>
My aim is to create several "attempts" of the game, each time tweaking the game until it properly functions as it should (according to the rules); however, I am not to directly search "how to create Mastermind in Python". Afterthat, I would like to delve into Pygame so that I can add graphics (essentially creating a GUI). 

## Attempt One - Updated October 17, 2020
**The rules of the game**<br/>
* a random list of 4 numbers is generated by the game (ranNum)
* the user inputs a guess of what those 4 numbers are, in the correct order (userList)
* the "O counter" adds a point for every correct value at the correct index of ranNum
* the "X counter" adds a point for every correct value, given that it is not in the same index as ranNum <br/>

Given these rules, I knew I would have to learn some of the most fundamental components of Python, namely functions, if statements, and loops. Going in, I had a mild understanding of functions and if statements, but my knowledge stopped there. <br/><br/>

**Looking at my first code:**<br/>
With some knowledge from my Python-Game tests (another repository), I knew that I had to import the library "random" so that my variable ranNum could generate the list of 4 numbers. 

![Generating ranNum](https://github.com/j3nny-zhang/Mastermind-Game/blob/main/images/generating_ranNum.png)

As shown in the image, I learned about for loops and ranges so that ranNum could generate the random list. Further on in the code, I also learned about the while loop to continue the game, as long as ranNum != userList (ie. the user has not correctly guessed the random list). <br/><br/>

**What I've learned in my first attempt**
* for loops
* while loops
* differentiating between list indices/indexes and values

**What I want to modify for my next attempt** <br/>
- [ ] Identify when the user does not enter an integer number, or enters a numbers outside the range of 1-6
- [ ] Simplify the O counter (it is currently made of 4 if statements)<br/>
![O_counter](https://github.com/j3nny-zhang/Mastermind-Game/blob/main/images/O_counter.png)
- [ ] get X counter working (right now it adds a point each time there is a duplicated number - for instance, if ranNum is 1 2 3 4 and userList is 3 3 6 3, as both lists contain a 3, I want the X counter to go up by one; however, it currently goes up by 3 as there are three 3s.)<br/>
![X_counter](https://github.com/j3nny-zhang/Mastermind-Game/blob/main/images/X_counter.png)
