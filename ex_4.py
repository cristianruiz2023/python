sh = input('Input hours ')
sr = input('Input your price ')

try:
    fh = float(sh)
    fr = float(sr)
except:
    print('Error input valid number')
    exit()
print(fh, fr)
if fh > 40:
    print('overtime')
    reg = fh*fr
    otp = (fh - 40.0) * (fr * 0.5)
    print(reg, otp)
    px = reg + otp
else:
    px = fh * fr
    print('regular', px)


print('total of pay is: ',px)