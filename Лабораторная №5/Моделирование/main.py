import matplotlib.pyplot as plt
import math


def main():
    dt = 0.001
    k = 400
    E = 1.0
    T = 0.0014
    tau = 0
    tau = 0.0021464 #tau=taukr
    tau = 0.0026 #tau>taukr
    tau = 0.0016 #tau<taukr

    w = 250
    L = 710
    Re = []
    Im = []

    while w < L:
        Aw = k / (w * math.sqrt((1 - T ** 2 * w ** 2) ** 2 + 4 * E ** 2 * T ** 2 * w ** 2))
        Phi = - math.pi / 2 - math.atan((2 * E * T * w) / (1 - T ** 2 * w ** 2)) - tau * w
        x = Aw * math.cos(Phi)
        y = Aw * math.sin(Phi)
        if Aw >= 1 and Aw <= 1.000001:
            w_kr = w
            tau_r = (math.pi + Phi) / w_kr
            Phi_kr = Phi
            print(w_kr, tau_r, Phi)
        Re.append(x)
        Im.append(y)
        w += dt

    Cir_X = []
    Cir_Y = []
    x = 0
    radius = 1
    x_krit = 6.5
    while x < x_krit:
        Cir_X.append(radius * math.cos(x))
        Cir_Y.append(radius * math.sin(x))
        x += 0.01

    plt.grid()
    plt.scatter(-1, 0, label="Точка (-1; 0j)")
    #plt.text(-0.09,-2.4,"w кр = 329.73, tau кр = 0.0021464")
    plt.plot(Re, Im)
    plt.plot(Cir_X, Cir_Y)
    plt.xlabel("Re")
    plt.ylabel("Im")

    plt.legend()
    plt.title("АФЧХ разомкнутой системы")
    plt.show()


if __name__ == "__main__":
    main()
