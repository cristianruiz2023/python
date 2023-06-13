def computing(hours, rate):
    print('im computing',hours,rate)
    if hours > 40:
        # print('overtime')
        reg = hours * rate
        otp = (hours - 40.0) * (rate * 0.5)
        # print(reg, otp)
        pay = reg + otp
    else:
        pay = hours * rate

    print('returning',pay)
    return pay


sh = input('Input hours ')
sr = input('Input your price ')
fh = float(sh)
fr = float(sr)
px=computing(fh,fr)
#print(fh, fr)



print('total of pay is: ',px)