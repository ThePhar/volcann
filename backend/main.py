import uvicorn
from os import path
import sys

if __name__ == "__main__":
    # uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)

    # TODO: For testing purposes, we're just trying to get data.
    sys.path.append(path.abspath("./archipelago"))
    from archipelago.Generate import roll_settings
    return_val = roll_settings({
        "name": "Phar",
        "description": "Test",
        "game": "Archipelago",
        "Archipelago": {},
    })
    print(return_val)
