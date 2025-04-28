
name = input('hey type your name: ')

print("Hello" + " " + name + " " + "welcome to my game!")

should_we_play =input("Do you want to play!").lower()

if should_we_play == "y" or should_we_play == "yes":
  print("we are gonna play!")

  direction =input("Do you want to go left or right?)(left/right)").lower()
  if direction=="left":
    print("you went left and fell of a cliff,game over,try again.!")

  elif direction == "right":
    choice = input(
    "ok,you now see abridge,do you want to swim under it or cross it?(swim/cross)"
    )
    if choice== "swim":
      print("you got eaten by an alligator,you die the end!")
  else:
    print("you found the gold and won!")
else :
    print("sorry not a valid replay,you die!")  