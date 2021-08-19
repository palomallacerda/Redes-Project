import threading ## Biblioteca para importação da thread

def job_one():
    i = 0
    for i in range(10):
        print("Test 1")
        i+=1

def job_two():
    i = 0
    for i in range(10):
        print("Test 2")
        i+=1

threading.Thread(target=job_one).start() ## metodo usado + função + ação
job_two()