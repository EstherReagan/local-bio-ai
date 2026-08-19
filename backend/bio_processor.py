from Bio import SeqIO
import json
import requests

def parse_genomic_file(file_path):
    try:
        for record in SeqIO.parse(file_path, "fasta"):
            print(f"🧬 Found Sequence ID: {record.id}")
            return str(record.seq)[:2000] 
    except Exception as e:
        return f"Error reading file: {str(e)}"

def send_to_local_ollama(prompt, context_data):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3",
        "prompt": f"Context: {context_data}\n\nQuestion: {prompt}",
        "stream": False
    }
    print("🤖 Processing sequence securely on local hardware...")
    response = requests.post(url, json=payload)
    return response.json()['response']

if __name__ == "__main__":
    print("--- Local Bio-Processor Module Initialized ---")
