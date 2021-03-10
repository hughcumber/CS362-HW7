def leap(input):

    if int(input) % 4 == 0:                                                                                                     #   logic of the program checks if its a leap year
        leap = True;
    else:
        return "Not a leap year";


    if int(input) % 100 == 0:
        if input % 400 != 0:
            leap = False;



    if leap == False:
        return "Not a leap year";

    else:
        return "Leap year!";
