import time
from datetime import datetime
import numpy as np
from pylab import figure, show
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import logging
import re 
import string as st
from datetime import timedelta
import Tkinter
import tkMessageBox
import tkMessageBox
from Tkinter import Tk
from tkFileDialog import askopenfilename
import validateRow 

from Tkinter import *

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   



fig=plt.figure()

ax1=plt.subplot(3,3,1)
ax1.set_ylim(top = 4.3, bottom = 3)   
ax1.set_xlim(auto = True)  
#plt.subplots_adjust(bottom=.06)
hfmt = mdates.DateFormatter('%H:%M')
ax1.xaxis.set_major_locator(mdates.MinuteLocator(interval=15))
ax1.xaxis.set_major_locator(mticker.MaxNLocator(5))

ax1.xaxis.set_major_formatter(hfmt)
ax1.grid(True)
plt.ylabel('voltage 1')

#for label in ax1.xaxis.get_ticklabels():
    #label.set_rotation()
ax2=plt.subplot(3,3,2, sharex=ax1)
ax2.xaxis.set_major_locator(mdates.MinuteLocator())
ax2.xaxis.set_major_locator(mticker.MaxNLocator(5))
ax2.xaxis.set_major_formatter(hfmt)
ax2.set_ylim(top = 4.3, bottom = 3)   
ax2.set_xlim(auto=True)
ax2.grid(True)
plt.ylabel('voltage 2')

#voltage 3
ax3=plt.subplot(3,3,3, sharex=ax1)
ax3.xaxis.set_major_locator(mdates.MinuteLocator())
ax3.xaxis.set_major_locator(mticker.MaxNLocator(5))
ax3.xaxis.set_major_formatter(hfmt)
ax3.set_ylim(top = 4.3, bottom = 3)   
ax3.set_xlim(auto=True)
ax3.grid(True)
plt.ylabel('voltage 3')

#voltage 1
ax4=plt.subplot(3,3,4, sharex=ax1)
ax4.xaxis.set_major_locator(mdates.MinuteLocator())
ax4.xaxis.set_major_locator(mticker.MaxNLocator(5))
ax4.xaxis.set_major_formatter(hfmt)
ax4.set_ylim(top =4.3, bottom =3)   
ax4.set_xlim(auto=True)
ax4.grid(True)
plt.ylabel('voltage 4')

ax5=plt.subplot(3,3,5, sharex=ax1)
ax5.xaxis.set_major_locator(mdates.MinuteLocator())
ax5.xaxis.set_major_locator(mticker.MaxNLocator(5))
ax5.xaxis.set_major_formatter(hfmt)
ax5.set_ylim(top =4.3, bottom = 3)   
ax5.set_xlim(auto=True)
ax5.grid(True)
plt.ylabel('voltage 5')

ax6=plt.subplot(3,3,6, sharex=ax1)
ax6.xaxis.set_major_locator(mdates.MinuteLocator())
ax6.xaxis.set_major_locator(mticker.MaxNLocator(5))
ax6.xaxis.set_major_formatter(hfmt)
ax6.set_ylim(top =4.3, bottom = 3)   
ax6.set_xlim(auto=True)
ax6.grid(True)
plt.ylabel('voltage 6')

ax7=plt.subplot(3,3,7, sharex=ax1)
ax7.xaxis.set_major_locator(mdates.MinuteLocator())
ax7.xaxis.set_major_locator(mticker.MaxNLocator(5))
ax7.xaxis.set_major_formatter(hfmt)
ax7.set_ylim(top =4.3, bottom = 3)   
ax7.set_xlim(auto=True)
ax7.grid(True)
plt.ylabel('voltage 7')

ax8=plt.subplot(3,3,8, sharex=ax1)
ax8.xaxis.set_major_locator(mdates.MinuteLocator())
ax8.xaxis.set_major_locator(mticker.MaxNLocator(5))
ax8.xaxis.set_major_formatter(hfmt)
ax8.set_ylim(top =32, bottom = 20)   
ax8.set_xlim(auto=True)
ax8.grid(True)
plt.ylabel('total voltage')

ax9=plt.subplot(3,3,9, sharex=ax1)
ax9.xaxis.set_major_locator(mdates.MinuteLocator())
ax9.xaxis.set_major_locator(mticker.MaxNLocator(5))
ax9.xaxis.set_major_formatter(hfmt)
ax9.set_ylim(top =100, bottom = 0)   
ax9.set_xlim(auto=True)
ax9.grid(True)
plt.ylabel('state of charge')


