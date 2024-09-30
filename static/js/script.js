document.getElementById('send-button').addEventListener('click', sendMessage);
document.getElementById('user-input').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (!userInput) return;

    appendMessage('user', userInput);
    document.getElementById('user-input').value = '';

    fetch('/get_response', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 'message': userInput })
    })
    .then(response => response.json())
    .then(data => {
        appendMessage('assistant', data.response);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function appendMessage(sender, message) {
    const chatLog = document.getElementById('chat-log');
    const messageWrapper = document.createElement('div');
    messageWrapper.classList.add('message', sender);

    const messageContent = document.createElement('div');
    messageContent.classList.add('message-content');
    messageContent.textContent = message;

    messageWrapper.appendChild(messageContent);
    chatLog.appendChild(messageWrapper);
    chatLog.scrollTop = chatLog.scrollHeight;
}
