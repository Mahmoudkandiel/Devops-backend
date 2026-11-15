from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Exponential Counter API")

# Enable CORS so your public frontend can talk to this private backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simple in-memory counter state (starts at 1)
counter_state = {"value": 1}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/counter")
def get_counter():
    return {"value": counter_state["value"]}

@app.post("/counter/exponential")
def exponential_increment():
    # Multiplies by 2 on each click (1 -> 2 -> 4 -> 8 -> 16...)
    if counter_state["value"] == 0:
        counter_state["value"] = 1
    else:
        counter_state["value"] *= 2
    return {"value": counter_state["value"]}