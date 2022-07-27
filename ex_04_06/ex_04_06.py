def computepay(hours, rate):
    # print('In computepay', hours, rate)
    if hours > 40 :
        reg = hours * rate
        otp = (hours - 40.0) * (ir * 0.5)
        print(reg,'regular', 'and', otp, 'overtime')
        pay = reg + otp
        print(pay, " This is your total pay with Overtime")
    else :
        print(hours,'X',rate)
        pay = hours * rate
        print(pay, "This is your total pay")
    print('returning', pay)
    return pay  
sh = input('Enter hours : ')
sr = input('Enter rate : ')
print('hour -- rate')
print(sh,'-----', sr,)
ih = float(sh)
ir = float(sr)

xp = computepay(ih, ir)

print('Pay', xp)
