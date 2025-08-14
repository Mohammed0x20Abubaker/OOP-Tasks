class Phone:
    def __init__(self):
        self.__book = {}

    def add_contact(self, name, phone_no):
        self.__book[name] = phone_no

    def remove_contact(self, name):
        keys = self.__book.keys()
        if name in keys:
            del self.__book[name]
        else:
            print("Not found")

    def make_call(self, name):
        keys = self.__book.keys()
        if name in keys:
            print("calling")
        else:
            print(f"No results for {name}")

    def view_contacts(self):
        print(self.__book)


class Camera:
    def __init__(self):
        pass

    def take_photo(self):
        print("The picture was taken successfully")


class SmartPhone(Phone, Camera):
    def __init__(self):
        super().__init__()


phone = SmartPhone()

while True:
    user = input(
        "To open contacts enter the following : contacts , To open camera enter the following: camera , quit : quit/q \n").lower().strip()
    if user in ["contacts"]:
        choice = input(
            "Add Contacts : A/add ,Remove contact : R/remove,To view all contacts : v/view , quit : quit/q \n").lower().strip()
        if choice in ["add", "a"]:
            num_of_contacts = int(input("No. of contacts :"))
            for i in range(num_of_contacts):
                name = input("Contact name : ").lower().strip()
                phonenum = input("Phone number : ")
                phone.add_contact(name, phonenum)
        elif choice in ["remove", "r"]:
            name = input("Contact name to be removed : ").lower().strip()
            phone.remove_contact(name)
        elif choice in ["view", "v"]:
            phone.view_contacts()
        elif user in ["quit", "q"]:
            break
        else:
            print("Unspecified input")

    elif user in ["camera"]:
        phone.take_photo()

    elif user in ["quit", "q"]:
        break

    else:
        print("Unspecified input")
