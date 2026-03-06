'''

crop disease prediction system 

'''

from fastapi import FastAPI

app = FastAPI(
    title="Crop Disease Prediction System",
    description="""A system to predict crop diseases based on input data/images.
    - Identifies plant species from images
    - Detects known + unknown diseases (open-set)
    - Multi-label detection (multiple diseases per leaf)
    - Grad-CAM explainability heatmaps
    - Human-in-the-loop continuous learning pipeline
    """,
    version="1.0.0",
)

@app.get("/")
async def root():
    return { 
        "message": "crop disease prediction system api is running",
        "docs": "/docs",
        "redoc": "1.0.0"
    }
