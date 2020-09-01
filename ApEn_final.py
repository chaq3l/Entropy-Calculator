import numpy as np


def ApEn(data, m, r, Chebyshev, Euclidean, calc_normal, calc_approx):

    # m: długość próbki (okna) - the length of template
    # r: zakładane odchylenie standardowe - assumed standard deviation
    # N_start i N_stop lepiej zrobić, żeby było sprawdzane w aplikacji
    # w aplikacji jest ptaszek do zaznaczania i można go wykorzystać

    r = np.std(data) * r

    def calc_Chebyshev_matches(xmi, xmj, input_r):
        matches = np.sum(np.abs(xmi - xmj).max(axis=1) <= input_r)
        return matches

    def calc_Euclidean_matches(xmi, xmj, input_r):
        matches = np.sum(np.sqrt(((xmi - xmj)**2).sum(axis=1)) <= input_r)
        return matches

    def phi(input_data, input_m, input_r):

        N = len(input_data)
        all_Chebyshev_matches = []
        all_Euclidean_matches = []
        for i in range(0, N - input_m+1):

            xmi = input_data[i:i + input_m]

            xmj = np.array([input_data[j: j + input_m] for j in range(i, N - input_m + 1)])

            if Chebyshev:
                Chebyshev_matches = calc_Chebyshev_matches(xmi, xmj, input_r)
                all_Chebyshev_matches.append(Chebyshev_matches / (N - input_m + 1))

            else:
                all_Chebyshev_matches = None


            if Euclidean:
                Euclidean_matches = calc_Euclidean_matches(xmi, xmj, input_r)
                all_Euclidean_matches.append(Euclidean_matches / (N - input_m + 1))

            else:
                all_Euclidean_matches = None

        if all_Chebyshev_matches != None:
            Chebyshev_phi_for_full_method = np.sum(np.log(all_Chebyshev_matches)) / (N - input_m + 1)
        else:
            Chebyshev_phi_for_full_method = None
        if all_Euclidean_matches != None:
            Euclidean_phi_for_full_method = np.sum(np.log(all_Euclidean_matches)) / (N - input_m + 1)
        else:
            Euclidean_phi_for_full_method = None
        # trzeba będzie zreturnować all_Euclidean_matches i all_Chebyshev_matches i póżniej to wykożystać dalej
        return [all_Chebyshev_matches, all_Euclidean_matches, Chebyshev_phi_for_full_method,
                Euclidean_phi_for_full_method]

        #dokończyć


    B = phi(data, m, r)
    A = phi(data, m + 1, r)

    if calc_normal:
        if B[2] != None:
            Chebyshev_full_method = B[2] - A[2]
        else:
            Chebyshev_full_method = None
        if B[3] != None:
            Euclidean_full_method = B[3] - A[3]
        else:
            Euclidean_full_method = None

    else:
        Chebyshev_full_method = None
        Euclidean_full_method = None

    if calc_approx:
        if Chebyshev:
            B_approx_Chebyshev = B[0]
            A_approx_Chebyshev = A[0]
            C = []
            for i in range(len(A_approx_Chebyshev)):
                C.append(np.log(B_approx_Chebyshev[i] / A_approx_Chebyshev[i]))
            approx_Chebyshev = np.sum(C) / (len(data) - m)
        else:
            approx_Chebyshev = None

        if Euclidean:
            B_approx_Euclidean = B[1]
            A_approx_Euclidean = A[1]
            C = []
            for i in range(len(A_approx_Euclidean)):
                C.append(np.log(B_approx_Euclidean[i] / A_approx_Euclidean[i]))
            approx_Euclidean = np.sum(C) / (len(data) - m)
        else:
            approx_Euclidean = None
    else:
        approx_Chebyshev = None
        approx_Euclidean = None

    return [approx_Chebyshev, approx_Euclidean, Chebyshev_full_method, Euclidean_full_method]



