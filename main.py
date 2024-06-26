
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = 'Importance of Large Language Models'
    content = '''
    <h2>What are Large Language Models (LLMs)?</h2>
    <p>LLMs are a type of machine learning model that is trained on a massive dataset of text and code. This training allows them to understand and generate natural language, perform complex tasks like translation and summarization, and even write creative content.</p>

    <h2>Benefits of LLMs</h2>
    <ul>
        <li>Improved Natural Language Processing (NLP)</li>
        <li>Enhanced Machine Translation</li>
        <li>Efficient Text Summarization</li>
        <li>Code Generation and Analysis</li>
    </ul>
    '''
    return render_template('index.html', title=title, content=content)

@app.route('/use-cases')
def use_cases():
    title = 'Use Cases of LLMs'
    use_cases = [
        {'title': 'Chatbots and Virtual Assistants', 'desc': 'LLMs power chatbots and virtual assistants, enabling them to engage in natural language conversations and provide personalized assistance.'},
        {'title': 'Language Translation', 'desc': 'LLMs enhance machine translation, enabling real-time translation of text and speech across different languages.'},
        {'title': 'Text Summarization', 'desc': 'LLMs can summarize long pieces of text into concise and informative summaries, making it easier to digest large amounts of information.'},
        {'title': 'Code Generation', 'desc': 'LLMs can generate code in multiple programming languages, assisting developers with coding tasks and improving productivity.'}
    ]
    return render_template('use-cases.html', title=title, use_cases=use_cases)

@app.route('/benefits')
def benefits():
    title = 'Benefits of LLMs'
    benefits = [
        {'title': 'Enhanced Accuracy', 'desc': 'LLMs are trained on vast datasets, giving them a deep understanding of language and context, leading to highly accurate results.'},
        {'title': 'Improved Efficiency', 'desc': 'LLMs automate many language-related tasks, freeing up human resources for more complex and creative endeavors.'},
        {'title': 'Reduced Costs', 'desc': 'LLMs can reduce the need for manual labor in tasks such as data annotation and content creation, resulting in cost savings.'},
        {'title': 'Innovative Applications', 'desc': 'LLMs open up new possibilities for applications in various industries, such as healthcare, finance, and education.'}
    ]
    return render_template('benefits.html', title=title, benefits=benefits)

@app.route('/limitations')
def limitations():
    title = 'Limitations of LLMs'
    limitations = [
        {'title': 'Bias and Fairness', 'desc': 'LLMs can inherit biases from the data they are trained on, leading to potentially unfair or inaccurate results.'},
        {'title': 'Computational Cost', 'desc': 'Training and deploying LLMs requires significant computational resources and can be expensive.'},
        {'title': 'Ethical Concerns', 'desc': 'The use of LLMs raises ethical questions about privacy, copyright, and the spread of misinformation.'}
    ]
    return render_template('limitations.html', title=title, limitations=limitations)

@app.route('/resources')
def resources():
    title = 'Resources on LLMs'
    resources = [
        {'title': 'Hugging Face', 'link': 'https://huggingface.co/'},
        {'title': 'OpenAI', 'link': 'https://openai.com/'},
        {'title': 'Google AI', 'link': 'https://ai.google/'}
    ]
    return render_template('resources.html', title=title, resources=resources)

if __name__ == '__main__':
    app.run(debug=True)
