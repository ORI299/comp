import time

# Chudnovsky algorithm for Pi calculation
def chudnovsky_algorithm(iterations: int) -> float:
    C = 426880 * 10005 ** 0.5
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = L
    for i in range(1, iterations):
        M = (K ** 3 - 16 * K) * M // i ** 3
        L += 545140134
        X *= -262537412640768000
        K += 12
        S += M * L / X
    return C / S

# Calculate Pi 100 times
def run_python_test():
    start_time = time.time()
    for _ in range(100):
        pi = chudnovsky_algorithm(1000)  # Number of iterations for accuracy
    end_time = time.time()
    return end_time - start_time, pi

python_time, python_pi = run_python_test()
print(f"Python Pi Calculation Time: {python_time} seconds")
