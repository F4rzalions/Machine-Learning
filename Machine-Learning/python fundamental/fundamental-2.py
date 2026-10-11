#exception handling
#penanganan error yang sudah diperkirakan tanpa berhenti secara tak terkendali

#2.1  Exception handling

def divide(a: float, b: float) -> float:
    return a/b

try:
    result = divide(10, 0)
except ZeroDivisionError:
    print("Pembagi tidak boleh nol")
else:
    print(result)
finally:
    print("proses selesai")