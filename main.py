# input the data
# input the character/word
# print the position

options = ("charcter,\nline count :\n")
choice = input("what is your choice? :\n" +options).lower()
if choice == "character":
  data = input("insert the data: \n")
  find = input("insert word/character you want to find: \n")
  pos= data.find(find)
  print(pos)
if choice == "line count":
  data = input("insert the data: \n")
  fhand = open("data")
  count = 0
  for line in fhand:
    count = count+1
  print("line count:", count)