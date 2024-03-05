from huggingface_hub import HfApi
api = HfApi()

model_id = "fotiecodes/jarvis-7b-v0.1-gguf"
api.create_repo(model_id, exist_ok=True, repo_type="model")
api.upload_file(
    path_or_fileobj="jarvis-7b-v0.1.gguf",
    path_in_repo="jarvis-7b-v0.1.gguf",
    repo_id=model_id,
)
