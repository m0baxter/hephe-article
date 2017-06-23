
import numpy as np
import matplotlib
matplotlib.use('cairo')
import matplotlib.pyplot as plt


#Dubois 89:
Dub89_111 = [ [ 16.7,    25,      33.3,    37.5,    50,     75,     100,    175,  250,     375,    500    ],
              [ 0.339,   0.542,   0.647,   0.882,   0.975,  1.08,   1.07,   1.00, 0.879,   0.628,   0.560  ],
              [ 0.06102, 0.09756, 0.11646, 0.15876, 0.1755, 0.1944, 0.1926, 0.18, 0.15822, 0.11304, 0.1008 ] ]

Dub89_012 = [ [ 33.3,     37.5,    50,      75,       100,     175,     250,     375,     500      ], 
              [ 0.0129,   0.0268,  0.0461,  0.0553,   0.0545,  0.0386,  0.0248,  0.0127,  0.0087   ],
              [ 0.002322, 0.00804, 0.01383, 0.009954, 0.00981, 0.01158, 0.00744, 0.00381, 0.001566 ] ]

Dub89_021 = [ [ 16.7,     25,      33.3,    37.5,    50,      75,       100,     175,     250,      375,     500       ],
              [ 0.0348,   0.059,   0.0817,  0.113,   0.106,   0.0719,   0.0475,  0.0140,  0.00522,  0.00130, 0.000584  ],
              [ 0.006264, 0.01062, 0.01471, 0.02034, 0.01908, 0.012942, 0.00855, 0.00252, 0.001566, 0.00039, 0.0001752 ] ]

Dub89_120 = [ [ 3.33,  8.33, 16.7,   25,     33.3,   37.5,   50,    75,      100,   175,      250,      375,       500      ],
              [ 5.9,   4.5,  3.06,   2.39,   1.97,   1.79,   1.20,  0.503,   0.300, 0.0886,   0.0317,   0.00871,   0.00583  ],
              [ 1.062, 0.81, 0.5508, 0.4302, 0.3546, 0.3222, 0.216, 0.09054, 0.09,  0.015948, 0.005706, 0.0015678, 0.001749 ] ] 

Dub89_201 = [ [ 37.5,    50,      75,      100,     175,    250,     375,     500     ],
                  [ 0.066,   0.097,   0.127,   0.119,   0.105,  0.114,   0.081,   0.061   ],
                  [ 0.01188, 0.01746, 0.02286, 0.02142, 0.0189, 0.02052, 0.01458, 0.01098 ] ]

Dub89_102 = [ [ 37.5,    50,       75,       100,      175,     250,   375,     500      ],
              [ 0.0130,  0.0263,   0.0544,   0.0886,   0.118,   0.100, 0.0985,  0.0871   ],
              [ 0.00234, 0.004734, 0.009792, 0.015948, 0.02124, 0.018, 0.01773, 0.002613 ] ]

Dub89_003 = [ [ 37.5,     50,       75,       100,       175,       250,      375,     500      ],
              [ 0.00141,  0.00167,  0.00331,  0.00584,   0.00717,   0.00584,  0.00530, 0.00415  ],
              [ 0.000423, 0.000501, 0.000993, 0.0010512, 0.0012906, 0.001752, 0.00159, 0.001245 ] ]

#Forest:
FTFHLP_95_111 = [ [ 125,  150, 200, 250,  500,  1000, 1500, 2000, 2500, 3000 ],
                  [ 0.91, 1.2, 1.0, 0.77, 0.49, 0.29, 0.19, 0.16, 0.14, 0.12 ],
                  [ 0.09, 0.1, 0.1, 0.08, 0.05, 0.03, 0.02, 0.02, 0.01, 0.01 ] ]

