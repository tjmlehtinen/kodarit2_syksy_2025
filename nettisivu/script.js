const blaaNappi = document.getElementById("blaa-nappi")
const blaaKappale = document.getElementById("blaa-kappale")

blaaNappi.addEventListener("click", function() {
    blaaKappale.textContent += " blaa"
})