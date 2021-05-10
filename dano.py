dano = {'apple': 800, 'banana': 600, 'milk': 700}
def func(arg):
  key = (arg.keys())
  for key, value in arg.items():
          simple = round(arg.get(key) * 1.15)
          if simple % 10 > 5:
            arg[key] = simple  + 10 - (simple % 10)      
          if simple % 10 < 5:
             arg[key] = simple - (simple % 10)
          if simple % 10 == 5:
            arg[key] = simple
  return arg           
func(dano)