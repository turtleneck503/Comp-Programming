# Instructions  
Yondu Udonta and his crew of space pirates arrive at the Iron Lotus after several weeks of plundering the high seas. Since the crew has been in space for nearly six months, they are ready for a night of celebration. 

Yondu doesn’t want to divvy up the plunder just yet, so he gives each crew member other than himself and Peter Quill 3 units and sends them off to the Iron Lotus. After the crew has gone, he and Peter count what’s left and decide how to split it up among the crew. 

Yondu takes 13% plunder, which he transfers to a hidden bank account. Yondu gives Peter 11% of the remaining units, which Peter transfers to his account. The next morning, the remaining units are divided evenly among all of the crew, including Yondu and Quill. Little do they know that Yondu and Quill have already taken a cut. If the remaining treasure can’t be split evenly, the units left over are given to the Reaver’s Benevolent Fund (RBF).

The problem is to compute how many units each person gets and how how much goes to the RBF. A unit cannot be split, so if some calculation yields a number that contains a fractional part, you can only give that person the integer part of the value. 

For example, if your program computed the captain’s share as 25.67 units, you could only give him 25 units, not 25.67 units. Warning: Always round down, NOT up. Simply drop the fractional part, but don’t lose any units from the overall total amount.

Do not count the 3 coins each crew took into town as part of their total share, since they already spent them. Of course, you have to count those coins when you check your totals for correctness versus the total.

  ## Steps
  1. Get two numbers as `input()` from the user - how many pirates are on the ship (including Yondu and Quill), and how many units (coins) the Reavers came into port with.
  2. `print()` Yondu's share
  3. `print()` Peter's share
  4. `print()` the Crew's share
  5. `print()` the leftover shares in the RBF

## Example
```
How many Reavers:
20
How many units:
1000
Yondu's share: 158
Peter's share: 126
Crew: 36
RBF: 14
```

## FAQ

**Q: What does it mean to round down instead of rounding up?**

A: When you do division or multiply by a percentage, you get a floating point number. Rounding down means you drop the fractional part and just keep the whole number. Since galactic units are whole numbers, you’ll get incorrect amounts if you don’t use integer arithmetic properly.

**Q: When I add up all the amounts from the example, the total doesn’t add up to 2000. What’s wrong?**

A: Well, did you correctly compute shore leave money? Yondu and Peter don’t get any. Yondu’s and Peter’s total amount DO include crew share, though, so don’t double count them in the total.

**Q: Why should I care about integer arithmetic in my code?**

A: Most real numbers (floating point numbers) can’t be stored exactly in a computer in decimal form; they have to be approximated. This can sometimes lead to inaccurate or strange, inconsistent results, depending on what problem is being solved and how much precision you need. This isn’t a "Python Problem", it’s a more general problem with computers. For many problems, this is not an issue, but we want you to be aware of it.