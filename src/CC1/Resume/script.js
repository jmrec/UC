function showOrHide(element) {
    const elementDisplay = element.style.display;

    if (elementDisplay === "none") {
        element.style.display = "block";
    } else {
        element.style.display = "none"
    }
}

function elementSwitch(element, currentBg, darkBg, lightBg) {
    const elementBgColor = element.style.backgroundColor;

    if (elementBgColor === currentBg) {
        element.style.backgroundColor = lightBg;
        element.style.color = "black";
    } else {
        element.style.backgroundColor = darkBg;
        element.style.color = "white";
    }
}

function switchBackgrounds() {
    toChangeAppearance.forEach(function(element) {
        const darkBg = "rgb(54, 69, 79)";
        const darkBgHex = "#36454F";
        const lightBgHex = "#d6d6d6";
        elementSwitch(element, darkBg, darkBgHex, lightBgHex)
    });

    elementSwitch(profile, currentBg="black", darkBg="black", lightBg="#c9c9c9")

    toChangeBgImage.forEach(function(element) {
        const currentBg = element.style.backgroundImage;
        const imgDarkBg = "url(./images/dark_bg.png)";
        const imgLightBg = "url(./images/light_bg.jpg)";
    
        if (currentBg.indexOf("./images/dark_bg.png") != -1) {
            element.style.backgroundImage = imgLightBg;
            element.style.color = "black";
        } else {
            element.style.backgroundImage = imgDarkBg;
            element.style.color = "white";
        }
    });
}

const imgSwitch = document.querySelector("#imgAppearanceSwitch");
const profile = document.querySelector("#divProfile");
const toChangeAppearance = document.querySelectorAll(".toFlip");
const toChangeBgImage = document.querySelectorAll(".toFlipBg");

imgSwitch.addEventListener("click", switchBackgrounds);

const hamburger = document.querySelector("#imgHamburger");
hamburger.addEventListener("click", () => {
    showOrHide(profile);
})