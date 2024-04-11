import {
    processSliderGroup
} from "./global";


declare var document: any;


export default function () {
    let slider: any = document.querySelector("#crime-child-1-slider-member-pct");
    let eles: any = slider.querySelectorAll("[data-slider-member-pct]");
    let totalSum: any = slider.querySelector("[data-total-pct-value]");
    let pCTValueBox: any = slider.querySelectorAll("[data-current-pct-value-box]");
  return  processSliderGroup(pCTValueBox, slider, totalSum, eles);
}