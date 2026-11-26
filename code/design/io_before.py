def mean_energy(path):
    data = np.loadtxt(path)
    result = data[:, 3].mean()
    print(f"Mean energy: {result}")
    return result
