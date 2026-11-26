def simple_computation(data):
    import numpy as np
    import matplotlib.pyplot as plt
    f = open("C:/Users/john/Desktop/params.txt")
    params = f.read().split(",")
    a = float(params[0])
    b = float(params[1])
    # b = 0.5
    result = []
    for i in range(len(data)):
        if data[i][3] > 0:
            x = data[i][3] * 0.0259
            if x > a:
                if x < b:
                    result.append(x)
                else:
                    result.append(b)
            else:
                pass
    try:
        fit = np.polyfit(range(len(result)), result, 2)
    except:
        pass
    plt.plot(result)
    plt.savefig("fig_final_v2.png")
    np.savetxt("out.txt", result)
    for i in range(len(result)):
        result[i] = result[i] / fit[0]
