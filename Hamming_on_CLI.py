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

def detectAndCorrectError(arr, r):
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
        print(f"Error detected at bit position: {actual_position + 1}")
        
        corrected_arr = list(arr)
        corrected_arr[actual_position] = '1' if corrected_arr[actual_position] == '0' else '0'
        corrected_data = "".join(corrected_arr)
        print(f"Corrected Received Data: {corrected_data}")
    else:
        print("No error in the received message.")

while True:
    print("\n|------------ Hamming Code --------------|\n")
    print("1. Calculate Transmitted Data")
    print("2. Detect and Correct Error in Received Data")
    print("3. Exit")
    choice = input("\nEnter your choice: ")

    print("\n")
    if choice == "1":
        data = input("Enter Data to Transmit (Binary): ")
        if not data or not all(bit in '01' for bit in data):
            print("Error: Please enter valid binary data.")
            continue

        m = len(data)
        r = calcRedundantBits(m)
        arr = posRedundantBits(data, r)
        arr = calcParityBits(arr, r)

        print(f"Transmitted Data: {arr}")

    elif choice == "2":
        received_data = input("Enter Received Data (Binary): ")
        if not received_data or not all(bit in '01' for bit in received_data):
            print("Error: Please enter valid binary data.")
            continue

        m = len(received_data)
        r = calcRedundantBits(m)

        detectAndCorrectError(received_data, r)

    elif choice == "3":
        print("        Bye Hamming Code!\n")
        break

    else:
        print("Invalid choice! Please enter a valid option.")

