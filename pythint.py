def hi(name):
    print("merhaba " + name + "!")

girls = ["ayşe", "ecem", "zeynep", "sen"]
for name in girls:
    hi(name)
    print("sıradaki kız")
    for i in range(1, 6):
        print(i)
        
