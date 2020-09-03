#Project 1:Voyager
miles_from_sun = 16637000000 #distance from the sun and im going to use that number to caluate 

speed_miles = 38241 #this is the spped that the voyager is travling away from the sun so in one day its that number times 24 so i can see how far it is

days = input("Number of days after 9/25/09: ") # i use the days as a input so the user can input the number of days that he wants to see 

days_int = int(days) #here i have the days but becosue the days is in str and we want to have to calute then we must make an int 

miles_day = days_int * 24 * speed_miles # this here is the miles per day it travled svo number of days times 24 that is the one day and that times speed_miles so i can see how far it has travled

totalmiles = miles_from_sun + miles_day #this is just the total miles so the orginal number plus the miles_day so i can see the whole number that the voyager has travled 

conversion_num_km = 1.609344 # i use this number to convert miles to km 

astronomical_conversion_num = 0.0000000066846 # i use this number to convert km to au 

km_from_the_sun = round(totalmiles *  conversion_num_km) # i use round to approx the number them i have the totalmiles times the convert number so i will get the number for km

au_from_the_sun = round(km_from_the_sun * astronomical_conversion_num) # i use the round to approx the number i will get so it will not be many extra numbers then i have the km from the sun times the convert number so i will get the number for au 

print("Miles from the sun:" , totalmiles) # print miles.... then call totalmiles and will show the user the totalmiles

print("Kilometers from the sun:", km_from_the_sun) # print km..... then call km_from_the_sun and will show the user the totalkm

print("AU from the sun:", au_from_the_sun) #print au ..... then call au_from_the_sun and it will show the user the au 