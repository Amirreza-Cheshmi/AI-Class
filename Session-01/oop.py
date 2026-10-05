class std:
    def __init__(self, name : str, std_id : int, field: str):
        self.name=name
        self.std_id=std_id
        self.field=field

    def Show(self):
        print("information student :")
        print(self.name)
        print(self.std_id)
        print(self.field)
        print("")
    
    def edit_stdnumber(self, new_id : int):
        self.std_id = new_id
        self.Show()


std1=std("ali",127689,"Ai")
std2=std("mmd",547812,"Game")

std1.Show()
std2.Show()

print("update information => ")
std1.edit_stdnumber(123456)
std2.edit_stdnumber(987765)
