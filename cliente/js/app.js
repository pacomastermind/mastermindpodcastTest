const loginForm = document.getElementById("login")

loginForm.addEventListener("submit", (e) => {
  e.preventDefault()
  console.log("Aprieto")

  const formData = new FormData(loginForm)

  console.log(formData)

  fetch("http://localhost:8000/token", {
    method: "POST",
    body: formData,
  })
  .then((res) => res.json())
  .then((token) => {
    console.log("Token", token)
  })
  .catch((err) => {
    console.log("Error", err)
  })
})