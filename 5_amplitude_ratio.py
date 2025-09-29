#######################################################################################################################
###                             Training Onboard & Underwater Radiated Noise & Vibrations                           ###
#######################################################################################################################
#
# Example - Amplitude Ratio (undamped)
# 
# Author: Kevin Runge
# Last Updated: 24-Sept-2025
#  
# (License information at the end of this file)
# 
#######################################################################################################################


import numpy as np
import matplotlib.pyplot as plt


# --------------------------------------------------------------- 
# Constants
# ---------------------------------------------------------------
k = 4           # [N / m]
m = 1           # [kg]

# --------------------------------------------------------------- 
# initial conditions
# ---------------------------------------------------------------

# simulation settings
f_end = 5   # [rad/s]
steps = 20    # [1/s]
f = np.linspace(0,f_end, f_end * steps + 1)

# --------------------------------------------------------------- 
# Solution to equation of motion
# ---------------------------------------------------------------
nfreq = np.sqrt(k / m) # [rad/s]
solution = np.abs(1 / (1 - np.power((f/nfreq), 2)))


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
    fig = plt.figure("Amplitude Ratio (undamped)")
    plt.plot(f, solution, "b", lw=2, label=r"$x$")
    plt.ylim(0,15)
    plt.title("Amplitude Ratio")    
    plt.xlabel("frequency [rad/s]")
    plt.ylabel("|M|")
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