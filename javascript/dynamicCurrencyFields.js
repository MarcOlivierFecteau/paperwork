const dynamicCurrencyFields = document.getElementById("dynamic-currency-fields");

function changeCurrencyFields(src) {
    dynamicCurrencyFields.textContent = '';
    if (src.value === 'Autre') {
        addOtherCurrencyField(dynamicCurrencyFields);
    }
    if (src.value !== 'CAD') {
        addPurchaseAmountCADField(dynamicCurrencyFields);
    }
}

function addOtherCurrencyField(parent) {
    const label = document.createElement('label');
    label.htmlFor = "otherCurrency";
    label.innerHTML = "Spécifiez: ";
    const otherCurrency = document.createElement('input');
    otherCurrency.type = 'text';
    otherCurrency.name = "otherCurrency";
    otherCurrency.pattern = "[A-Z]{3,}";
    otherCurrency.required = true;

    parent.appendChild(label);
    parent.appendChild(otherCurrency);
}

function addPurchaseAmountCADField(parent) {
    const label = document.createElement('label');
    label.htmlFor = "purchaseAmountCAD";
    label.innerHTML = "Montant à rembourser (CAD): ";
    const purchaseAmountCAD = document.createElement('input');
    purchaseAmountCAD.type = 'text';
    purchaseAmountCAD.name = "purchaseAmountCAD";
    // purchaseAmountCAD.pattern = "\d+(,|\.)\d{2}";
    purchaseAmountCAD.placeholder = "99,99";
    purchaseAmountCAD.required = true;

    parent.appendChild(document.createElement('br'));
    parent.appendChild(label);
    parent.appendChild(purchaseAmountCAD);
}