FTFHLP_95_012 = [ [ 125,   150,   200,   250,   500,    1000,   1500,   2000,   2500,    3000    ],
                  [ 0.033, 0.041, 0.031, 0.022, 0.0083, 0.0028, 0.0013, 0.0010, 0.00079, 0.00072 ],
                  [ 0.005, 0.006, 0.005, 0.003, 0.0012, 0.0004, 0.0002, 0.0002, 0.00012, 0.00011 ]  ]

FTFHLP_95_120 = [ [ 125,    150,    200,    250,    500,    1000,    1500,     2000,     2500     ],
                  [ 0.18,   0.12,   0.049,  0.026,  0.0026, 0.00017, 0.000025, 0.000006, 0.000002 ],
                  [ 0.4E-1, 0.2E-1, 1.0E-2, 0.5E-2, 0.5E-3, 0.3E-4,  0.5E-5,   1.2E-6,   0.4E-6   ] ]

FTFHLP_95_021 = [ [ 125,    150,    200,    250,    500,    1000,   1500,   2000,   2500   ],
                  [ 3.0E-2, 2.1E-2, 7.6E-3, 3.4E-3, 2.9E-4, 1.2E-5, 1.6E-6, 3.4E-7, 1.1E-7 ],
                  [ 0.6E-2, 0.4E-2, 1.5E-3, 0.7E-3, 0.6E-4, 0.2E-5, 0.3E-6, 0.7E-7, 0.2E-7 ] ]

#Santos:
SSMSM_95_201 = [ [ 250,     312.5,   375,     500,     625,    750,    875    ],
                 [ 20.1E-2, 19.2E-2, 16.7E-2, 12.9E-2, 9.8E-2, 8.7E-2, 9.3E-2 ],
                 [ 2.4E-2,  2.3E-2,  2.0E-2,  1.5E-2,  1.2E-2, 1.0E-2, 1.1E-2 ] ]

SSMSM_11_102 = [ [ 250,    312.5,  375,    500,    625,    750,    875    ],
                 [ 8.9E-2, 7.9E-2, 7.9E-2, 6.9E-2, 4.4E-2, 4.6E-2, 3.6E-2 ],
                 [ 1.5E-2, 1.3E-2, 1.3E-2, 1.2E-2, 0.7E-2, 0.9E-2, 0.6E-2 ] ]

SSMSM_11_003 = [ [ 312.5,   375,      500,     625,     750,     875     ],
                 [ 0.46E-2, 0.31E-2,  0.18E-2, 0.20E-2, 0.14E-2, 0.11E-2 ],
                 [ 0.12E-2, 0.008E-2, 0.05E-2, 0.05E-2, 0.04E-2, 0.03E-2 ] ]

#Dubois and Toburen:
DT_88_111 = [ [ 33.3,    37.5,   50,      75,    100,    175,  250,     375,    500   ],
              [ 0.647,   0.882,  0.975,   1.08,  1.07,   1.00, 0.879,   0.628,  0.560 ],
              [ 0.09705, 0.1323, 0.14625, 0.162, 0.1605, 0.15, 0.13185, 0.0942, 0.084 ] ]

DT_88_012 = [ [ 33.3,     37.5,    50,      75,       100,      175,    250,     375,     500      ],
              [ 0.0129,   0.0268,  0.0481,  0.0553,   0.0545,   0.0386, 0.0248,  0.0127,  0.0087   ],
              [ 0.001935, 0.00804, 0.01443, 0.008295, 0.008175, 0.01158, 0.00744, 0.00381, 0.001305 ] ]


def readCross( path ):
    """Read cross section data from file at path."""

    Es    = []
    c210s = []
    c111s = []
    c012s = []
    c021s = []
    c120s = []
    c201s = []
    c102s = []
    c003s = []
    c300s = []
    c030s = []

    with open( path, 'r' ) as readFile:
        
        readFile.readline()
        readFile.readline()
        
        for line in readFile:
            
            E, c210, c111, c012, c021, c120, c201, c102, c003, c300, c030 = line.split()
            
            Es.append( float(E) )
            c210s.append( float(c210) )
            c111s.append( float(c111) )
            c012s.append( float(c012) )
            c021s.append( float(c021) )
            c120s.append( float(c120) )
            c201s.append( float(c201) )
            c102s.append( float(c102) )
            c003s.append( float(c003) )
            c300s.append( float(c300) )
            c030s.append( float(c030) )

    return [ Es, c210s, c111s, c012s, c021s, c120s, c201s, c102s, c003s, c300s, c030s ]


