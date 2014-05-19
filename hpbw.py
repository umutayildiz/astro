#! /usr/bin python
import os, sys
from pylab import *
import scipy
import numpy

c = 2.99792458E8

def hpbwFreq(frequency,D):
	result = 1.22*((c/(frequency*1.0E9))/D)*206265.0
	return result
def hpbwWaveum(lamda,D):
	result = 1.22*((c/((2.99792458E11/(lamda*1000000.0))*1.0E9))/D)*206265.0
	return result
def hpbwWavem(lamda,D):
	result = 1.22*(lamda/D)*206265.0
	return result


print "Are you entering frequency (f), wavelength in m (wm), or wavelength in um (wum)?"
wavefreq = raw_input()
if ((wavefreq == '') or (wavefreq != 'f') and (wavefreq != 'wm') and (wavefreq != 'wum')):
	print "No/Wrong value entered, program exists!"
	sys.exit()

if wavefreq == 'f':
	print "Enter Frequency (GHz)?"
	frequency = raw_input()
	if (frequency == ''):
		print "No value entered, program exists!"
		sys.exit()
elif wavefreq == 'wum':
	print "Enter Wavelength (um)?"
	lamda = raw_input()
	if (lamda == ''):
		print "No value entered, program exists!"
		sys.exit()
elif wavefreq == 'wm':
	print "Enter Wavelength (m)?"
	lamda = raw_input()
	if (lamda == ''):
		print "No value entered, program exists!"
		sys.exit()

print "Enter Dish size (m)?"
D = raw_input()
if (D == ''):
	print "No value entered, program exists!"
	sys.exit()



if wavefreq == 'f':
	frequency = float(frequency)
	D = float(D)
	result = hpbwFreq(frequency,D)
	print('>>> For %s m telescope at a frequency of %s GHz' %(D, frequency))
	print('>>> HPBW Beam Size   = %.2f arcsec' %(result))
elif wavefreq == 'wum':
	lamda = float(lamda)
	D = float(D)
	result = hpbwWaveum(lamda,D)
	print('>>> For %s m telescope at a wavelength of %s um' %(D, lamda))
	print('>>> HPBW Beam Size   = %.2f arcsec' %(result))
elif wavefreq == 'wm':
	lamda = float(lamda)
	D = float(D)
	result = hpbwWavem(lamda,D)
	print('>>> For %s m telescope at a wavelength of %s m' %(D, lamda))
	print('>>> HPBW Beam Size   = %.2f arcsec' %(result))








