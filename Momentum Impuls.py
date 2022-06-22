#mengimport tkinter
from tkinter import *

#mendefinisikan frame
def bingkai(frame):
    frame.tkraise()

#membuat class
class kalkulator:
    def __init__(self, master):

        #mengatur jendela root
        master.title("Kalkulator Momentum & Impuls")
        master.minsize(340,200)
        master.maxsize(340,200)

        #mengatur frame
        self.momentum = Frame(master)
        self.impuls = Frame(master)
        for frame in (self.momentum, self.impuls):
            frame.grid(row=0, column=0, sticky='nesw')

        # ==============================================================================================================
        # ======================= Tata Letak Menu Momentum =============================================================
        # ==============================================================================================================

        #teks
        self.momentum_judul_teks = Label(self.momentum, text="Momentum").grid(row=0, column=1)
        self.momentum_kecepatan_teks = Label(self.momentum, text="Kecepatan (m/s): ").grid(row=1, column=0)
        self.momentum_massa_teks = Label(self.momentum, text="Massa (kg): ").grid(row=2, column=0)
        self.momentum_hasil_teks = Label(self.momentum, text="Momentum (kgm/s): ").grid(row=3, column=0)

        #kolom
        self.momentum_kecepatan = Entry(self.momentum)
        self.momentum_massa = Entry(self.momentum)
        self.momentum_hasil = Entry(self.momentum)

        self.momentum_kecepatan.grid(row=1, column=1)
        self.momentum_massa.grid(row=2, column=1)
        self.momentum_hasil.grid(row=3, column=1)

        #tombol
        self.momentum_kecepatan_tombol = Button(self.momentum, text="Hitung Kecepatan", command=self.momentum_kecepatan_hitung)
        self.momentum_massa_tombol = Button(self.momentum, text="Hitung Massa", command=self.momentum_massa_hitung)
        self.momentum_hasil_tombol = Button(self.momentum, text="Hitung Momentum", command=self.momentum_hasil_hitung)

        self.momentum_kecepatan_tombol.grid(row=4, column=1)
        self.momentum_massa_tombol.grid(row=5, column=1)
        self.momentum_hasil_tombol.grid(row=6, column=1)

        # ==============================================================================================================
        # ======================= Tata Letak Menu Impuls =============================================================
        # ==============================================================================================================

        # teks
        self.impuls_judul_teks = Label(self.impuls, text="Impuls").grid(row=0, column=1)
        self.impuls_gaya_teks = Label(self.impuls, text="Gaya Impulsif (N): ").grid(row=1, column=0)
        self.impuls_waktu_teks = Label(self.impuls, text="Perubahan Waktu (s): ").grid(row=2, column=0)
        self.impuls_hasil_teks = Label(self.impuls, text="Impuls (Ns): ").grid(row=3, column=0)

        # kolom
        self.impuls_gaya = Entry(self.impuls)
        self.impuls_waktu = Entry(self.impuls)
        self.impuls_hasil = Entry(self.impuls)

        self.impuls_gaya.grid(row=1, column=1)
        self.impuls_waktu.grid(row=2, column=1)
        self.impuls_hasil.grid(row=3, column=1)

        # tombol
        self.impuls_gaya_tombol = Button(self.impuls, text="Hitung Gaya Impulsif", command=self.impuls_gaya_hitung)
        self.impuls_waktu_tombol = Button(self.impuls, text="Hitung Perubahan Waktu", command=self.impuls_waktu_hitung)
        self.impuls_hasil_tombol = Button(self.impuls, text="Hitung Impuls", command=self.impuls_hasil_hitung)

        self.impuls_gaya_tombol.grid(row=4, column=1)
        self.impuls_waktu_tombol.grid(row=5, column=1)
        self.impuls_hasil_tombol.grid(row=6, column=1)

        # ==============================================================================================================
        # ========================= Tata Letak RadioButton ============================================================
        # ==============================================================================================================
        #menginisialisasi radiobutton
        self.menubar = Menu(master)

        #membuat menu pada file
        self.menu_file = Menu(self.menubar, tearoff=0)
        self.menu_file.add_command(label="Keluar", command=master.destroy)

        #membuat menu pada rumus
        self.menu_rumus = Menu(self.menubar, tearoff=0)
        self.menu_rumus.add_separator()
        self.menu_rumus.add_command(label="Momentum", command=lambda: bingkai(self.momentum))
        self.menu_rumus.add_command(label="Impuls", command=lambda: bingkai(self.impuls))

        #membuat menu radiobutton
        self.menubar.add_cascade(label="File", menu=self.menu_file)
        self.menubar.add_cascade(label="Rumus", menu=self.menu_rumus)

        #membuat konfigurasi menu
        master.config(menu=self.menubar)

    # ==================================================================================================================
    # ======================= Perhitungan Momentum =====================================================================
    # ==================================================================================================================

    #kecepatan
    def momentum_kecepatan_hitung(self):
        self._momentum = float(self.momentum_hasil.get())
        self._massa = float(self.momentum_massa.get())

        self.momentum_kecepatan.delete(0, END)
        self.momentum_kecepatan.insert(INSERT, str(self._momentum / self._massa))

    #massa
    def momentum_massa_hitung(self):
        self._momentum = float(self.momentum_hasil.get())
        self._kecepatan = float(self.momentum_kecepatan.get())

        self.momentum_massa.delete(0, END)
        self.momentum_massa.insert(INSERT, str(self._momentum / self._kecepatan))

    #momentum
    def momentum_hasil_hitung(self):
        self._massa = float(self.momentum_massa.get())
        self._kecepatan = float(self.momentum_kecepatan.get())

        self.momentum_hasil.delete(0, END)
        self.momentum_hasil.insert(INSERT, str(self._massa * self._kecepatan))

    # ==================================================================================================================
    # ======================= Perhitungan Impuls =======================================================================
    # ==================================================================================================================

    #gaya
    def impuls_gaya_hitung(self):
        self._impuls = float(self.impuls_hasil.get())
        self._waktu = float(self.impuls_waktu.get())

        self.impuls_gaya.delete(0, END)
        self.impuls_gaya.insert(INSERT, str(self._impuls / self._waktu))

    #waktu
    def impuls_waktu_hitung(self):
        self._impuls = float(self.impuls_hasil.get())
        self._gaya= float(self.impuls_gaya.get())

        self.impuls_waktu.delete(0, END)
        self.impuls_waktu.insert(INSERT, str(self._impuls / self._gaya))

    #impuls
    def impuls_hasil_hitung(self):
        self._gaya = float(self.impuls_gaya.get())
        self._waktu = float(self.impuls_waktu.get())

        self.impuls_hasil.delete(0, END)
        self.impuls_hasil.insert(INSERT, str(self._gaya * self._waktu))

root = Tk()
main = kalkulator(root)
root.mainloop()
