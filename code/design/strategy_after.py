def work(force, a, b, method, n=101):
    xs = np.linspace(a, b, n)
    return method.integrate(force(xs), xs)


work(spring, 0, 0.1, Trapezoid())
work(spring, 0, 0.1, Simpson())
