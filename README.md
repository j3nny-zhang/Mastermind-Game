# Mastermind-Game
As a beginner in coding, I've decided to teach myself Python through small projects, hopefully learning the fundamentals of the language on the way.<br/><br/>
**But why choose Python as my language of choice?** <br/>
Well, I've always had in interest in Machine Learning and AI (which primarly uses Python as it focuses on Data Science), and it is in general a widely used language by some of the biggest companies to date. Furthermore, I believe that by understanding the logic behind script languages, I will be able to easily adapt to other programming languages as well.<br/><br/>
**My Mastermind-Game project plan**<br/>
My aim is to create several "attempts" of the game per week, each time tweaking the game until it properly functions as it should (according to the rules); however, I am not to directly search "how to create Mastermind in Python". Afterthat, I would like to delve into Pygame so that I can add graphics (essentially creating a GUI). 

## Attempt One - Updated October 17, 2020
**The rules of the game**<br/>
* a random list of 4 numbers is generated by the game (ranNum)
* the user inputs a guess of what those 4 numbers are, in the correct order (userList)
* the "O counter" adds a point for every correct value at the correct index of ranNum
* the "X counter" adds a point for every correct value, given that it is not in the same index as ranNum <br/>

Given these rules, I knew I would have to learn some of the most fundamental components of Python, namely functions, if statements, and loops. Going in, I had a mild understanding of functions and if statements, but my knowledge stopped there. <br/><br/>

**Looking at my first code:**<br/>
With some knowledge from my Python-Game tests (another repository), I knew that I had to import the library "random" so that my variable ranNum could generate the list of 4 numbers. 

![Generating ranNum](⁨Macintosh HD⁩/⁨Users⁩/jennyzhang/documents/Coding/Mastermind/generating_ranNum.PNG?raw=true "Generating ranNum")
