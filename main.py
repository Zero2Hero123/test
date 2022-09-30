from Human import Human

me = Human("Hero",15)

def greet(human_obj: Human):

  print(f"Hello, {human_obj.name}")

greet(me)