# import lib
import os
import json

def settings():
    folder_name = "database"
    filename = "information.json"
    return folder_name, filename

def get_name(prompt):
  while True:
      name = input(prompt).strip()
      if name == "":
          print("กรุณาพิมพ์บางอย่าง!")
      else:
          return name
        
def get_nick(prompt):
    while True:
        nick = input(prompt).strip()
        if nick == "":
            print("ป้อนอะไรบางอย่าง!")
        elif len(nick) > 10:
           print("ชื่อเล่นสั้นเกินไปกรุณาพิมพ์ใหม่ ขึ้นต่ำไม่เกิน 10 ตัวอักษร")
        else:
            return nick

def get_number(prompt):
    while True: 
      age = input(prompt)
      if age.isdigit():
        return int(age)
      else:
        print("กรุณาป้อนแค่ตัวเลข!")

def save_info(data, folder_name="data"):
    folder_name, filename = settings()
    base_dir = os.path.dirname(__file__)
    folder_path = os.path.join(base_dir, folder_name)
    if not os.path.exists(folder_path):
      os.makedirs(folder_path)

    file_path = os.path.join(folder_path,filename)

    with open(file_path, "w", encoding="utf-8") as f:
      json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"\nข้อมูลถูกบันทึกเป็นไฟล์ {filename} ที่ {folder_path} เรียบร้อยแล้ว!")

def main():
    firstname = get_name("What is your name? : ")
    nickname = get_nick("What is your nickname? : ")
    age = get_number("How old are you? : ")

    print("\nกรุณาเช็คและยืนยันข้อมูลให้ถูกต้อง:")
    print(f"Name: {firstname}")
    print(f"Nickname: {nickname}")
    print(f"Age: {age}")

    comfirm = input("นี่คือข้อมูลที่ถูกต้องของคุณแล้วใช่หรือไม่ (y/n): ").lower()
    
    if comfirm == "y":
        info = {
          "name": firstname,
          "nickname": nickname,
          "age": age
        }
        save_info(info)
    elif comfirm == "n":
      print("กรุณากรอกข้อมูลที่ถูกต้องใหม่")
      main()
    else:
      print("\nข้อมูลผิดพลาดกรุณากรอกข้อมูลใหม่อีกครั้ง!")
      main()

if __name__ == "__main__":
  main()