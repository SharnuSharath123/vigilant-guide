// frontend/script.js

document.getElementById('fetchData').addEventListener('click', async () => {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/data');
        const data = await response.json();
        document.getElementById('response').textContent = data.message;
    } catch (error) {
        console.error('Error fetching data:', error);
    }
});
