from datetime import datetime

def main():
    bornBefore = datetime(1981, 9, 19)
    date = extractDate()
    while date is not None :
        if date <= bornBefore :
            print( "You are older than me: ", date )
            date = extractDate()
            break
        else:
            print( "You are younger than me: ", date )
            break



def extractDate():
    print( "Enter your birth date." )
    month = int( input("month (0 to quit): ") )
    if month == 0 :
        return None
    else :
        day = int( input("day: ") )
        year = int( input("year: ") )
        return datetime(year,month,day)
main()
