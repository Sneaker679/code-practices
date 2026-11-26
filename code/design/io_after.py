def mean_energy(energies):
    return energies.mean()


energies = np.loadtxt(path)[:, 3]
result = mean_energy(energies)
print(f"Mean energy: {result}")
