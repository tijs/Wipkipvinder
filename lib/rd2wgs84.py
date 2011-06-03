"""
2010.08.31, blue chips - Henkjan Faber

"""

import math
import sys

"""
Translates Rijksdriehoekscoordinaten to WGS84
Uses transformation formulae provided in Transformatieformules.pdf (from dekoepel.nl)
Specifically, formula 6 and table 4 from the pdf is used.

    > python rd2wgs84.py 233883.131 582065.167 #coordinates of martinitoren
    [53.219383166978588, 6.5682005290780019]

"""
def RD_to_WGS84(x, y):

    # table 3 from the pdf
    X0 = 155000.
    Y0 = 463000.
    phi0 = 52.15517440
    lambda0 = 5.38720621

    # table 4 from the pdf
    # K_pq = K_12 = K[1][2]
    # p = 0-5, q = 0-4
    K = [
        [ 0., 3235.65389, -.24750, -.06550, 0.],
        [ -.00738, -.00012, 0., 0., 0.],
        [ -32.58297, -.84978, -.01709, -.00039, 0.],
        [ 0., 0., 0., 0., 0.],
        [ .00530, 0.00033, 0., 0., 0.],
        [ 0., 0., 0., 0., 0.]
    ]
    L = [
        [ 0., .01199, 0.00022, 0., 0.],
        [ 5260.52916, 105.94684, 2.45656, .05594, .00128 ],
        [ -.00022, 0., 0., 0., 0.],
        [ -.81885, -.05607, -.00256, 0., 0.],
        [ 0., 0., 0., 0., 0.],
        [ .00026, 0., 0., 0., 0.]
    ]

    # formula 6
    dX = (x - X0) * .00001
    dY = (y - Y0) * .00001
    phi = 0.
    _lambda = 0.
    for q in range(0,5):
        for p in range(0,6):
            phi = phi + K[p][q] * math.pow(dX, p) * math.pow(dY, q)
            _lambda = _lambda + L[p][q] * math.pow(dX, p) * math.pow(dY, q)
    phi = phi0 + phi / 3600.
    _lambda = lambda0 + _lambda / 3600.

    return [ phi, _lambda ]

def convert(x, y):
    try:
      x = float(x)
      y = float(y)
    except:
      print "Coordinates should be numbers"
    else:
      coords = RD_to_WGS84(x, y)
      return coords


if __name__ == "__main__":
    try:
        convert(sys.argv[1], sys.argv[2])
    except:
      print "Please supply an X and Y value"

