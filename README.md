<div align="center">

# Multimodal RAG: Conversational Video Bot
</div>

A state-of-the-art multimodal retrieval-augmented generation (RAG) system that enables semantic search and conversational interactions across video and text content. Leveraging BridgeTower embeddings with LanceDB for efficient vector storage, Whisper for accurate transcription, and LLaVA 1.5 for advanced captioning. Built with LangChain for multi-turn conversational capabilities.

## 🌟 Key Features

- **Multimodal RAG System**: Seamlessly integrates video and text processing capabilities
- **High-Precision Search**: Achieves 80% precision 
- **Advanced Embeddings**: Utilizes BridgeTower embeddings with LanceDB for efficient storage and retrieval
- **Transcription**: Implements Whisper for accurate video transcription
- **Image Understanding**: Leverages LLaVA 1.5 for advanced image captioning
- **Conversational Interface**: Supports multi-turn queries through LangChain integration

## 🛠️ Architecture

The system combines several cutting-edge components:

1. **BridgeTower Embeddings**: Generates high-quality embeddings for both text and image content
2. **LanceDB**: Provides efficient vector storage and retrieval capabilities
3. **Whisper**: Handles accurate transcription of video content
4. **LLaVA 1.5**: Enables sophisticated image captioning
5. **LangChain**: Powers the conversational interface and query processing

## 🚀 Getting Started

### Prerequisites

```bash
pip install -r requirements.txt
```

### Usage

1. **Run the Demo**:
```bash
python run_demo.py
```

2. **Jupyter Notebook**:
Explore the interactive demo in `L1_Chat with Video_ Interactive Demo.ipynb`

## 📁 Project Structure

```
├── mm_rag/
│   ├── embeddings/         # BridgeTower embedding implementation
│   ├── MLM/               # Machine learning model components
│   └── vectorstores/      # LanceDB integration
├── shared_data/          # Example data and images
└── requirements.txt      # Project dependencies
```

## 🤝 Acknowledgments

This project was developed under the guidance and support of:
- deeplearning.ai
- Intel

<div align="center">
Developed with ❤️ by <href mailto=peravali810@gmail.com> peravali810@gmail.com as part of the deeplearning.ai and Intel collaboration.
</div>

---



