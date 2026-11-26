forces = [Gravity(), Drag()]
total = sum(f.force(body) for f in forces)
