#def pos ():
#wind direction is the direction the wind is going; it is represented by the degree it is at in relation to the top of a compass (north)
#North- 0
#Northeast- 45
#East- 90
#Southeast- 135
#South- 180
#Southwest- 270
#Northwest- 315
    #wind_speed= int(input("wind speed= "))
    #boat_heading= float(input("boat heading= ")) #degrees off the wind
    #rounded_heading= round(boat_heading/45)*45
    #if boat_heading < 45 or boat_heading > 315:
        #print("Point of sail: No-Go Zone")
        #print("What to do: Fall of the wind until you are at a 45° angle \n\tand can get \"in the groove.\"")#link to a how to get out of irons page for final project
    #if boat_heading==45 or boat_heading==315:
        #print("Point of sail: Close Haul")
        #print("What to do: ")
        #print("Sail position: ")
        #print("Crew position: Crew should be as far forward as possible \n\tand be ready to move to either port or starboard in \n\torder to counter the skipper's weight. ")
        #print("Skipper position: Skipper should be as far forward as \n\tpossible and stay on the side opposit of the mainsail.")
        #print("Heel: Keep the boat at a 15°-20° angle. You may have to hike\n\t out or lean in toward the centerline to achieve this \n\t angle.")
        #print("Centerboard: Should be fully down to maximize stability.")
        #print("Outhaul: ")
    #if boat_heading>45 or boat_heading<90:
        #print("Point of sail: Close Reach")
        #print("What to do: ")
        #print("Sail position: Keep sail close to the centerline to allow \n\tit to fill. ")
        #print("Crew position: Crew should be as far forward as possible \n\tand be ready to move to either port or starboard in \n\torder to counter the skipper's weight. ")
        #print("Skipper position: Skipper should be as far forward as \n\tpossible and stay on the side opposit of the mainsail.")
        #print("Heel: Keep the boat at a 15°-20° angle. You may have to hike\n\t out or lean in toward the centerline to achieve this \n\t angle.")
        #print("Centerboard: Should be fully down to maximize stability.")
        #print("Outhaul: ")
    #if boat_heading >45 or boat_heading< 90:
        #print("Point of sail: Close Reach")
        #print("What to do: ")
        #print("Sail position: Keep sail close to the centerline to allow \n\tit to fill. ")
        #print("Crew position: Crew should be as far forward as possible \n\tand be ready to move to either port or starboard in \n\torder to counter the skipper's weight. ")
        #print("Skipper position: Skipper should be as far forward as \n\tpossible and stay on the side opposit of the mainsail.")
        #print("Heel: Keep the boat at a 15°-20° angle. You may have to hike\n\t out or lean in toward the centerline to achieve this \n\t angle.")
        #print("Centerboard: Should be fully down to maximize stability.")
        #print("Outhaul: ")
def pos(wind_speed, boat_heading):

    if boat_heading < 45 or boat_heading > 315:
        return {
            "point": "No-Go Zone",
            "advice": "Fall off the wind until you reach 45°."
        }

    elif boat_heading == 45 or boat_heading == 315:
        return {
            "point": "Close Haul",
            "advice": "Keep sails tight and balanced."
        }

    elif 45 < boat_heading < 90:
        return {
            "point": "Close Reach",
            "advice": "Let sails out slightly."
        }

    else:
        return {
            "point": "Unknown",
            "advice": "Adjust heading."
        }