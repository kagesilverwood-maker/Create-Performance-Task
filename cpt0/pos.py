def pos(boat_heading):
    #rounded_heading = round(boat_heading / 45) * 45


    if boat_heading < 45 or boat_heading > 315:
        return {
            "point": "No-Go Zone",
            "advice": [
                "Fall of the wind until you are at a 45° angle and can get 'in the groove.'"
            ]
        }


    if boat_heading == 45 or boat_heading == 315:
        return {
            "point": "Close Haul",
            "advice": [
                "What to do: Watch the sail and fall off the wind if luffing occurs. \n\n",
                "Sail position: Sail should be pulled in close (\"close hauled\") with the end of the boom between the center and the"
                "\n corner of the boat.\n\n",
                "Crew position: Crew should be between slightly below the jib sheet block and the shroud.\n  "
                "They should be ready to move to either port or starboard in order to counter the skipper's weight.\n\n",
                "Skipper position: Skipper should be as far forward as possible and stay on the side opposite of the mainsail.\n\n",
                "Heel: Keep the boat at a 15°-20° angle. You may have to hike out or lean in toward the center of the boat to achieve this angle.\n\n",
                "Centerboard: Should be fully down to maximize stability.\n\n",
                "Outhaul: In light wind, the outhaul should be slightly loosened to allow more wind to fill the sail. In heavier wind, it should be as tight as it can go to spill wind.\n\n"
            ]
        }


    if boat_heading > 45 or boat_heading < 90 or boat_heading < 315 or boat_heading > 270:
        return {
            "point": "Close Reach",
            "advice": [
                "What to do: Keep the boat flat and stay on a steady course, adjusting the mainsail as needed.",
                "Sail position: Sail should be slightly off the corner of the boat.",
                "Crew position: Crew should be as far forward as possible and be ready to move to either port or starboard in order to counter the skipper's weight.",
                "Skipper position: Skipper should be as far forward as possible and stay on the side opposite of the mainsail.",
                "Heel: Keep the boat at a 15°-20° angle. You may have to hike out or lean in toward the centerline to achieve this angle.",
                "Centerboard: Should be fully down to maximize stability.",
                "Outhaul:"
                ]}


    if boat_heading > 45 or boat_heading < 90 or boat_heading < 315 or boat_heading > 270:
        return {
            "point": "Beam Reach",
            "advice": [
                "What to do:",
                "Sail position: Keep sail close to the centerline to allow it to fill.",
                "Crew position: Crew should be as far forward as possible and be ready to move to either port or starboard in order to counter the skipper's weight.",
                "Skipper position: Skipper should be as far forward as possible and stay on the side opposite of the mainsail.",
                "Heel: Keep the boat at a 15°-20° angle. You may have to hike out or lean in toward the centerline to achieve this angle.",
                "Centerboard: Should be fully down to maximize stability.",
                "Outhaul:"
                 ]}
    if boat_heading > 45 or boat_heading < 90 or boat_heading < 315 or boat_heading > 270:
        return {
            "point": "Broad Reach",
            "advice": [
                "What to do:",
                "Sail position: Keep sail close to the centerline to allow it to fill.",
                "Crew position: Crew should be as far forward as possible and be ready to move to either port or starboard in order to counter the skipper's weight.",
                "Skipper position: Skipper should be as far forward as possible and stay on the side opposite of the mainsail.",
                "Heel: Keep the boat at a 15°-20° angle. You may have to hike out or lean in toward the centerline to achieve this angle.",
                "Centerboard: Should be fully down to maximize stability.",
                "Outhaul:"


            ]
        }
    if boat_heading > 45 or boat_heading < 90 or boat_heading < 315 or boat_heading > 270:
        return {
            "point": "Run",
            "advice": [
                "What to do:",
                "Sail position: Keep sail close to the centerline to allow it to fill.",
                "Crew position: Crew should be as far forward as possible and be ready to move to either port or starboard in order to counter the skipper's weight.",
                "Skipper position: Skipper should be as far forward as possible and stay on the side opposite of the mainsail.",
                "Heel: Keep the boat at a 15°-20° angle. You may have to hike out or lean in toward the centerline to achieve this angle.",
                "Centerboard: Should be fully down to maximize stability.",
                "Outhaul:"
            ]}


    # fallback
    return {
        "point": "Unknown",
        "advice": ["Adjust heading."]
    }
