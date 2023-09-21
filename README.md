# dalle2-azure-openai
This application integrates with OpenAI's DALL-E 2 to generate images based on user prompts.

## Prerequisites

- Python (e.g., 3.8 or higher)
- [pip](https://pip.pypa.io/en/stable/installation/)

## Getting Started

### 1. Clone the Repository

To clone the repository, run:
git clone [YOUR_REPOSITORY_LINK]

### 2. Install dependencies

pip install Flask OpenAI

### 3. Obtain Azure OpenAI API Key and URL

To get your Azure OpenAI API key:
Navigate to the Azure OpenAI portal.
Follow the portal's instructions to create a new OpenAI instance and obtain your API key.
When the OpenAI instance is created, go to Resource Management > Keys and endpoints
Copy Endpoint to OPENAI_API_BASE and Key 1 to OPENAI_API_KEY in the next step

### 4. Setup Environment Variables using a .env File
In the root of your project directory:

Create a file named .env.
Open the .env file and add the following:
OPENAI_API_BASE=YOUR_OPENAI_URL
OPENAI_API_KEY=YOUR_OPENAI_KEY
Replace YOUR_OPENAI_URL and YOUR_OPENAI_KEY with the actual key you obtained from Azure.

Important: This .env file is for local use only. Do NOT commit it to your Git repository to ensure your API key remains confidential.

### 5. Run the Application
With all the above steps completed, you can now run the application:
python app.py
Once the app is running, access it in your browser at http://127.0.0.1:5000.
