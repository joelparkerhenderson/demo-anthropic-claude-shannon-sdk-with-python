#!/usr/bin/env python
 
import anthropic

client = anthropic.Anthropic(
    # api_key defaults to process.env["ANTHROPIC_API_KEY"]
    # api_key="my_api_key",
)

message = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude"}
    ]
)

print(message.content)
