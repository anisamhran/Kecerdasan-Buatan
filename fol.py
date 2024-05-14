import tkinter as tk
from tkinter import messagebox
from pyDatalog import pyDatalog

def sistem_pakar():
    # Aturan-aturan sistem pakar
    pyDatalog.create_terms('gejala, penyakit')

    # Fakta-fakta gejala dan penyakit
    pyDatalog.assert_fact('gejala', 'demam', 'demam biasa')
    pyDatalog.assert_fact('gejala', 'batuk', 'demam biasa')
    pyDatalog.assert_fact('gejala', 'sakit kepala', 'demam biasa')

    pyDatalog.assert_fact('gejala', 'demam', 'flu')
    pyDatalog.assert_fact('gejala', 'batuk', 'flu')
    pyDatalog.assert_fact('gejala', 'pilek', 'flu')

    # Penyakit kronis
    pyDatalog.assert_fact('penyakit', 'asma')
    pyDatalog.assert_fact('gejala', 'sesak napas', 'asma')
    pyDatalog.assert_fact('gejala', 'batuk berdahak', 'asma')

def diagnosa():
    gejala_input = gejala_entry.get()
    gejala_list = gejala_input.split(',')

    # Mencari penyakit yang sesuai dengan gejala yang dimasukkan pengguna
    scores = {}
    for gejala in gejala_list:
        penyakit_gejala = pyDatalog.ask('gejala("' + gejala.strip() + '", X)')
        if penyakit_gejala:
            for penyakit in penyakit_gejala.answers:
                scores[penyakit[0]] = scores.get(penyakit[0], 0) + 1
    
    # Mengurutkan penyakit berdasarkan skor
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    if sorted_scores:
        most_likely_disease = sorted_scores[0][0]
        messagebox.showinfo("Diagnosa", f"Kemungkinan penyakit: {most_likely_disease}")
    else:
        messagebox.showinfo("Diagnosa", "Tidak ada diagnosis yang sesuai.")

# Create main window
root = tk.Tk()
root.title("Sistem Pakar Diagnosa Penyakit")
root.geometry("400x200")  # Ukuran jendela
root.configure(bg="#C5FF95")  # Warna latar belakang

# Label for symptom input
gejala_label = tk.Label(root, text="Masukkan gejala (pisahkan dengan koma):", bg="#C5FF95", font=("Helvetica", 12))
gejala_label.pack()

# Entry for symptom input
gejala_entry = tk.Entry(root, font=("Helvetica", 12))
gejala_entry.pack()

# Diagnosis button
diagnosa_button = tk.Button(root, text="Diagnosa", command=diagnosa, bg="#FEFFAC", fg="#000000", font=("Helvetica", 12))
diagnosa_button.pack(pady=10)

# Run program
sistem_pakar()
root.mainloop()
