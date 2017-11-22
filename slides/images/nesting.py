

def foo(arg):
    try:
        if arg > 2:
            print("It's not trivial.")
            if arg % 2 == 1:
                print("In fact, it's a little odd.")
            else:
                for smaller in range(arg):
                    if smaller == arg / 2:
                        print("%d is only the half of it." % smaller)
    finally:
        print("Sod it.")


