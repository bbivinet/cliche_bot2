def handle_response(msg: str) -> str:
    message = msg.lower()

    if message == "plot":
        return "plot"
    