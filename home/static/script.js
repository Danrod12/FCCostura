const phoneNumber = "50672079861"; // <-- cámbialo por tu número real

// Cada producto tiene su nombre y la categoría (título del grupo)
const products = {

  cosplay: {
    name: "Cosplay ",
    category: "Cosplays y Personajes Famosos",
  },
  uniforme: {
    name: "Uniforme Profesional",
    category: "Uniformes Profesionales",
  },
  disfraz: {
    name: "Disfraz Personalizado",
    category: "Disfraces Personalizados y Creativos",
  },
};

const quantities = {};

// 🔹 Actualiza los enlaces dinámicamente
function updateLinks(id) {
  const product = products[id];
  const quantity = quantities[id] || 0;

  // Si no se seleccionó nada, mensaje base
  if (quantity === 0) {
    document.getElementById(`${id}-whatsapp`).href = `https://wa.me/${phoneNumber}`;
    document.getElementById(`${id}-instagram`).href = `https://www.instagram.com/direct/t/`;
    return;
  }

  // Mensaje completo con título (categoría)
  const message = `Hola! Me interesa pedir ${quantity} del producto "${product.name}" en la categoría "${product.category}".`;
  const encoded = encodeURIComponent(message);

  // Actualiza los enlaces
  document.getElementById(`${id}-whatsapp`).href = `https://wa.me/${phoneNumber}?text=${encoded}`;
  document.getElementById(`${id}-instagram`).href = `https://www.instagram.com/direct/t/`;
}

// 🔹 Incrementar cantidad
function increment(id) {
  quantities[id] = (quantities[id] || 0) + 1;
  document.getElementById(`${id}-quantity`).textContent = quantities[id];
  updateLinks(id);
}

// 🔹 Disminuir cantidad
function decrement(id) {
  if ((quantities[id] || 0) > 0) {
    quantities[id]--;
    document.getElementById(`${id}-quantity`).textContent = quantities[id];
    updateLinks(id);
  }
}

// 🔹 Inicializar productos
for (const id in products) {
  quantities[id] = 0;
  updateLinks(id);
}
