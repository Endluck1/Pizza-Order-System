#gerekli kitaplıkları içeri aktarma
import csv
import datetime

#menüyü ekrana yazdırıyoruz
file = open("menu.txt", "r")
print(file.read())

#Pizza üst sınıfını oluşturuyoruz.
class Pizza:
    def get_description(self): 
        return self.__class__.__name__

    def get_cost(self): 
        return self.__class__.cost 
#Pizza alt sınıflarını oluşturuyoruz.
    def __init__(self):
        self.description = "Bilinmeyen Pizza"
    
    def get_description(self):
        return self.description

    def get_cost(self):
        return 0.0

class KlasikPizza(Pizza):
    def __init__(self):
        self.description = "Klasik Pizza"
    
    def get_cost(self):
        return 8.99

class MargheritaPizza(Pizza):
    def __init__(self):
        self.description = "Margherita Pizza"
    
    def get_cost(self):
        return 9.99

class TürkPizza(Pizza):
    def __init__(self):
        self.description = "Türk Pizza"
    
    def get_cost(self):
        return 10.99
class SadePizza(Pizza):
    def __init__(self):
        self.description = "Sade Pizza"
    
    def get_cost(self):
        return 6.99    

#Decorator üst sınıf oluşturulacak.
class Decorator(Pizza):
    def __init__(self, component):
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)

#Decorator alt sınıf oluşturulacak 
class Zeytin(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Zeytin"
    
    def get_cost(self):
        return self.component.get_cost() + 1.99

class Mantar(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Mantar"
    
    def get_cost(self):
        return self.component.get_cost() + 2.99

class Keçipeyniri(Decorator):
    def __init__(self, component):
        Decorator.__init__(self,component)
        self.description = "Keçi Peyniri" 
    def get_cost(self):
        return self.component.get_cost() + 3.99

class Et(Decorator):
    def __init__(self,component):
        Decorator.__init__(self,component)
        self.description = "Et"
    def get_cost(self):
        return self.component.get_cost() + 6.99

class Soğan(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Soğan"
    
    def get_cost(self):
        return self.component.get_cost() + 0.99   

class Mısır(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Mısır"
    
    def get_cost(self):
        return self.component.get_cost() + 3.99      
               
def main():
    print("Pizza restoranımıza hoş geldiniz!")
    while True:

     print("Lütfen Bir Pizza Seçin:")
     print("1: Klasik")
     print("2: Margherita")
     print("3: Türk")
     print("4: Sade")
     pizza_choice = input("Sizin Seçiminiz:")

     if pizza_choice == "1":
        pizza = KlasikPizza()
        break
     elif pizza_choice == "2":
        pizza = MargheritaPizza()
        break
     elif pizza_choice == "3":
        pizza = TürkPizza()
        break
     elif pizza_choice == "4":
        pizza = SadePizza()
        break
     else:
        print("Geçersiz Seçim, Lütfen Tekrar Deneyin.")
        
     
    while True:
   
     print("Lütfen Bir Sos Seçin Seçimiz Bitince 0 tuşlayınız:")
     print("1: Zeytin")
     print("2: Mantar")
     print("3: Keçi Peyniri")
     print("4: Et")
     print("5: Soğan")
     print("6: Mısır")
     topping_choice = input("Sizin Seçiminiz: ")

     if topping_choice == "0":
      break
     if topping_choice == "1":
      pizza = Zeytin(pizza)
     elif topping_choice == "2":
        pizza = Mantar(pizza)
     elif topping_choice == "3":
        pizza = Keçipeyniri(pizza)
     elif topping_choice == "4":
        pizza = Et(pizza)
     elif topping_choice == "5":
        pizza = Soğan(pizza)
     elif topping_choice == "6":
        pizza = Mısır(pizza)
     else:
        print("Geçersiz Seçim, Lütfen Tekrar Deneyin.")

    print("Sipariş Verdiğiniz İçin Teşekkürler!")
    print("Pizza Maliyetiniz: ₺", pizza.get_cost())

#Sipariş Bilgi Kartı oluşturuyoruz.
    print("Sipariş Bilgileri")
    name = input("Lütfen İsminizi Girin: ")
    id_number = input("Lütfen TC kimliğinizi Girin : ")
    card_number = input("Lütfen Kart Numaranızı Girin: ")
    card_password = input("Lütfen Kart Şifrenizi Girin: ")

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("Orders_Database.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([pizza.get_description(), name, id_number, card_number, current_time, card_password])
        
if __name__ == "__main__":
    main()
