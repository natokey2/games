
name = input('hey type your name: ')

print("Hello" + " " + name + " " + "welcome to my game!")

should_we_play =input("Do you want to play!").lower()

if should_we_play == "y" or should_we_play == "yes":
  print("we are gonna play!")

  direction =input("Do you want to go left or right?)(left/right)").lower()
  if direction=="left":
    print("okay we went left")

  elif direction == "right":
    print("we went right")
  else:
    print("sorry not a valid replay,you die!")  