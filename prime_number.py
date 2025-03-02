def asal_mi(sayi):
    if sayi < 2:
        print(f"{sayi} bir asal sayı değildir.")
        return
    
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            print(f"{sayi} bir asal sayı değildir.")
            return
    
    print(f"{sayi} bir asal sayıdır.")

# Örnek 
asal_mi(7)  
asal_mi(99)  
asal_mi(111)   
