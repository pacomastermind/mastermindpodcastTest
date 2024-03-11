async function peticion() {
    const response = await fetch("http://localhost:8000");
    const jsonResponse = await response.json();
    console.log(jsonResponse);
}

peticion()