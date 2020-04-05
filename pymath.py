__author__ = "Essam Mohamed"


def about():
    tkinter.messagebox.showinfo("About", "I have been created by Essam Mohamed")


def mail():
    Mail()


def sys_ex():
    SysAcc()


def sp_equ_solver():
    SpecialSolver()


def equ_solver():
    EquationSolver()


def app():
    Application()


def how_to_use():
    info = """"/*/" means Prime test \n"//" means empty(required)\n "\/" means square root\n "//**//" means 'print prime
     numbers between a and b'\n 'sin' means sin(a)\n 'log10' means log(a) for base 10\n 'log' means log(a) for base (b)
     """
    tkinter.messagebox.showinfo("How to use", info)


class Application(object):

    """The main Application"""

    def __init__(self):
        self.root = Tk()
        self.root.title("PyMath")
        self.root.maxsize(600, 220)
        self.root.minsize(600, 220)
        self.menu_bar = Menu(self.root)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=app)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.destroy)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.go_to_menu = Menu(self.menu_bar, tearoff=0)
        self.go_to_menu.add_command(label="Equation solver", command=equ_solver)
        self.go_to_menu.add_command(label="Special equation", command=sp_equ_solver)
        self.menu_bar.add_cascade(label="GoTo", menu=self.go_to_menu)
        self.Spe_menu = Menu(self.menu_bar, tearoff=0)
        self.Spe_menu.add_command(label="MailSys", command=mail)
        self.Spe_menu.add_command(label="PySys", comman=sys_ex)
        self.menu_bar.add_cascade(label="Special services", menu=self.Spe_menu)
        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="About", command=about)
        self.help_menu.add_command(label="How to use", command=how_to_use)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.root.config(menu=self.menu_bar)
        self.greet = Label(self.root, fg="dark red", text="Hello...")
        self.greet.pack(padx=5, pady=5)
        self.first = Label(self.root, fg="dark green", text="First number is :")
        self.first.pack()
        self.first_num = Entry(self.root, width=100)
        self.first_num.pack()
        self.opp = Label(self.root, fg="dark green", text="Operator")
        self.opp.pack()
        self.opp = Entry(self.root, width=100)
        self.opp.pack()
        self.second = Label(self.root, fg="dark green", text="Second number is :")
        self.second.pack()
        self.second_num = Entry(self.root, width=100)
        self.second_num.pack()
        self.result = Label(self.root)
        self.result.pack()
        self.calc = Button(self.root, text="Calculate", bg="royal blue", fg="white", relief=FLAT)
        self.calc["command"] = self.calculate
        self.calc.pack(padx=5, pady=5)
        self.root.mainloop()

    def prime_tester(self, num):
        avg = list()
        for i in range(2, num):
            if (num % i) == 0:
                avg.append(0)
                break
            elif (num % i) != 0:
                avg.append(1)
        if 0 in avg:
            pass
        else:
            print(num, end="  ")
            self.result.configure(text=str(self.result["text"]))

    def calculate(self):

        try:
            a = self.first_num.get()
            b = self.second_num.get()
            o = self.opp.get()
            if o == "+":
                self.result.configure(text="The result is " + str(eval(a) + eval(b)))
            elif o == "-":
                self.result.configure(text="The result is " + str(eval(a) - eval(b)))
            elif o == "*":
                self.result.configure(text="The result is " + str(eval(a) * eval(b)))
            elif o == "/":
                try:
                    self.result.configure(text="The result is " + str(eval(a) / eval(b)))
                except ZeroDivisionError:
                    self.result.configure(text="Division by zero is not allowed")
            elif o == "^":
                self.result.configure(text="The result is " + str(eval(a) ** eval(b)))
            elif o == "\/":
                self.result.configure(text="The result is " + str(eval(a) ** 0.5))
            elif o == "/*/":

                """Successfully working"""
                args = list()
                for x in range(2, eval(a)):

                    if eval(a) % x == 0:
                        args.append(0)
                        break
                    else:
                        args.append(1)
                if 0 in args:
                    self.result.configure(text="The number you entered is not prime")
                else:
                    self.result.configure(text="The number you entered is prime")
            elif o == "//**//":
                for x in range(eval(a), eval(b)):
                    self.prime_tester(x)
                print()
            elif o == "sin":
                self.result.configure(text=math.sin((eval(a) / 180)*math.pi))
            elif o == "cos":
                self.result.configure(text=math.cos((eval(a) / 180)*math.pi))
            elif o == "tan":
                self.result.configure(text=math.tan((eval(a) / 180)*math.pi))
            elif o == "log10":
                self.result.configure(text=math.log10(eval(a)))
            elif o == "log":
                self.result.configure(text=math.log(eval(a), eval(b)))

        except ValueError:
            self.result.configure(text="Enter a valid value")


