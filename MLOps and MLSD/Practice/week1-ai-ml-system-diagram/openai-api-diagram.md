## OpenAI API Architecture

```text
├── Client Application
├── API Gateway
│   ├── Auth & Rate Limiter
│   └── Request Router
│       ├── GPT Model (Text Completion)
│       ├── DALL·E Model (Image Generation)
│       ├── Whisper Model (Speech-to-Text)
│       └── Embedding Model
└── Response Formatter
```
- Client Application: The entry point where users send requests.
- API Gateway: Handles incoming requests, including authentication and rate limiting.
- Auth & Rate Limiter: Verifies user credentials and controls request frequency.
- Request Router: Directs the request to the appropriate model:
  - GPT Model: Handles text completions.
  - DALL·E Model: Manages image generation.
  - Whisper Model: Converts speech to text.
  - Embedding Model: Processes embeddings.
- Response Formatter: Aggregates and formats responses before sending them back to the client.
