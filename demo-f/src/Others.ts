import {processSliderGroup, getCSVKV} from "./global";


declare var document: any;

export default function () {

    // % total population


    // income

    // unemployment rate
    let slider2: any = document.querySelector("#unemployment-slider-member-pct");
    let eles2: any = slider2.querySelectorAll("[data-slider-member-pct]");
    let totalSum2: any = slider2.querySelector("[data-total-pct-value]");
    let pCTValueBox2: any = slider2.querySelectorAll("[data-current-pct-value-box]");
    let unemployment = processSliderGroup(pCTValueBox2, slider2, totalSum2, eles2);

    // % poverty
    let slider3: any = document.querySelector("#poverty-slider-member-pct");
    let eles3: any = slider3.querySelectorAll("[data-slider-member-pct]");
    let totalSum3: any = slider3.querySelector("[data-total-pct-value]");
    let pCTValueBox3: any = slider3.querySelectorAll("[data-current-pct-value-box]");
    let poverty = processSliderGroup(pCTValueBox3, slider3, totalSum3, eles3);

    // other fierlds
    let otherFields = getCSVKV(["#ftotalpopulation-value",  "#frenter-value","#fhousing-home-value", "#fhousing-price-mean-value", "#fincome-value"])
    return {
        unemployment,
        poverty,
        otherFields
    };
}