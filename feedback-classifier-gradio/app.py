import gradio as gr
from transformers import pipeline
import os
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = ""

# Initialize sentiment analysis pipeline
classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

# Define prediction function
def analyze_feedback(feedback):
    result = classifier(feedback)[0]
    sentiment = result['label'].capitalize()
    score = result['score']
    return f"Sentiment: {sentiment}\nConfidence: {score:.4f}"

# Create Gradio interface
iface = gr.Interface(
    fn=analyze_feedback,
    inputs=gr.Textbox(label="Enter Feedback", placeholder="Type your feedback here..."),
    outputs=gr.Textbox(label="Result"),
    title="Sentiment Analysis",
    description="Enter customer feedback to classify it as Positive or Negative."
)

# Launch the interface
if __name__ == "__main__":
    iface.launch()