class SimpleList:
    def __init__(self, items) -> None:
        self.items = list(items)

    def add(self, item):
        self.items.append(item)
        
    def __getitem__(self, idx):
        return self.items[idx]
    
    def __len__(self):
        return len(self.items)

class SortedList(SimpleList):
    def __init__(self, items) -> None:
        super().__init__(items) 
        self.items.sort()

    def add(self, item):
        super().add(item)
        self.items.sort()


class IntList(SimpleList):
    def __init__(self, items) -> None:
        for x in items:
            if isinstance(x, int) == False:
                raise TypeError("Data provided is not an integer.")
        super().__init__(items)

    def add(self, item):
        if isinstance(item, int) == False:
            raise TypeError("Data provided is not an integer.")
        super().add(item)

class PositiveIntList(IntList):
    def __init__(self, items) -> None:
        for x in items:
            if x < 0:
                raise ValueError("Datapoint in negative range")
        super().__init__(items)
    
    def add(self, item):
        if item < 0:
            raise TypeError
        super().add(item)

def Main():
    try:
        l1 = SimpleList((23, 11, 46, 7))
        l1.add(34)
        # conn.close()
    except (ValueError, TypeError) as ex:
        print("Exception raised, and handled\n", ex)
        # conn.close()
        raise
    finally:
        # conn.close()
        pass
    
    print(l1[2])

    sl1 = SortedList((23, 11, 45, 27))
    sl1.add(26)
    sl1.add(943)

    for x in range(len(sl1)):
        print(sl1[x], end=", ")
    print("\n")

Main()