from langchain_core.messages import HumanMessage, AIMessage
from graphs import graph
from utils.logger import logger
from utils.summarizer import summarize_chat_history

rag_agent = graph.rag_agent()
conversation_history = []

def running_agent():
    global conversation_history
    logger.info("\n=== RAG AGENT===")
    while True:
        user_input = input("\nWhat is your question: ")
        if user_input.lower() in ['exit', 'quit']:
            logger.info("\nExiting agent. Goodbye!")
            break

        # Append the user input as HumanMessage (not a list!)
        conversation_history.append(HumanMessage(content=user_input))

        # Call the agent
        result = rag_agent.invoke({"messages": conversation_history})

        # Extract model’s reply
        ai_reply = result['messages'][-1]
        if not isinstance(ai_reply, AIMessage):
            ai_reply = AIMessage(content=str(ai_reply))

        # Add AI response to conversation history
        conversation_history.append(ai_reply)

        # Optionally summarize (but keep history as BaseMessage objects)
        summary = summarize_chat_history(conversation_history)
        logger.debug(f"Conversation summary: {summary}")

        # Print outputs cleanly
        logger.info("\n=== ANSWER ===")
        print(ai_reply.content)

running_agent()
