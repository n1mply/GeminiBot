import google.generativeai as genai
import asyncio


async def get_gemini_response(user_text):
  genai.configure(api_key="YOUR-KEY")
  model = genai.GenerativeModel(model_name='gemini-pro')
  response = await model.generate_content_async(f"{user_text} Учти, что форматирование текста должно быть согласно форматированию Telegram")
  return response.text
