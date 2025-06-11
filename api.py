from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import os
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = ""

app = FastAPI()

# Initialize sentiment analysis pipeline
classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

# Define input model
class Feedback(BaseModel):
    text: str

# Sentiment analysis endpoint
@app.post("/analyze")
async def analyze_feedback(feedback: Feedback):
    result = classifier(feedback.text)[0]
    return {"feedback": feedback.text, "sentiment": result['label'], "score": result['score']}

# Run with: uvicorn api:app --reload