class EquationSolver(object):

    """Equation Solver"""

    def __init__(self):
        self.root = Tk()
        self.root.title("EquationSolver")
        self.root.maxsize(200, 100)
        self.root.minsize(200, 100)
        self.menu_bar = Menu(self.root)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=equ_solver)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.destroy)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.go_to_menu = Menu(self.menu_bar, tearoff=0)
        self.go_to_menu.add_command(label="Equation solver", command=equ_solver)
        self.go_to_menu.add_command(label="Special equations", command=sp_equ_solver)
        self.menu_bar.add_cascade(label="GoTo", menu=self.go_to_menu)
        self.Spe_menu = Menu(self.menu_bar, tearoff=0)
        self.Spe_menu.add_command(label="MailSys", command=mail)
        self.Spe_menu.add_command(label="PySys", comman=sys_ex)
        self.menu_bar.add_cascade(label="Special services", menu=self.Spe_menu)
        self.root.config(menu=self.menu_bar)
        self.first_form = Label(self.root, text="aX + y = 0", fg="dark red")
        self.first_form.grid(row=0, column=0, padx=5, pady=10)
        self.second_form = Label(self.root, text="aX^2 + bX + c = 0", fg="dark red")
        self.second_form.grid(row=0, column=1, padx=5, pady=10)
        self.first_choice = Button(self.root, bg="royal blue", text="Choose this", fg="white", relief=FLAT)
        self.first_choice["command"] = FirstEqu
        self.first_choice.grid(row=1, column=0, padx=5, pady=10)
        self.second_choice = Button(self.root, bg="royal blue", text="Choose this", fg="white", relief=FLAT)
        self.second_choice.grid(row=1, column=1, padx=30, pady=10)
        self.second_choice["command"] = SecondEqu
        self.root.mainloop()


class FirstEqu:
    def __init__(self):
        self.first_box = Tk()
        self.first_box.title("FirstDegree")
        self.first_box.maxsize(200, 150)
        self.first_box.minsize(200, 150)
        self.form = Label(self.first_box, text="aX + b = 0")
        self.form.grid(row=0, column=0)
        self.a = Label(self.first_box, text="a = ")
        self.a.grid(row=2, column=0)
        self.b = Label(self.first_box, text="b = ")
        self.b.grid(row=3, column=0)
        self.num_a = Entry(self.first_box)
        self.num_a.grid(row=2, column=1)
        self.num_b = Entry(self.first_box)
        self.num_b.grid(row=3, column=1)
        self.calc = Button(self.first_box, text="Solve", bg="royal blue", fg="white", command=self.solve, relief=FLAT)
        self.calc.grid(row=5, column=0, pady=5)
        self.results = Label(self.first_box)
        self.results.grid(row=6, column=0)
        self.first_box.mainloop()

    def solve(self):
        try:
            self.results.configure(text="X = " + str(-eval(self.num_b.get()) / eval(self.num_a.get())))
        except SyntaxError:
            self.results.configure(text="Please, Enter a valid value")


class SecondEqu:
    def __init__(self):
        self.second_box = Tk()
        self.second_box.title("SecondDegree")
        self.second_box.maxsize(280, 150)
        self.second_box.minsize(280, 150)
        self.form = Label(self.second_box, text="aX^2 + bX + c = 0")
        self.form.grid(row=0, column=0)
        self.a = Label(self.second_box, text="a = ")
        self.a.grid(row=2, column=0)
        self.b = Label(self.second_box, text="b = ")
        self.b.grid(row=3, column=0)
        self.c = Label(self.second_box, text="c = ")
        self.c.grid(row=4, column=0)
        self.num_a = Entry(self.second_box)
        self.num_a.grid(row=2, column=1)
        self.num_b = Entry(self.second_box)
        self.num_b.grid(row=3, column=1)
        self.num_c = Entry(self.second_box)
        self.num_c.grid(row=4, column=1)
        self.calc = Button(self.second_box, text="Solve", bg="royal blue", fg="white", command=self.solve, relief=FLAT)
        self.calc.grid(row=5, column=0, pady=5)
        self.results1 = Label(self.second_box)
        self.results1.grid(row=6, column=0)
        self.results2 = Label(self.second_box)
        self.results2.grid(row=6, column=1)
        self.second_box.mainloop()

    def solve(self):
        try:
            a = self.num_a.get()
            b = self.num_b.get()
            c = self.num_c.get()
            self.results1.configure(
                text="X1 = " + str((-eval(b) + (eval(b) ** 2 - 4 * eval(a) * eval(c)) ** .5) / 2 * eval(a)))
            self.results2.configure(
                text="X2 = " + str((-eval(b) - (eval(b) ** 2 - 4 * eval(a) * eval(c)) ** .5) / 2 * eval(a)))
        except SyntaxError:
            self.results1.configure(text="Please, Enter a valid value")


