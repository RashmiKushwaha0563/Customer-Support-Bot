import requests
import gradio as gr

# DeepSeek API URL
OLLAMA_URL = "http://localhost:11434/api/generate"

# Sample FAQ Database
FAQ_DB = {
    "order tracking": "You can track your order by logging into your account and navigating to 'My Orders'.",
    "return policy": "We accept returns within 30 days. Visit our Returns page to initiate a return.",
    "customer support contact": "You can reach customer support at support@example.com or call us at +1-800-555-1234.",
    "payment methods": "We accept Visa, MasterCard, PayPal, and Apple Pay for secure transactions.",
    "shipping details": "Orders are processed within 24 hours. Standard shipping takes 3-5 business days.",
    "change shipping address": "To change your shipping address, go to your account settings before your order is shipped.",
    "cancel order": "You can cancel your order within 1 hour of placing it from the 'My Orders' section.",
    "delayed shipment": "If your shipment is delayed, please check your order status or contact support for assistance.",
    "warranty information": "All products come with a 1-year warranty. Visit our Warranty page for details.",
    "international shipping": "We offer international shipping to select countries. Check our Shipping Policy for the full list.",
    "lost password": "Click 'Forgot Password' on the login page to reset your password via email.",
    "update payment method": "You can update your payment method in your account settings under 'Payment Options'.",
    "product availability": "If a product is out of stock, you can sign up for restock notifications on the product page.",
    "bulk orders": "For bulk or corporate orders, please contact sales@example.com for special pricing.",
    "refund status": "Refunds are processed within 5-7 business days after we receive your returned item.",
    "technical support": "For technical issues, visit our Help Center or contact techsupport@example.com.",
    "subscription management": "Manage your subscriptions from your account dashboard under 'Subscriptions'.",
    "gift cards": "Gift cards can be purchased and redeemed during checkout. Check your balance in your account.",
    "order invoice": "Download your order invoice from the 'My Orders' section after your order is shipped.",
    "product customization": "Some products can be customized. Look for the 'Customize' option on the product page.",
    "environmental policy": "Read about our sustainability and environmental initiatives on our Environmental Policy page.",
    "track refund": "You can track your refund status in the 'My Orders' section or contact support for updates.",
    "change email address": "To change your email address, go to your account settings and update your contact information.",
    "mobile app support": "Download our mobile app from the App Store or Google Play for easy order management.",
    "report damaged product": "If you received a damaged product, please contact support within 48 hours for a replacement.",
    "loyalty program": "Join our loyalty program to earn points on every purchase. Visit the Rewards section for more info.",
    "reschedule delivery": "To reschedule your delivery, contact our support team before the scheduled date.",
    "invoice for business": "For business invoices, please email business-support@example.com with your order details.",
    "customer helpline number": "You can reach our 24/7 customer helpline at +1-800-555-1234 for immediate assistance."
}

def chatbot_response(user_query, language="English"):
    """
    Uses DeepSeek AI to answer customer queries by matching them with predefined FAQ responses.
    """
    prompt = f"Find the best match from the FAQ database for this customer query:\n\n'{user_query}'\n\n" \
             f"Available FAQs: {list(FAQ_DB.keys())}\n" \
             f"Provide a response based on the closest matching FAQ in {language}."

    payload = {
        "model": "llama2",
        "prompt": prompt,
        "stream": False
    }


    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        # return "I'm sorry, I couldn't find an answer. Please contact support@example.com for further assistance."
        ai_response = response.json().get("response", "I'm sorry, I don't have an answer for that.")
        return FAQ_DB.get(ai_response.lower(), ai_response)  # Return AI response or predefined answer
    else:
        print("Error:", response.status_code, response.text)
        return "Sorry, I couldn't process your request."



# Create Gradio interface
interface = gr.Interface(
    fn=chatbot_response,
    inputs=gr.Textbox(lines=2, placeholder="Ask your customer support question..."),
    outputs=gr.Textbox(label="Chatbot Response"),
    title="AI-Powered Customer Support Chatbot",
    description="Ask a question, and the AI will respond with the best-matching FAQ answer."
)

# Launch the web app
if __name__ == "__main__":
    interface.launch()





# # Test Customer Support Chatbot
# if __name__ == "__main__":
#     sample_query = "How can I return a product?"
#     print("### Chatbot Response ###")
#     print(chatbot_response(sample_query))







