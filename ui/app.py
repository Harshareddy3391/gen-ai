import gradio as gr

def chat(message):
    return f"You typed: {message}"

demo = gr.Interface(
    fn=chat,
    inputs=gr.Textbox(
        placeholder="write something harsha..."
    ),
    outputs="text",
    title="heyy hii harsha"
)

demo.launch()