### 🔢 **Hamming Code Implementation (Network Prog.)**
A **GUI-based** implementation of **Hamming Code** for **error detection and correction** in network communication, developed using **Python and Tkinter**.

---

## 🚀 **Features**
- **Graphical User Interface (GUI):** Easy-to-use Tkinter-based interface.
- **Hamming Code Implementation:** Supports **single-bit error detection and correction**.
- **Redundant Bit Calculation:** Determines the required **redundant bits** automatically.
- **Encoded Data Transmission:** Computes and displays the transmitted data.
- **Error Position Identification:** Detects and highlights **error positions** in the received message.

---

## 🛠 **Technologies Used**
- **Python:** Core programming language.
- **Tkinter:** GUI framework for user interaction.
- **Bitwise Operations:** Used for fast **parity bit calculations**.
- **Development Environment:** VS Code / PyCharm.

---

## 🎮 **How to Use**
1. **Enter Binary Data**: Input the data bits to be transmitted.
2. **Compute Transmitted Data**: The system will calculate redundant bits and generate the encoded message.
3. **Detect Errors**: Enter received data to check for errors.
4. **Correction**: The system highlights the erroneous bit (if any).

---

## 📜 **Code Overview**
### **Main Functions**
✔ **`calcRedundantBits(m)`** – Calculates the number of redundant bits.  
✔ **`posRedundantBits(data, r)`** – Places redundant bits at powers of 2.  
✔ **`calcParityBits(arr, r)`** – Computes parity bits for error correction.  
✔ **`detectError(arr, nr)`** – Detects and identifies errors in received data.  

### **GUI Components**
✔ **Entry Field** – Accepts binary data input.  
✔ **Buttons** – Compute encoded message & detect errors.  
✔ **Labels** – Displays encoded messages, redundant bits, and error detection results.  

---

## 📌 **Applications**
🔹 **Digital & Network Communication** – Used in **Wi-Fi, Ethernet, and TCP/IP**.  
🔹 **Data Storage Systems** – Error correction in **RAM & hard drives**.  
🔹 **QR Codes & Barcodes** – Used for **error correction in scanned data**.  
🔹 **Satellite & Wireless Communication** – Ensures **data integrity** during transmission.  

---

## 🎯 **Future Enhancements**
🔹 **File Input/Output** – Process large binary data streams.  
🔹 **Graphical Parity Bit Visualization** – Display how errors are corrected.  

---
