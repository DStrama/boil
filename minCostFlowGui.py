import tkinter
from minCostFlow import Solver
import numpy as np
from PIL import ImageTk, Image


def solve():
    solver = Solver()
    supply = [int(podaz1.get()), int(podaz2.get())]
    demand = [int(popyt1.get()), int(popyt2.get()), int(popyt3.get())]
    flow_value = [int(kt21.get()), int(kt13.get()), int(kt16.get()), int(kt26.get()),
                  int(kt25.get()), int(kt63.get()), int(kt64.get()), int(kt65.get()),
                  int(kt34.get()), int(kt45.get())]
    res = solver.calculate_min_flow(supply, demand, flow_value)
    show_results(res)

    pass

def show_results(res):
    window = tkinter.Tk()
    window.title("Optymalizacja przepływu w sieciach transportowych")


    label1 = tkinter.Label(window, text=" Koszt całkowity: "+ str(round(res.fun))).grid(row=0, column=0)
    label2 = tkinter.Label(window, text=" Koszty jednostkowe: "+str(np.ndarray.round(res.x))).grid(row=1, column=0)
    # window.geometry('500x400')
    pass


window = tkinter.Tk()

window.title("Optymalizacja przepływu w sieciach transportowych")


# label0 = tkinter.Label(window, text="Podaż dostawców ").grid(row=0, column=0)
# label1 = tkinter.Label(window, text=" Popyt odbiorców ").grid(row=0, column=2)

label1 = tkinter.Label(window, text=" a1: ").grid(row=0, column=0)
podaz1 = tkinter.Entry(window, width=10)
podaz1.grid(row=0, column=2)
# label2 = tkinter.Label(window, text=" 1 ").grid(row=0, column=3)
# label3 = tkinter.Label(window, text=" 2 ").grid(row=0, column=5)
label4 = tkinter.Label(window, text=" b1: ").grid(row=0, column=6)
popyt1 = tkinter.Entry(window, width=10)
popyt1.grid(row=0, column=7)
# label6 = tkinter.Label(window, text=" 4 ").grid(row=1, column=5)
label7 = tkinter.Label(window, text=" b2: ").grid(row=1, column=6)
popyt2 = tkinter.Entry(window, width=10)
popyt2.grid(row=1, column=7)
label8 = tkinter.Label(window, text=" a2: ").grid(row=2, column=0)
podaz2 = tkinter.Entry(window, width=10)
podaz2.grid(row=2, column=2)
# label9 = tkinter.Label(window, text=" 2 ").grid(row=2, column=3)
# label10 = tkinter.Label(window, text=" 5 ").grid(row=2, column=5)
label11 = tkinter.Label(window, text=" b3: ").grid(row=2, column=6)
popyt3 = tkinter.Entry(window, width=10)
popyt3.grid(row=2, column=7)

label13 = tkinter.Label(window, text=" 2->1: ").grid(row=4, column=0)
label14 = tkinter.Label(window, text=" 1->3: ").grid(row=5, column=0)
label15 = tkinter.Label(window, text=" 1->6: ").grid(row=6, column=0)
label16 = tkinter.Label(window, text=" 2->6: ").grid(row=7, column=0)
label17 = tkinter.Label(window, text=" 2->5: ").grid(row=8, column=0)
label18 = tkinter.Label(window, text=" 6->3: ").grid(row=9, column=0)
label20 = tkinter.Label(window, text=" 6->4: ").grid(row=10, column=0)
label21 = tkinter.Label(window, text=" 6->5: ").grid(row=11, column=0)
label22 = tkinter.Label(window, text=" 3->4: ").grid(row=12, column=0)
label23 = tkinter.Label(window, text=" 4->5: ").grid(row=13, column=0)
kt21 = tkinter.Entry(window, width=10)
kt21.grid(row=4, column=1)
kt13 = tkinter.Entry(window, width=10)
kt13.grid(row=5, column=1)
kt16 = tkinter.Entry(window, width=10)
kt16.grid(row=6, column=1)
kt26 = tkinter.Entry(window, width=10)
kt26.grid(row=7, column=1)
kt25 = tkinter.Entry(window, width=10)
kt25.grid(row=8, column=1)
kt63 = tkinter.Entry(window, width=10)
kt63.grid(row=9, column=1)
kt64 = tkinter.Entry(window, width=10)
kt64.grid(row=10, column=1)
kt65 = tkinter.Entry(window, width=10)
kt65.grid(row=11, column=1)
kt34 = tkinter.Entry(window, width=10)
kt34.grid(row=12, column=1)
kt45 = tkinter.Entry(window, width=10)
kt45.grid(row=13, column=1)
img = ImageTk.PhotoImage(Image.open("reference1.png"))
panel = tkinter.Label(window, image = img)
panel.grid(row = 1, column=4)
# label6 = tkinter.Label(window, text=" W1 ").grid(row=3, column=0)
# label7 = tkinter.Label(window, text=" D2 ").grid(row=5, column=0)
# label8 = tkinter.Label(window, text=" KT11 ").grid(row=3, column=1)
# label9 = tkinter.Label(window, text=" KT12 ").grid(row=3, column=2)
# label10 = tkinter.Label(window, text=" KT13 ").grid(row=3, column=3)
# label11 = tkinter.Label(window, text=" KT21 ").grid(row=5, column=1)
# label12 = tkinter.Label(window, text=" KT22 ").grid(row=5, column=2)
# label13 = tkinter.Label(window, text=" KT23 ").grid(row=5, column=3)
#
# label16 = tkinter.Label(window, text="Podaż dostawców ").grid(row=0, column=0)
# label17 = tkinter.Label(window, text=" Popyt odbiorców ").grid(row=0, column=2)
#
# popyt1 = tkinter.Entry(window, width=10)
# popyt1.grid(row=2, column=1)
# popyt2 = tkinter.Entry(window, width=10)
# popyt2.grid(row=2, column=2)
# popyt3 = tkinter.Entry(window, width=10)
# popyt3.grid(row=2, column=3)
# # podaz1 = tkinter.Entry(window, width=10)
# # podaz1.grid(row=4, column=0)
# kt11 = tkinter.Entry(window, width=10)
# kt11.grid(row=4, column=1)
# kt12 = tkinter.Entry(window, width=10)
# kt12.grid(row=4, column=2)
# kt13 = tkinter.Entry(window, width=10)
# kt13.grid(row=4, column=3)
# kt21 = tkinter.Entry(window, width=10)
# kt21.grid(row=6, column=1)
# kt22 = tkinter.Entry(window, width=10)
# kt22.grid(row=6, column=2)
# kt23 = tkinter.Entry(window, width=10)
# kt23.grid(row=6, column=3)
#
# podaz1 = tkinter.Entry(window, width=10)
# podaz1.grid(row=4, column=0)
# podaz2 = tkinter.Entry(window, width=10)
# podaz2.grid(row=6, column=0)


calculateButton = tkinter.Button(window, text="Oblicz", command=solve)
calculateButton.grid(row=8, column=7)
window.geometry('650x450')
window.mainloop()
