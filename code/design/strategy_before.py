def work_trapezoid(force, a, b, n=101):
    xs = np.linspace(a, b, n)
    return np.trapezoid(force(xs), xs)


def work_simpson(force, a, b, n=101):
    xs = np.linspace(a, b, n)
    return simpson(force(xs), x=xs)
