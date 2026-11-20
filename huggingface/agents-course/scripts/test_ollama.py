from smolagents import LiteLLMModel

model = LiteLLMModel(
    model_id="ollama_chat/qwen3:8b",
    api_base="http://127.0.0.1:11434",
    num_ctx=8192,
)