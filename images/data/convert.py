
import numpy as np
from scipy.interpolate import interp1d


def readData(path):

    xs = []
    ys = []

    with open(path, 'r') as readFile:
        for line in readFile:

            x, y = line.split()
            xs.append( float(x) )
            ys.append( float(y) )

    return (xs, ys)


def writeData(xs, ys, path):

    with open(path, 'w') as writeFile:
        for i in range(len(xs)):

            line = "{x}   {y}\n".format( x = xs[i], y = ys[i])

            writeFile.write( line )

    return


if __name__ == "__main__":

    data1 = readData("SM03-1.txt")
    data2 = readData("SM03-2.txt")
    data3 = readData("SM03-3.txt")
    data4 = readData("SM03-4.txt")

    curve1 = interp1d( data1[0], data1[1], kind = 'cubic' )
    curve2 = interp1d( data2[0], data2[1], kind = 'cubic' )
    curve3 = interp1d( data3[0], data3[1], kind = 'cubic' )
    curve4 = interp1d( data4[0], data4[1], kind = 'cubic' )


    Es = np.linspace( 0.7, 4, num = 30, endpoint=True)

    s02 = curve2(Es)
    s03 = curve4(Es)
    s01 = curve1(Es) - (s02 - s03)

    writeData( Es, s01, "SM03-s01.txt")
    writeData( Es, s02, "SM03-s02.txt")
    writeData( Es, s03, "SM03-s03.txt")

