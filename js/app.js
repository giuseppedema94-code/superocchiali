(function () {
  "use strict";

  // Test della faccia: un clic sulla forma del viso aggiorna il consiglio
  var tips = {
    tondo: "montature squadrate o rettangolari, che aggiungono angoli.",
    ovale: "ti sta bene quasi tutto. Prova aviator e wayfarer.",
    quadrato: "montature tonde o ovali, che ammorbidiscono la mascella.",
    cuore: "cat-eye leggeri o montature senza bordo sotto.",
    allungato: "montature alte o oversize, che accorciano il viso."
  };
  var faces = document.querySelectorAll(".face");
  var tipLabel = document.getElementById("tip-label");
  var tipText = document.getElementById("tip-text");
  faces.forEach(function (btn) {
    btn.addEventListener("click", function () {
      faces.forEach(function (b) { b.setAttribute("aria-pressed", "false"); });
      btn.setAttribute("aria-pressed", "true");
      if (tipLabel) tipLabel.textContent = btn.dataset.label;
      if (tipText) tipText.textContent = tips[btn.dataset.face] || "";
    });
  });

  // Lenti del Giorno: le offerte arrivano da /data/offerte.json (feed affiliati)
  var box = document.getElementById("offerte");
  if (!box) return;
  var reparto = box.dataset.reparto || "";
  var bgs = ["#FFD23F", "#E3D5FF", "#FFC2B0", "#BDEBD4"];

  fetch("/data/offerte.json", { cache: "no-cache" })
    .then(function (r) { return r.ok ? r.json() : []; })
    .then(function (list) {
      if (!Array.isArray(list)) return;
      if (reparto) list = list.filter(function (o) { return o.reparto === reparto; });
      list = list.slice(0, 8);
      if (!list.length) return;
      var grid = document.createElement("div");
      grid.className = "grid";
      list.forEach(function (o, i) {
        if (!/^https:\/\//.test(o.url || "")) return;
        var a = document.createElement("a");
        a.className = "card";
        a.href = o.url;
        a.rel = "sponsored noopener";
        a.target = "_blank";
        a.innerHTML = '<div class="art"><img alt="" width="150" height="54" loading="lazy"></div>' +
          '<div class="body"><p class="kind"></p><p class="name"></p>' +
          '<div class="row"><span class="price"></span><span class="chip"></span></div></div>';
        a.querySelector(".art").style.background = bgs[i % bgs.length];
        a.querySelector("img").src = /^https:\/\//.test(o.img || "") ? o.img : "/img/occhiali-" + (o.reparto === "vista" ? "vista" : "sole") + ".svg";
        a.querySelector(".kind").textContent = (o.reparto === "vista" ? "Vista" : "Sole") + (o.tipo ? " · " + o.tipo : "");
        a.querySelector(".name").textContent = [o.marca, o.modello].filter(Boolean).join(" ");
        a.querySelector(".price").textContent = "da " + Number(o.prezzo).toLocaleString("it-IT", { style: "currency", currency: "EUR" });
        a.querySelector(".chip").textContent = (o.negozi || 1) + (o.negozi > 1 ? " negozi" : " negozio");
        grid.appendChild(a);
      });
      if (grid.children.length) box.replaceChildren(grid);
    })
    .catch(function () {});
})();
