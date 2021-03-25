class Student:
  def __init__(self, name, year, gr):
    self.name = name
    self.year = year
    self.gr = gr
    
  
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.gr.append(grade)
  def __repr__(self):
    return self.gr
            

class Grade:
  minimum_passing = 65
  
  def __init__(self, score):
    self.score = score
    
roger = Student("Roger van der Weyden", 10 ,[])
sandro = Student("Sandro Botticelli", 12 , [])
pieter = Student("Pieter Bruegel the Elder", 8, [])
pieter.add_grade(Grade(100))
print(pieter.name)
print(pieter.year)
print(repr(pieter.gr))


#learn how to print that list gr in the class 