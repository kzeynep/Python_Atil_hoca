import os 

class PhoneBook :
    FILE_NAME = "Files/phonebook.txt"
    
    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME,"w",encoding="utf-8") as f:
                pass
            
    def add_contact(self, firstname, lastname, phone):
        with open(self.FILE_NAME, "a", encoding="utf-8") as f:
            f.write(f"{firstname},{lastname},{phone}\n")
        print(f"{firstname} {lastname} başarıyla eklendi.")
        
    def list_contacts(self):
        with open(self.FILE_NAME, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if not lines : 
                print("Rehber boş.")
            else:
                print("Kişiler:")
                for line in lines:
                    firstname, lastname, phone = line.strip().split(",")
                    print(f"Ad: {firstname}, Soyad: {lastname}, Telefon: {phone}")
                    
                    
    def delete_contact(self, name):
        with open(self.FILE_NAME, "r", encoding="utf-8") as f:
            lines = f.readlines()
        contact_found = False
        with open(self.FILE_NAME, "w", encoding="utf-8") as f:
            for line in lines:
                firstname, lastname, phone = line.strip().split(",")
                if firstname != name:
                    f.write(line)
                else:
                    contact_found = True
                    
        if contact_found:
            print(f"{name} başarıyla silindi.")
        else:
            print(f"{name} bulunamadı.")