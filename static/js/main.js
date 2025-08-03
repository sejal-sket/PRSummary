document.getElementById('pr-form').addEventListener('submit', async function (e) {
    e.preventDefault();
    const prUrl = document.getElementById('pr_url').value.trim();
    const output = document.getElementById('result');
    output.textContent = "⏳ Generating summary...";

    if (!prUrl) {
        output.textContent = "❌ Please enter a valid PR URL.";
        return;
    }

    try {
        const response = await fetch('/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ pr_url: prUrl })
        });

        const data = await response.json();
        if (response.ok) {
            output.textContent = data.summary;
        } else {
            output.textContent = "❌ Error: " + data.error;
        }
    } catch (err) {
        output.textContent = "❌ Unexpected error: " + err.message;
    }
});
