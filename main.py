import csv

# Here is a template for the CSV with the requested columns, to be filled with real data
tool_data = [
    ["ChatGPT", "Chat / Conversational AI", "Conversational AI", "Freemium", "USA", "OpenAI", "Sam Altman", "2022-11", "100,000,000+", "4.8/5", "Web, iOS, Android, API, Chrome Extension", "Closed-source", "Natural language conversations and various tasks", "Sometimes inaccurate, no real-time info", "Claude, Gemini, Perplexity, Grok", "Custom GPTs, plugin support", "$20/month Plus, Free tier"],
    ["Midjourney", "Image generation & editing", "Text-to-image", "Paid", "USA", "Midjourney Inc.", "David Holz", "2022-07", "20,000,000+", "4.7/5", "Web (Discord)", "Closed-source", "Artistic image generation via text prompts", "No photo editing, Discord only", "DALL-E, Stable Diffusion, Adobe Firefly", "Distinct art style, community gallery", "$10-60/month"],
    ["Synthesia", "Video generation & editing", "AI video platform", "Paid", "UK", "Synthesia Ltd", "Victor Riparbelli", "2017-08", "60,000+", "4.6/5", "Web", "Closed-source", "AI avatar video creation", "Script-only, avatar realism limits", "HeyGen, Colossyan, DeepBrain", "230+ avatars, 140+ languages", "$22-70/month"],
    ["ElevenLabs", "Audio & Music AI", "Text-to-speech, voice cloning", "Freemium", "USA", "ElevenLabs", "Matvei V. and Piotr D.", "2022-04", "1,000,000+", "4.5/5", "Web, API", "Closed-source", "Realistic speech synthesis & voice cloning", "Limits for free users", "Murf, WellSaid Labs", "Voice lab, multi-lingual", "Free, $5+, Enterprise"],
    ["GitHub Copilot", "Coding & Developer AI", "Code completion", "Paid", "USA", "GitHub (Microsoft)", "Satya Nadella (Microsoft CEO)", "2021-06", "1,500,000+", "4.5/5", "IDE plugins, API", "Closed-source", "AI code suggestions in IDE", "Not always correct, context limits", "Cursor, Tabnine, Codeium", "Trained on public code, multi-language", "$10-19/user/mo"],
    ["Perplexity AI", "Research & Knowledge AI", "Search engine, web AI", "Freemium", "USA", "Perplexity AI", "Aravind Srinivas", "2022-12", "10,000,000+", "4.7/5", "Web, iOS, Android, API", "Closed-source", "Fact-checked real-time answers", "Sometimes incomplete data", "ChatGPT, Gemini, You.com", "Citation-first, Pro with web search", "Free, $20/mo Pro"],
    ["Notion AI", "Productivity & Office AI", "Document, workspace assistant", "Freemium", "USA", "Notion Labs Inc.", "Ivan Zhao", "2016-06", "30,000,000+", "4.8/5", "Web, iOS, Android, API", "Closed-source", "AI for writing, organizing, note-taking", "Context-binding within workspace", "Coda AI, Guru, Evernote", "All-in-one platform, embed AI everywhere", "Free, $10/user/mo AI"],
    ["DALL-E 3", "Image generation & editing", "Text-to-image", "Freemium", "USA", "OpenAI", "Sam Altman", "2023-09", "5,000,000+", "4.7/5", "Web, API (via ChatGPT)", "Closed-source", "High-fidelity image gen via text", "Biases, SFW filters, closed-source", "Midjourney, Adobe Firefly, Stable Diffusion", "Photorealistic + illustrative output", "Integrated, token-based"],
    ["Claude 3", "Chat / Conversational AI", "Conversational AI", "Freemium", "USA", "Anthropic", "Dario Amodei", "2023-03", "10,000,000+", "4.8/5", "Web, iOS, API", "Closed-source", "Safer, longer context chat", "Some feature limits", "ChatGPT, Gemini, Llama 3", "Long context, helpfulness", "Free, Pro $20/mo"],
    ["Google Veo", "Video generation & editing", "Video AI", "Freemium", "USA", "Google", "Sundar Pichai", "2024-05", "N/A", "4.6/5", "Web, API", "Closed-source", "Text-to-video generation", "Beta, output control limits", "Synthesia, Runway", "Google integration, fast render", "Free/beta, TBA"],
]

# Save as CSV
csv_file = "ai_tools_list_2025.csv"
columns = [
    "Name", "Category", "Sub-category", "Free/Paid/Freemium", "Country of origin", "Company/Organization", "CEO/Founder/Owner",
    "Launch year/date", "Number of users", "Popularity/ratings", "Supported platforms", "Open/closed source",
    "Speciality", "Limitations", "Competitors/Alternatives", "Unique features", "Pricing tiers"
]

with open(csv_file, mode="w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(columns)
    for row in tool_data:
        writer.writerow(row)

csv_file
