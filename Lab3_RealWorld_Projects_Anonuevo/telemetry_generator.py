def stream_telemetry(surname, seed_num, artist):
    base = len(surname) + seed_num + len(artist)
    raw_stream = [
        base * 3,
        base * 6,
        "ERR_SENSOR_TIMEOUT",
        base * 12,
        base * 2,
        base * 20,
        "BAD_VAL"
    ]
    for val in raw_stream:
        yield val
    