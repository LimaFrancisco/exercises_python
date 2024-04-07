from point import Point

class Rectangle:

    # contructor
    def __init__(self, bottom_left_vertex: Point, height: float, width: float) -> None:
        self.__bottom_left_vertex = bottom_left_vertex
        self.__height = height
        self.__width = width

    # getters
    def get_bottom_left_vertex(self) -> Point:
        return self.__bottom_left_vertex

    def get_height(self) -> float:
        return self.__height
    
    def get_width(self) -> float:
        return self.__width
    
    # setters
    def set_bottom_left_vertex(self, new_bottom_left_vertex: Point) -> Point:
        if isinstance(new_bottom_left_vertex, Point):
            self.__bottom_left_vertex = new_bottom_left_vertex

    def set_height(self, new_height: float) -> None:
        if isinstance(new_height, float):
            self.__height = new_height

    def set_width(self, new_width: float) -> None:
        if isinstance(new_width, float):
            self.__width = new_width

    # other methods
    def find_center(self) -> Point:
        vertical_center = self.get_height() / 2
        horizontal_center = self.get_width() / 2
        center = Point(vertical_center , horizontal_center)
        center.print_values()
         