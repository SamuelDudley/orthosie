from escpos import *
spool = "192.168.192.168"
if type(spool) is str:
    print spool

print len(spool)

# Epson = printer.Network("192.168.192.168")
# Epson.set(align='CENTER')
# Epson.text("Hello World\n")
# Epson.set(font='B')
# Epson.text("Hello World\n")
# Epson.set(width=2)
# Epson.text("Hello World\n")
# Epson.set(height=2)
# Epson.text("Hello World\n")
# # Epson.qr("You can readme from your smartphone")
# # 
# # Epson.image("logo.jpg")
# # Epson.cut(mode='PART') #perform a part cut
# Epson.cut()
# 
# #note: need to send the cashdraw open request twice...
# Epson.cashdraw(2) #this is the cash draw pin for 
# Epson.cashdraw(2)