sh = input('Enter hours : ')
sr = input('Enter rate : ')
print('hour -- rate')
print(sh,'-----', sr,)
ih = float(sh)
ir = float(sr)

if ih > 40 :
    # print('Overtime')
    reg = ih * ir
    otp = (ih - 40.0) * (ir * 0.5)
    print(reg,'regular', 'and', otp, 'overtime')
    pay = reg + otp
    print(pay, " This is your total pay with Overtime")
else :
    # print('Regular')
    print(ih,'X', ir)
    pay = ih * ir
    print(pay, "This is your total pay")
