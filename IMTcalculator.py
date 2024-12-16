import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100
        bmi = weight / (height ** 2)
        result_label_bmi.config(text=f"Индекс массы тела: {bmi:.2f}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные значения веса и роста.")

def calculate_hr_zones():
    try:
        age = int(age_entry.get())
        resting_hr = int(resting_hr_entry.get())
        max_hr = 220 - age
        reserve_hr = max_hr - resting_hr
        zones = {
            "Зона 1 (легкая активность)": 0.5,
            "Зона 2 (контроль веса)": 0.6,
            "Зона 3 (аэробная)": 0.7,
            "Зона 4 (анаэробная)": 0.8,
            "Зона 5 (максимальная нагрузка)": 0.9,
        }
        result_text = ""
        for zone, factor in zones.items():
            lower = resting_hr + reserve_hr * factor
            upper = resting_hr + reserve_hr * (factor + 0.1)
            result_text += f"{zone}: {lower:.0f} - {upper:.0f} уд/мин\n"
        result_label_hr.config(text=result_text)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные значения возраста и ЧСС.")

root = tk.Tk()
root.title("Фитнес калькулятор")

# BMI Section
tk.Label(root, text="Вес (кг):").grid(row=0, column=0, padx=5, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Рост (см):").grid(row=1, column=0, padx=5, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Button(root, text="Рассчитать ИМТ", command=calculate_bmi).grid(row=2, column=0, columnspan=2, pady=5)
result_label_bmi = tk.Label(root, text="")
result_label_bmi.grid(row=3, column=0, columnspan=2, pady=5)

# Heart Rate Section
tk.Label(root, text="Возраст (лет):").grid(row=4, column=0, padx=5, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(root, text="Покоящийся пульс (уд/мин):").grid(row=5, column=0, padx=5, pady=5)
resting_hr_entry = tk.Entry(root)
resting_hr_entry.grid(row=5, column=1, padx=5, pady=5)

tk.Button(root, text="Рассчитать пульсовые зоны", command=calculate_hr_zones).grid(row=6, column=0, columnspan=2, pady=5)
result_label_hr = tk.Label(root, text="")
result_label_hr.grid(row=7, column=0, columnspan=2, pady=5)

root.mainloop()
