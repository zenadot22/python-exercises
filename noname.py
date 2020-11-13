#What is the output of the following code snippets:

class Dog:
 2     def walk(self):
 3          return "*walking*"
 4
 5     def speak(self):
 6          return "Woof!"
 7 
 8  class JackRussellTerrier(Dog):
 9      def speak(self):
10         return "Arff!"
11 
12 bobo = JackRussellTerrier()
13 bobo.walk()