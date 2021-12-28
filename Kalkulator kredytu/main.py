from tkinter import *
from tkinter import ttk


class KalkulatorKredytu:

    def __init__(self):
        # Okno wraz z napisami rozmieszczocznymi odpowiednio
        root = Tk()
        root.geometry("280x140")
        root.title("Kalkulator kredytu")
        # Dynamiczne zmienianie rozmieszczenia wszystkiego
        for x in range(0, 6):
            Grid.rowconfigure(root, x, weight=1)

        Grid.columnconfigure(root, 0, weight=1)
        Grid.columnconfigure(root, 1, weight=1)
        # Dodanie Label
        ttk.Label(root, text="RRSO").grid(column=0, row=0, sticky=W)
        ttk.Label(root, text="Liczba miesięcy").grid(column=0, row=1, sticky=W)
        ttk.Label(root, text="Kwota kredytu").grid(column=0, row=2, sticky=W)
        ttk.Label(root, text="Miesięczna rata").grid(column=0, row=3, sticky=W)
        ttk.Label(root, text="Całkowita kwota").grid(column=0, row=4, sticky=W)

        # Określenie zmiennych i Entry
        self.rrsoVar = StringVar()
        ttk.Entry(root, textvariable=self.rrsoVar, justify=RIGHT).grid(column=1, row=0, sticky=E)
        self.monthsOfPaymentVar = StringVar()
        ttk.Entry(root, textvariable=self.monthsOfPaymentVar, justify=RIGHT).grid(column=1, row=1, sticky=E)
        self.loanAmountVar = StringVar()
        ttk.Entry(root, textvariable=self.loanAmountVar, justify=RIGHT).grid(column=1, row=2, sticky=E)
        self.monthlyInstalmentsVar = StringVar()
        ttk.Label(root, textvariable=self.monthlyInstalmentsVar).grid(column=1, row=3, sticky=E)
        self.totalAmountVar = StringVar()
        ttk.Label(root, textvariable=self.totalAmountVar).grid(column=1, row=4, sticky=E)

        # Przycisk
        btn_compute = ttk.Button(root, text="Oblicz", command=self.oblicz_kwote).grid(column=1, row=5, sticky=E)
        root.mainloop()

    # Funkcja obliczająca dane kwoty
    def oblicz_kwote(self):
        try:
            # Nie może długość kredytu być mniejsza bądź równa 0
            if int(self.monthsOfPaymentVar.get()) <= 0:
                raise ValueError
            # Inne parametry kiedy jest procent, a kiedy go nie ma + zamienianie przecinków na kropki
            if self.rrsoVar.get().find('%') != -1:
                monthly_instalments = self.oblicz_miesieczna_rate(float(self.loanAmountVar.get().replace(",", ".")),
                                                                  float(self.rrsoVar.get().replace(",", ".").strip(
                                                                      '%')) / 100,
                                                                  int(self.monthsOfPaymentVar.get()))
            else:
                monthly_instalments = self.oblicz_miesieczna_rate(float(self.loanAmountVar.get().replace(",", ".")),
                                                                  float(self.rrsoVar.get().replace(",", ".")),
                                                                  int(self.monthsOfPaymentVar.get()))
            self.monthlyInstalmentsVar.set(format(monthly_instalments, '0.2f') + " zł")
            total_amount = monthly_instalments * int(self.monthsOfPaymentVar.get())
            self.totalAmountVar.set(format(total_amount, '0.2f') + " zł")
        # Typowe błędy są pod wyjątkiem ValueError
        except ValueError:
            self.monthlyInstalmentsVar.set("ERROR#!?")
            self.totalAmountVar.set("ERROR#!?")

    # Obliczanie miesięczniej raty | Metoda statyczna
    @staticmethod
    def oblicz_miesieczna_rate(loan_amount, rrso, months_of_payment):
        # Przy RRSO równym 0% to praktycznie jest dzielenie wysokości kredytu przez liczbę miesięcy
        if rrso <= 0:
            monthly_instalments = loan_amount / months_of_payment
        # W lekko zmodyfikowanym wzorze liczba płatności w roku nie może być większa niż liczba miesięcy w roku (12)
        elif months_of_payment <= 12:
            monthly_instalments = (loan_amount * rrso) / (
                    months_of_payment * (1 - (months_of_payment / (months_of_payment + rrso)) ** months_of_payment))
        else:
            monthly_instalments = (loan_amount * rrso) / (
                    12 * (1 - (12 / (12 + rrso)) ** months_of_payment))

        return monthly_instalments


KalkulatorKredytu()
