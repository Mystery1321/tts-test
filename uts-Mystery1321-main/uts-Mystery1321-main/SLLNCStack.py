from Node import Node

class Stack: #SLLNC dengan head
    def __init__(self):
        self._head=None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def push(self, e): #sama dengan tambah depan
        self._data.append(data)
        self._size+= 1

    def pop(self): #hapus depan
        pass

    def printAll(self): #loop
        if self.isEmpty()==False:
            bantu = self._head
            while(bantu!=None):
                print(bantu._element," ",end='')
                bantu = bantu._next
                print()
        else:
            print("Kosong")