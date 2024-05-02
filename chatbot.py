import time
class Chatbot:  
     def __init__(self):
         self.user_name=None
         self.user_age=None
         self.user_job=None
         self.user_hobbies=None
         

     def greet(self):
         print("Hello I am Your Friendly Chatbot")
         time.sleep(1)
     
     def  get_user_info(self):
         self.user_name=input("What is Your Name?")
         print(f" Welcome ,{self.user_name}")
         time.sleep(1)

         self.user_age=int(input("How old are you?"))
         self.describe_age()
         time.sleep(1)

         self.user_job=input("What do you do for living?")
         self.describe_job()
         time.sleep(1)

         self.user_hobbies=input("What are your Hobbie?")
         time.sleep(1)
         print("Thanks for sharing your hobbies")
         time.sleep(1)
     
     def describe_age(self):
         if 18<=self.user_age<=25:
             print("Your in the prime of your youth")
         elif 26<=self.user_age<=40:
             print("You are mid of your life")
         elif self.user_age>40:
             print("You are very great exprience of your life")
         else:
             print("You are Tennage")

     def describe_job(self):
          print(f" {self.user_job}, it is your interesting proffesion")

     def remind_Lunch_Or_Dinner(self):
          response=input("Have You Had Your Lunch Or Dinner:(yes/no)").lower()
          if response=="yes":
               print("Great make sure to stay hydrated and take breake.")
          else:
               print("Take a break and have a nutricious meal..Your health is important")

        
def main():
    chatbot=Chatbot()
    chatbot.greet()
    chatbot.get_user_info()
    chatbot.remind_Lunch_Or_Dinner()
    
if __name__=="__main__":
         main()
    



