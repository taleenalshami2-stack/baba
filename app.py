from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Enable cross-origin resource sharing so index.html can call the api
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/predict")
def get_prediction(pair: str, tf: str):
    simulated_rsi = random.randint(25, 75)
    confidence = random.randint(65, 95)
    volatility = round(random.uniform(0.0012, 0.0035), 4)
    
    clean_pair = pair.split(":")[-1] if ":" in pair else pair
    
    if simulated_rsi >= 65:
        prediction = "STRONG_SELL"
        rationale = f"[AI INSIGHT] {clean_pair} on {tf} frame indicates deep overhead volume exhaustion. Heavy distribution detected near psychological resistance boundaries."
    elif simulated_rsi <= 35:
        prediction = "STRONG_BUY"
        rationale = f"[AI INSIGHT] {clean_pair} on {tf} frame has tapped institutional demand block. Momentum structural sweep confirms strong bullish reversal probability."
    else:
        prediction = "HOLD"
        rationale = f"[AI INSIGHT] {clean_pair} remains rangebound in efficient market territory. Volume profiles are thin; wait for breakout confirmation."

    return {
        "prediction": prediction,
        "confidence": confidence,
        "rsi": simulated_rsi,
        "volatility": volatility,
        "rationale_string": rationale
    }