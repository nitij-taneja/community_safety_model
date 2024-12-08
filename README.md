# Community Safety Model

This project enhances community safety and well-being by predicting safety risks and providing real-time alerts to students commuting to rural-area colleges. Using advanced machine learning (ML), deep learning (DL), and natural language processing (NLP) techniques, the system identifies high-risk areas and times, enabling users to take proactive measures.

---

## Features
- **Predictive Modeling**: Utilizes CNN-LSTM for spatial and temporal risk analysis.
- **Real-Time Chatbot**: Powered by GPT for queries and incident reporting.
- **Heatmaps and Visualizations**: Highlights high-risk zones for better awareness.
- **Cloud Deployment**: Features continuous model updates using MLOps practices.

---

## Installation

1. **Clone the repository**:  
   `git clone https://github.com/nitij-taneja/community_safety_model.git`

2. **Navigate to the project directory**:  
   `cd community_safety_model`

3. **Activate the virtual environment**:  
   - For Windows: `.\venv\Scripts\activate`  
   - For Mac/Linux: `source venv/bin/activate`

4. **Install dependencies**:  
   `pip install -r requirements.txt`

---

## Usage

- **Run the Backend**: Start the FastAPI server:  
  `uvicorn backend.app:app --reload`

- **Perform EDA**: Open `notebooks/eda.ipynb` in Jupyter or VS Code to explore the dataset and analyze trends.

---

## Folder Structure
- **data/**: Raw and processed datasets.
- **scripts/**: Data processing and model training scripts.
- **notebooks/**: Jupyter notebooks for EDA and model evaluation.
- **outputs/**: Model predictions and visualizations.
- **backend/**: FastAPI server for API handling.
- **frontend/**: Chatbot and safety dashboard implementation.
- **config/**: Configuration files for global settings.
- **models/**: Saved trained models.
- **mlops/**: Scripts and configurations for MLOps pipelines.

---

## Technologies Used
- **Data Science**: pandas, numpy, matplotlib, seaborn
- **Machine Learning**: scikit-learn, tensorflow
- **NLP**: OpenAI GPT API, Hugging Face Transformers
- **Backend**: FastAPI, Flask, Uvicorn
- **Deployment**: Docker, MLflow, AWS

---

## License
This project is licensed under the **MIT License**. See the LICENSE file for details.

---

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch:  
   `git checkout -b feature-branch`
3. Commit your changes:  
   `git commit -m "Add feature"`
4. Push to the branch:  
   `git push origin feature-branch`
5. Open a pull request.

---

## Contact
For any inquiries, please reach out via **tanejanitij4002@gmail.com**.

   
