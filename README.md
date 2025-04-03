### 🔢 **Hamming Code Implementation (Network Prog.)**
A **GUI-based** implementation of **Hamming Code** for **error detection and correction** in network communication, developed using **Python and Tkinter**.

---

## 🚀 **Features**
- **Graphical User Interface (GUI):** Easy-to-use Tkinter-based interface.
- **Hamming Code Implementation:** Supports **single-bit error detection and correction**.
- **Redundant Bit Calculation:** Determines the required **redundant bits** automatically.
- **Encoded Data Transmission:** Computes and displays the transmitted data.
- **Error Position Identification:** Detects and highlights **error positions** in the received message.
-  **Error Correction:** Corrects the detected error and displays the corrected data.

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
4. **Correction**: The system corrects the single-bit error (flips '0' to '1' or vice-versa)

---

## 📜 **Code Overview**
### **Main Functions**
✔ **`calcRedundantBits(m)`** – Calculates the number of redundant bits.  
✔ **`posRedundantBits(data, r)`** – Places redundant bits at powers of 2.  
✔ **`calcParityBits(arr, r)`** – Computes parity bits for error correction.  
✔ **`detectError(arr, nr)`** – Detects and identifies errors in received data.  
✔ **`correctError(arr, error_position)`** – Corrects and displays   errors in received data.  

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

## 💻 **Project Screenshots**

![image](https://github.com/user-attachments/assets/719b41b1-4578-45c2-9291-276b924b0f5d)
![image](https://github.com/user-attachments/assets/90a3b9fc-7f33-4cac-86c7-fcf373805a2d)
![image](https://github.com/user-attachments/assets/38f609d4-b3be-475d-a176-3583b8e6d96b)
![image](https://github.com/user-attachments/assets/02483b82-85df-417a-941a-0d7d013ab8e0)
![image](https://github.com/user-attachments/assets/2b790ebc-80e3-48a1-97ee-7068fbfbc50c)

---
