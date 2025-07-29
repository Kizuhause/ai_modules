def run(*args):
    import requests, json
    city = " ".join(args) if args else "Berlin"
    url = f"https://wttr.in/{city}?format=j1"
    try:
        data = requests.get(url, timeout=5).json()
        temp = data["current_condition"][0]["temp_C"]
        return f"In {city} sind es {temp} Grad."
    except Exception as e:
        return "Wetter konnte nicht abgerufen werden."
