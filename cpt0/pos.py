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
                "Sail position: Sail should be pulled in close (\"close hauled\") with the end of the boom between the center and the "
                "\n corner of the boat.\n\n",
                "Crew position: Crew should be between slightly below the jib sheet block and the shroud.\n  "
                "They should be ready to move to either port or starboard in order to counter the skipper's weight.\n\n",
                "Skipper position: Skipper should be as far forward as possible and stay on the side opposite of the mainsail.\n\n",
                "Heel: Keep the boat at a 15°-20° angle. You may have to hike out or lean in toward the centerline to achieve this angle.\n\n",
                "Centerboard: Should be fully down to maximize stability.\n\n",
                "Outhaul: \n\n"
            ]
        }

    if 45 < boat_heading < 90:
        return {
            "point": "Close Reach",
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

    # fallback
    return {
        "point": "Unknown",
        "advice": ["Adjust heading."]
    }