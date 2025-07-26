// services/gemini.js
import axios from "axios";
import dotenv from "dotenv";
dotenv.config();

export async function generateGeminiSummary(prompt) {
  try {
    const response = await axios.post(
      "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent",
      {
        contents: [
          {
            parts: [{ text: prompt }],
          },
        ],
      },
      {
        headers: {
          "Content-Type": "application/json",
          "X-Goog-Api-Key": process.env.GEMINI_API_KEY,
        },
      },
    );

    return (
      response.data.candidates?.[0]?.content?.parts?.[0]?.text ||
      "❌ No response text"
    );
  } catch (err) {
    console.error("Gemini API error:", err.response?.data || err.message);
    return null;
  }
}
