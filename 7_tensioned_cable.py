#######################################################################################################################
###                             Training Onboard & Underwater Radiated Noise & Vibrations                           ###
#######################################################################################################################
#
# Example - Tensioned Cable
# 
# Author: Kevin Runge
# Last Updated: 27-Sept-2025
#  
# (License information at the end of this file)
# 
#######################################################################################################################


import numpy as np
import matplotlib.pyplot as plt


# --------------------------------------------------------------- 
# Constants
# ---------------------------------------------------------------
mode = 3        # mode
L = 5           # [m]
m = 0.1         # [kg / m]
P = 5           # tension force [N]  

# --------------------------------------------------------------- 
# initial conditions
# ---------------------------------------------------------------
# simulation settings
step = L / 100  # [m]
x = np.linspace(0, L, int(L / step + 1))

# --------------------------------------------------------------- 
# Solution to equation of motion & plot range of modes
# ---------------------------------------------------------------

nfreq = (mode / 2 * L) * np.sqrt(P / m) # [Hz]
solution = np.sin(mode * np.pi * x / L)


#######################################################################################################################
#
# Utilities
#
#######################################################################################################################

STATIC_PLOT = True


# --------------------------------------------------------------- 
# Plot
# ---------------------------------------------------------------
if STATIC_PLOT:
    fig = plt.figure("Tensioned Cable")
    plt.plot(x, solution, "b", lw=2, label=f"Mode {mode}")
    plt.legend([f'Mode {mode} - freq = {round(nfreq,3)} [Hz]'], loc="lower left")
    plt.xlabel("x [m]")
    plt.grid()
    plt.show()


#######################################################################################################################
#
# Released under MIT License
#
# Copyright 2025, TNO
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this 
# software and associated documentation files (the “Software”), to deal in the Software 
# without restriction, including without limitation the rights to use, copy, modify, 
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to 
# permit persons to whom the Software is furnished to do so, subject to the following 
# conditions:
#
# The above copyright notice and this permission notice shall be included in all copies 
# or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF 
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE 
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#######################################################################################################################