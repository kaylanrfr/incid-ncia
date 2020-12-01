arq = open("mega sena.txt", "r")
arr =[0]*60
dic = {}
while(True):
    linha = arq.readline()
    i = 18
    if linha == "": break
    while (i<34):
        val = int(linha[i:i+2:])
        arr[val-1] = arr[val-1] + 1
        i = i + 3
     
for i in range (len(arr)):
    print("A quantidade de {:2d} foi de {:4d}".format(i+1, arr[i]))
    dic[i+1] = arr[i]
print("\nEm ordem crescente: ")
for item in sorted(dic, key = dic.get):
    print ("O valor {:2d} tem a incidência: {:4d}".format(item, dic[item]))
input("")