class SpecialSolver(object):

    """Special Equations"""

    def __init__(self):
        self.root = Tk()
        self.root.title("EquationSolver")
        self.root.maxsize(190, 90)
        self.root.minsize(190, 90)
        self.menu_bar = Menu(self.root)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=sp_equ_solver)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.destroy)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.go_to_menu = Menu(self.menu_bar, tearoff=0)
        self.go_to_menu.add_command(label="Equation solver", command=equ_solver)
        self.go_to_menu.add_command(label="Special equations", command=sp_equ_solver)
        self.menu_bar.add_cascade(label="GoTo", menu=self.go_to_menu)
        self.Spe_menu = Menu(self.menu_bar, tearoff=0)
        self.Spe_menu.add_command(label="MailSys", command=mail)
        self.Spe_menu.add_command(label="PySys", comman=sys_ex)
        self.menu_bar.add_cascade(label="Special services", menu=self.Spe_menu)
        self.root.config(menu=self.menu_bar)
        self.first_lbl = Label(self.root, text="Log", fg="dark red")
        self.first_lbl.grid(row=0, column=0)
        self.log = Button(self.root, text="Choose this", command=LogSolver, bg="royal blue", fg="white", relief=FLAT)
        self.log.grid(row=1, column=0, padx=10, pady=5)
        self.second_lbl = Label(self.root, text="Triangle solver", fg="dark red")
        self.second_lbl.grid(row=0, column=1)
        self.triangle = Button(self.root, text="Choose this", command=TriangleSolver, fg="white", bg="royal blue")
        self.triangle["relief"] = FLAT
        self.triangle.grid(row=1, column=1, padx=10, pady=5)
        self.root.mainloop()


class LogSolver:

    def __init__(self):
        self.root = Tk()
        self.root.title("Log solver")
        self.root.maxsize(300, 200)
        self.root.minsize(300, 200)
        self.log_lbl = Label(self.root, text="Log (value1) = (value2)")
        self.log_lbl.grid(row=2, column=0)
        self.log_lbl = Label(self.root, text=""""//" = Empty""")
        self.log_lbl.grid(row=2, column=1)
        self.value1_lbl = Label(self.root, text="value1")
        self.value1_lbl.grid(row=3, column=0)
        self.value1 = Entry(self.root)
        self.value1.grid(row=3, column=1)
        self.value2_lbl = Label(self.root, text="value2")
        self.value2_lbl.grid(row=4, column=0)
        self.value2 = Entry(self.root)
        self.value2.grid(row=4, column=1)
        self.base_lbl = Label(self.root, text="Base")
        self.base_lbl.grid(row=5, column=0)
        self.base = Entry(self.root)
        self.base.grid(row=5, column=1)
        self.calc = Button(self.root, text="Calculate", fg="white", bg="royal blue", command=self.calc, relief=FLAT)
        self.calc.grid(row=6, column=0, padx=10, pady=5)
        self.result = Label(self.root)
        self.result.grid(row=7, column=0)

    def calc(self):
        value1 = self.value1.get()
        value2 = self.value2.get()
        base = self.base.get()
        if value1 == "//":
            result = eval(base) ** eval(value2)
            self.result.configure(text="Value1 = " + str(result))
        elif value2 == "//":
            result = math.log(eval(value1), eval(base))
            self.result.configure(text="Value2 = " + str(result))
        elif base == "//":
            result = eval(value1) ** (1 / eval(value2))
            self.result.configure(text="Base = " + str(result))


class TriangleSolver:

    def __init__(self):
        self.root = Tk()
        self.root.title("Triangle solver")
        self.root.maxsize(400, 200)
        self.root.minsize(400, 200)
        self.triangle_lbl = Label(self.root, text="""[(a, b, c) are Angles (x, y, z) are Sides] in order""")
        self.triangle_lbl.grid(row=2, column=0)
        self.a_lbl = Label(self.root, text="a = ").grid(row=3, column=0)
        self.a = Entry(self.root)
        self.a.grid(row=3, column=1)
        self.y_lbl = Label(self.root, text="y = ").grid(row=7, column=0)
        self.y = Entry(self.root)
        self.y.grid(row=7, column=1)
        self.z_lbl = Label(self.root, text="z = ").grid(row=8, column=0)
        self.z = Entry(self.root)
        self.z.grid(row=8, column=1)
        self.solve = Button(self.root, text="Solve", fg="white", bg="royal blue", command=self.solve, relief=FLAT)
        self.solve.grid(row=9, column=0, padx=10, pady=5)
        self.result_x = Label(self.root)
        self.result_x.grid(row=13, column=0)

    def solve(self):
        a = self.a.get()
        y = self.y.get()
        z = self.z.get()
        a = (eval(a) / 180) * math.pi
        x = math.sqrt((eval(z) ** 2) + (eval(y) ** 2) - (2 * eval(z) * eval(y) * math.cos(a)))
        self.result_x.configure(text="X = " + str(x))


