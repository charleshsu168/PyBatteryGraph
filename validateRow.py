import re
def validate_row( row=[]):
# row array 
# index position 	Definition						Range					
# 0 				time							
# 1				voltage 1				0 <=  x	<	100		
# 2 				voltage 2				0 <=  x	<	100
# 3 				voltage 3				0 <=  x	<	100
# 4 				voltage 4				0 <=  x	<	100
# 5 				voltage 5				0 <=  x	<	100
# 6 				voltage 6				0 <=  x	<	100
# 7 				voltage 7				0 <=  x	<	100
# 8 				charge state			        0 <=  x	<	100
# 9 				Discharge state				0 <=  x	<	100
# 10 				flag					0 <=  x	<	100
# 11				average current				0 <=  x	<	100
# 12				instant current				0 <=  x	<	100
# 13				total voltage				0 <=  x	<	100
# 14				BMS voltage				0 <=  x	<	100
# 15				temperature				0 <=  x	<	100
# 16				capacity(soc)				0 <=  x	<	100
# 17				bottom balace of location		0 <=  x	<	100	
# 18				top balance of location			0 <=  x	<	100
# 19				jumper					characters
# 20 				ticks					positive integers 
    try:
            if ( 0 <= float(row[1]) <= 100 ):
                pass
            else:
                print 'row[1] out of range', row[1]
                return False
            if ( 0 <= float(row[2]) <= 100 ):
                pass
            else:
                print 'row[2] out of range', row[2]
                return False
            if ( 0 <= float(row[3]) < 100 ):
                pass
            else:
                print 'row[3] out of range', row[3]
                return False
            if ( 0 <= float(row[4]) < 100 ):
                pass
            else:
                print 'row[4] out of range', row[4]
                return False
            if ( 0 <= float(row[5]) < 100 ):
                pass
            else:
                print 'row[5] out of range', row[5]
                return False
            if (0 <= float(row[6]) < 100):
                pass
            else:
                print 'row[6] out of range', row[6]
                return False
            if (0 <= float(row[7]) < 100):
                pass
            else:
                print 'row[7] out of range', row[7]
                return False
            if (0 <= float(row[8]) < 100 ):
                pass
            else:
                print 'row[8] out of range', row[8]
                return False
            if (0 <= float(row[9]) < 100 ):
                pass
            else:
                print 'row[9] out of range', row[9]
                return False
            if ( 0 <= float(row[10]) < 100 ):
                pass
            else:
                print 'row[10] out of range', row[10]
                return False
            #if (0 <= float(row[11]) < 100):
            #    pass
            #else:
            #    print 'row[11] out of range', row[11]
            #if ( 0 <= float(row[12]) < 100):
            #    pass
            #else
            #    print 'fow[12] out of range', row[12]
            if (0 <= float(row[13]) < 100):
                pass
            else:
                print 'row[13] out of range', row[13]
                return False
            if (0 <= float(row[14]) < 100):
                pass
            else: 
                print 'row[14] out of range', row[14]
                return False
            if ( 0 <= float(row[15]) < 100 ):
                pass
            else:
                print 'row[15] out of range', row[15]
                return False
            if (0 <= float(row[16]) < 100 ):
                pass
            else:
                print 'row[16] out of range', row[16]
                return False
            if (0 <= float(row[17]) < 100):
                pass
            else:
                print 'row[17] out of range', row[17]
                return False
            if (0 <= float(row[18]) < 100 ):
                pass
            else:
                print  'row[18] out of range', row[18]
                return False
            pattern=re.compile(r'\d+x\d+')
            if (pattern.match(row[19].strip())!=None):
                pass
            else:
                print 'bad row 19', row[19]
                return False
            if ( 0 <= int(row[20])   < 1000000 ):
                pass
            else:
                print 'row[20] out of range', row[20]
                return False
            return True

    except Exception, e:
                    print e
                    return False
