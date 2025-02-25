


class Animal:

    def __init__(self) -> None:
        
        self.mutation: bool = True 

        self.cat = Cat(mutation=self.mutation)

    def change_mutation_state(self) -> None:
        self.mutation = False

        print("This is the self.mutation state: ", self.mutation)
        print("This is the cat self.mutation state: ", self.cat.mutation)
    
class Cat: 

    def __init__(self, mutation: bool) -> None:
        
        self.mutation: bool = mutation


if __name__ == "__main__":
    
    animal1 = Animal()

    animal1.change_mutation_state()
