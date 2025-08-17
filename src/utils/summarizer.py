from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain

from llm.gemini import get_gemini
from utils.logger import logger

# Initialize the LLM for summarization
llm = get_gemini()


def summarize_chat_history(chat_history: list):
    """Summarize chat history while retaining key details of both user queries and chatbot responses.
    """
    if not chat_history:
        return ""
    
    try:
        # Prepare document for summarization
        formatted_history = "\n".join(
            f"{msg.type}: {msg.content}" if hasattr(msg, "type") and hasattr(msg, "content") else str(msg)
            for msg in chat_history
        )
            
        doc = Document(page_content=formatted_history)
        chain = load_summarize_chain(llm, chain_type="map_reduce")

        # Generate summary
        summary = chain.invoke([doc])
        return summary.get('output_text', '')

    except Exception as e:
        logger.error(
            f"Error summarizing chat history: {str(e)}", exc_info=True)
        return chat_history