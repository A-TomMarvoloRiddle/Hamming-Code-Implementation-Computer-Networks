import tkinter as tk
from tkinter import messagebox

def calcRedundantBits(m):
    for i in range(m):
        if(2**i >= m + i + 1):
            return i

def posRedundantBits(data, r):
    j = 0
    k = 1
    m = len(data)
    res = ''
    for i in range(1, m + r + 1):
        if(i == 2**j):
            res = res + '0'
            j += 1
        else:
            res = res + data[-1 * k]
            k += 1
    return res[::-1]

def calcParityBits(arr, r):
    n = len(arr)
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])
        arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]
    return arr

def detectError(arr, nr):
    n = len(arr)
    res = 0
    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])
        res = res + val * (10**i)
    return int(str(res), 2)

class HammingCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hamming Code GUI")
        
        # Input for data
        self.data_label = tk.Label(root, text="Enter Data to Transmit (Binary):")
        self.data_label.pack(pady=10)
        
        self.data_entry = tk.Entry(root, width=30)
        self.data_entry.pack(pady=5)
        
        # Buttons
        self.calculate_button = tk.Button(root, text="Calculate Transmitted Data", command=self.calculate_transmitted_data)
        self.calculate_button.pack(pady=5)
        
        self.error_button = tk.Button(root, text="Detect Error in Received Data", command=self.detect_error)
        self.error_button.pack(pady=5)
        
        # Output Labels
        self.transmitted_label = tk.Label(root, text="Transmitted Data:")
        self.transmitted_label.pack(pady=5)
        
        self.transmitted_data = tk.Label(root, text="", bg="lightgray", width=40, height=2)
        self.transmitted_data.pack(pady=5)
        
        self.error_label = tk.Label(root, text="Error Detection Result:")
        self.error_label.pack(pady=5)
        
        self.error_data = tk.Label(root, text="", bg="lightgray", width=40, height=2)
        self.error_data.pack(pady=5)
        
    def calculate_transmitted_data(self):
        data = self.data_entry.get()
        
        if not data:
            messagebox.showerror("Error", "Please enter the data to transmit.")
            return
        
        m = len(data)
        r = calcRedundantBits(m)
        
        # Determine the positions of Redundant Bits
        arr = posRedundantBits(data, r)
        
        # Determine the parity bits
        arr = calcParityBits(arr, r)
        
        self.transmitted_data.config(text=arr)
        
    def detect_error(self):
        data = self.data_entry.get()
        
        if not data:
            messagebox.showerror("Error", "Please enter the data to transmit.")
            return
        
        arr = data
        
        m = len(arr)
        r = calcRedundantBits(m)
        
        # Detect Error
        correction = detectError(arr, r)
        if correction == 0:
            self.error_data.config(text="No error in the received message.")
        else:
            self.error_data.config(text=f"Error detected at position: {len(arr) - correction + 1}")


root = tk.Tk()
app = HammingCodeApp(root)

root.mainloop()
