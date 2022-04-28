class TD3:
    
    def __init__(self, a, b) -> None:
        self.mrz1 = a
        self.mrz2 =  b
    
    def __parse__(self):
        

        if len(self.mrz1) < 44:
            self.mrz1 = self.mrz1 + '<' *(44 - len(self.mrz1))
        if len(self.mrz2) < 44 :
            self.mrz2 = self.mrz2 + '<'*(44 - len(self.mrz2))
        
        self.ptype = self.mrz1[0:2]
        
        self.country =  self.mrz1[2:5]
        
        

        surname_names  = self.mrz1[5:44].split('<<',1)

        

        if len(surname_names) < 2:
            surname_names += ['']
        
        surname, names  = surname_names

        self.names  =  names.replace('<', ' ').strip()
        self.surname  = surname.replace('<',' ').strip()
        self.number = self.mrz2[0:9]

    
        self.nationality = self.mrz2[10:13]
        self.dob = self.mrz2[13:19]
        self.sex = self.mrz2[20]
        self.expiry  = self.mrz2[21:27]
    
    def __str__(self) -> str:
        self.__parse__()
        return str({"type": self.ptype, "nationality": self.nationality, "surname": self.surname, "names": self.names,
         "sex": self.sex,"dob":self.dob, "expiry_date":self.expiry, "number": self.number,"country": self.country})
    
    def values(self) -> dict:
        self.__parse__()
        return {"type": self.ptype, "nationality": self.nationality, "surname": self.surname, "names": self.names,
         "sex": self.sex,"dob":self.dob, "expiry_date":self.expiry, "number": self.number,"country": self.country}
    
    def parse(self):
        self.__parse__()
        return self


#Examples

a = TD3("P<NGAOJO<<GABRIEL<SUSAN<<<<<<<<<<<<<<<<<<<<<","A119274455NGA9908181M2606107<<<<<<<<<<<<<<06")

print(a)

val = a.values()

print(val["names"])

from datetime import datetime
print(datetime.strptime(val["expiry_date"], '%y%m%d'))


td = a.parse()

print(td.number, td.names, td.expiry, td.country)
