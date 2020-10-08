hrs = input('Enter hours:')
h = float(hrs)
rate = input('Enter rate:')
r = float(rate)

def computepay(h,r):
    if h<=40 :
           print(h*r)
    else :
        p = 40 * r + (h-40) * 1.5 * r
        print("Pay",p)
        return p

computepay(h,r)
