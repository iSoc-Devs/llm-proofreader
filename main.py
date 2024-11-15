from dotenv import load_dotenv
from langchain_openai import ChatOpenAI  # Import for ChatOpenAI
from langchain.prompts import PromptTemplate  # Import for PromptTemplate

load_dotenv()
# Load the API key from the environment variables

# Initialize the model with GPT-3.5 Turbo
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# Define the prompt template for strengths and improvements
email_feedback_prompt = PromptTemplate(
    input_variables=["author_name", "article_content", "previous_post_topic"],
    template=(
        "Analyze the following article by {author_name} on the topic '{previous_post_topic}'.\n\n"
        "Article content:\n{article_content}\n\n"
        "Identify 2-3 specific strengths of the article and list them. Then, suggest 2-3 improvements for the author to consider in future posts. "
        "Format the response as:\n"
        "Strengths:\n- (Point 1)\n- (Point 2)\n\n"
        "Improvement Areas:\n- (Point 1)\n- (Point 2)"
    )
)

# Initialize the language model
llm = ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo")

# Set up the LLMChain for generating feedback
feedback_chain = email_feedback_prompt | llm

# Define a function to generate the feedback content
def generate_feedback_email(author_name, article_content, previous_post_topic):
    # Run the model chain to analyze the article and get feedback
    analysis = feedback_chain.invoke({
        "author_name": author_name,
        "article_content": article_content,
        "previous_post_topic": previous_post_topic
    }).content

    # Format the output into a professional email
    email_feedback = f"""
    Subject: Feedback on Your Recent Post on {previous_post_topic}

    Hi {author_name},

    Thank you for contributing such insightful content on {previous_post_topic} to our platform! We truly appreciate your expertise and the effort you put into your writing.

    Here are a few highlights we loved about your recent post:
    {analysis.split('Improvement Areas:')[0].strip()}

    To help you make future posts even more engaging and impactful, here are some recommendations:
    {analysis.split('Improvement Areas:')[1].strip()}

    We look forward to seeing your next piece!

    Best regards,
    The Ghost Editorial Team
    """
    return email_feedback

# Example input
author_name = "Alice"
previous_post_topic = "AI Transforming Healthcare"
article_text = """
Artificial intelligence is an exciting field. Its application in healthcare, for instance, helps to predict outcomes...
[Insert more detailed synthetic article content with some strengths and intentional weaknesses for analysis]
"""

# Code below is now done later
# feedback_email = generate_feedback_email(author_name, article_text, previous_post_topic)
# print(feedback_email)

# Define the evaluation prompt template
evaluation_prompt = PromptTemplate(
    input_variables=["feedback_email"],
    template=(
        "You are an editorial assistant. Please evaluate the following feedback email for tone, formatting, and helpfulness.\n\n"
        "Feedback Email:\n{feedback_email}\n\n"
        "Analyze the email on these points:\n"
        "1. Is the tone constructive and polite?\n"
        "2. Are the strengths and improvements balanced?\n"
        "3. Is the formatting clear and easy to read?\n"
        "4. Give an overall rating (Excellent, Good, Fair, Poor) and provide a brief reason.\n\n"
        "Format your response as:\n\n"
        "Evaluation:\n- Tone: (Constructive/Neutral/Negative)\n"
        "- Balance: (Balanced/Too Positive/Too Negative)\n"
        "- Formatting: (Clear/Unclear)\n"
        "- Overall Rating: (Excellent/Good/Fair/Poor)\n"
        "- Summary: (Brief explanation of your assessment)"
    )
)

# Initialize an LLMChain for the evaluation process
evaluation_chain = evaluation_prompt | llm

# Function to evaluate the generated feedback email
def evaluate_feedback_email(feedback_email):
    # Run the evaluation chain
    evaluation = evaluation_chain.invoke({
        "feedback_email": feedback_email
    }).content

    return evaluation

# Run the feedback generation step to get a sample email
feedback_email = generate_feedback_email(author_name, article_text, previous_post_topic)
print("Generated Feedback Email:\n", feedback_email)

print('###########################')
print('###########################')
print('###########################')

# Evaluate the feedback email
evaluation_result = evaluate_feedback_email(feedback_email)
print("\nEvaluation of the Feedback Email:\n", evaluation_result)