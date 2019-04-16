print ("Function to check whether a char is vowel or not")
 
def vowelChecker (inputChar):
 if (inputChar == "a" or inputChar == "A" or
 inputChar == "e" or inputChar == "E" or
 inputChar == "i" or inputChar == "I" or
 inputChar == "o" or inputChar == "O" or
 inputChar == "u" or inputChar == "U"):
  return "True"
 else:
  return "False"
 
print ("Enter the string to check")
inputChar = input()
 
if vowelChecker(inputChar) == "True":
 print("The enterted character is Vowel")
else:
 print("The enterted character is not Vowel")