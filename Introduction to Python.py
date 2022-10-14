#Fill in the correct Python command to put “My first Python program” onto the screen.
>>> print("My first Python program")
My first Python program


#Convert this Bash command into Python: 
echo Have a nice day
======================================
>>> print("Have a nice day")
Have a nice day


#Fill in the correct Python commands to put “This is fun!” onto the screen 5 times. 
>>> for i in range(5):
...     print("This is fun!")
...
This is fun!
This is fun!
This is fun!
This is fun!
This is fun!


#Select the Python code snippet that corresponds to the following Javascript snippet:
for (let i = 0; i < 10; i++) {
        console.log(i);
    }
===============================
for i in range(10):
  print(i)


#Output a message that says "Programming in Python is fun!" to the screen.
>>> print("Programming in Python is fun!")
Programming in Python is fun!


#Replace the ___ placeholder and calculate the Golden ratio: 1 + √ 5 / 2. 
#Tip: to calculate the square root of a number xx, you can use x**(1/2).
>>> ratio = (1+5**(1/2))/2
>>> print (ratio)
1.618033988749895


#Write a Python script that outputs "Automating with Python is fun!" to the screen.
>>> print("Automating with Python is fun!")
Automating with Python is fun!


#Fill in the blanks so that the code prints "Yellow is the color of sunshine".
>>> color = "Yellow"
>>> thing = "sunshine"
>>> print(color + " is the color of " + thing)
Yellow is the color of sunshine


#Keeping in mind there are 86400 seconds per day, write a program that calculates how many seconds there are in a week, if a week is 7 days. 
#Print the result on the screen.
>>> print(86400*7)
604800


#Use Python to calculate how many different passwords can be formed with 6 lower case English letters. 
#For a 1 letter password, there would be 26 possibilities.  
#For a 2 letter password, each letter is independent of the other, so there would be 26 times 26 possibilities.  
#Using this information, print the amount of possible passwords that can be formed with 6 letters.
>>> p = 26
>>> total = p**6
>>> print(total)
308915776


#Most hard drives are divided into sectors of 512 bytes each. 
#Our disk has a size of 16 GB. 
#Fill in the blank to calculate how many sectors the disk has. 
#Note: Your result should be in the format of just a number, not a sentence.
>>> disk_size = 16*1024*1024*1024
>>> sector_size = 512
>>> sector_amount = (16*1024*1024*1024)/512
>>> print(sector_amount)
33554432.0
