async function sendPrompt() {

    const prompt = document.getElementById("prompt").value;

    const response = await fetch("/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            prompt
        })
    });

    const data = await response.json();

    document.getElementById("output").textContent =
        data.response;
}