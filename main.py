from rich.console import Console
from rich import print
import time
import json
import os
from fastapi import FastAPI
import importlib
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

console = Console()

for module in os.listdir("./modules"):
    with console.status(f"Loading {module}...", spinner="point"):
        with open(f"./modules/{module}/config.json") as f:
            config = json.load(f)

        match config.get("type"):
            case "API":

                try:
                    router = importlib.import_module(f"modules.{module}")
                except ModuleNotFoundError as e:
                    console.log(f"[red] Dependency not found: {e.name.split('.')[-1]}")
                app.include_router(router.setup())

                # app.include_router(router)
                
                console.log(f"Loaded {module} as API")

            case "CLI":
                console.log(f"Loaded {module} as CLI")

            case "Module":
                console.log(f"Loaded {module} as module")

console.log("[green bold]Loaded all modules")

if __name__ == "__main__":
    uvicorn.run(app)