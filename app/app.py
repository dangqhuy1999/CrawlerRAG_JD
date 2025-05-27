# File: app/app.py
import gradio as gr
from agent.rag_chain import search_jobs

gr.ChatInterface(fn=search_jobs, title="Job Market RAG Assistant").launch()
