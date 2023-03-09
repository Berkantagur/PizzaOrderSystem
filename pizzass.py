class Pizza:
    def __init__(self, description,prices):
        self.description = description
        self.prices = prices
    
    def get_description(self):
        return self.description

    def get_cost(self):
        return self.prices

     

# Pizza Alt Sınıfları
class KlasikPizza(Pizza):
    def __init__(self):
        description = f"Klasik pizza"
        prices = 8.99
        super().__init__(description,prices)

class MargheritaPizza(Pizza):
    def __init__(self):
        description = f"Margherita pizza"
        prices = 9.99
        super().__init__(description,prices)


class TurkPizza(Pizza):
    def __init__(self):
        description = f"Turk pizza"
        prices = 13.99
        super().__init__(description,prices)


class DominosPizza(Pizza):
    def __init__(self):
        description = f"Dominos pizza"
        prices = 16.99
        super().__init__(description,prices)

     
# Boyut Üst Sınıfı
class DecoratorSize(Pizza):
    def __init__(self, pizza, size_multiplier):
        self.pizza = pizza
        self.size_multiplier = size_multiplier
        self.prices = self.pizza.get_cost() * self.size_multiplier

    def get_description(self):
        return self.pizza.get_description()

    def get_cost(self):
        return self.prices
     

# Boyut Alt Sınıfları
class SmallSize(DecoratorSize):
    def __init__(self, pizza):
        super().__init__(pizza,0.75)
        self.description = "Small"

    def get_description(self):
        return self.description


class MediumSize(DecoratorSize):
    def __init__(self, pizza):
        super().__init__(pizza,1)
        self.price_multiplier = 1
        self.description = "Medium"

    def get_description(self):
        return self.description


class LargeSize(DecoratorSize):
    def __init__(self, pizza):
        super().__init__(pizza,1.25)
        self.description = "Large"

    def get_description(self):
        return self.description
     
#Sos Üst Sınıfı
class DecoratorSos(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description()

    def get_cost(self):
        return self.pizza.get_cost()
     

# Sos Alt Sınıfları
class ZeytinSos(DecoratorSos):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.price = 0.99
        self.description = " Zeytin Sos"

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price


class MantarSos(DecoratorSos):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.price = 1.99
        self.description = " Mantar Sos"

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price


class KeciPeyniriSos(DecoratorSos):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.price = 2.99
        self.description = " Keçi Peyniri Sos"

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price


class EtSos(DecoratorSos):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.price = 3.99
        self.description = " Et Sos"

    def get_description(self):
        return self.description

def get_cost(self):
        return self.price


class SoganSos(DecoratorSos):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.price = 0.99
        self.description = " Soğan Sos"

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price


class MisirSos(DecoratorSos):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.price = 1.99
        self.description = " Mısır Sos"

    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.price
     

# Siparişimizin Veritabanına Yazdırılması
import csv
import os
from datetime import datetime

def add_order_to_database(name, id_no, card_no, description, card_cvv, total_cost):
    # Sipariş tarihini ve saatinin alınması
    now = datetime.now()
    order_time = now.strftime("%Y-%m-%d %H:%M:%S")

    # Yeni bir sipariş satırı oluşturulması
    new_order = [name, id_no, card_no, description, order_time, card_cvv, total_cost]

    file_exists = os.path.isfile("Orders_Database.csv")

    # Orders_Database.csv dosyasına sipariş satırının eklenmesi
    with open("Orders_Database.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        if file_exists:
            writer.writerow(new_order)
        else:
            header = (["Name", "Id", "Card Number", "Order Description", "Order Time", "Card Password", "Total Price"])
            writer.writerow(header)
            writer.writerow(new_order)
     

# Siparişi Sağlayacak main() Fonksiyonu
def main():
  
    with open('menu.txt', 'r') as f:
       menu_items = f.readlines()
    for item in menu_items:
       print(item.strip())


    # Kullanıcıdan pizza seçimini al
    pizza_choice = input("Lütfen pizza seçiniz (1-4): ")
    while pizza_choice not in ["1", "2", "3", "4"]:
        pizza_choice = input("Lütfen geçerli bir pizza numarası seçiniz (1-4): ")

    # Seçilen pizzayı al
    if pizza_choice == "1":
        pizza = KlasikPizza()
    elif pizza_choice == "2":
        pizza = MargheritaPizza()
    elif pizza_choice =="3":
        pizza = TurkPizza()
    else:
        pizza = DominosPizza()

    # Kullanıcıdan pizza seçimini al
    size_choice = input("Lütfen pizza boyutunuzu seçiniz (5-7): ")
    while size_choice not in ["5", "6", "7"]:
        size_choice = input("Lütfen geçerli bir pizza boyutu numarası seçiniz (5-7): ")

    # Seçilen pizzayı al
    if size_choice == "5":
        size = SmallSize(pizza)
    elif size_choice == "6":
        size = MediumSize(pizza)
    elif size_choice == "7":
        size = LargeSize(pizza)
    else:
        size = DominosPizza()

    # Kullanıcıdan sos seçimini al
    sos_choice = input("Lütfen sos seçiniz (11-16): ")
    while sos_choice not in ["11", "12", "13", "14", "15", "16"]:
        sos_choice = input("Lütfen geçerli bir sos harfi seçiniz (11-16): ")
    # Seçilen sosu al
    if sos_choice == "11":
        sos = ZeytinSos(pizza)
    elif sos_choice == "12":
        sos = MantarSos(pizza)
    elif sos_choice == "13":
        sos = KeciPeyniriSos(pizza)
    elif sos_choice == "14":
        sos = EtSos(pizza)
    elif sos_choice == "15":
        sos = SoganSos(pizza)
    else:
        sos = SoganSos(pizza)
    
    # Kullanıcı bilgilerinin alınması
    name = input("Adınız: ")
    id_no = input("TC Kimlik Numaranız: ")
    card_no = input("Kredi Kartı Numaranız: ")
    card_cvv = input("Kredi Kartı CVV Kodu: ")

    # Siparişin açıklamasının oluşturulması
    order_description = size.get_description() + " " + pizza.get_description() + " with" + sos.get_description()

    # Siparişin fiyatının hesaplanması
    total_cost = size.get_cost() + sos.get_cost()

    # Siparişin veritabanına kaydedilmesi
    add_order_to_database(name, id_no, card_no, order_description, card_cvv,total_cost)

    # Kullanıcıya sipariş detaylarının gösterilmesi
    print("Sipariş Detayları:")
    print("------------------")
    print("Ad: ", name)
    print("TC Kimlik Numarası: ", id_no)
    print("Kredi Kartı Numarası: ", card_no)
    print("Sipariş Açıklaması: ", order_description)
    print("Toplam Fiyat: ", total_cost)
    print("Sipariş Zamanı: ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    # Siparişi onayla
    print("\nSiparişiniz alınmıştır. Teşekkür ederiz!")

     

main()
     