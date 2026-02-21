from predictor import predict_delay
from services.directions_service import get_directions
from utils import get_accidents, get_construction_status, calculate_score, generate_explanation 
def evaluate_route(road_name, coords):
    delay = predict_delay(coords)
    accidents = get_accidents()
    construction = get_construction_status()

    score = calculate_score(delay, accidents, construction)

    explanation = generate_explanation(
        delay, accidents, construction
    )

    directions = get_directions(road_name)

    return {
        "delay": delay,
        "score": score,
        "explanation": explanation,
        "directions": directions,
        "coords": coords
    }
    
def generate_all_routes(roads_coords):
    roads = {}

    for road, coords in roads_coords.items():
        roads[road] = evaluate_route(road, coords)

    best = min(roads, key=lambda r: roads[r]["score"])

    return roads, best