# Program will calculate leap year

def leapYear():
    print("Hello World")
    year = input("Enter a year: ")
    # check year is leap year or not
    if(year.isdigit() == True):
        if( int(year) % 4 == 0 and int(year) %100 != 0 or int(year) % 400 == 0 ):
       # if ( ):
            print ("This is a leap-year!")

        else:
            print ("This is not a leap-year!")
    else :
        print("Please Enter valid Year ,digit only!")

leapYear()
