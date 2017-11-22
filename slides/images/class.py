
class Vehicle:
    """Documentation.

    We use a simple multi-line string for this.  It's a habit.
    """

    # Class variable.
    class_var = 10

    # Constructor.
    def __init__(self):
        # Instance variable.
        self.instance_var = 11

    # Method.
    def show(self, argument):
        print("My class variable is %s." % self.class_var)
        print("My instance variable is %s." % self.instance_var)
        print("And the argument you gave me is %s." % argument)



