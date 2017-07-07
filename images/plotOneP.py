
import matplotlib
matplotlib.use('PS')
import matplotlib.pyplot as plt

#plot parameter things:
lbl_size = 24
lgd_size = 20
mrks = 9
lw = 3
fontsize = 24
matplotlib.rcParams.update({'font.size': fontsize, 'text.usetex': True, "ps.usedistiller" : "xpdf"})


def readData(path):

    xs = []
    ys = []

    with open( path, 'r' ) as readFile:
        for line in readFile:

            x, y = line.split()

            xs.append( float(x) )
            ys.append( float(y) )

    return ( xs, ys )


def plotProbs(E):

    Qup1 = readData( "./images/data/HepUpToI-E" + str(E) + ".txt" )
    Qup2 = readData( "./images/data/HeUpToI-E"  + str(E) + ".txt" )
    Qdn1 = readData( "./images/data/HeDnToI-E"  + str(E) + ".txt" )

    Cup1 = readData( "./images/data/HepUpToO-E" + str(E) + ".txt" )
    Cup2 = readData( "./images/data/HeUpToO-E"  + str(E) + ".txt" )
    Cdn1 = readData( "./images/data/HeDnToO-E"  + str(E) + ".txt" )

    fig = plt.figure(1, figsize = (12,10))

    plt.figure(1)

    plt.plot( Qup2[0], Qup2[1], "--", color = "#0000FF", linewidth = 0.5 * lw,
              label = r"$\mathrm{He}(\uparrow_1)$ $\rightarrow$ $I$" )
    plt.plot( Qdn1[0], Qdn1[1], ":", color = "#0000FF", linewidth = 0.5 * lw,
              label = r"$\mathrm{He}(\downarrow_1)$ $\rightarrow$ $I$" )
    plt.plot( Qup1[0], Qup1[1], "-", color = "#0000FF", linewidth = 0.5 * lw,
              label = r"$\mathrm{He}^{+}(\uparrow_2)$ $\rightarrow$ $I$" )

    plt.plot( Cup2[0], Cup2[1], "--", color = "#008000", linewidth = 1.1 * lw,
              label = r"$\mathrm{He}(\uparrow_1)$ $\rightarrow$ $\mathrm{He}^{+}$" )
    plt.plot( Cdn1[0], Cdn1[1], ":", color = "#008000", linewidth = 1.1 * lw,
              label = r"$\mathrm{He}(\downarrow_1)$ $\rightarrow$ $\mathrm{He}^{+}$" )
    plt.plot( Cup1[0], Cup1[1], "-", color = "#008000", linewidth = 1.1 * lw,
             label = r"$\mathrm{He}^{+}(\uparrow_2)$ $\rightarrow$ $\mathrm{He}$" )

    plt.xlabel("$\mathrm{b}$ $[\mathrm{a.u.}]$")
    plt.ylabel("$p(b)$")
    plt.xlim([0,5])
    plt.ylim( ymin = 0 )

    plt.legend( loc="best", fancybox=True, labelspacing = .2 )

    leg = plt.gca().get_legend()
    ltext  = leg.get_texts()
    plt.setp(ltext, fontsize = lgd_size)

    ax = plt.gca()
    ax.xaxis.set_tick_params(which='both', width=2)
    ax.yaxis.set_tick_params(which='both', width=2)

    ax.xaxis.set_tick_params(which='major', length=8)
    ax.yaxis.set_tick_params(which='major', length=8)
    ax.xaxis.set_tick_params(which='minor', length=5)
    ax.yaxis.set_tick_params(which='minor', length=5) 

    fig.savefig('./images/hephe-pb-{0}.eps'.format(E),
                format = 'eps', dpi = 20000, bbox_inches='tight')
    fig.clear()

    return


if __name__ == "__main__":

    plotProbs( 40 )

