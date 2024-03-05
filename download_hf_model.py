from huggingface_hub import snapshot_download
model_id = "fotiecodes/Llama-2-7b-chat-jarvis"
snapshot_download(repo_id=model_id, local_dir="jarvis-hf",
                  local_dir_use_symlinks=False, revision="main")
