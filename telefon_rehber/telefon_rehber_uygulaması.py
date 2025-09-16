from phone_class import PhoneBook

pb=PhoneBook()

while True:
    print("\nTelefon Rehberi Uygulamasına Hoşgeldiniz")
    print("1. Kişi Ekle")
    print("2. Kişiyi Listele")
    print("3. Kişi Sil")
    print("4. Çıkış")

    secim = int(input("Bir seçenek girin (1-4): "))

    if secim == 1:
        first_name =input("Ad:")
        last_name =input("Soyad:")
        phone = input("Telefon Numarası:")
        pb.add_contact(first_name, last_name, phone)
    elif secim == 2:
        pb.list_contacts()
    elif secim == 3:
        name = input("Silinecek kişinin adını girin: ")
        pb.delete_contact(name)
    elif secim == 4:
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen 1-4 arasında bir sayı girin.")