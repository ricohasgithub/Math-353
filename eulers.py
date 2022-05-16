
# Methods to be integrated
def method_2_7_1():
    pass

# Performs euler's method with step h on callback func f for up to n steps
def eulers_method(f, h, t0, y0, n, verbose=True):

    tn = t0
    yn = y0
    fn = 0

    for i in range(0, n):

        # Find slope via derivative eq callback
        tn = tn + h
        fn = f(tn, yn)
        yn = yn + fn * tn

        if verbose:
            print("n: {} tn: {} yn: {} fn: {}".format(n, tn, yn, fn))

        n = n + 1