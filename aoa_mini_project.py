from tkinter import *
window = Tk()
menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Exit', command=window.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
window.geometry("300x200")
window.title("Enter the matrix" )
top = Toplevel()
top.geometry("500x400")
top.title('Final Matrix')

swaps = [(0, 1), (1, 2), (3, 4), (4, 5), (6, 7), (7, 8),
(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)]
primes = {3, 5, 7, 11, 13, 17}
final_states = [(1, 2, 3, 4, 5, 6, 7, 8, 9)]
possible_states = {(1, 2, 3, 4, 5, 6, 7, 8, 9): 0}
steps=IntVar()
new_state = []
steps=0
sp1=IntVar()
sp2=IntVar()
sp3=IntVar()
sp4=IntVar()
sp5=IntVar()
sp6=IntVar()
sp7=IntVar()
sp8=IntVar()
sp9=IntVar()

def puzzle():
   global steps
   while final_states:
       for _ in range(len(final_states)):
            state = list(final_states.pop(0))
            for i, j in swaps:
                 if state[i] + state[j] in primes:
                     state[i], state[j] = state[j], state[i]
                     t = tuple(state)

                     if t not in possible_states:
                          possible_states[t] = steps + 1
                          final_states.append(t)
                     state[i], state[j] = state[j], state[i]
       steps += 1
   but3 = Button(window, text="ENTER", width=15, command=display(), fg="yellow", bg="black")
   but3.grid(row=3, column=1)

def result(new_state):
   if new_state in possible_states:
        Button(top, text=' 1 ', fg='black', bg='red', height=2, width=9).grid(row=2, column=0)
        Button(top, text=' 2 ', fg='black', bg='red', height=2, width=9).grid(row=2, column=1)
        Button(top, text=' 3 ', fg='black', bg='red', height=2, width=9).grid(row=2, column=2)
        Button(top, text=' 4 ', fg='black', bg='red', height=2, width=9).grid(row=3, column=0)
        Button(top, text=' 5 ', fg='black', bg='red', height=2, width=9).grid(row=3, column=1)
        Button(top, text=' 6 ', fg='black', bg='red', height=2, width=9).grid(row=3, column=2)
        Button(top, text=' 7 ', fg='black', bg='red', height=2, width=9).grid(row=4, column=0)
        Button(top, text=' 8 ', fg='black', bg='red', height=2, width=9).grid(row=4, column=1)
        Button(top, text=' 9 ', fg='black', bg='red', height=2, width=9).grid(row=4, column=2)
        print("Minimum number of steps required are {}\n".format(possible_states[new_state]))
        Label(top, text="Minimum Number of steps required are " ,fg="yellow", font=("bold",16), bg="royal blue").place(x=0, y=150)
        Label(top, text=possible_states[new_state], fg="yellow", font=("bold",16), bg="royal blue").place(x=375, y=150)
   else:
        print("Final state cannot be achieved\n")
        Label(top, text="Final state cannot be achieved",fg="yellow",font=("bold",16), bg="royal blue").place(x=100, y=100)

def display():
   new_state=[]
   a=sp1.get()
   b=sp2.get()
   c=sp3.get()
   d=sp4.get()
   e=sp5.get()
   f=sp6.get()
   g=sp7.get()
   h=sp8.get()
   i=sp9.get()
   print(sp1.get() + " " + sp2.get() + " " + sp3.get())
   print(sp4.get() + " " + sp5.get() + " " + sp6.get())
   print(sp7.get() + " " + sp8.get() + " " + sp9.get())
   r=list(map(int, a))
   r.extend(map(int, b))
   r.extend(map(int, c))
   r.extend(map(int, d))
   r.extend(map(int, e))
   r.extend(map(int, f))
   r.extend(map(int, g))
   r.extend(map(int, h))
   r.extend(map(int, i))
   new_state.extend(r)
   new_state = tuple(new_state)
   but2 = Button(window, text="ENTER", width=15, command=result(new_state), fg="yellow", bg="black")
   but2.grid(row=3, column=1)

sp1=Spinbox(window,from_=1, to=9, width=9)
sp1.grid(row=0,column=0)
sp2=Spinbox(window,from_=1, to=9, width=9)
sp2.grid(row=0,column=1)
sp3=Spinbox(window,from_=1, to=9, width=9)
sp3.grid(row=0,column=2)
sp4=Spinbox(window,from_=1, to=9, width=9)
sp4.grid(row=1,column=0)
sp5=Spinbox(window,from_=1, to=9, width=9)
sp5.grid(row=1,column=1)
sp6=Spinbox(window,from_=1, to=9, width=9)
sp6.grid(row=1,column=2)
sp7=Spinbox(window,from_=1, to=9, width=9)
sp7.grid(row=2,column=0)
sp8=Spinbox(window,from_=1, to=9, width=9)
sp8.grid(row=2,column=1)
sp9=Spinbox(window,from_=1, to=9, width=9)
sp9.grid(row=2,column=2)
but1=Button(window,text="ENTER",width=15,command=puzzle,
fg="yellow",bg="black")
but1.grid(row=3,column=1)
window.mainloop()