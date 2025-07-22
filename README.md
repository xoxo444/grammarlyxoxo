Grammarly Xoxo

Grammarly Xoxo is an elegant, AI-powered grammar and spelling corrector built using Hugging Face's `T5-base` model and Gradio. It corrects flawed English sentences and quietly polishes your words — with clarity and just the right touch of precision.

 ✨ Features

-  Grammar and spelling correction via `vennify/t5-base-grammar-correction`
-  Post-processing to fix sentence capitalization
-  Beautiful pastel pink-beige themed Gradio interface
-  Handles incomplete or poorly written sentences
-  Ready for deployment on Hugging Face Spaces or Streamlit

 📸 Preview

![App Screenshot](<img width="1382" height="823" alt="Screenshot (533)" src="https://github.com/user-attachments/assets/f01485d3-3e02-4903-a3f0-c56e5cede7fc" />)


 🚀 How to Run

1. Clone the repo 
```bash
git clone https://github.com/xoxo444/grammarly-xoxo.git
cd grammarly-xoxo
````
2. Install dependencies

```bash
pip install -r requirements.txt
```
3. Run the app

```bash
python app.py
```
4. View in browser
   The app will run at `http://localhost:7860/`


Sample Input:
> we talked at wrong hours maybe that why we never said the right things.
Output:
> We talked at wrong hours maybe that's why we never said the right things.


 🛠 Tech Stack
* Python
* Hugging Face Transformers (`T5-base`)
* Gradio
* Regex (for post-processing)
* Custom CSS


For every sentence that was nearly right, and still remembered.
Because the way we say things matters.


Made by [xoxo](https://github.com/xoxo444)





