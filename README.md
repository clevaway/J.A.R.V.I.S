# Jarvis

The J.A.R.V.I.S Large Language Model, 100% offline

We have use custom jarvis dataset and various other open datasets on the internet of jarvis's dialog with stark to fine-tune on top of Llama2 7b

## Content

- Dataset [here](https://huggingface.co/datasets/fotiecodes/jarvis-llama2-dataset) | dataset is being created progresively
- Model: [here](https://huggingface.co/fotiecodes/Llama-2-7b-chat-jarvis) | Updated every week or so

Jarvis is bing built with privacy in mind, everything runs locally. This fine-tuned model is better at responding like jarvis and producing response in the best jarvis tone possible.

### Usage

#### Installation

I. You will need Ollama to download and install the model for use locally.

1. Download and install ollama [here](https://ollama.com/)
2. Run the command:

  ```bash
    ollama run fotiecodes/jarvis
  ```

  This will install the model [jarvis](https://ollama.com/fotiecodes/jarvis) model locally.
3. From here you can already chat with jarvis from the command line by running the command `ollama run jarvis` or `ollama run jarvis:latest` to run the lastest stable release.

II. After installing the model locally and started the ollama sever and can confirm it is working properly, clone this repositry and run the main.py file

That's it, you can start talking to Jarvis✨

### Setup local dev

Please go to [CONTRIBUTOR.md](CONTRIBUTOR.md) for more info.

To-Do:

- [ ] Prepare instruct dataset(WIP)
- [ ] Fine-tune llama2-7b for a costum model `Llama-2-7b-chat-jarvis"`(WIP)
- [ ] Build a proper voice clone of jarvis(In progress): currently having difficulties finding clean voice samples of jarvis on the internet, so working with what i have, i guess won't be perfect.
- [ ] Use Whisper for voice to text input(if anyone has anything better, please suggest as this is the best i found out there.)
- [ ] Deploy the voice model as an API for everyone to be able to use it(We can deploy on my vps i don't know, if the specs will even let us though, we'll see)

<!-- ## Converting model from hf to gguf file
Command:
```bash
python llama.cpp/convert.py jarvis-hf \
  --outfile jarvis-7b-v0.1.gguf \
  --outtype q8_0
``` -->

## Why Jarvis?

Well, simple. I have always wanted to have my very own Jarvis, now i'm not talking about a siri clone or google home assitant clone. I am talking about my very own Jarvis, talks like jarvis, response like jarvis, feels like jarvis in the most accurate way possible.

## Acknowledgments

Special thanks to:

- [ollama]([ollama](https://github.com/ollama/ollama)) for the amazing project
- [ggerganov](https://github.com/ggerganov) the genius behind [llama.cpp](https://github.com/ggerganov/llama.cpp)
- Every contributor to this repo:)

### Supporters ✨

- We're looking for Sponsors!

### License 📜

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details. 📄

### Support 💬

If you have any questions, suggestions, or need assistance, please open an issue:)

**Disclaimer**:
Jarvis can make mistakes. Consider checking important information.

###### * This project was inspired by "J.A.R.V.I.S" from the Marvel movie series
