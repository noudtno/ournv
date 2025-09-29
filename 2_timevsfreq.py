#######################################################################################################################
###                             Training Onboard & Underwater Radiated Noise & Vibrations                           ###
#######################################################################################################################
#
# Example - Time vs Frequency Domain
# 
# Author: Kevin Runge
# Last Updated: 23-Sept-2025
#  
# (License information at the end of this file)
# 
#######################################################################################################################

import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------------------- 
# Constants
# ---------------------------------------------------------------
ampl_1 = 1                  # [m]
freq_1 = 50                 # [Hz]
phase_1 = 0                 # [rad]
ampl_2 = 3                  # [m]
freq_2 = freq_1 * 3         # [Hz]
phase_2 = np.radians(45)    # [rad]

sampling_freq = 1000

# --------------------------------------------------------------- 
# initial conditions
# ---------------------------------------------------------------
# simulation settings
time_step = 1 / sampling_freq
N = 10 * int(sampling_freq / freq_1)

t = np.linspace(0, (N - 1) * time_step, N)
freq_step = sampling_freq / N
f = np.linspace(0, (N - 1) * freq_step, N)

# --------------------------------------------------------------- 
# Fast Fourier Transform
# ---------------------------------------------------------------
solution = ampl_1 * np.sin(2 * np.pi * freq_1 * t + phase_1) + ampl_2 * np.sin(2 * np.pi * freq_2 * t + phase_2)
X = np.fft.fft(solution)    # returns complex values
X_ampl = np.abs(X) / N      # normalized amplitude

# Nyquist Theorem
f_plot = f[0:int(N / 2 + 1)] 
X_ampl_plot = 2 * X_ampl[0:int(N / 2 + 1)] 
X_ampl_plot[0] = X_ampl_plot[0] / 2

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
    fig, [ax_time, ax_freq] = plt.subplots(nrows=2, ncols=1)
    ax_time.plot(t, solution)
    ax_freq.plot(f_plot, X_ampl_plot)
    
    ax_time.title.set_text('Time Signal')
    ax_freq.title.set_text('Frequency Content')

    plt.subplots_adjust(bottom=0.05)

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