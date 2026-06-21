try:
    number = int(input("Enter a number: "))
    print(1/number)
# except Exception as e:
    # print("Something went wrong!")
except ZeroDivisionError:
    print("You cant divide by zero!")
except ValueError:
    print("Please enter a valid number!")
except TypeError:
    print("Invalid type!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("This will always be executed, regardless of whether an exception occurred or not.")