def readData( path ):
    """Reads a data file for another calculation."""

    Es = []
    vals = []

    with open(path,'r') as readFile:
        for line in readFile:

            E, v = line.split()

            Es.append( float(E) )
            vals.append( float(v) )

    return ( Es, vals )


def vToE(v):

    return 27.2114 * 1836.15 * v * v / 2000


if __name__ == "__main__":
 
    lbl_size = 24 #22
    lgd_size = 20 #18
    mrks = 9
    lw = 3
    fontsize = 24

    matplotlib.rcParams.update({'font.size': fontsize, 'text.usetex': True, "ps.usedistiller" : "xpdf"})

    full = readCross("./images/data/resp-etf.txt")
    part = readCross("./images/data/resp-netf.txt")
    petf = readCross("./images/data/noresp-etf.txt")
    netf = readCross("./images/data/noresp-netf.txt")

    MMA03s01 = readData( "./images/data/MMA03-s01.txt" )
    MG10s11 = np.array( readData( "./images/data/MG10-s11.txt" ) )
    GAG15s20 = np.array( readData( "./images/data/GAG15-s20.txt" ) )

    SM03s01 = np.array( readData( "./images/data/SM03-s01.txt" ) )
    SM03s02 = np.array( readData( "./images/data/SM03-s02.txt" ) )
    SM03s03 = np.array( readData( "./images/data/SM03-s03.txt" ) )

    fig1 = plt.figure(1, figsize = (12,10))
    fig2 = plt.figure(2, figsize = (12,10))
    fig3 = plt.figure(3, figsize = (12,10))
    fig4 = plt.figure(4, figsize = (12,10))
    fig5 = plt.figure(5, figsize = (12,10))
    fig6 = plt.figure(6, figsize = (12,10))
    fig7 = plt.figure(7, figsize = (12,10))
    fig8 = plt.figure(8, figsize = (12,10))
    fig9 = plt.figure(9, figsize = (12,10))
 
    #Plot: TPI-111
    plt.figure(1)

    plt.plot( full[0],  full[2],  "k-",  linewidth = lw, label = "$\mathrm{Resp}$ $\mathrm{pETF}$" )
    plt.plot( part[0],  part[2],  "r:",  linewidth = lw, label = "$\mathrm{Resp}$ $\mathrm{nETF}$" )
    #plt.plot( petf[0],  petf[2],  "g--", linewidth = lw, label = "$\mathrm{pETF}$" )
    #plt.plot( netf[0],  netf[2],  "b-.", linewidth = lw, label = "$\mathrm{nETF}$" )
    plt.plot( vToE(MG10s11[0]), MG10s11[1] * 0.5291772083**2, "g--", linewidth = lw )
    plt.errorbar(Dub89_111[0], Dub89_111[1], yerr = Dub89_111[2], fmt = "bd", markersize = mrks)
    plt.errorbar(FTFHLP_95_111[0], FTFHLP_95_111[1], yerr = FTFHLP_95_111[2], fmt = "go", markersize = mrks)
    plt.errorbar(DT_88_111[0], DT_88_111[1], yerr = DT_88_111[2], fmt = "ys", markersize = mrks)

    plt.xlim([8,1100])
    plt.xscale("log")

    plt.xlabel( "$E_P$ $[\mathrm{keV}/\mathrm{amu}]$", fontsize = lbl_size )
    plt.ylabel( "$\sigma_{11}$ $[10^{-16}\mathrm{cm}^2]$", fontsize = lbl_size )

    ax = plt.gca()
    ax.xaxis.set_tick_params(which='both', width=2)
    ax.yaxis.set_tick_params(which='both', width=2)
 
    ax.xaxis.set_tick_params(which='major', length=8)
    ax.yaxis.set_tick_params(which='major', length=8)
    ax.xaxis.set_tick_params(which='minor', length=5)
    ax.yaxis.set_tick_params(which='minor', length=5)

    #Plot: TPI-012
    plt.figure(2)

    plt.plot( full[0],  full[3],  "k-",  linewidth = lw, label = "$\mathrm{Resp}$ $\mathrm{pETF}$" )
    plt.plot( part[0],  part[3],  "r:",  linewidth = lw, label = "$\mathrm{Resp}$ $\mathrm{nETF}$" )
    #plt.plot( petf[0],  petf[3],  "g--", linewidth = lw, label = "$\mathrm{pETF}$" )
    #plt.plot( netf[0],  netf[3],  "b-.", linewidth = lw, label = "$\mathrm{nETF}$" )
    plt.errorbar(Dub89_012[0], Dub89_012[1], yerr = Dub89_012[2], fmt = "bd", markersize = mrks)
    plt.errorbar(FTFHLP_95_012[0], FTFHLP_95_012[1], yerr = FTFHLP_95_012[2], fmt = "go", markersize = mrks)
    plt.errorbar(DT_88_012[0], DT_88_012[1], yerr = DT_88_012[2], fmt = "ys", markersize = mrks)

    plt.xlim([8,1100])
    plt.ylim( ymin = 0.0 )
    plt.xscale("log")

    plt.xlabel( "$E_P$ $[\mathrm{keV}/\mathrm{amu}]$", fontsize = lbl_size )
    plt.ylabel( "$\sigma_{12}$ $[10^{-16}\mathrm{cm}^2]$", fontsize = lbl_size )
 
    ax = plt.gca()
    ax.xaxis.set_tick_params(which='both', width=2)
    ax.yaxis.set_tick_params(which='both', width=2)
 
    ax.xaxis.set_tick_params(which='major', length=8)
    ax.yaxis.set_tick_params(which='major', length=8)
    ax.xaxis.set_tick_params(which='minor', length=5)
    ax.yaxis.set_tick_params(which='minor', length=5)

    #Plot: TPI-021
    plt.figure(3)

    plt.plot( full[0],  full[4],  "k-",  linewidth = lw, label = "$\mathrm{Resp}$ $\mathrm{pETF}$" )
    plt.plot( part[0],  part[4],  "r:",  linewidth = lw, label = "$\mathrm{Resp}$ $\mathrm{nETF}$" )
    #plt.plot( petf[0],  petf[4],  "g--", linewidth = lw, label = "$\mathrm{pETF}$" )
    #plt.plot( netf[0],  netf[4],  "b-.", linewidth = lw, label = "$\mathrm{nETF}$" )
    plt.errorbar(Dub89_021[0], Dub89_021[1], yerr = Dub89_021[2], fmt = "bd", markersize = mrks)
    plt.errorbar(FTFHLP_95_021[0], FTFHLP_95_021[1], yerr = FTFHLP_95_021[2], fmt = "gd", markersize = mrks)

    plt.xlim([8,1100])
    plt.ylim( ymin = 0 )
    plt.xscale("log")

    plt.xlabel( "$E_P$ $[\mathrm{keV}/\mathrm{amu}]$", fontsize = lbl_size )
    plt.ylabel( "$\sigma_{21}$ $[10^{-16}\mathrm{cm}^2]$", fontsize = lbl_size )
 
    ax = plt.gca()
    ax.xaxis.set_tick_params(which='both', width=2)
    ax.yaxis.set_tick_params(which='both', width=2)
 
    ax.xaxis.set_tick_params(which='major', length=8)
    ax.yaxis.set_tick_params(which='major', length=8)
    ax.xaxis.set_tick_params(which='minor', length=5)
    ax.yaxis.set_tick_params(which='minor', length=5)

    #Plot: TPI-120
    plt.figure(4)

    plt.plot( full[0],  full[5],  "k-",  linewidth = lw, label = "$\mathrm{Resp}$ $\mathrm{pETF}$" )
    plt.plot( part[0],  part[5],  "r:",  linewidth = lw, label = "$\mathrm{Resp}$ $\mathrm{nETF}$" )
    #plt.plot( petf[0],  petf[5],  "g--", linewidth = lw, label = "$\mathrm{pETF}$" )
    #plt.plot( netf[0],  netf[5],  "b-.", linewidth = lw, label = "$\mathrm{nETF}$" )
    plt.plot( GAG15s20[0], GAG15s20[1] * 0.5291772083**2, "g--", linewidth = lw )
    plt.errorbar(Dub89_120[0], Dub89_120[1], yerr = Dub89_120[2], fmt = "bd", markersize = mrks)
    plt.errorbar(FTFHLP_95_120[0], FTFHLP_95_120[1], yerr = FTFHLP_95_120[2], fmt = "go", markersize = mrks)

    plt.xlim([8,1100])
    plt.ylim( ymin = 0, ymax = 5.5 )
    plt.xscale("log")

    plt.xlabel( "$E_P$ $[\mathrm{keV}/\mathrm{amu}]$", fontsize = lbl_size )
    plt.ylabel( "$\sigma_{20}$ $[10^{-16}\mathrm{cm}^2]$", fontsize = lbl_size )
 
    ax = plt.gca()
    ax.xaxis.set_tick_params(which='both', width=2)
    ax.yaxis.set_tick_params(which='both', width=2)
 
    ax.xaxis.set_tick_params(which='major', length=8)
    ax.yaxis.set_tick_params(which='major', length=8)
    ax.xaxis.set_tick_params(which='minor', length=5)
    ax.yaxis.set_tick_params(which='minor', length=5)

    #Plot: TPI-201
    plt.figure(5)

    plt.plot( full[0],  full[6],  "k-", linewidth = lw, label = "$\mathrm{Resp}$ $\mathrm{pETF}$" )
    plt.plot( part[0],  part[6],  "r:", linewidth = lw, label = "$\mathrm{Resp}$ $\mathrm{nETF}$" )
    #plt.plot( petf[0],  petf[6],  "g--", linewidth = lw, label = "$\mathrm{pETF}$" )
    #plt.plot( netf[0],  netf[6],  "b-.", linewidth = lw, label = "$\mathrm{nETF}$" )
    plt.plot( 1000 * SM03s01[0]/4, SM03s01[1] * 1E-2, "g--", linewidth = lw )
    plt.errorbar(Dub89_201[0], Dub89_201[1], yerr = Dub89_201[2], fmt = "bd", markersize = mrks)

    plt.xlim([8,1100])
    plt.ylim( ymin = 0 )
    plt.xscale("log")

    plt.xlabel( "$E_P$ $[\mathrm{keV}/\mathrm{amu}]$", fontsize = lbl_size )
    plt.ylabel( "$\sigma_{01}$ $[10^{-16}\mathrm{cm}^2]$", fontsize = lbl_size )
 
    ax = plt.gca()
    ax.xaxis.set_tick_params(which='both', width=2)
    ax.yaxis.set_tick_params(which='both', width=2)
 
    ax.xaxis.set_tick_params(which='major', length=8)
    ax.yaxis.set_tick_params(which='major', length=8)
    ax.xaxis.set_tick_params(which='minor', length=5)
    ax.yaxis.set_tick_params(which='minor', length=5)

    #Plot: TPI-102
    plt.figure(6)

    plt.plot( full[0],  full[7],  "k-",  linewidth = lw, label = "$\mathrm{Resp}$ $\mathrm{pETF}$" )
    plt.plot( part[0],  part[7],  "r:",  linewidth = lw, label = "$\mathrm{Resp}$ $\mathrm{nETF}$" )
    #plt.plot( petf[0],  petf[7],  "g--", linewidth = lw, label = "$\mathrm{pETF}$" )
    #plt.plot( netf[0],  netf[7],  "b-.", linewidth = lw, label = "$\mathrm{nETF}$" )
    plt.plot( 1000 * SM03s02[0]/4, SM03s02[1] * 1E-2, "g--", linewidth = lw )
    plt.errorbar(Dub89_102[0], Dub89_102[1], yerr = Dub89_102[2], fmt = "bd", markersize = mrks)
    plt.errorbar(SSMSM_11_102[0], SSMSM_11_102[1], yerr = SSMSM_11_102[2], fmt = "r+", markersize = mrks)

    plt.xlim([8, 1100])
    plt.ylim( ymin = 0 )
    plt.xscale("log")

    plt.xlabel( "$E_P$ $[\mathrm{keV}/\mathrm{amu}]$", fontsize = lbl_size )
    plt.ylabel( "$\sigma_{02}$ $[10^{-16}\mathrm{cm}^2]$", fontsize = lbl_size )
 
    ax = plt.gca()
    ax.xaxis.set_tick_params(which='both', width=2)
    ax.yaxis.set_tick_params(which='both', width=2)
 
    ax.xaxis.set_tick_params(which='major', length=8)
    ax.yaxis.set_tick_params(which='major', length=8)
    ax.xaxis.set_tick_params(which='minor', length=5)
    ax.yaxis.set_tick_params(which='minor', length=5)

    #Plot: TPI-003
    plt.figure(7)

    plt.plot( full[0],  full[8],  "k-", linewidth = lw, label = "$\mathrm{Resp}$ $\mathrm{pETF}$" )
    plt.plot( part[0],  part[8],  "r:", linewidth = lw, label = "$\mathrm{Resp}$ $\mathrm{nETF}$" )
    #plt.plot( petf[0],  petf[8],  "g--", linewidth = lw, label = "$\mathrm{pETF}$" )
    #plt.plot( netf[0],  netf[8],  "b-.", linewidth = lw, label = "$\mathrm{nETF}$" )
    plt.plot( 1000 * SM03s03[0]/4, SM03s03[1] * 1E-2, "g--", linewidth = lw )
    plt.errorbar(Dub89_003[0], Dub89_003[1], yerr = Dub89_003[2], fmt = "bd", markersize = mrks)
    plt.errorbar(SSMSM_11_003[0], SSMSM_11_003[1], yerr = SSMSM_11_003[2], fmt = "r+", markersize = mrks)

    plt.xlim([8, 1100])
    plt.ylim( ymin = 0 )
    plt.xscale("log")

    plt.xlabel( "$E_P$ $[\mathrm{keV}/\mathrm{amu}]$", fontsize = lbl_size )
    plt.ylabel( "$\sigma{03}$ $[10^{-16}\mathrm{cm}^2]$", fontsize = lbl_size )
 
    ax = plt.gca()
    ax.xaxis.set_tick_params(which='both', width=2)
    ax.yaxis.set_tick_params(which='both', width=2)
 
    ax.xaxis.set_tick_params(which='major', length=8)
    ax.yaxis.set_tick_params(which='major', length=8)
    ax.xaxis.set_tick_params(which='minor', length=5)
    ax.yaxis.set_tick_params(which='minor', length=5)

    #Plot: TPI-300
    plt.figure(8)

    plt.plot( full[0],  full[9],  "k-",  linewidth = lw, label = "$\mathrm{Resp}$ $\mathrm{pETF}$" )
    plt.plot( part[0],  part[9],  "r:",  linewidth = lw, label = "$\mathrm{Resp}$ $\mathrm{nETF}$" )
    #plt.plot( petf[0],  petf[9],  "g--", linewidth = lw, label = "$\mathrm{pETF}$" )
    #plt.plot( netf[0],  netf[9],  "b-.", linewidth = lw, label = "$\mathrm{nETF}$" )

    plt.xlim([8, 1100])
    plt.ylim( ymin = 0 )
    plt.xscale("log")

    plt.xlabel( "$E_P$ $[\mathrm{keV}/\mathrm{amu}]$", fontsize = lbl_size )
    plt.ylabel( "$\sigma_{00}$ $[10^{-16}\mathrm{cm}^2]$", fontsize = lbl_size )

    plt.legend( loc="best", fancybox=True, labelspacing = .2, numpoints=1 )
 
    ax = plt.gca()
    ax.xaxis.set_tick_params(which='both', width=2)
    ax.yaxis.set_tick_params(which='both', width=2)
 
    ax.xaxis.set_tick_params(which='major', length=8)
    ax.yaxis.set_tick_params(which='major', length=8)
    ax.xaxis.set_tick_params(which='minor', length=5)
    ax.yaxis.set_tick_params(which='minor', length=5)

    #Plot: TPI-030
    plt.figure(9)

    plt.plot( full[0],  full[10],  "k-",  linewidth = lw, label = "$\mathrm{Resp}$ $\mathrm{pETF}$" )
    plt.plot( part[0],  part[10],  "r:",  linewidth = lw, label = "$\mathrm{Resp}$ $\mathrm{nETF}$" )
    #plt.plot( petf[0],  petf[10],  "g--", linewidth = lw, label = "$\mathrm{pETF}$" )
    #plt.plot( netf[0],  netf[10],  "b-.", linewidth = lw, label = "$\mathrm{nETF}$" )

    plt.xlim([8, 1100])
    plt.ylim( ymin = 0 )
    plt.xscale("log")

    plt.xlabel( "$E_P$ $[\mathrm{keV}/\mathrm{amu}]$", fontsize = lbl_size )
    plt.ylabel( "$\sigma^{30}$ $[10^{-16}\mathrm{cm}^2]$", fontsize = lbl_size )

    plt.legend( loc="best", fancybox=True, labelspacing = .2, numpoints=1 )
 
    ax = plt.gca()
    ax.xaxis.set_tick_params(which='both', width=2)
    ax.yaxis.set_tick_params(which='both', width=2)
 
    ax.xaxis.set_tick_params(which='major', length=8)
    ax.yaxis.set_tick_params(which='major', length=8)
    ax.xaxis.set_tick_params(which='minor', length=5)
    ax.yaxis.set_tick_params(which='minor', length=5)


    #Save figures:
    fig1.savefig( "./images/crossPlots/HepHe-111.eps", format = 'eps', dpi = 20000, bbox_inches='tight')
    fig2.savefig( "./images/crossPlots/HepHe-012.eps", format = 'eps', dpi = 20000, bbox_inches='tight')
    fig3.savefig( "./images/crossPlots/HepHe-021.eps", format = 'eps', dpi = 20000, bbox_inches='tight')
    fig4.savefig( "./images/crossPlots/HepHe-120.eps", format = 'eps', dpi = 20000, bbox_inches='tight')
    fig5.savefig( "./images/crossPlots/HepHe-201.eps", format = 'eps', dpi = 20000, bbox_inches='tight')
    fig6.savefig( "./images/crossPlots/HepHe-102.eps", format = 'eps', dpi = 20000, bbox_inches='tight')
    fig7.savefig( "./images/crossPlots/HepHe-003.eps", format = 'eps', dpi = 20000, bbox_inches='tight')
    fig8.savefig( "./images/crossPlots/HepHe-300.eps", format = 'eps', dpi = 20000, bbox_inches='tight')
    fig9.savefig( "./images/crossPlots/HepHe-030.eps", format = 'eps', dpi = 20000, bbox_inches='tight')

