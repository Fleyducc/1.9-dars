son = int(input("Son kiriting: "))
sum = 0

for i in range(1, son + 1):
    sum = sum + i

print("Yig'indisi:", sum)

# for i in range (1, 10, 2):
#    print(i)

# for i in range(10):
#    print("salom")
 
matn = input("Matn Kiriting: ")
 
katta = ""
kichkina = ""

for i in matn:
    if i.isupper():
        katta += i
    elif i.islower():
        kichkina += i
        
soni1 = len(katta) 
soni2 = len(kichkina)    
        
print("Katta harf: ", katta,  soni1)
print("Kichkina harf: ", kichkina, soni2)
print(katta + kichkina)






































# for i in range(10,0,1):
#     print(f"{i} Ketmon")

# text = "dadakda"


# for i in range(len(text)):
#     print(f"{i}")


# # text = "Olma aka olmazorda Olma sotadi"

# # word = text.split()

# # for i in(text.split):
# #    print()

