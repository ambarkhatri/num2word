#This python program converts Numerals to Words following Indian Number System
#There are three logics present in this program
#Logic 1 and Logic 2 are initial versions hence commented out
#Logic 3 is currently functional
#
#


qones = [
    [1,'one'],
    [2,'two'],
    [3,'three'],
    [4,'four'],
    [5,'five'    ],
    [6,'six'     ],
    [7,'seven'   ],
    [8,'eight'   ],
    [9,'nine'    ],
    [10,'ten'     ],
    [11,'eleven'  ],
    [12,'twelve'  ],
    [13,'thirteen'],
    [14,'fourteen'],
    [15,'fifteen' ],
    [16,'sixteen' ],
    [17,'seventeen'],
    [18,'eighteen'],
    [19,'nineteen']
    ]
qtens = [
    [2,'twenty'] , 
    [3,'thirty'] , 
    [4,'fourty'] ,
    [5,'fifty'] ,
    [6,'sixty'] ,
    [7,'seventy'] ,
    [8,'eigthy'] ,
    [9,'ninety']
    ]

divisors = [
    [10000000,' crore'],
    [100000 , ' lakh'],
    [1000 , ' thousand'],
    [1 , ' ']
    ]


def iHateMaths(k,w):
    for item in qones:
        if m//100==item[0]:
            w = w + item[1] + ' hundred '
            print("Inwords :",w)
    if m%100//10==1:
        for item in qones:
            if m%100==item[0]:
                w = w + item[1] 
                print("Inwords :",w)
    else:
        for item in qtens:
            if m%100//10==item[0]:
                w = w + ' ' + item[1] 
                print("Inwords :",w)
        for item in qones:
            if m%100%10==item[0]:
                w = w + ' ' + item[1] 
                print("Inwords :",w)
    return w
        




while True:
    n = int(input("*********START************\n\nEnter any number between 1 to 99999 : "))  ##Taking user input

#Final and Improved Logic  - LOGIC3
    Inwords=''
    for div in divisors:
        m = n//div[0]
        print("m",m,"n",n)
        if m!=0:
            Inwords = iHateMaths(m,Inwords)
            Inwords = ' ' + Inwords + div[1] + ' '
        n = n%div[0]
        print(Inwords.upper())


        
     
     
    




#LOGIC1
'''    #Thousand place
    q10000= n//10000 #Quotient of a number divided by 10000
    q1000= (n%10000)//1000 #Quotient of a number divided by 1000
    #Hundreds place
    q100 = ((n%10000)%1000)//100 #Quotient of a number divided by 100
    q10 =  (((n%10000)%1000)%100)//10 #Quotient of (remainder of number divided by 100) when divided by 10
    r =    (((n%10000)%1000)%100)%10 #Remainder of remainder of N divided by 100 when divided by 10

    Inwords = ''
 
    #for Ten Thousand
    if q10000==1:
        for item in qones:
            if (n//1000)==item[0]:
                Inwords = item[1]  + ' thousand '
    else:
        for item in qtens:
            if q10000==item[0]:
                Inwords = item[1]
                if q1000==0:
                    Inwords = Inwords  + ' thousand '
 
        for item in qones:
            if q1000==item[0]:
                Inwords = Inwords + ' ' + item[1] + ' thousand '
    
    #for Hundreds
    for item in qones:
        if q100==item[0]:
            Inwords = Inwords + item[1] + ' hundred '
    #for tens and teens
    if q10==1:
        for item in qones:
            if (n%100)==item[0]:
                Inwords = Inwords + ' ' + item[1]
    else:
    #for tens and ones
        for item in qtens:
            if q10==item[0]:
               Inwords = Inwords + ' ' + item[1]
        for item in qones:
            if r==item[0]:
                Inwords = Inwords + ' ' + item[1]
    print("\nIn Words : " , Inwords.upper())
'''



#LOGIC2
'''    if n > 0 and n <= 19:  #number range 1 to 19
        for item in qones:
            if n==item[0]:
                Inwords = item[1]
                print("\nIn Words : " , Inwords.upper())

    elif n >= 20 and n < 100 :  #number range 20 to 99
        q = n//10   ##Quotient of a number divided by 10
        r = n%10    ##Remainder of a number divided by 10
        for item in qtens:
            if q==item[0]:
                Inwords = item[1]
        for item in qones:
            if r==item[0]:
                Inwords = Inwords + ' ' + item[1]
        print("\nIn Words : " , Inwords.upper())

    elif n >= 100 and n < 1000 :  #number range 100 to 999  ; 3 digit number
        q100 = n//100 #Quotient of a number divided by 100
        q10 = (n%100)//10 #Quotient of (remainder of number divided by 100) when divided by 10
        r = (n%100)%10 #Remainder of remainder of N divided by 100 when divided by 10
        for item in qones:
            if q100==item[0]:
                Inwords = item[1] + ' hundred '
        if q10==1:
            for item in qones:
                if (n%100)==item[0]:
                    Inwords = Inwords + ' ' + item[1]
        else:
            for item in qtens:
                if q10==item[0]:
                   Inwords = Inwords + ' ' + item[1]
            for item in qones:
                if r==item[0]:
                    Inwords = Inwords + ' ' + item[1]
        print("\nIn Words : " , Inwords.upper())

    elif n >= 1000 and n < 100000 : #number range 1000 to 99999 ;  4 and 5 digit number
        q10000= n//10000 #Quotient of a number divided by 10000
        q1000= (n%10000)//1000 #Quotient of a number divided by 1000
        q100 = ((n%10000)%1000)//100 #Quotient of a number divided by 100
        q10 =  (((n%10000)%1000)%100)//10 #Quotient of (remainder of number divided by 100) when divided by 10
        r =    (((n%10000)%1000)%100)%10 #Remainder of remainder of N divided by 100 when divided by 10
        Inwords = ''

        if q10000==1:
            for item in qones:
                if (n//1000)==item[0]:
                    Inwords = Item[1]  + ' thousand '
        else:
            for item in qtens:
                if q10000==item[0]:
                    Inwords = item[1]
                    if q1000==0:
                        Inwords = Inwords  + ' thousand '

            for item in qones:
                if q1000==item[0]:
                    Inwords = Inwords + ' ' + item[1] + ' thousand '
        for item in qones:
            if q100==item[0]:
                Inwords = Inwords + item[1] + ' hundred '
        if q10==1:
            for item in qones:
                if (n%100)==item[0]:
                    Inwords = Inwords + ' ' + item[1]
        else:
            for item in qtens:
                if q10==item[0]:
                   Inwords = Inwords + ' ' + item[1]
            for item in qones:
                if r==item[0]:
                    Inwords = Inwords + ' ' + item[1]
        print("\nIn Words : " , Inwords.upper())
'''

    
    
