energies = []
for path in files:
    try:
        energies.append(read_energy(path))
    except:
        pass

print(sum(energies) / len(energies))
