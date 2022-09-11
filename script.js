caixa.innerHTML = "";
for (i = 1; i < 356; i++) {
  caixa.innerHTML += `<img src="imgs/${i}.jpg" />`;
}

ran.onmousemove = function () {
  n = Number(this.value);
  caixa.scrollTo(0, n * 480);
};

// caixa.scrollTo(0, 10000);
