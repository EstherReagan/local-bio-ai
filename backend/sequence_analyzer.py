import sys
import requests

def calculate_gc_content(sequence):
    sequence = sequence.upper()
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    total = len(sequence)
    if total == 0:
        return 0
    return ((g_count + c_count) / total) * 100

def pipeline_analysis(dna_sequence, user_query):
    gc_val = calculate_gc_content(dna_sequence)
    system_prompt = (
        f"Analyze this sequence. Base Count: {len(dna_sequence)}bp | GC-Content: {gc_val:.2f}%.\n"
        f"Sequence Fragment: {dna_sequence}\n"
        f"Instruction: {user_query}"
    )
    try:
        response = requests.post('http://localhost:11434/api/generate', json={
            "model": "llama3",
            "prompt": system_prompt,
            "stream": False
        })
        return response.json().get('response', 'Inference empty.')
    except Exception:
        return "Connection Error: Is your offline engine running?"

if __name__ == "__main__":
    print("🧬 Sequence Analyzer Module Core Ready.")
