declare var axios: any;

import population from "./Population";
import educationLevel from "./EducationLevel";
import housing from "./Housing";
import others from "./Others";
import {resultActionBox, loaderActions, addPctSign, showError} from "./global";

// addPctSign(document.querySelector(".pct-field"));
// POPULATION
// @ts-ignore d s
let populationMethods: any = population();
let educationMethods: any = educationLevel();
let housingMethods: any = housing();
let otherMethods: any = others();
let chosenAlgorithm: any = document.querySelectorAll("[data-chosen-algorithm]");
let chosenAlgorithmOpt: any = document.querySelector("#chosen-algorithm");
let loader: any = loaderActions();
let resultBox: any = resultActionBox();

chosenAlgorithm.forEach(x => {
    x.addEventListener("click", function (e) {
        chosenAlgorithm.forEach(y => y.style = "opacity:0.2;");
        e.target.style = "opacity:1;";
        let chosa = e.target.dataset.dataset;
        chosenAlgorithmOpt.value = chosa;
    });
});

function getRequestPayload() {
    let algorithmEl: any = document.querySelector("#chosen-algorithm");
    if (algorithmEl.value.length == 0) {
        showError("Please select the model to evaluate", "Missing model");
        return false;
    }
    let populationValues = (populationMethods.getVals());
    let educationsValues = (educationMethods.getVals());
    let housingValues = (housingMethods.getVals());
    let singleFields = otherMethods;
    let incomeValues = singleFields.income.getVals();
    let unemploymentValues = singleFields.unemployment.getVals();
    let povertyValues = singleFields.poverty.getVals();
    let otherFields = singleFields.otherFields;
    return {
        algorithm: algorithmEl.value,
        cs: {
            ...populationValues,
            ...educationsValues,
            ...housingValues,
            ...incomeValues,
            ...unemploymentValues,
            ...povertyValues,
            ...otherFields
        }
    }
}

document.getElementById("request-prediction-button").addEventListener("click", function () {
    let requestPayload = getRequestPayload();
    if (!requestPayload) {
        return;
    }
    if (!loader.isLoading()) {
        loader.showLoader();
        axios.post('/predict', requestPayload).then(function (response) {
            console.log(response);
            loader.hideLoader();
            resultBox.show();
        }).catch(function (error) {
            showError(error, "error while predicting");
            loader.hideLoader();
        });
    }
});