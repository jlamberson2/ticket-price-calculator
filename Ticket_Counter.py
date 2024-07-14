#Ticket Counter
#A basic ticket counter program for Forrest

#importing tkinter for GUI
import tkinter
from tkinter import *
import tkinter.messagebox
from decimal import Decimal


#main execution of the program
def main():
    print("In progess...")

#def make_change(total, paid):


#class for making/executing the gui
class gui:
    def __init__(self):

        #Ticket Prices
        self.student_ticket_price = 5
        self.alumni_ticket_price = 7
        self.general_ticket_price = 10

        #tickets sold for the customer
        self.student_tickets = 0
        self.alumni_tickets = 0
        self.general_tickets = 0

        #payment made
        self.payment = 0


        #creating main window
        self.main_window = tkinter.Tk()

        #frame levels for window
        self.ticket_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()

        #buttons for calculation actions
        self.calculate_button = tkinter.Button(self.button_frame, text="Calculate", command=self.calculate_change, width=15)
        self.quit_button = tkinter.Button(self.button_frame, text="Quit", command=self.main_window.destroy, width=15)
        self.recept_button = tkinter.Button(self.button_frame, text="Save Transaction", width=15, command=self.save_transaction)

        #input boxes for tickets
        self.student_ticket_input = Text(self.ticket_frame, height=1, width=10)
        self.alumni_ticket_input = Text(self.ticket_frame, height=1, width=10)
        self.general_ticket_input = Text(self.ticket_frame, height=1, width=10)
        self.payment_input = Text(self.ticket_frame, height=1, width=10)

        #labels for ticket inputs
        self.student_label = Label(self.ticket_frame, text="Student Tickets - $5.00")
        self.alumni_label = Label(self.ticket_frame, text="Alumni Tickets - $7.00")
        self.general_label = Label(self.ticket_frame, text="General Tickets - $10.00")
        self.payment_label = Label(self.ticket_frame, text="Total Payment: ")

        #packing the ticket frame
        self.student_label.grid(row=0, column=0, pady=2)
        self.student_ticket_input.grid(row=0, column=1, pady=2)

        self.alumni_label.grid(row=1, column=0, pady=2)
        self.alumni_ticket_input.grid(row=1, column=1, pady=2)

        self.general_label.grid(row=2, column=0, pady=2)
        self.general_ticket_input.grid(row=2, column=1, pady=2)

        self.payment_label.grid(row=3, column=0, pady=2)
        self.payment_input.grid(row=3, column=1, pady=2)

        #packing the buttons into the button frmae
        self.calculate_button.grid(row=0, column=0, pady=2)
        self.quit_button.grid(row=1, column=0, pady=2)
        self.recept_button.grid(row=2, column=0, pady=2)

        #packing the frames
        self.ticket_frame.grid(row=0, column=0, pady=2, padx=2)
        self.button_frame.grid(row=0, column=1, pady=2, padx=2)

        #Sets the title of the frame
        self.main_window.title("Ticket Calculator")

        #calling main loop
        self.main_window.mainloop()

    def calculate_change(self):
        #Gets the inputs from the user
        try:
            self.student_tickets = int(self.student_ticket_input.get(1.0, 'end-1c'))
            self.alumni_tickets = int(self.alumni_ticket_input.get(1.0, 'end-1c'))
            self.general_tickets = int(self.general_ticket_input.get(1.0, 'end-1c'))
            self.payment = Decimal(self.payment_input.get(1.0, 'end-1c'))
        except ValueError:
            tkinter.messagebox.showerror("Error", "Input must be a number for all fields")
        
        #calculates cost and payment
        cost = (self.student_tickets * self.student_ticket_price) + (self.alumni_tickets * self.alumni_ticket_price) + (self.general_tickets * self.general_ticket_price)
        change = self.payment - cost

        #shows message box with the change
        if(change >= 0):
            tkinter.messagebox.showinfo("Change", "Change: $" + str(change))
        else:
            tkinter.messagebox.showinfo("Error", "The cost of the tickets is greater than what was payed")
        

    def save_transaction(self):
        print("In progress")


#calling gui to be made
window = gui()