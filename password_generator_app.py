import random
import string
import os
import tkinter as tk
from tkinter import messagebox

def get_user_info(name, favorite_word, significant_number, app_name):
    return {
        'name': name.get(),
        'favorite_word': favorite_word.get(),
        'significant_number': significant_number.get(),
        'app_name': app_name.get()
    }

def generate_password(user_info):
    name = user_info.get('name', '')
    favorite_word = user_info.get('favorite_word', '')
    significant_number = user_info.get('significant_number', '')
    
    components = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*()_+")
    ]
    
    base_password = ''.join([name[:2].capitalize(), favorite_word[:2].capitalize(), significant_number[-2:]])
    components.extend(random.choices(base_password, k=4))
    
    random.shuffle(components)
    secure_password = ''.join(components[:8])
    return secure_password

def save_password(app_name, password, user_info):
    filename = "passwords.txt"
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            file.write("Website/App\t\tPassword\t\tDetails\n")
            file.write("-" * 50 + "\n")
    
    with open(filename, 'a') as file:
        file.write(f"{app_name}\t\t{password}\t\tName: {user_info['name']}, Favorite Word: {user_info['favorite_word']}, Number: {user_info['significant_number']}\n")

def on_generate():
    user_info = get_user_info(name_entry, favorite_word_entry, significant_number_entry, app_name_entry)
    password = generate_password(user_info)
    password_label.config(text=f"Generated Password: {password}")
    
    save_password(user_info['app_name'], password, user_info)
    messagebox.showinfo("Success", "Password saved successfully in 'passwords.txt'.")

root = tk.Tk()
root.title("Password Generator")
root.geometry("500x350")
root.config(bg="#1E1E1E")

frame = tk.Frame(root, bg="#1E1E1E", padx=30, pady=30)
frame.pack(padx=20, pady=20)

font = ("Helvetica", 12)
entry_font = ("Helvetica", 10)

tk.Label(frame, text="Your name:", font=font, bg="#1E1E1E", fg="#ffffff").grid(row=0, column=0, sticky="w", pady=5)
name_entry = tk.Entry(frame, font=entry_font, bg="#353535", fg="#ffffff", insertbackground="white")
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Your favorite word:", font=font, bg="#1E1E1E", fg="#ffffff").grid(row=1, column=0, sticky="w", pady=5)
favorite_word_entry = tk.Entry(frame, font=entry_font, bg="#353535", fg="#ffffff", insertbackground="white")
favorite_word_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="A significant number:", font=font, bg="#1E1E1E", fg="#ffffff").grid(row=2, column=0, sticky="w", pady=5)
significant_number_entry = tk.Entry(frame, font=entry_font, bg="#353535", fg="#ffffff", insertbackground="white")
significant_number_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame, text="App/Website name:", font=font, bg="#1E1E1E", fg="#ffffff").grid(row=3, column=0, sticky="w", pady=5)
app_name_entry = tk.Entry(frame, font=entry_font, bg="#353535", fg="#ffffff", insertbackground="white")
app_name_entry.grid(row=3, column=1, padx=10, pady=5)

generate_button = tk.Button(frame, text="Generate Password", font=("Helvetica", 14, "bold"), bg="#4CAF50", fg="white", relief="raised", command=on_generate)
generate_button.grid(row=4, column=0, columnspan=2, pady=20, padx=5)

password_label = tk.Label(frame, text="Generated Password: ", font=("Helvetica", 14, "bold"), bg="#1E1E1E", fg="#ffffff")
password_label.grid(row=5, column=0, columnspan=2, pady=10)

credit_label = tk.Label(root, text="Created by Abrar | LinkedIn: www.linkedin.com/in/siyran-shafi", font=("Helvetica", 8), fg="#ffffff", bg="#1E1E1E")
credit_label.pack(side="bottom", pady=10)

root.mainloop()
