
# Methods to be integrated, must have (tn, yn) as input
def method_2_7_1(tn, yn):
    return 3 + tn - yn

# Performs euler's method with step h on callback func f for up to n steps
def eulers_method(f, h, t0, y0, n, verbose=True):

    i = 0
    tn = t0
    yn = y0

    if verbose:
        print("n: {} tn: {} yn: {} fn: {}".format(i, tn, yn, f(tn, yn)))

    i = i + 1

    for i in range(1, n):

        # Find slope via derivative eq callback
        yn = yn + f(tn, yn) * h
        tn = tn + h

        if verbose:
            print("n: {} tn: {} yn: {} fn: {}".format(i, round(tn, 3), round(yn, 5), round(f(tn, yn), 5)))

        i = i + 1

# Finds runs eulers up to a final time tf
def eulers_endpoint(f, h, t0, y0, tf, verbose=True):
    
    i = 0
    tn = t0
    yn = y0

    if verbose:
        print("n: {} tn: {} yn: {} fn: {}".format(i, tn, yn, f(tn, yn)))

    i = i + 1

    while True:

        # Find slope via derivative eq callback
        yn = yn + f(tn, yn) * h
        tn = tn + h

        if verbose:
            print("n: {} tn: {} yn: {} fn: {}".format(i, round(tn, 3), round(yn, 5), round(f(tn, yn), 5)))

        i = i + 1

        if tn >= tf:
            break

eulers_endpoint(method_2_7_1, 0.05, 0, 1, 0.4)