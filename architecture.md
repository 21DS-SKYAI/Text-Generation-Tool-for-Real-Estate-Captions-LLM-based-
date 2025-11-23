flowchart LR
    User[Agent / Marketer] --> UI[Web UI / Streamlit]
    UI --> API[FastAPI Backend]
    API --> Prompt[Prompt Builder]
    Prompt --> LLM[Hugging Face LLM]
    LLM --> API
    API --> Logs[Prompt & Output Logs]
    API --> UI
    Logs --> FineTune[Optional Fine-tuning Later]
