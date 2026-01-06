# This code will Utilize alphabet A-Z and
# numbers 0-9 and a minimum of one special
# characters to generate a password
import tkinter as tk
import random

def generate_password():

      answer1 = entry1.get()
      answer2 = entry2.get()
      answer3 = entry3.get()

      password = ""

      letterStore = []
      NumStore = []
      #print(random.randint(0,9))
      for x in range(int(answer1)):
            alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            number = random.randint(0,24)
            letter = alphabet[number]
            letterStore.append(letter)
#print(letterStore)
#alp= 
#this is the index function - skim textbook 
#print(alphabet)

      if answer2 == 1 :
            for x in range(2) :
                charCount = ["0", "1", "2", "3" "4", "5", "6", "7" "8", "9"]
                numberone = random.randint(0,9)
                numbertwo = charCount[numberone]
                NumStore.append(numbertwo)
                letterStore.append(numbertwo)
      else :
          charCount = ["0", "1", "2", "3" "4", "5", "6", "7" "8", "9"]
          numberone = random.randint(0,9)
          numbertwo = charCount[numberone]
          NumStore.append(numbertwo)
          letterStore.append(numbertwo)
#this is the index function - skim textbook 
#print(NumStore)

      if answer3 == 1 :
          specCharList = ['$','#','@','!']
          specChar1 = random.randint(0,3)
          specChar2 = specCharList[specChar1]
          letterStore.append(specChar2)
    
#password += str(letterStore)
      password = ''
      count = 0 
      for x in letterStore:
          password += x
#print(password)

      
      result_label.config(text=f'Your password is {password}\n')



window = tk.Tk()

window.title( "Password Generator")





intro_text = 'This program will generate a randomized password. \nPlease select a 1 if your answer is yes.\nPlease select a 0 if your answer is no.'
intro_label = tk.Label(text=intro_text, fg="black")
intro_label.pack(pady=10)
intro_label.pack(padx=5)

question_frame = tk.Frame(window)
question_frame.pack(pady=10)

tk.Label(question_frame, text="How many characters do you want? (please choose between 6-12", bg= "gray").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(question_frame)
entry1.grid(row=1, column=0, padx=5, pady=5)

tk.Label(question_frame, text='Do you want numbers?', bg= "gray").grid(row=2, column=0, padx=5, pady=5)
entry2 = tk.Entry(question_frame)
entry2.grid(row=3, column=0, padx=5, pady=5)

tk.Label(question_frame, text='Do you want special characters?', bg= "gray").grid(row=4, column=0, padx=5, pady=5)
entry3 = tk.Entry(question_frame)
entry3.grid(row=5, column=0, padx=5, pady=5)


#Why is it only displaying the third entry and not the other two?

generate_button = tk.Button(text='Generate Password',command=generate_password)
generate_button.pack(pady=10)

result_label = tk.Label(text='', bg="white", fg="black")
result_label.pack(pady=10)




#question_frame = tk.Frame()
#question_frame.pack(pady=10)

#question_one = tk.Label(text='How many characters do you want your password?', fg="black").grid(row=0, column=0, padx=5, pady=5)
#question_one.pack()

window.mainloop()


window.mainloop()

#can we do a return statement without it being a function?
#We want like a textbox to appear or something after the you press 'Generate Password' with the password

#print(str(password))

        
#numbers = input(int("does password need more than 1 number , yes or no"))
                #mak
                
# variable ( alp) that has a list of characters A-Z - Ghal


                
# if input is yes numbers will pick "1" number from range 0-9 , if no number will pick "2" numbers from range 0-9   
 
#ask user if password needs speacil charcaters 

#if input is yes ask user to enter "1" speacil charcater

# variable(specChar) that is set to equal any one of the following charcaters ( $ , # , @ , ! )
                # ellen & brit

# take stored information and generate a password based on conditions: ex - if numchar > 1 then: 

                





