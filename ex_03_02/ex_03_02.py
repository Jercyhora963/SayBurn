sh = input('Enter hours : ')
sr = input('Enter rate : ')
try :
    fh = float(sh)
    fr = float(sr)

except :
    print('please enter, numeric number')
    quit()

if fh > 40 :
    # print('Overtime')
    reg = fh * fr
    otp = (fh - 40.0) * (fr * 0.5)
    print(reg,'regular', 'and', otp, 'overtime')
    pay = reg + otp
    print(pay, " This is your total pay with Overtime")
else :
    # print('Regular')
    print(fh,'X', fr)
    pay = fh * fr
    print(pay, "This is your total pay")
