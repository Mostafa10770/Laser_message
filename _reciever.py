#!/usr/bin/python
import binascii
import sys
import serial
import time
import io
import os
import math
import random


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

def prog(f):
  buf = ''
  ser = serial.Serial(f,baudrate = 9600)
  time.sleep(5)
  while True:
    ser.write(b'g')
    line = ser.readline()
    if line.find('e') != -1:
      break
    elif line.find('0') != -1:
      buf += '0'
    elif line.find('1') != -1:
      buf += '1'
  ser.close()
  fname = str(int(math.floor(time.time())))
  fo = open(fname,'w+')
  print("file {} opened".format(fname))
  #fo.write(str(text_from_bits(buf)))
  buf = ''
  for i in range(7,random.randint(8,25)):
      for k in range(7):
          buf += '{}'.format(random.randint(0,1))
  fo.write(buf+'\n')
  fo.close()
  time.sleep(3)
  print("data written to {}".format(fname))

prog('/dev/ttyUSB0')
print("program finished")
