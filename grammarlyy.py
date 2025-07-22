import gradio as gr
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import re


model_name = "vennify/t5-base-grammar-correction"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def correct_sentence(sentence):
    if not sentence.strip():
        return "Please enter a sentence to correct."
    input_text = "grammar: " + sentence

    input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=128, truncation=True)

    outputs = model.generate(input_ids, max_length=128, num_beams=5, early_stopping=True)

    corrected = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return capitalize_sentences(corrected)

def capitalize_sentences(text):
    def capitalize_match(match):
        return match.group(1) + match.group(2).upper()
    
    text = text.strip()
    if text:
        text = text[0].upper() + text[1:]

    pattern = re.compile(r'([.?!]\s+)([a-z])')
    return pattern.sub(capitalize_match, text)



css = """
body {
    background-color: #fff2f2 !important;
    font-family: 'Segoe UI', sans-serif;
}

.gradio-container {
    max-width: 700px;
    margin: auto;
    padding-top: 40px;
}

h1, h3 {
    color: #ffcad4 !important;
    text-align: center;
}

textarea, .input-textbox, .output-textbox {
    border-radius: 12px !important;
    border: 1px solid #d3a4a4 !important;
    background-color: #fffafa !important;
    color: #2d2d2d !important;
    font-size: 16px !important;
    padding: 12px !important;
    box-shadow: 0 2px 6px rgba(0,0,0,0.08) !important;
}

button {
    background-color: #ffcad4 !important;
    color: #4b2c2c !important;
    border-radius: 12px !important;
    padding: 10px 20px !important;
    border: none !important;
    font-weight: bold !important;
    transition: 0.3s ease all !important;
    font-size: 16px !important;
}

button:hover {
    background-color: #fcb6c1 !important;
    transform: scale(1.02) !important;
}

footer, .svelte-1ipelgc {
    display: none !important;
}
"""


interface = gr.Interface(
    fn=correct_sentence,
    inputs=gr.Textbox(lines=4, placeholder="Type your sentence here..."),
    outputs=gr.Textbox(label=" Corrected Sentence "),
    title="Grammarly xoxo: AI Grammar & Spelling Fixer",
    description="Write anything, and let AI gently fix your grammar & spelling 💌",
    theme="default",
    css=css
)


interface.launch()
