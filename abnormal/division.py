print("Give me two numbets,and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number=input("\nFirst number:")
    if first_number == 'q':
        break
   second_number=input("\nSecond number:")

   try:
       answer=int(first_number)/int(second_number)
   except ZeroDivisionError:
       print("YOU can't  divide by 0!")
   else:
       print(answer)

