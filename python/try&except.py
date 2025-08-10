#exception = events detected during execution that interupt the flow of a program

try: 
    numerator = int (input("enter a number to divide: "))
    denominator = int (input("enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError:
    print("don't be stupid")
# except Exception:
#     print("somethings went wrong :(")
except ValueError:
    print("enter only number please!!!")
else:
    print(result)
finally:
    ("good")