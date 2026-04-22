class MyError(Exception):
    pass

try:
    x = int(input())
    if x < 0:
        raise MyError("Negative number")
finally:
    print("Execution complete")