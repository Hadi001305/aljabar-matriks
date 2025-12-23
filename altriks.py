import tkinter as tk
from tkinter import messagebox
import copy

# nama Kelompok: Altriks
# Muhammad Hadi Lesmana (25031554271)
# Andini Tia Andita (25031554069)

# ===============================
# FUNGSI MATEMATIKA MATRIKS
# ===============================

def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    det = 0
    for col in range(n):
        sub_matrix = [row[:col] + row[col+1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(sub_matrix)
    return det


def cofactor_matrix(matrix):
    n = len(matrix)
    cof = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            sub_matrix = [
                row[:j] + row[j+1:]
                for k, row in enumerate(matrix) if k != i
            ]
            cof[i][j] = ((-1) ** (i+j)) * determinant(sub_matrix)
    return cof


def transpose(matrix):
    return list(map(list, zip(*matrix)))


def inverse_matrix(matrix):
    det = determinant(matrix)
    if det == 0:
        return None

    cof = cofactor_matrix(matrix)
    adj = transpose(cof)

    inv = [[adj[i][j] / det for j in range(len(matrix))] for i in range(len(matrix))]
    return inv


# ===============================
# GUI TKINTER
# ===============================

def hitung_invers():
    try:
        n = int(entry_n.get())
        data = text_matrix.get("1.0", tk.END).strip().split("\n")

        if len(data) != n:
            raise ValueError("Jumlah baris tidak sesuai")

        matrix = []
        for row in data:
            values = list(map(float, row.split()))
            if len(values) != n:
                raise ValueError("Jumlah kolom tidak sesuai")
            matrix.append(values)

        inv = inverse_matrix(matrix)

        if inv is None:
            messagebox.showerror("Error", "Determinan = 0\nMatriks tidak memiliki invers")
            return

        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "INVERS MATRIKS:\n\n")
        for row in inv:
            result_text.insert(
                tk.END,
                " ".join(f"{val:8.4f}" for val in row) + "\n"
            )

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ===============================
# WINDOW UTAMA
# ===============================

root = tk.Tk()
root.title("Invers Matriks - Metode Kofaktor")
root.geometry("600x500")

tk.Label(root, text="Ukuran Matriks (n x n):").pack(pady=5)
entry_n = tk.Entry(root, width=5)
entry_n.insert(0, "3")
entry_n.pack()

tk.Label(root, text="Masukkan elemen matriks (pisahkan dengan spasi):").pack(pady=5)
text_matrix = tk.Text(root, height=6, width=60)
text_matrix.insert(tk.END, "1 2 3\n0 1 4\n5 6 0")
text_matrix.pack()

tk.Button(
    root,
    text="Hitung Invers (Kofaktor)",
    command=hitung_invers,
    bg="#c4cc2e",
    fg="red",
    font=("Arial", 10, "bold")
).pack(pady=10)

tk.Label(root, text="Hasil:").pack()
result_text = tk.Text(root, height=8, width=60)
result_text.pack()


root.mainloop()
