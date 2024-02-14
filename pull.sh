#!/bin/bash

pgrep ollama | xargs kill

ollama serve 2>&1 | tee ollama.server.log &

while ! ollama pull $1; do
    sleep 1
done

pgrep ollama | xargs kill
