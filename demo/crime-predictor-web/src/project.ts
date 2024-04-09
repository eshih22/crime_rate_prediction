let populationSliders = document.querySelector("#population-slider-member-pct");
let populationsliderEles: any = populationSliders.querySelectorAll("[slider-member-pct]");

populationsliderEles.forEach(x => {
    x.addEventListener("change", function () {
        console.log(sliderValidator(populationSliders))

    });
});

function sliderValidator(mainElement: any, totalSum: number = 100) {
    let acumSum = 0;
    let sliders = mainElement.querySelectorAll("[slider-member-pct]")
    sliders.forEach(slider => {
        acumSum += parseInt(slider.value);
    });

    return {
        "total": acumSum,
        "isValid": acumSum <= totalSum
    }
}

function callPrediction() {
    
}