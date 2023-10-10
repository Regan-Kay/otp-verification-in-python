#import library
import math,random

#function to generate OTP
def generateOTP () :
	return random.randit (100000, 999999)
	
import random
import smtplib

def initialize():
  email = get_user_email()
  otp = generate_random_otp()
  send_mail(otp, email)
  print(f"Email has been sent to {email}")
  get_user_otp = input("Enter OTP code: ")
  if str(get_user_otp) == str(otp):
  	print("OTP Verification Successful")

  else:
  	print("OTP Verification Failed, Try again.")



def get_user_email():
	user_input = input("Welcome to OTP Verification System. \nEnter your email to recieve your One Time Verification Password: ")
	return str(user_input)


def generate_random_otp():
	return str(random.randint(100000, 999999))


def send_mail(otp, user_email):
 content = f"Your one time verification code is {otp}"
 mail = smtplib.SMTP('smtp.gmail.com', 587)
 mail.ehlo()
 mail.starttls()
 sender = "your email"
 recipient = f"{user_email}"
 mail.login(' ')
 header = "OTP Verification Code\n"
 content = header + content
 mail.sendmail(sender, recipient, content)
 mail.close()

initialize()