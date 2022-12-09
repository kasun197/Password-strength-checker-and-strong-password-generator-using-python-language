import string
import random 
from myFirstApp import *
import sys

text = 0 



class FirstApp(Ui_MainWindow):
	def __init__(self, window):
		self.setupUi(window)
		self.checkNameBtn.clicked.connect(self.clickMe)
		
	def clickMe(self):
		global test
		text = self.nameTxt.text()
		
		
		#############
				# user entered password as a parameter to passwordStrength function 
		def pwsugster():
			chars = "abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*"
			pwlength = 11
			stpassword = ""
			for x in range (0,pwlength):
					password_char = random.choice(chars)
					stpassword = stpassword + password_char
			#print( "\n Use this as a Strong Password : ", stpassword)
			#print("\n")
			test1 = f"Use this as a strong password : {stpassword}"
			self.stpw.setText(test1)
			
			
		#to remove garbage values    
		passcode = 0
		#passcode = input(" Enter the new password : ")
		passcode = text

		#to remove garbage values
		lower_case = 0
		upper_case = 0
		number = 0
		special = 0
		length = 0
		digits = 0


		lower_case = any([1 if c in string.ascii_uppercase else 0 for c in text])
		upper_case = any([1 if c in string.ascii_lowercase else 0 for c in text])
		special = any([1 if c in string.punctuation else 0 for c in text])
		digits = any ([1 if c in string.digits else 0 for c in text])


		characters = [upper_case, lower_case, special, digits]

		 #Check password length
		length = len(passcode)

		score = 0

		#Open a common password file

		with open('common.txt','r') as f:
			common = f.read().splitlines()

		#If the password is in the common password file,     
		if passcode in common:
			print("\n password was found in a common list. Score: 0 / 14")
			self.mainoutput.setText("Password was found in a common list. Score: 0 / 14")
			pwsugster()
			#exit()

		if length > 5:
			score += 2
		if length > 7:
			score += 2
		if length > 9:
			score += 2
		if length > 10:
			score += 2
		# End of passwordStrength function 
		#print(f"\n password length is {str(length)}, adding {str(score)} points!")
		score1 = f"password length is {str(length)}, adding {str(score)} points!"
		#self.mainoutput.setText(score1)

		if sum(characters) > 1:
			score += 2
		if sum(characters) > 2:
			score += 2
		if sum(characters) > 3:
			score += 2

		#print (f" Password has {str(sum(characters))} different character types, adding {str(sum(characters) - 1)} points!")
		score2 = f"Password has {str(sum(characters))} different character types, adding {str(sum(characters) - 1)} points!"
		

		if score < 6:
			#print (f"\n the password is quite weak! Score: {str(score)} / 14")
			score3 =f"The password is quite weak! Score: {str(score)} / 14"
			fscore =f"{score1}\n{score2}\n{score3}"
			self.mainoutput.setText(fscore)
			pwsugster()
		elif score == 6:
			#print (f"\n the password is OK! Score: {str(score)} / 14")
			score3 =f"The password is OK! Score: {str(score)} / 14"
			fscore =f"{score1}\n{score2}\n{score3}"
			self.mainoutput.setText(fscore)
			pwsugster()
		elif 6 < score <= 10:
			#print (f"\n the password is pretty good! Score: {str(score)} / 14")
			score3 = f"The password is pretty good! Score: {str(score)} / 14"
			fscore =f"{score1}\n{score2}\n{score3}"
			self.mainoutput.setText(fscore)
		elif score > 10 :
			#print (f"\n the password is strong! Score: {str(score)} / 14")
			score3 = f"The password is strong! Score: {str(score)} / 14"
			fscore =f"{score1}\n{score2}\n{score3}"
			self.mainoutput.setText(fscore)

		
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = FirstApp(MainWindow)



MainWindow.show()
app.exec_()



	
