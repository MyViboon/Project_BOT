#Checkfile
import os

path = os.getcwd()
# path = r'C:\Users\bakpu\Desktop\Auto-Web\img'
# print(path)
allflie = os.listdir(path) # ฟังชั่น เช๊คชื่อไฟล์
print(allflie)
print("Apples.jpg" in allflie)

# print(os.path.join(path, "Apples"))