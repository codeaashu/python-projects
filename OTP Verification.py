# Importing the libraries
import twilio.rest
import random
from future.moves import tkinter
from tkinter import messagebox

# Creating Window
root = tkinter.Tk()
root.title("OTP Verification")
root.geometry("600x550")

# Twilio account details
account_sid = ""
auth_token = ""


# resend the OTP
def resendOTP():
    n = random.randint(1000, 9999)
    client = twilio.rest.Client(account_sid, auth_token)
    client.messages.create(to=[""], from_=" ", body=n)


# Checking the OTP
def checkOTP():
    global n
    try:
        user_input = int(user.get(1.0, "end01c"))
        if user_input == n:
            messagebox.showinfo("showinfo", "Login Success")
            n = "done"
        elif n == "done":
            messagebox.showinfo("showinfo", "Already entered")
        else:
            messagebox.showinfo("showinfo", "wrong OTP")
    except:
        messagebox.showinfo("showinfo", "Invalid OTP")


# Drawing the canvas
c = tkinter.Canvas(root, bg="white", width=400, height=300)
c.place(x=100, y=60)

# Label widget
login = tkinter.Label(root, text="OTP Verification", font="bold,20", bg="white")
login.place(x=210, y=90)

# Entry widget
user = tkinter.Text(root, borderwidth=2, wrap="word", width=29, height=2)
user.place(x=190, y=160)

# Sending the otp
n = random.randint(1000, 9999)
client = twilio.rest.Client(account_sid, auth_token)
client.messages.create(to=[""], from_="", body=n)

# Submit button
submit_button = tkinter.Button(root, text="Submit", command=checkOTP(), font=('bold', 15))
submit_button.place(x=258, y=250)

# Resend Button
resend_button = tkinter.Button(root, text="Resend OTP", command=resendOTP(), font=("bold", 15))
resend_button.place(x=240, y=400)

# Event Loop
root.mainloop()