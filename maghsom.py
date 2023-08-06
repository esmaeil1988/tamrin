def maghsom(number):
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)

maghsom(int(input("number")))