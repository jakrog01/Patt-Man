def check_oposite(direction: str, newdirection: str) -> bool:
    directions_list = [direction, newdirection]

    if "Up" in directions_list and "Down" in directions_list:
        return True
    elif "Right" in directions_list and "Left" in directions_list:
        return True
    
    return False