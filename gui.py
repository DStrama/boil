import tkinter
from tkinter import ttk
import calculation

def helperFunction():
    #popyt odbiorców
    demand = [int(popyt1.get()), int(popyt2.get()), int(popyt3.get())]
    #podaz dostawcow
    supply = [int(podaz1.get()), int(podaz2.get())]
    transport_cost = [[int(kt11.get()), int(kt12.get()), int(kt13.get())], [int(kt21.get()), int(kt22.get()), int(kt23.get())]]

    # cena sprzedazy
    demand_cost = [int(cs1.get()), int(cs2.get()), int(cs3.get())]
    # cena zakupu
    supply_cost = [int(cz1.get()), int(cz2.get())]

    # demand_cost = [10, 8, 10 , 8]
    # supply_cost = [5, 5]
    # transport_cost = [[5, 2, 4, 3], [3, 1, 7, 3]]
    # demand = [10, 10, 10, 10]
    # supply = [15, 2

    # demand_cost = [15, 14, 16]
    # supply_cost = [6, 9]
    # transport_cost = [[5, 3, 8], [9, 2, 4]]
    # demand = [10, 30, 10]
    # supply = [20, 30]

    cal = calculation.Calculation(supply, demand, transport_cost, supply_cost, demand_cost)

    show_results(cal.solve_problem())


def show_results(arr):
    print(arr)
    results = arr[len(arr)-1]
    unit_transport_cost = results[2]
    transport_cost = results[3]
    alfa = results[4]
    beta = results[5]
    ckt = results[6]
    ckz = results[7]
    przychod = results[8]
    ck = results[9]
    cz = results[10]


    window = tkinter.Tk()
    window.title("Zagadnienie pośrednika")
    window.resizable(0, 0)

    label2 = tkinter.Label(window, text=" Wyniki: ").grid(row=0, column=0)
    label2 = tkinter.Label(window, text=" O1 ").grid(row=1, column=1)
    label3 = tkinter.Label(window, text=" O2 ").grid(row=1, column=2)
    label4 = tkinter.Label(window, text=" O3 ").grid(row=1, column=3)
    label5 = tkinter.Label(window, text=" D1 " + str()).grid(row=3, column=0)
    label6 = tkinter.Label(window, text=" D2 ").grid(row=5, column=0)
    # label7 = tkinter.Label(window, text=" KT11 ").grid(row=3, column=1)
    # label8 = tkinter.Label(window, text=" KT12 ").grid(row=3, column=2)
    # label9 = tkinter.Label(window, text=" KT13 ").grid(row=3, column=3)
    # label10 = tkinter.Label(window, text=" KT21 ").grid(row=5, column=1)
    # label11 = tkinter.Label(window, text=" KT22 ").grid(row=5, column=2)
    # label12 = tkinter.Label(window, text=" KT23 ").grid(row=5, column=3)
    label17 = tkinter.Label(window, text=" Ai ").grid(row=1, column=4)
    label18 = tkinter.Label(window, text=" Bj ").grid(row=8, column=0)
    label19 = tkinter.Label(window, text=" Całkowity koszt transportu: ").grid(row=1, column=6)
    label20 = tkinter.Label(window, text=" Całkowity koszt zakupu: ").grid(row=2, column=6)
    label21 = tkinter.Label(window, text=" Przychód: ").grid(row=3, column=6)
    label22 = tkinter.Label(window, text=" Całościowy koszt: ").grid(row=4, column=6)
    label23 = tkinter.Label(window, text=" Zysk całkowity: ").grid(row=5, column=6)

    delta11 = tkinter.Label(window, text=str(unit_transport_cost[0][0]), foreground="green").grid(row=2, column=1)
    delta12 = tkinter.Label(window, text=str(unit_transport_cost[0][1]), foreground="green").grid(row=2, column=2)
    delta13 = tkinter.Label(window, text=str(unit_transport_cost[0][2]), foreground="green").grid(row=2, column=3)
    delta21 = tkinter.Label(window, text=str(unit_transport_cost[1][0]), foreground="green").grid(row=4, column=1)
    delta22 = tkinter.Label(window, text=str(unit_transport_cost[1][1]), foreground="green").grid(row=4, column=2)
    delta23 = tkinter.Label(window, text=str(unit_transport_cost[1][2]), foreground="green").grid(row=4, column=3)

    kt11 = tkinter.Label(window, text=str(transport_cost[0][0]), foreground="red").grid(row=3, column=1)
    kt12 = tkinter.Label(window, text=str(transport_cost[0][1]), foreground="red").grid(row=3, column=2)
    kt13 = tkinter.Label(window, text=str(transport_cost[0][2]), foreground="red").grid(row=3, column=3)
    kt21 = tkinter.Label(window, text=str(transport_cost[1][0]), foreground="red").grid(row=5, column=1)
    kt22 = tkinter.Label(window, text=str(transport_cost[1][1]), foreground="red").grid(row=5, column=2)
    kt23 = tkinter.Label(window, text=str(transport_cost[1][2]), foreground="red").grid(row=5, column=3)
    a1 = tkinter.Label(window, text=str(alfa[0]), foreground="blue").grid(row=3, column=4)
    a2 = tkinter.Label(window, text=str(alfa[1]), foreground="blue").grid(row=5, column=4)
    b1 = tkinter.Label(window, text=str(beta[0]), foreground="blue").grid(row=8, column=1)
    b2 = tkinter.Label(window, text=str(beta[1]), foreground="blue").grid(row=8, column=2)
    b3 = tkinter.Label(window, text=str(beta[2]), foreground="blue").grid(row=8, column=3)

    kosztTransportu = tkinter.Label(window, text=str(ckt), foreground="red").grid(row=1, column=7)
    kosztZakupu = tkinter.Label(window, text=str(ckz), foreground="red").grid(row=2, column=7)
    przychod = tkinter.Label(window, text=str(przychod), foreground="red").grid(row=3, column=7)
    caloscKoszt = tkinter.Label(window, text=str(ck), foreground="red").grid(row=4, column=7)
    zyskCalk = tkinter.Label(window, text=str(cz), foreground="red").grid(row=5, column=7)
    window.geometry('500x200')
    window.mainloop()
    pass

