# AI Sentiment Analysis API

A FastAPI-based sentiment analysis service that uses the DistilBERT model to analyze text feedback and provide sentiment classifications.

## 🚀 Features

- Real-time sentiment analysis using DistilBERT
- RESTful API built with FastAPI
- Docker containerization
- Asynchronous request handling
- Interactive API documentation (Swagger UI)
- High performance and scalability

## 📋 Prerequisites

- Python 3.9+
- Docker (optional)
- pip (Python package manager)

## 🛠️ Installation

### Local Setup

1. Clone the repository:
```bash
git clone https://github.com/atasolouki/DX-Solutions-sentiment-analysis.git
cd DX-Solutions-sentiment-analysis
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Start the server:
```bash
uvicorn api:app --reload
```

The API will be available at `http://localhost:8000`

### 🐳 Docker Setup

1. Build the image:
```bash
docker build -t sentiment-analysis-api .
```

2. Run the container:
```bash
docker run -d -p 8000:8000 sentiment-analysis-api
```

## 📚 API Reference

### Analyze Sentiment

```http
POST /analyze
```

#### Request Body
```json
{
    "text": "This app is great!"
}
```

#### Response
```json
{
    "feedback": "This app is great!",
    "sentiment": "POSITIVE",
    "score": 0.9998
}
```

#### Example Usage

Using curl:
```bash
curl -X POST "http://localhost:8000/analyze" \
     -H "Content-Type: application/json" \
     -d '{"text": "This product is amazing!"}'
```

Using Python requests:
```python
import requests

response = requests.post(
    "http://localhost:8000/analyze",
    json={"text": "This product is amazing!"}
)
print(response.json())
```

## 📖 Documentation

Access the interactive API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
