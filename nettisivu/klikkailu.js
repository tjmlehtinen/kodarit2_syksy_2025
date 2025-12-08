const klikkailualusta = document.getElementById("klikkailualusta")
const klikit = document.getElementById("klikit")

let klikkauksia = 0;

klikkailualusta.addEventListener("click", () => {
    klikkauksia += 1
    klikit.textContent = "klikattu " + klikkauksia + " kertaa"
})