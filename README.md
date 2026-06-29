# FastAPI Hugging Face LLM Integration

This project uses FastAPI to build an API endpoint that connects to a Hugging Face Large Language Model (LLM). It allows you to send a prompt to an endpoint and receive a generated response from the model.

## Prerequisites

Before running the project, you need to set up your Hugging Face API token.

1. Get a token from your [Hugging Face Account](https://huggingface.co/settings/tokens).
2. Create a `.env` file in the root directory of this project.
3. Add your token to the `.env` file using the following variable name:

```env
HF_TOKEN=your_hugging_face_token_here
```

### Configuration

You can easily change the LLM model used by the application. By default, this project is configured to use:
* `meta-llama/Llama-3.1-8B-Instruct`

---

## How to Run the Application

You can run this project either directly on your local machine or by using Docker.

### Option 1: Run Locally (Without Docker)

To start the FastAPI application directly, run the following command in your terminal:

```bash
fastapi run main.py
```

### Option 2: Run with Docker

If you prefer to containerize the application, follow these steps to build and run the Docker image.

**1. Build the Docker image:**

```bash
docker build -t fastapimage .
```

**2. Run the Docker container:**

```bash
docker run --name fastapicontainer -p 8000:8000 fastapimage
```

Once the application is running via either method, you can access the API and its interactive documentation (Swagger UI) at `http://localhost:8000/docs`.
