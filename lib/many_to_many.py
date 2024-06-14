class Author:
    all = []

    @classmethod
    def add_to_all(cls,author):
        cls.all.append(author)

    def __init__(self,name):
        if isinstance(name,str):
            self.name = name
        else:
            raise Exception(f'{name} is not a string')
        self.add_to_all(self)     

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]

    def sign_contract(self,book,date,royalties):
        return Contract(self,book,date,royalties)

    def total_royalties(self):
        return sum([contract.royalties for contract in Contract.all if contract.author == self])    


class Book:
    all = []

    @classmethod
    def add_to_all(cls,book):
        cls.all.append(book)    

    def __init__(self,title):
        if isinstance(title,str):
            self.title = title
        else:
            raise Exception(f'{title} is not a string')
        self.add_to_all(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]        
    pass


class Contract:
    all = []

    @classmethod
    def add_to_all(cls,contract):
        cls.all.append(contract)

    @classmethod
    def contracts_by_date(cls,date):
        return [contract for contract in cls.all if contract.date == date]    

    def __init__(self,author,book,date,royalties):
        if isinstance(author,Author):
            self.author = author
        else:
            raise Exception(f'{author} is not an Author object')
        if isinstance(book,Book):
            self.book = book
        else:
            raise Exception(f'{book} is not a Book object')
        if isinstance(date,str):
            self.date = date
        else:
            raise Exception(f'{date} is not a string')
        if isinstance(royalties,int):
            self.royalties = royalties
        else:
            raise Exception(f'{royalties} is not an integer')
        self.add_to_all(self)
    pass