jumper_50_dates_array=[]
jumper_52_dates_array=[]
jumper_50_total_voltage_array=[]
jumper_50_voltage_1_array=[]
jumper_50_voltage_2_array=[]
jumper_50_voltage_3_array=[]
jumper_50_voltage_4_array=[]
jumper_50_voltage_5_array=[]
jumper_50_voltage_6_array=[]
jumper_50_voltage_7_array=[]
jumper_52_voltage_arrary=[]
jumper_52_total_voltage_array=[]
jumper_52_voltage_1_array=[]
jumper_52_voltage_2_array=[]
jumper_52_voltage_3_array=[]
jumper_50_tick = 0
jumper_52_tick = 0
jumper_52_ticks_array=[]
jumper_50_state_of_charge_array=[]
jumper_52_state_of_charge_array=[]

#top = Tkinter.Tk()
#def hello():
   #tkMessageBox.showinfo("Say Hello", "Hello World")

#B1 = Tkinter.Button(top, text = "Say Hello", command = hello)
#B1.pack()
#top.mainloop()
def  plot_battery( ):
   global jumper_50_dates_array;
   global jumper_52_dates_array;
   global jumper_50_total_voltage_array;
   global jumper_50_voltage_1_array;
   global jumper_50_voltage_2_array;
   global jumper_50_voltage_3_array;
   global jumper_50_voltage_4_array;
   global jumper_50_voltage_5_array;
   global jumper_50_voltage_6_array;
   global jumper_50_voltage_7_array;
   global jumper_52_voltage_arrary;
   global jumper_52_total_voltage_array;
   global jumper_52_voltage_1_array;
   global jumper_52_voltage_2_array;
   global jumper_52_voltage_3_array;
   global jumper_50_tick; 
   global jumper_52_tick;
   global jumper_52_ticks_array;
   global jumper_50_state_of_charge_array;
   global jumper_52_state_of_charge_array;
#Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
   filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
   file_Contents=open(filename, 'r' ) #Open files
   #row_pat = re.compile(r'\d{1,2}/\d{1,2}/\d{4}\s\d{1,2}:\d{1,2}:\d{2}\s\[A-Z][A-Z],\s\d{1,2}\.{0,1}\d{0,3},\s\d{1,2}\.{0,1}\d{0,3}')   # Create row-pattern object to match
   row_pat = re.compile(r'\d{1,2}/\d{1,2}/\d{4}\s\d{1,2}:\d{1,2}:\d{2}\s[A-Z][A-Z],\s\d{1,2}\.{0,1}\d{0,3},\s\d{1,2}\.{0,1}\d{0,3}')   # Create row-pattern object to match
   # string, for example  '10/11/2013 10:45,3.626,3.62'
   for line in file_Contents:  # Go through file line one by one in for loop
       cells=re.split(r'[;,]', line)
       if (len(cells)==21):
           if (row_pat.match( line) ):
               if ( validateRow.validate_row(cells)):# If row-pattern does not match line,
                   if  (cells[19].strip() == '0x50'):  # else if row_pat match line and jumper address is 0x50
                     if ( jumper_50_tick == 0):
                       jumper_50_tick=int( cells[20])
                       jumper_50_total_voltage_array.append(float(cells[13]))
                       jumper_50_state_of_charge_array.append(int(cells[16]))
                       jumper_50_voltage_1_array.append(float(cells[1]))
                       jumper_50_voltage_2_array.append(float(cells[2]))
                       jumper_50_voltage_3_array.append(float(cells[3]))
                       jumper_50_voltage_4_array.append(float(cells[4]))
                       jumper_50_voltage_5_array.append(float(cells[5]))
                       jumper_50_voltage_6_array.append(float(cells[6]))
                       jumper_50_voltage_7_array.append(float(cells[7]))
                       jumper_50_dates_array.append(datetime.strptime(cells[0], '%m/%d/%Y %I:%M:%S %p'))
                       #print str(jumper_50_dates_array[-1].year)+str(jumper_50_dates_array[-1].month)+str(jumper_50_dates_array[-1].day)+" "+str(jumper_50_dates_array[-1].hour)+":"+str(jumper_50_dates_array[-1].minute)+":"+str(jumper_50_dates_array[-1].second)

                   else:
                   # tick is already initialized
                       delta = timedelta(minutes=15)
                       if (   jumper_50_dates_array[-1] +delta <= datetime.strptime(cells[0], '%m/%d/%Y %I:%M:%S %p')  ):
                           # if current row's time is greater than or equal to specified amount of time( delta ) away from previous row
                           jumper_50_tick=cells[20]
                           jumper_50_tick=int( cells[20])
                           jumper_50_total_voltage_array.append(float(cells[13]))
                           jumper_50_state_of_charge_array.append(int(cells[16]))
                           jumper_50_voltage_1_array.append(float(cells[1]))
                           jumper_50_voltage_2_array.append(float(cells[2]))
                           jumper_50_voltage_3_array.append(float(cells[3]))
                           jumper_50_voltage_4_array.append(float(cells[4]))
                           jumper_50_voltage_5_array.append(float(cells[5]))
                           jumper_50_voltage_6_array.append(float(cells[6]))
                           jumper_50_voltage_7_array.append(float(cells[7]))
                           jumper_50_dates_array.append(datetime.strptime(cells[0], '%m/%d/%Y %I:%M:%S %p'))

                       else:
                           pass
               elif( str(cells[19].strip())=='0x52' ):
                   if ( jumper_52_tick == 0):
                       jumper_52_tick=int(cells[20])
                       jumper_52_total_voltage_array.append(float(cells[13]))
                       jumper_52_state_of_charge_array.append(int(cells[16]))
                       jumper_52_voltage_1_array.append(float(cells[1]))
                       jumper_52_voltage_2_array.append(float(cells[2]))
                       jumper_52_voltage_3_array.append(float(cells[3]))
                       jumper_52_dates_array.append(datetime.strptime(cells[0], '%m/%d/%Y %I:%M:%S %p'))      
                   else:
                       if (  int(cells[20]) <= (jumper_52_tick+100)  ):
                           jumper_52_tick=int(cells[20])
                           jumper_52_total_voltage_array.append(float(cells[13]))
                           jumper_52_state_of_charge_array.append(int(cells[16]))
                           jumper_52_voltage_1_array.append(float(cells[1]))
                           jumper_52_voltage_2_array.append(float(cells[2]))
                           jumper_52_voltage_3_array.append(float(cells[3]))
                           jumper_52_dates_array.append(datetime.strptime(cells[0], '%m/%d/%Y %I:%M:%S %p'))
                           
                       else:
                           pass
           else:
               pass
       else:
           pass

   print "jumper_50_dates_array=", jumper_50_dates_array, 'length=', len( jumper_50_dates_array)
   print "jumper_50_state_of_charge_array=" , jumper_50_state_of_charge_array, 'length=', len( jumper_50_total_voltage_array)
   ax1.plot( jumper_50_dates_array, jumper_50_voltage_1_array, 'bo', label='voltage 1')
   ax2.plot( jumper_50_dates_array, jumper_50_voltage_2_array, 'go', label='voltage 2')
   ax3.plot( jumper_50_dates_array, jumper_50_voltage_3_array, 'ro', label='voltage 3')
   ax4.plot( jumper_50_dates_array, jumper_50_voltage_4_array, 'co', label='voltage 4')
   ax5.plot( jumper_50_dates_array, jumper_50_voltage_5_array, 'mo', label='voltage 5')
   ax6.plot( jumper_50_dates_array, jumper_50_voltage_6_array, 'yo', label='voltage 6')
   ax7.plot( jumper_50_dates_array, jumper_50_voltage_7_array, 'bo', label='voltage 7')
   ax8.plot( jumper_50_dates_array, jumper_50_total_voltage_array, 'go', label='total voltage')
   ax9.plot(  jumper_50_dates_array, jumper_50_state_of_charge_array, 'bo', label='state of charge')



   ax1.legend(fontsize='x-small', loc=2)
   ax2.legend(fontsize='x-small', loc=2)
   ax3.legend(fontsize='x-small', loc=2)
   ax4.legend(fontsize='x-small',  loc=2)
   ax5.legend(fontsize='x-small',  loc=2)
   ax6.legend(fontsize='x-small' , loc=2)
   ax7.legend(fontsize='x-small' , loc=2)
   ax8.legend(fontsize='x-small' , loc=2)
   ax9.legend(fontsize='x-small',  loc=2)

   plt.show()
   
root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
#filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=plot_battery)
#filemenu.add_command(label="Save", command=donothing)
#filemenu.add_command(label="Save as...", command=donothing)
#filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()

