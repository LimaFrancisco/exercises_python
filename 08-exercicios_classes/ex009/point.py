class Point:

    # constructor
    def __init__(self, x: float, y: float) -> None:
        self.__x = x
        self.__y = y

    # getters
    def get_x(self) -> float:
        return self.__x
    
    def get_y(self) -> float:
        return self.__y
    
    # setters
    def set_x(self, new_x: float) -> None:
        self.__x = new_x

    def set_y(self, new_y: float) -> None:
            self.__y = new_y

    # other methods 
    def print_values(self) -> None:
        print(f"x: {self.get_x():.2f}\ny: {self.get_y():.2f}")
