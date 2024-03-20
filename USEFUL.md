

Useful links:
-  converting model from hf to gguf https://github.com/ggerganov/llama.cpp/discussions/2948
-  Fixing issue with llama2 7b model error:Exception: Vocab size mismatch (model has 32000, but jarvis-hf/tokenizer.model has 32001). Fix here-> https://github.com/ggerganov/llama.cpp/issues/3900
- convert command: python llm/llama.cpp/convert.py ../jarvis-hf --outtype f16 --outfile converted.bin
- quantize: llm/llama.cpp/quantize converted.bin quantized.bin q4_0

- Link for the issue we had while working on converting the model, this is the solution which worked: https://github.com/ggerganov/llama.cpp/issues/6111
  