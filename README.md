# Jarvis
The J.A.R.V.I.S Large Language Model, 100% offline

We have use custom jarvis dataset and various other open datasets on the internet of jarvis's dialog with stark to fine-tune on top of Llama2 7b

## Content:
- Dataset [here](https://huggingface.co/datasets/fotiecodes/jarvis-llama2-dataset) | dataset is being created progresively
- Model: [here](https://huggingface.co/fotiecodes/Llama-2-7b-chat-jarvis) | Updated every week or so

Jarvis is bing built with privacy in mind, everything runs locally. In the main time it works with local LLama2 7b with ollama until the fine-tuned mondel is ready to be used.
The fine-tuned model is better at resonding like jarvis and producing response in the best jarvis tone possible.

To-Do:

- [ ] Prepare instruct dataset(WIP)
- [ ] Fine-tune llama2-7b for a costum model `Llama-2-7b-chat-jarvis"`(WIP)
- [ ] Build a proper voice clone of jarvis(In progress): currently having difficulties finding clean voice samples of jarvis on the internet, so working with what i have, i guess won't be perfect.
- [ ] Use Whisper for voice to text input(if anyone has anything better, please suggest as this is the best i found out there.)
- [ ] Deploy the voice model as an API for everyone to be able to use it(We can deploy on my vps i don't know, if the specs will even let us though, we'll see)

## Converting model from hf to gguf file
Command:
```bash
python llama.cpp/convert.py jarvis-hf \  ml-env  01:41:56 PM
  --outfile jarvis-7b-v0.1.gguf \
  --outtype q8_0
```

## Why Jarvis?
Well, simple. I have always wanted to have my very own Jarvis, now i'm not talking about a siri clone or google home assitant clone. I am talking about my very own Jarvis, talks like jarvis, response like jarvis, feels like jarvis in the most accurate way possible.

###### * This project was inspired by "J.A.R.V.I.S" from the Marvel movie series.

Useful links:
-  converting model from hf to gguf https://github.com/ggerganov/llama.cpp/discussions/2948
-  Fixing issue with llama2 7b model error:Exception: Vocab size mismatch (model has 32000, but jarvis-hf/tokenizer.model has 32001). Fix here-> https://github.com/ggerganov/llama.cpp/issues/3900
- convert command: python llm/llama.cpp/convert.py ../jarvis-hf --outtype f16 --outfile converted.bin
- quantize: llm/llama.cpp/quantize converted.bin quantized.bin q4_0