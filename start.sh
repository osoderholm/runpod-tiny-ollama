#!/bin/bash

pgrep ollama | xargs kill

ollama serve 2>&1 | tee ollama.server.log &

while ! ollama list; do
    sleep 0.1
done

python -u runpod_wrapper.py $1
