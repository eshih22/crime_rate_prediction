declare var Swal: any;

export function processSliderGroup(pCTValueBox: any, slider: any, totalSum: any, eles: any, maxNumberOfPct: number = 100) {
    pCTValueBox.forEach(x => {
        x.addEventListener("change", function (e) {
            let theId: any = `#${e.target.id.replace("-value", "")}`;
            if (e.target.value <= maxNumberOfPct) {
                slider.querySelector(theId).value = e.target.value;
                applyValidation(slider, totalSum);
            } else {
                showError("value cannot be greater than 100, please modify your input", "Value not allowed");
            }
        });
    });
    eles.forEach(x => {
        x.addEventListener("input", function (e) {
            // @ts-ignore
            let theId: any = `#${e.target.id}-value`;
            slider.querySelector(theId).value = e.target.value;
            let validations: any = (sliderValidator(slider));
            if (totalSum) {
                totalSum.textContent = validations.total + "%";
            }
        });

        x.addEventListener("mouseup", function (e) {
            // @ts-ignore
            let theId: any = `#${e.target.id}-value`;
            applyValidation(slider, totalSum);
        });
    });

    return {
        "getVals": function () {
            let containerElement = {};
            eles.forEach(x => {
                containerElement[x.dataset.csv_column] = (x.value);
            });
            return containerElement;
        }
    };
}

export function getCSVKV(elements:string[]){
    let containerElement = {};
    console.log(containerElement)
    elements.forEach(x => {
        let resultEL: any = document.querySelector(x);
        console.log(resultEL.value)
        containerElement[resultEL.dataset.csv_column] = (resultEL.value);
    });
    console.log(containerElement)
    return containerElement;
}
export function applyValidation(sliderElem, sliderTotal) {
    let validations: any = (sliderValidator(sliderElem));
    if (!validations.isValid) {
        showError("The total pct of this attribute should not be greater than 100%", validations.total + "% not allowed");
    }
    if (sliderTotal) {
        sliderTotal.textContent = validations.total + "%";
    }
}

export function showError(text: string, title: string) {
    Swal.fire({
        title: title,
        text: text,
        icon: "error"
    });
}

export function sliderValidator(mainElement: any, totalSum: number = 100) {
    let acumSum = 0;
    let sliders: any = mainElement.querySelectorAll("[data-slider-member-pct]");
    sliders.forEach(slider => {
        // @ts-ignore
        acumSum += parseFloat(slider.value);
    });

    return {
        "total": acumSum,
        "isValid": acumSum <= totalSum
    };

}

export function resultActionBox() {
    let resultEL: any = document.querySelector("[data-result-section]");
    let titleBox: any = resultEL.querySelector("[data-title-section-box]");
    let resultSectionBox: any = resultEL.querySelector("[data-result-section-box]");

    return {
        "title": function (value: string) {
            titleBox.textContent = value;
        },
        "result": function (value: string) {
            let icone = `<h6><strong><i class="material-icons">bolt</i>&nbsp;${value}</strong></h6>`;
            resultSectionBox.innerHTML = icone;
        },
        "show": function () {
            titleBox.style = "display:block;";
            resultSectionBox.style = "display:block;";
        },
        "hide": function () {
            titleBox.style = "display:none;";
            resultSectionBox.style = "display:none;";
            resultSectionBox.textContent = "";

        }
    };
}

export function loaderActions() {
    let loaderEl: any = document.querySelector("[data-loader-container]");
    let loaderText: any = loaderEl.querySelector("[data-text-loader]");
    let isLoading: boolean = false;
    return {
        "isLoading": function () {
            return isLoading;
        },
        "text": function (value: string) {
            loaderText.textContent = value;
        },
        "showLoader": function () {
            loaderEl.style = "display:block;";
            isLoading = true;
        },
        "hideLoader": function () {
            loaderEl.style = "display:none;";
            isLoading = false;
        }
    };
}

export function requestPrediction() {

}

export function addPctSign(pctEL) {

    const wrapperElement = document.createElement('div');
    const pctText = document.createElement('span');
    wrapperElement.classList.add('pct-field-parent'); // Add a class to the wrapper if needed

    pctEL.parentNode.insertBefore(wrapperElement, pctEL);
    wrapperElement.appendChild(pctEL);
    pctText.textContent = "%";
    wrapperElement.appendChild(pctText);
}