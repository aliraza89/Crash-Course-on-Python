#Expressions and Variables

#In this scenario, two friends are eating dinner at a restaurant. The bill comes in the amount of 47.28 dollars. The friends decide to split the bill evenly between them, after adding 15% tip for the service. Calculate the tip, the total amount to pay, and each friend's share, then output a message saying "Each person needs to pay: " followed by the resulting number.
>>> Tip = (47.28*(15/100))
>>> Total = (47.28)+(Tip)
>>> Each = (Total)/2
>>> print("Each person needs to pay:" + str(Each))
Each person needs to pay:27.186
  

#This code is supposed to take two numbers, divide one by another so that the result is equal to 1, and display the result on the screen. Unfortunately, there is an error in the code. Find the error and fix it, so that the output is correct.
>>> numerator = 10
>>> denominator = 10
>>> result = numerator / denominator
>>> print(result)
1.0


#Combine the variables to display the sentence "How do you like Python so far?" 
>>> word1 = "How"
>>> word2 = "do"
>>> word3 = "you"
>>> word4 = "like"
>>> word5 = "Python"
>>> word6 = "so"
>>> word7 = "far?"
>>> print(word1, word2, word3, word4, word5, word6, word7)
How do you like Python so far?


#This code is supposed to display "2 + 2 = 4" on the screen, but there is an error. Find the error in the code and fix it, so that the output is correct.
>>> print("2 + 2 = " + str(2+2))
2 + 2 = 4


#Functions

#This function converts miles to kilometers (km). Complete the function to return the result of the conversion. Call the function to convert the trip distance from miles to kilometers. Fill in the blank to print the result of the conversion. Calculate the round-trip in kilometers by doubling the result, and fill in the blank to print the result

