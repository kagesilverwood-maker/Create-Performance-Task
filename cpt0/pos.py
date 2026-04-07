def pos(boat_heading):
    rounded_heading = round(boat_heading / 45) * 45

    if boat_heading < 45 or boat_heading > 315:
        return {
            "point": "No-Go Zone",
            "advice": "What to do: Fall off the wind until you are at a 45° angle and can get 'in the groove.'"
        }

    if boat_heading == 45 or boat_heading == 315:
        return {
            "point": "Close Haul",
            "advice": (
                "What to do:\n"
                "Sail position:\n"
                "Crew position: Crew should be as far forward as possible and be ready to move to either port or starboard to counter the skipper's weight.\n"
                "Skipper position: Skipper should be as far forward as possible and stay on the side opposite of the mainsail.\n"
                "Heel: Keep the boat at a 15°-20° angle. You may have to hike out or lean in toward the centerline to achieve this angle.\n"
                "Centerboard: Should be fully down to maximize stability.\n"
                "Outhaul:"
            )
        }

    if 45 < boat_heading < 90:
        return {
            "point": "Close Reach",
            "advice": (
                "What to do:\n"
                "Sail position: Keep sail close to the centerline to allow it to fill.\n"
                "Crew position: Crew should be as far forward as possible and be ready to move to either port or starboard to counter the skipper's weight.\n"
                "Skipper position: Skipper should be as far forward as possible and stay on the side opposite of the mainsail.\n"
                "Heel: Keep the boat at a 15°-20° angle. You may have to hike out or lean in toward the centerline to achieve this angle.\n"
                "Centerboard: Should be fully down to maximize stability.\n"
                "Outhaul:"
            )
        }

    # fallback for other headings
    return {
        "point": "Unknown",
        "advice": "Adjust heading."
    }
# def pos(boat_heading):
#     # boat_heading= float(input("boat heading= "))  # removed, now comes from Flask/JS
#     rounded_heading = round(boat_heading / 45) * 45

#     if boat_heading < 45 or boat_heading > 315:
#         print("Point of sail: No-Go Zone")
#         print("What to do: Fall of the wind until you are at a 45° angle \n\tand can get \"in the groove.\"")  # link to a how to get out of irons page for final project

#     if boat_heading == 45 or boat_heading == 315:
#         print("Point of sail: Close Haul")
#         print("What to do: ")
#         print("Sail position: ")
#         print("Crew position: Crew should be as far forward as possible \n\tand be ready to move to either port or starboard in \n\torder to counter the skipper's weight. ")
#         print("Skipper position: Skipper should be as far forward as \n\tpossible and stay on the side opposit of the mainsail.")
#         print("Heel: Keep the boat at a 15°-20° angle. You may have to hike\n\t out or lean in toward the centerline to achieve this \n\t angle.")
#         print("Centerboard: Should be fully down to maximize stability.")
#         print("Outhaul: ")

#     if boat_heading > 45 or boat_heading < 90:
#         print("Point of sail: Close Reach")
#         print("What to do: ")
#         print("Sail position: Keep sail close to the centerline to allow \n\tit to fill. ")
#         print("Crew position: Crew should be as far forward as possible \n\tand be ready to move to either port or starboard in \n\torder to counter the skipper's weight. ")
#         print("Skipper position: Skipper should be as far forward as \n\tpossible and stay on the side opposit of the mainsail.")
#         print("Heel: Keep the boat at a 15°-20° angle. You may have to hike\n\t out or lean in toward the centerline to achieve this \n\t angle.")
#         print("Centerboard: Should be fully down to maximize stability.")
#         print("Outhaul: ")

#     if boat_heading > 45 or boat_heading < 90:
#         print("Point of sail: Close Reach")
#         print("What to do: ")
#         print("Sail position: Keep sail close to the centerline to allow \n\tit to fill. ")
#         print("Crew position: Crew should be as far forward as possible \n\tand be ready to move to either port or starboard in \n\torder to counter the skipper's weight. ")
#         print("Skipper position: Skipper should be as far forward as \n\tpossible and stay on the side opposit of the mainsail.")
#         print("Heel: Keep the boat at a 15°-20° angle. You may have to hike\n\t out or lean in toward the centerline to achieve this \n\t angle.")
#         print("Centerboard: Should be fully down to maximize stability.")
#         print("Outhaul: ")
#def pos(wind_speed, boat_heading):

    #if boat_heading < 45 or boat_heading > 315:
        #return {
            #"point": "No-Go Zone",
            #"advice": "Fall off the wind until you reach 45°."
       # }

    #elif boat_heading == 45 or boat_heading == 315:
       # return {
          #  "point": "Close Haul",
         #   "advice": "Keep sails tight and balanced."
       # }

    #elif 45 < boat_heading < 90:
       # return {
        #    "point": "Close Reach",
        #    "advice": "Let sails out slightly."
        #}

    #else:
    #    return {
     #       "point": "Unknown",
     #       "advice": "Adjust heading."
     #   }