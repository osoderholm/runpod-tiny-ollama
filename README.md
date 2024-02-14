# runpod-tiny-ollama

Ready to use Runpod Serverless container for running `tinyllama` using Ollama.

The `tinyllama` is already pulled, making the Docker image larger but shortening the startup time.

The request is a normal [Ollama generate endpoint request](https://github.com/ollama/ollama/blob/main/docs/api.md#generate-a-completion) but must me wrapped in an `input` object:

```
{
  "input": {
    "system": "You are an ironic and unhelpful assistant because you don't get enough salary.",
    "prompt": "In what country is Paris?"
  }
}
```

`model` and `stream` parameters can not be set as they have already been specified.
