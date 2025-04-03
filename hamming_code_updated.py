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

def detectError(arr,r):
    n = len(arr)
    res = 0
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])
        res = res + val * (10**i)
    error_position = int(str(res), 2)
    if error_position != 0:
        actual_position = len(arr) - error_position
        return actual_position
    else:
        return 0

def correctError(arr, error_position):
    corrected_arr = list(arr)
    corrected_arr[error_position] = '1' if corrected_arr[error_position] == '0' else '0'
    return "".join(corrected_arr)

class HammingCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hamming Code GUI")
        
        # Input for data
        self.data_label = tk.Label(root, text="Enter Data to Transmit (Binary):")
        self.data_label.pack(pady=10)
        
        self.data_entry = tk.Entry(root, width=30)
        self.data_entry.pack(pady=5)
        
        # Button to calculate transmitted data
        self.calculate_button = tk.Button(root, text="Calculate Transmitted Data", command=self.calculate_transmitted_data)
        self.calculate_button.pack(pady=5)
        
        # Output Label for transmitted data
        self.transmitted_label = tk.Label(root, text="Transmitted Data:")
        self.transmitted_label.pack(pady=5)
        
        self.transmitted_data = tk.Label(root, text="", bg="lightgray", width=40, height=2)
        self.transmitted_data.pack(pady=5)
        
        # Additional Info Labels
        self.data_bits_label = tk.Label(root, text="Number of Data Bits: ")
        self.data_bits_label.pack(pady=5)
        
        self.redundant_bits_label = tk.Label(root, text="Number of Redundant Bits: ")
        self.redundant_bits_label.pack(pady=5)
        
        self.transmitted_bits_label = tk.Label(root, text="Number of Transmitted Bits: ")
        self.transmitted_bits_label.pack(pady=5)
        
        self.redundant_positions_label = tk.Label(root, text="Positions of Redundant Bits: ")
        self.redundant_positions_label.pack(pady=5)

        #Buttons for error detection
        self.error_button = tk.Button(root, text="Detect Error in Received Data", command=self.detect_error)
        self.error_button.pack(pady=5)

        # Output Label for error detection
        self.error_label = tk.Label(root, text="Error Detection Result:")
        self.error_label.pack(pady=5)
        
        self.error_data = tk.Label(root, text="", bg="lightgray", width=40, height=2)
        self.error_data.pack(pady=5)

        # Button to correct error
        self.corr_button = tk.Button(root, text="Correct Error in Received Data", command=self.correct_error)
        self.corr_button.pack(pady=5)

        # Output Label for corrected data
        self.corr_label = tk.Label(root, text="Corrected Received Data:")
        self.corr_label.pack(pady=5)
        
        self.corr_data = tk.Label(root, text="", bg="lightgray", width=40, height=2)
        self.corr_data.pack(pady=5)
        
    def calculate_transmitted_data(self):
        data = self.data_entry.get()
        
        # Clear the error and correction labels
        self.error_data.config(text="")
        self.corr_data.config(text="")
        
        if not data:
            messagebox.showerror("Error", "Please enter the data to transmit.")
            return
        
        m = len(data)
        r = calcRedundantBits(m)
        
        # Determine the positions of Redundant Bits
        arr = posRedundantBits(data, r)
        
        # Determine the parity bits
        arr = calcParityBits(arr, r)
        
        # Number of Data Bits
        self.data_bits_label.config(text=f"Number of Data Bits: {m}")
        
        # Number of Redundant Bits
        self.redundant_bits_label.config(text=f"Number of Redundant Bits: {r}")
        
        # Total Transmitted Bits
        total_transmitted_bits = m + r
        self.transmitted_bits_label.config(text=f"Number of Transmitted Bits: {total_transmitted_bits}")
        
        # Positions of Redundant Bits
        redundant_positions = [2**i for i in range(r)]  # Redundant bit positions are powers of 2
        self.redundant_positions_label.config(text=f"Positions of Redundant Bits: {', '.join(map(str, redundant_positions))}")
        
        # Display the transmitted data
        self.transmitted_data.config(text=arr)
        
    def detect_error(self):
        data = self.data_entry.get()
        if not data:
            messagebox.showerror("Error", "Please enter the data to transmit.")
            return
        arr = data
        m = len(arr)
        r = calcRedundantBits(m)
        error = detectError(arr, r)
        if error == 0:
            self.error_data.config(text="No error in the received message.")
        else:
            self.error_data.config(text=f"Error detected at position: {error + 1}")

    def correct_error(self):
        data = self.data_entry.get()
        if not data:
            messagebox.showerror("Error", "Please enter the received data.")
            return
        arr = data
        m = len(arr)
        r = calcRedundantBits(m)
        error_position = detectError(arr, r)
        if error_position == 0:
            self.corr_data.config(text="No correction needed.")
        else:
            corrected_data = correctError(arr, error_position)
            self.corr_data.config(text=f"Corrected Data: {corrected_data}")

root = tk.Tk()
app = HammingCodeApp(root)

root.mainloop()
