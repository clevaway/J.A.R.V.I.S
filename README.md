# Jarvis
The J.A.R.V.I.S Large Language Model, 100% offline

A fine-tune of LLama2 7b on Jarvis dataset

## Content:
- Dataset [here](https://huggingface.co/datasets/fotiecodes/jarvis-llama2-dataset) | dataset is being created progrsively
- Model: [here](https://huggingface.co/fotiecodes/Llama-2-7b-chat-jarvis) | Updated every week or so

Jarvis is bing built with privacy in mind, everything runs locally. In the main time it works with local LLama2 7b with ollama until the fine-tuned mondel is ready to be used.
The fine-tuned model is better at resonding like jarvis and producing response in the best jarvis tone possible.

To-Do:

- [ ] Prepare instruct dataset(WIP)
- [ ] Fine-tune llama2-7b for a costum model `Llama-2-7b-chat-jarvis"`(WIP)
- [ ] Build a proper voice clone of jarvis(In progress): currently having difficulties finding clean voice samples of jarvis on the internet, so working with what i have, i guess won't be perfect.
- [ ] Integrate with a fine-tuned version of any open source LLM out there, like Llama 2 or Mistral AI etc
- [ ] Use Whisper for voice to text input(if anyone has anything better, please suggest as this is the best i found out there.)
- [ ] Deploy the voice model as an API for everyone to be able to use it(We can deploy on my vps i don't know, if the specs will even let us though, we'll see)

