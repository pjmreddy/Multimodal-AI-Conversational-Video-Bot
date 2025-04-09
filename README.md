<div align="center">

# 🤖 Multimodal RAG: Conversational Video Bot

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Powered-green)](https://github.com/hwchase17/langchain)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[Features](#-key-features) • [Architecture](#%EF%B8%8F-architecture) • [Installation](#-installation) • [Usage](#-usage) • [Contributing](#-contributing)

</div>

## 🎯 Overview

A state-of-the-art multimodal retrieval-augmented generation (RAG) system that enables semantic search and conversational interactions across video and text content. This project combines cutting-edge AI technologies to deliver a powerful conversational video bot.

### What Makes It Special?
- 🎥 Process both video and text content seamlessly
- 🔍 Achieve 80% precision in content search
- 🧠 Utilize advanced BridgeTower embeddings
- 🗣️ Support natural multi-turn conversations

## 🌟 Key Features

- **Multimodal RAG System**: Seamlessly integrates video and text processing capabilities
- **High-Precision Search**: Achieves 80% precision in content retrieval
- **Advanced Embeddings**: Utilizes BridgeTower embeddings with LanceDB for efficient storage and retrieval
- **Smart Transcription**: Implements Whisper for accurate video transcription
- **Image Understanding**: Leverages LLaVA 1.5 for advanced image captioning
- **Conversational Interface**: Supports natural multi-turn queries through LangChain integration

## 🛠️ Architecture

The system combines several cutting-edge components:

1. **BridgeTower Embeddings**: Generates high-quality embeddings for both text and image content
2. **LanceDB**: Provides efficient vector storage and retrieval capabilities
3. **Whisper**: Handles accurate transcription of video content
4. **LLaVA 1.5**: Enables sophisticated image captioning
5. **LangChain**: Powers the conversational interface and query processing

## Demo Output
![Live Demo](output.jpg)


## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup
1. Clone the repository
```bash
git clone https://github.com/pjmreddy/Multimodal-RAG-Conversational-Video-Bot.git
cd Multimodal-RAG-Conversational-Video-Bot
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Quick Start
1. **Run the Demo**:
```bash
python run_demo.py
```

2. **Interactive Notebook**:
Explore the interactive demo in `Gradio.ipynb`

## 📁 Project Structure

```
├── mm_rag/
│   ├── embeddings/         # BridgeTower embedding implementation
│   ├── MLM/               # Machine learning model components
│   └── vectorstores/      # LanceDB integration
├── shared_data/          # Example data and images
└── requirements.txt      # Project dependencies
```

## 👥 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Acknowledgments

This project was developed under the guidance and support of:
- deeplearning.ai
- Intel

<div align="center">

---

Developed with ❤️ by [Jagan Reddy](mailto:peravali810@gmail.com) | Part of the deeplearning.ai and Intel collaboration

</div>



