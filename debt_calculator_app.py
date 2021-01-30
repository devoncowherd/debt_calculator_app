#Config
from tkinter import*
from PIL import ImageTk, Image


root = Tk()
root.title('Debt. Payment Calculator')

#Variables
count = 0
default = Label(root, text = 'Enter Your Type of Debt')
default.grid(column = 0, row = 3)
program_title  = Label(root, text = "Debt. Payment Calculator:")
program_title.grid(column = 0, row = 0)

e = Entry(root, width = 50)
e.grid(column = 0, row = 1)
e.focus()
user_input = 'default'
total_days = float(0)
total_weeks = float(0)
total_months = float(1)
enter_rate = float(0)
rate_fees = float(0)

#Functions
def restart():
    e.delete(0, END)
    if paid == True:
        show_final.grid_forget()
    if paid == False:
        never_paid.grid_forget()
    
    button_restart.grid_forget()
    default.grid(column = 0, row = 3)
    count = 0
 


def get_input():
    global enter_rate
    global total_days
    global total_weeks
    global total_months
    global enter_amount
    global enter_rent
    global enter_fees
    global enter_payment
    global debt_amount
    global total_debt
    global rent_fees
    global other_fees
    global rate_fees
    global count
    global debt_type
    global show_final
    global button_restart
    global default
    global paid
    global never_paid
   
    if count == 0:
        default.grid_forget()
        default = Label(root, text = 'Enter Your Type of Debt')
        default.grid(column = 0, row = 3)
    
    count += 1
    user_input = e.get()
   
    if count == 1:
        default.grid_forget()
        e.delete(0, END)
        debt_type = user_input
        enter_amount = Label(root, text = 'Enter Debt Amount (Numbers Only)')
        enter_amount.grid(column = 0, row =3)
    if count == 2:
        enter_amount.grid_forget()
        e.delete(0, END)
        debt_amount = user_input
        enter_rate =  Label(root, text = 'Enter Interest Rate (APR) in decimal (ex: 0.05 = 5%)')
        enter_rate.grid(column = 0, row  =3)
    if count == 3:
        enter_rate.grid_forget()
        e.delete(0 , END)
        rate_fees = user_input
        enter_rent = Label(root, text='Enter Rent Fees')
        enter_rent.grid(column = 0, row = 3)
    if count == 4:
        enter_rent.grid_forget()
        e.delete(0, END)
        rent_fees = user_input
        enter_fees = Label(root, text = 'Enter Total Amount Other Monthly Fees')
        enter_fees.grid(column = 0, row = 3)
    if count == 5:
        enter_fees.grid_forget()
        e.delete(0, END)
        other_fees = user_input
        enter_payment = Label(root, text = 'Enter Amount Deposited to Balance (Weekly)')
        enter_payment.grid(column = 0, row = 3)
    if count == 6:
        enter_payment.grid_forget()
        e.delete(0, END)
        deposit = float(user_input)
        total_debt = float(debt_amount) + float(rent_fees) +  float(other_fees)
        while total_debt >= deposit:
            total_debt = (float(total_debt) + float(total_debt) * float(rate_fees)) - float(deposit)
            total_days +=7
            total_weeks += 1
            total_months += 1/4
            if total_debt <= deposit:
                paid = True
                total_days = '{:.2f}'.format(total_days)
                total_weeks = '{:.2f}'.format(total_weeks)
                total_months = '{:.2f}'.format(total_months)
                final_statement = 'Your ' + str(debt_type) + ' will be paid off in \n' + 'Days: ' + str(total_days) + '\nWeeks: ' + str(total_weeks) + '\nMonths: ' + str(total_months)
                show_final = Label(root, text = final_statement)
                show_final.grid(column = 0, row = 3)
                button_restart.grid(column = 0, row = 4)
            if float(total_weeks) >= 5214:
                paid = False
                never_paid = Label(root, text = 'The Debt Will Never End! ;(')
                never_paid.grid(column = 0, row =3)
                button_restart.grid(column = 0, row = 4)
                break
        
    
#Buttons
button_restart = Button(root, text = 'Restart', command = restart)
button_one = Button(root, text = "Submit", command = get_input)
e.bind("<Return>",get_input)
button_one.grid(column = 0, row = 2)
e.bind('<Return>', lambda event: get_input())



#Main Loop
root.mainloop()