class SpecialServices(object):

    """Special Services"""
    pass


class Mail:

    def __init__(self):
        self.root = Tk()
        self.root.title("MailSys")
        self.root.maxsize(390, 450)
        self.root.minsize(390, 450)
        self.menu_bar = Menu(self.root)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=mail)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.destroy)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.go_to_menu = Menu(self.menu_bar, tearoff=0)
        self.go_to_menu.add_command(label="Equation solver", command=equ_solver)
        self.go_to_menu.add_command(label="Special equation", command=sp_equ_solver)
        self.menu_bar.add_cascade(label="GoTo", menu=self.go_to_menu)
        self.Spe_menu = Menu(self.menu_bar, tearoff=0)
        self.Spe_menu.add_command(label="MailSys", command=mail)
        self.Spe_menu.add_command(label="PySys", comman=sys_ex)
        self.menu_bar.add_cascade(label="Special services", menu=self.Spe_menu)
        self.root.config(menu=self.menu_bar)
        self.lbl = Label(self.root, fg="dark red", text="Welcome to our Mail system...")
        self.lbl.grid(row=0, column=1, pady=20)
        self.lbl1 = Label(self.root, text="From: ", fg="dark green")
        self.lbl1.grid(row=2, column=0)
        self.from_mail = Entry(self.root, width=50)
        self.from_mail.grid(row=2, column=1)
        self.lbl2 = Label(self.root, text="To: ", fg="dark green")
        self.lbl2.grid(row=3, column=0, padx=10, pady=20)
        self.to_mail = Entry(self.root, width=50)
        self.to_mail.grid(row=3, column=1, pady=20)
        self.message_lbl = Label(self.root, text="Message....", fg="dark green")
        self.message_lbl.grid(row=4, column=1)
        self.message = tkinter.scrolledtext.ScrolledText(self.root, width=38, height=12)
        self.message.grid(column=1)
        self.send = Button(self.root, bg="royal blue", fg="white", text="Send the message..", command=self.send)
        self.send["relief"] = FLAT
        self.send.grid(column=1, pady=20)
        self.result = Label(self.root)
        self.result.grid(column=1)
        self.root.mainloop()

# ##############!!!@%$%@!!!############
#   """This need to be tested"""       #
# ##############!!!@%$%@!!!############

    def send(self):
        try:
            from_mail = self.from_mail.get()
            to_mail = self.to_mail.get()
            message = self.message.get(0, self.message.size() + 1)
            server = smtplib.SMTP("localhost")
            server.sendmail(from_mail, to_mail, message)
            server.quit()
        except TypeError:
            self.result.configure(text="The message hasn't been sent")


class SysAcc(object):

    def __init__(self):
        self.root = Tk()
        self.root.title("PySys")
        self.root.maxsize(260, 80)
        self.root.minsize(260, 80)
        self.menu_bar = Menu(self.root)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=sys_ex)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.destroy)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.go_to_menu = Menu(self.menu_bar, tearoff=0)
        self.go_to_menu.add_command(label="Equation solver", command=equ_solver)
        self.go_to_menu.add_command(label="Special equations", command=sp_equ_solver)
        self.menu_bar.add_cascade(label="GoTo", menu=self.go_to_menu)
        self.Spe_menu = Menu(self.menu_bar, tearoff=0)
        self.Spe_menu.add_command(label="MailSys", command=Mail)
        self.Spe_menu.add_command(label="PySys", comman=sys_ex)
        self.menu_bar.add_cascade(label="Special services", menu=self.Spe_menu)
        self.root.config(menu=self.menu_bar)
        self.lbl = Label(self.root, text="Welcome to your System...", fg="dark red")
        self.lbl.grid(row=0, column=1)
        self.lbl_command = Label(self.root, text="Command:")
        self.lbl_command.grid(row=2, column=0)
        self.command = Entry(self.root)
        self.command.grid(row=2, column=1, pady=5)
        self.exec = Button(self.root, text="Execute", fg="white", bg="royal blue", command=self.exec, relief=FLAT)
        self.exec.grid(row=3, column=1)
        self.root.mainloop()

    def exec(self):
        command = self.command.get()
        os.system(command)


if __name__ == '__main__':
    import os
    import math
    import smtplib
    import tkinter.scrolledtext
    import tkinter.messagebox
    from tkinter import *
    app = Application()
