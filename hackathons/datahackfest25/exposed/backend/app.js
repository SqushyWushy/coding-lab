import express from "express";
import mongoose from "mongoose";
import cors from "cors";
import dotenv from "dotenv";
import { generateGeminiSummary } from "./services/gemini.js";
import analyzeRouter from "./routes/analyze.js";

dotenv.config(); // <-- config before anything

const app = express();
const PORT = process.env.PORT || 4000;

// Middleware
app.use(cors({
  origin: [
    'http://localhost:5173',
    'https://exposed-ten.vercel.app',
    'https://exposed-eyj8j05pv-hector-gonzalezs-projects-69248f08.vercel.app',
    'https://exposed-me4lf3z5y-hector-gonzalezs-projects-69248f08.vercel.app',
    'https://exposed-25k8mjn88-hector-gonzalezs-projects-69248f08.vercel.app',
    'https://exposed-fgx4reivq-hector-gonzalezs-projects-69248f08.vercel.app',
    'https://exposed-9min3t9ix-hector-gonzalezs-projects-69248f08.vercel.app',
    'https://exposed-di0a5xzwh-hector-gonzalezs-projects-69248f08.vercel.app',
    'https://*.vercel.app',
    'https://coding-lab-production-3953.up.railway.app',
    'https://*.railway.app'
  ],
  credentials: true
}));
app.use(express.json());

// MongoDB connection
mongoose
  .connect(process.env.MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log("🟢 Connected to MongoDB Atlas"))
  .catch((err) => console.error("🔴 MongoDB connection error:", err));

// Test route for Gemini
app.get("/gemini-test", async (req, res) => {
  const result = await generateGeminiSummary("Give me 3 AI facts.");
  res.send(result || "❌ Gemini failed");
});

// Analyze routes
app.use("/analyze", analyzeRouter);

// Basic route
app.get("/", (req, res) => {
  res.send("Backend is alive 🚀");
});

// Start server
app.listen(PORT, () => {
  console.log(`🔥 Backend running at http://localhost:${PORT}`);
});
