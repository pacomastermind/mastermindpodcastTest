/*
fetch("http://localhost:8000/categorias", {
    method: "GET"
  })
  .then(
    (res) => {
        categorias=res.json()
        console.log(categorias)
    })
  .catch((err) => {
    console.log("Error", err)
  })
*/
const grupoCategorias = document.getElementById("lista-categorias")
const grupoPodcastsCategoria = document.getElementById("lista-categoria-podcasts")

fetch("http://localhost:8000/categorias", {method: "GET"})
  .then((response) => response.json())
  .then((categorias) => {
    console.log(categorias)
        for (const cat of categorias) {
            const listItem = document.createElement("li");
            listItem.className="list-group-item d-flex justify-content-between align-items-start bg-mastermind-50 border-danger";
            listItem.innerHTML = `<div class="ms-2 me-auto"> <div class="fw-bold">${cat.nombre}</div> Content for list item</div><span class="badge bg-danger text-bg-primary rounded-pill">${cat.id}</span>`
            grupoCategorias.appendChild(listItem);
        }
    })
    .catch((err) => {
        console.log("Error", err)
    })

fetch("http://localhost:8000/categorias/5/podcasts", {method: "GET"})
  .then((response) => response.json())
  .then((podcasts) => {
    console.log(podcasts)
        for (const pod of podcasts) {
            const listItem = document.createElement("li");
            listItem.className="list-group-item d-flex justify-content-between align-items-start bg-mastermind-50 border-danger";
            listItem.innerHTML = `<div class="ms-2 me-auto"> <div class="fw-bold">${pod.titulo}</div>${pod.descripcion}</div><span class="badge bg-danger text-bg-primary rounded-pill">${pod.id}</span>`
            grupoPodcastsCategoria.appendChild(listItem);
        }
    })
    .catch((err) => {
        console.log("Error", err)
    })