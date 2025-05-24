from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from code.personal_learning.GENAI.schema import ProductPriceResponse
from langsmith import traceable

load_dotenv()

llm = ChatOpenAI(model="gpt-4", temperature=0.2)

prompt = PromptTemplate(
    input_variables=["product"],
     template="""
You are an expert pricing assistant. Your task is to estimate the current retail price in USD for the given product in the United States.

Return your answer as a valid JSON object using this schema:

{{
  "product": "<name of the product>",
  "price_usd": <integer>,  // Only an integer value, no decimals or strings
  "source": "<brief description of your estimate or a likely source>"
}}

Use your best judgment and knowledge to provide a realistic, confident estimate.

Product: {product}
""",
)

chain = LLMChain(llm=llm, prompt=prompt)

@traceable(name="GetProductPrice")
def get_product_price(product_name: str):
    response_text = chain.run(product=product_name)
    try:
        validated = ProductPriceResponse.parse_raw(response_text)
        return {"success": True, "data": validated.dict()}
    except Exception as e:
        return {
            "success": False,
            "error": "Validation failed",
            "raw_response": response_text,
            "details": str(e),
        }
