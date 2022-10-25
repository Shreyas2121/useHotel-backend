from flask import jsonify
from models.hall import Hall

def create_hall():
    hall = Hall(
        hall_id = 3,
        hall_type = "Birthday Party",
        hall_price = 10000,
        hall_max_occ = 40,
        hall_desc = "This is a birthday party hall",
        hall_amenities = ["AC","TV","Projector"],
        total_halls = 2,
        hall_image = ["https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.chennaiconventioncentre.com%2Fblog%2F10-questions-you-must-ask-about-birthday-party-halls%2F&psig=AOvVaw1-2AXxaV42felAvboWIw-j&ust=1666156269421000&source=images&cd=vfe&ved=0CA0QjRxqFwoTCLCpkP6B6foCFQAAAAAdAAAAABAE"]

    )
    hall.save()
    return jsonify({'hall': hall.to_json()})


def get_halls():
    halls = Hall.objects()
    return jsonify({'halls': [hall.to_json() for hall in halls]})
