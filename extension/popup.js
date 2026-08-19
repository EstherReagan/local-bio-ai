document.getElementById('analyzeBtn').addEventListener('click', async () => {
    const prompt = document.getElementById('userPrompt').value.trim();
    const outputBox = document.getElementById('outputBox');
    const resultText = document.getElementById('resultText');

    if (!prompt) {
        alert("Please enter a question or analysis prompt first.");
        return;
    }

    resultText.innerText = "Processing secure local analysis...";
    outputBox.classList.remove('hidden');

    try {
        const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
        const contextTitle = tab ? tab.title : "Unknown Research Document";
        
        const response = await fetch('http://localhost:11434/api/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                model: 'llama3',
                prompt: `Context Material: ${contextTitle}\nResearcher Instruction: ${prompt}`,
                stream: false
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP Error Status: ${response.status}`);
        }

        const data = await response.json();
        resultText.innerText = data.response;
    } catch (error) {
        resultText.innerText = "Connection Failed: Ensure that your Ollama application is active and running on your desktop.";
        console.error("Local core connection failure:", error);
    }
});
