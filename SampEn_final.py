import numpy as np


def SampEn(data, m, r):

    # m: długość próbki (okna) - the length of template
    # r: zakładane odchylenie standardowe - assumed standard deviation

    #data = (data - np.mean(data)) / np.std(data)

    r = np.std(data) * r

    def phi(input_data, input_m, input_r):

        N = len(input_data)
        all_matches = []
        for i in range(0, N - input_m):

            xmi = input_data[i:i + input_m]

            xmj = np.array([input_data[i: i + input_m] for i in range(i+1, N - input_m + 1)])
            matches = np.sum(np.abs(xmi - xmj).max(axis=1) <= input_r)

            all_matches.append(matches / (N - input_m + 1))

        phi_i = sum(all_matches)/(N - input_m + 1)

        return phi_i

    B = phi(data, m, r)
    A = phi(data, m + 1, r)
    if B>0:
        output = -np.log(A / B)
    else:
        output = None

    return output



