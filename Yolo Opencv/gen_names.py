import os

files_data = os.listdir('data')

ff = open(f"train.txt", "w+")

for n in files_data:
    if "jpg" in n:
        print(n)
        ff.write(f"data/obj/{n}\n")

ff.close()