energies = []
for path in files:
    try:
        energies.append(read_energy(path))
    except FileNotFoundError:
        print(f"Missing file: {path}")

print(sum(energies) / len(energies))
