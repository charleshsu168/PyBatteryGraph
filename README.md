PyBatteryGraph
==============

Python Battery Graph
  This is a Python Graph for plotting battery log data in the format.
To run it, download and run the windows exe file at https://drive.google.com/file/d/0Bz-PAzbRkPrSZUtYYUEzZ3lXLVk/edit?usp=sharing
Select Open and find the file path of the data log.

  Note the expected data log format per row entry is as follows: 

10/21/2013 07:51:46 PM, 3.448, 3.418, 3.430, 3.434, 3.451, 3.440, 3.444, 0.000, 0.003, 0.000,  0.000, 0.003, 24.065, 3.448, 25.1, 9, 0, 0, 0x50, 280841 

  The values, separated by commas, are defined as follows:


# index position 	        Definition						            Range					    Example
# 0 				              time							                                    10/21/2013 07:51:46 PM
# 1			                	voltage 1			                 	0 <=  x	<	100		      3.224
# 2 				              voltage 2				                0 <=  x	<	100         3.414
# 3 			              	voltage 3			                	0 <=  x	<	100         3.124
# 4 			              	voltage 4				                0 <=  x	<	100         3.126
# 5 			              	voltage 5			          	      0 <=  x	<	100         3.126
# 6 			              	voltage 6			                	0 <=  x	<	100         3.432
# 7 			              	voltage 7			          	      0 <=  x	<	100         3.125
# 8 			              	charge state			              0 <=  x	<	100         3.126
# 9 				              Discharge state			          	0 <=  x	<	100         0.000
# 10 				              flag				            	      0 <=  x	<	100         0.003
# 11			              	average current			    	      0 <=  x	<	100         0.000
# 12			              	instant current			    	      0 <=  x	<	100         0.000
# 13				              total voltage				            0 <=  x	<	100         21.064
# 14				              BMS voltage				              0 <=  x	<	100         3.452
# 15				              temperature			        	      0 <=  x	<	100         25.1  
# 16				              capacity(soc)			            	0 <=  x	<	100         9
# 17			              	bottom balace of location		    0 <=  x	<	100	        0
# 18			              	top balance of location			    0 <=  x	<	100         0
# 19				              jumper	                        characters            0x50 or 0x52
# 20 			              	ticks					                  positive integers     280841  

