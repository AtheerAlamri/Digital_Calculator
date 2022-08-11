from tkinter import *


# Main class for calculator
class Application(Frame):
    # Initialise the Frame
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.task = ""
        self.UserIn = StringVar()
        self.grid()
        self.create_widgets()

    # Create all the buttons for calculator
    def create_widgets(self):
        # User input stored as an Entry widget.
        self.user_input = Entry(self, bg="#cdd4d3", bd=29, insertwidth=4, width=24, font=("Verdana", 20, "bold"),
                                textvariable=self.UserIn, justify=RIGHT)
        self.user_input.grid(columnspan=4)

        self.user_input.insert(0, "0")

        # Button for value 7
        self.button1 = Button(self, bg="#a1afb5", bd=12, text="7", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.button_click(7))
        self.button1.grid(row=2, column=0, sticky=W)
        # Button for value 8
        self.button2 = Button(self, bg="#a1afb5", bd=12, text="8", padx=35, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.button_click(8))
        self.button2.grid(row=2, column=1, sticky=W)
        # Button for value 9
        self.button3 = Button(self, bg="#a1afb5", bd=12, text="9", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.button_click(9))
        self.button3.grid(row=2, column=2, sticky=W)
        # Button for value 4
        self.button4 = Button(self, bg="#a1afb5", bd=12, text="4", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.button_click(4))
        self.button4.grid(row=3, column=0, sticky=W)
        # Button for value 5
        self.button5 = Button(self, bg="#a1afb5", bd=12, text="5", padx=35, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.button_click(5))
        self.button5.grid(row=3, column=1, sticky=W)
        # Button for value 6
        self.button6 = Button(self, bg="#a1afb5", bd=12, text="6", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.button_click(6))
        self.button6.grid(row=3, column=2, sticky=W)
        # Button for value 1
        self.button7 = Button(self, bg="#a1afb5", bd=12, text="1", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.button_click(1))
        self.button7.grid(row=4, column=0, sticky=W)
        # Button for value 2
        self.button8 = Button(self, bg="#a1afb5", bd=12, text="2", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.button_click(2))
        self.button8.grid(row=4, column=1, sticky=W)
        # Button for value 3
        self.button9 = Button(self, bg="#a1afb5", bd=12, text="3", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.button_click(3))
        self.button9.grid(row=4, column=2, sticky=W)
        # Button for value 0
        self.button10 = Button(self, bg="#a1afb5", bd=12, text="0", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                               command=lambda: self.button_click(3))
        self.button10.grid(row=5, column=0, sticky=W)
        # Operator Buttons
        # Addition button
        self.addButton = Button(self, bg="#a1afb5", bd=12, text="+", padx=36, pady=25, font=("Helvetica", 20, "bold"),
                                command=lambda: self.button_click("+"))
        self.addButton.grid(row=2, column=3, sticky=W)
        # Subtraction button
        self.subButton = Button(self, bg="#a1afb5", bd=12, text="-", padx=39, pady=25, font=("Helvetica", 20, "bold"),
                                command=lambda: self.button_click("-"))
        self.subButton.grid(row=3, column=3, sticky=W)
        # Multiplication button
        self.mulButton = Button(self, bg="#a1afb5", bd=12, text="*", padx=38, pady=25, font=("Helvetica", 20, "bold"),
                                command=lambda: self.button_click("*"))
        self.mulButton.grid(row=4, column=3, sticky=W)
        # Division button
        self.divButton = Button(self, bg="#a1afb5", bd=12, text="/", padx=39, pady=25, font=("Helvetica", 20, "bold"),
                                command=lambda: self.button_click("/"))
        self.divButton.grid(row=5, column=3, sticky=W)
        # Equal button
        self.equalButton = Button(self, bg="#E6D72A", bd=12, text="=", padx=100, pady=25,
                                  font=("Helvetica", 20, "bold"), command=self.calculate_task)
        self.equalButton.grid(row=5, column=1, sticky=W, columnspan=2)
        # Clear button
        self.clearButton = Button(self, bg="#b75555", bd=12, text="AC", width=28, padx=7,
                                  font=("Helvetica", 20, "bold"),
                                  command=self.clear_display)
        self.clearButton.grid(row=1, sticky=W, columnspan=4)

    def button_click(self, number):
        self.task = str(self.task) + str(number)
        self.UserIn.set(self.task)

    def display_text(self, value):
        self.user_input.delete(0, END)
        self.user_input.insert(0, value)

    def calculate_task(self):
        self.data = self.user_input.get()
        try:
            self.answer = eval(self.data)
            self.display_text(self.answer)
            self.task = self.answer

        except SyntaxError as e:
            self.display_text("Invalid Syntax!")
            self.task = ""

    def clear_display(self):
        self.task = ""
        self.user_input.delete(0, END)
        self.user_input.insert(0, "0")


calculator = Tk()

calculator.title("Calculator")
app = Application(calculator)

calculator.resizable(width=False, height=False)

calculator.mainloop()