window = tkinter.Tk()

window.title("Zagadnienie pośrednika")
window.resizable(0, 0)

label0 = tkinter.Label(window, text="Podaż dostawców ").grid(row=0, column=0)
label1 = tkinter.Label(window, text=" Popyt odbiorców ").grid(row=0, column=2)
label2 = tkinter.Label(window, text=" Cena zakupu ").grid(row=0, column=4)
label3 = tkinter.Label(window, text=" O1 ").grid(row=1, column=1)
label4 = tkinter.Label(window, text=" O2 ").grid(row=1, column=2)
label5 = tkinter.Label(window, text=" O3 ").grid(row=1, column=3)
label6 = tkinter.Label(window, text=" D1 ").grid(row=3, column=0)
label7 = tkinter.Label(window, text=" D2 ").grid(row=5, column=0)
label8 = tkinter.Label(window, text=" KT11 ").grid(row=3, column=1)
label9 = tkinter.Label(window, text=" KT12 ").grid(row=3, column=2)
label10 = tkinter.Label(window, text=" KT13 ").grid(row=3, column=3)
label11 = tkinter.Label(window, text=" KT21 ").grid(row=5, column=1)
label12 = tkinter.Label(window, text=" KT22 ").grid(row=5, column=2)
label13 = tkinter.Label(window, text=" KT23 ").grid(row=5, column=3)
label14 = tkinter.Label(window, text=" CZ1 ").grid(row=3, column=4)
label15 = tkinter.Label(window, text=" CZ2 ").grid(row=5, column=4)
label16 = tkinter.Label(window, text="Podaż dostawców ").grid(row=0, column=0)
label17 = tkinter.Label(window, text=" Popyt odbiorców ").grid(row=0, column=2)
label18 = tkinter.Label(window, text="Cena sprzedaży").grid(row=8, column=0)
label19 = tkinter.Label(window, text=" CS1 ").grid(row=7, column=1)
label20 = tkinter.Label(window, text=" CS2 ").grid(row=7, column=2)
label21 = tkinter.Label(window, text=" CS3 ").grid(row=7, column=3)
popyt1 = tkinter.Entry(window, width=10)
popyt1.grid(row=2, column=1)
popyt2 = tkinter.Entry(window, width=10)
popyt2.grid(row=2, column=2)
popyt3 = tkinter.Entry(window, width=10)
popyt3.grid(row=2, column=3)
# podaz1 = tkinter.Entry(window, width=10)
# podaz1.grid(row=4, column=0)
kt11 = tkinter.Entry(window, width=10)
kt11.grid(row=4, column=1)
kt12 = tkinter.Entry(window, width=10)
kt12.grid(row=4, column=2)
kt13 = tkinter.Entry(window, width=10)
kt13.grid(row=4, column=3)
kt21 = tkinter.Entry(window, width=10)
kt21.grid(row=6, column=1)
kt22 = tkinter.Entry(window, width=10)
kt22.grid(row=6, column=2)
kt23 = tkinter.Entry(window, width=10)
kt23.grid(row=6, column=3)
cz1 = tkinter.Entry(window, width=10)
cz1.grid(row=4, column=4)
cz2 = tkinter.Entry(window, width=10)
cz2.grid(row=6, column=4)
podaz1 = tkinter.Entry(window, width=10)
podaz1.grid(row=4, column=0)
podaz2 = tkinter.Entry(window, width=10)
podaz2.grid(row=6, column=0)
cs1 = tkinter.Entry(window, width=10)
cs1.grid(row=8, column=1)
cs2 = tkinter.Entry(window, width=10)
cs2.grid(row=8, column=2)
cs3 = tkinter.Entry(window, width=10)
cs3.grid(row=8, column=3)

calculateButton = tkinter.Button(window, text="Oblicz", command=helperFunction)
calculateButton.grid(row=8, column=4)
window.geometry('500x250')
window.mainloop()
