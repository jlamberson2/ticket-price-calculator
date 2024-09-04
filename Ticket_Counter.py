#Ticket Counter
#A basic ticket counter program for Forrest
import sys

#importing tkinter for GUI
import tkinter
from tkinter import *
import tkinter.messagebox
from decimal import Decimal

#import for checking if a file exists in current directory
import os


#main execution of the program
def main():
    print("In progess...")


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

    #Function definition for the change button
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
        file_name = "tickets sold.txt" #current working filename for saved transactions
        #get current directory
        current_directory = os.getcwd()

        file_location = current_directory + '\\' + file_name

        #used to check if the file exists, if it doesnt, create it
        #if it does, append it
        if os.path.exists(file_location):
            previous_file = open(file_name, 'r')

            #Get the previous tickets from the file
            current_line = previous_file.readline()
            student_tickets = gui.get_tickets(current_line)

            current_line = previous_file.readline()
            alumni_tickets = gui.get_tickets(current_line)

            current_line = previous_file.readline()
            general_tickets = gui.get_tickets(current_line)

            previous_file.close()


            #Saves the data to the file
            current_file = open(file_name, 'w')
            #Gets the inputs from the user
            try:
                student_tickets += int(self.student_ticket_input.get(1.0, 'end-1c'))
                alumni_tickets += int(self.alumni_ticket_input.get(1.0, 'end-1c'))
                general_tickets += int(self.general_ticket_input.get(1.0, 'end-1c'))
            except ValueError:
                tkinter.messagebox.showerror("Error", "There must be an input for all ticket fields")

            #writing to the file
            current_file.write(str(student_tickets) + " Student tickets\n")
            current_file.write(str(alumni_tickets) + " Alumni tickets\n")
            current_file.write(str(general_tickets) + " General tickets\n")

            current_file.close()
        else:
            current_file = open(file_name, 'x')
            #Gets the inputs from the user
            try:
                self.student_tickets = int(self.student_ticket_input.get(1.0, 'end-1c'))
                self.alumni_tickets = int(self.alumni_ticket_input.get(1.0, 'end-1c'))
                self.general_tickets = int(self.general_ticket_input.get(1.0, 'end-1c'))
            except ValueError:
                tkinter.messagebox.showerror("Error", "There must be an input for all ticket fields")

            #writing to the file
            current_file.write(str(self.student_tickets) + " Student tickets\n")
            current_file.write(str(self.alumni_tickets) + " Alumni tickets\n")
            current_file.write(str(self.general_tickets) + " General tickets\n")

            current_file.close()

#takes in a line from the saved data file and gets the number of tickets from it
    def get_tickets(read_line):
        #takes the first character of the line
        current_char = read_line[0]

        #empty list to append to
        number_list = []
        counter = 0

        #takes only characters from the line up to the space
        #as it should only have numbers
        while(current_char != ' '):
            number_list.append(current_char)
            counter += 1
            current_char = read_line[counter]
        
        number = ''

        #convert the numbers into a singular string
        for i in number_list:
            number += i
        
        #convert the string into a number
        number = int(number)

        return number
    


#calling gui to be made
window = gui()