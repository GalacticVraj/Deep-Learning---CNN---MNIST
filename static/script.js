const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

ctx.fillStyle = "black";
ctx.fillRect(0, 0, 280, 280);
ctx.strokeStyle = "white";
ctx.lineWidth = 15;

let drawing = false;
canvas.addEventListener("mousedown", () => drawing = true);
canvas.addEventListener("mouseup", () => drawing = false);
canvas.addEventListener("mousemove", draw);

function draw(e) {
  if (!drawing) return;
  ctx.lineTo(e.offsetX, e.offsetY);
  ctx.stroke();
}

function clearCanvas() {
  ctx.clearRect(0, 0, 280, 280);
  ctx.fillStyle = "black";
  ctx.fillRect(0, 0, 280, 280);
  document.getElementById("result").innerText = "Prediction: ";
}

// async function predict() {
//   const image = canvas.toDataURL("image/png");
//   const res = await fetch("/predict", {
//     method: "POST",
//     headers: { "Content-Type": "application/json" },
//     body: JSON.stringify({ image })
//   });
//   const data = await res.json();
//   document.getElementById("result").innerText = `Prediction: ${data.digit}`;
// }

async function predict() {
  const image = canvas.toDataURL("image/png");

  try {
    const res = await fetch("/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ image })
    });

    if (!res.ok) {
      throw new Error("Prediction failed: " + res.statusText);
    }

    const data = await res.json();
    console.log("Prediction received:", data);
    document.getElementById("result").innerText = `Prediction: ${data.digit}`;
  } catch (error) {
    console.error("Error predicting digit:", error);
    document.getElementById("result").innerText = "Prediction failed!";
  }
}
