# #Single-Responsibility Principle (SRP) 
# from pathlib import Path 
# from zipfile import ZipFile 
 
# class FileManager: 
#     def __init__(self, filename): 
#         self.path = Path(filename) 
 
#     def read(self, encoding="utf-8"): 
#         return self.path.read_text(encoding) 
 
#     def write(self, data, encoding="utf-8"): 
#         self.path.write_text(data, encoding) 
 
# class ZipFileManager: 
#     def __init__(self, filename): 
#         self.path = Path(filename) 
 
#     def compress(self): 
#         with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive: 
#             archive.write(self.path) 
#     def decompress(self): 
#         with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive: 
#             archive.extractall() 

# #Open-Closed Principle (OCP)
# from math import pi
# class Shape(): 
#     def calculate_area(self): 
#         pass 
 
# class Circle(Shape): 
#     def __init__(self, radius): 
#         self.radius = radius 
 
#     def calculate_area(self): 
#         return pi * self.radius**2 
 
# class Rectangle(Shape): 
#     def __init__(self, width, height): 
#         self.width = width 
#         self.height = height 
 
#     def calculate_area(self): 
#         return self.width * self.height 
 
# class Square(Shape): 
#     def __init__(self, side): 
#         self.side = side 
 
#     def calculate_area(self): 
#         return self.side**2

# #Liskov Substitution Principle (LSP)
# class Bird:
#     def fly(self):
#         pass

# class Sparrow(Bird):
#     def fly(self):
#         print("Sparrow is flying")

# class Penguin(Bird):
#     def fly(self):
#         raise Exception("Penguin can't fly")
        
# #Interface Segregation Principle (ISP)
# class Flyable:
#     def fly(self):
#         pass

# class Swimmable:
#     def swim(self):
#         pass

# class Duck(Flyable, Swimmable):
#     def fly(self):
#         print("Duck is flying")

#     def swim(self):
#         print("Duck is swimming")

# #Dependency Inversion Principle (DIP)
# class FrontEnd: 
#     def __init__(self, data_source): 
#         self.data_source = data_source 
#     def display_data(self): 
#         data = self.data_source.get_data() 
#         print("Display data:", data) 
 
# class DataSource(): 
#     def get_data(self): 
#         pass 
 
# class Database(DataSource): 
#     def get_data(self): 
#         return "Data from the database" 
 
# class API(DataSource): 
#     def get_data(self): 
#         return "Data from the API"