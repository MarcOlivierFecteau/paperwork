const dynamicPaymentFields = document.getElementById("payment-info-fields");

function changePaymentFields(src) {
    dynamicPaymentFields.textContent = '';
    if (src.value === "supplier") {
        const label = document.createElement('label');
        label.htmlFor = "supplierName";
        label.innerHTML = "Nom du fournisseur: ";
        const supplierName = document.createElement('input');
        supplierName.type = 'text';
        supplierName.name = "supplierName";
        // supplierName.pattern = "\w+"; // TODO: add /m flag to patterns created with JS
        supplierName.required = true;

        dynamicPaymentFields.appendChild(label);
        dynamicPaymentFields.appendChild(supplierName);
    } else if (src.value === "student") {
        const labelCIP = document.createElement('label');
        labelCIP.htmlFor = "applicantCIP";
        labelCIP.innerHTML = "CIP: ";
        const applicantCIP = document.createElement('input');
        applicantCIP.type = 'text';
        applicantCIP.name = "applicantCIP";
        applicantCIP.minLength = '8';
        applicantCIP.maxLength = '8';
        // applicantCIP.pattern = '[a-z]{4}\d{4}'; // TODO: add /m flag to patterns created with JS
        applicantCIP.placeholder = "ageg4269";
        applicantCIP.required = true;
        const labelName = document.createElement('label');
        labelName.htmlFor = "applicantName";
        labelName.innerHTML = "Nom, Prénom: ";
        const applicantName = document.createElement('input');
        applicantName.type = 'text';
        applicantName.name = "applicantName";
        // applicantName.pattern = '([A-Z])\w+((-| )([A-Z])\w+)*, ([A-Z])\w+((-| )([A-Z])\w+)*'; // TODO: add /m flag to patterns created with JS
        applicantName.required = true;

        dynamicPaymentFields.appendChild(labelCIP);
        dynamicPaymentFields.appendChild(applicantCIP);
        dynamicPaymentFields.appendChild(document.createElement('br'));
        dynamicPaymentFields.appendChild(labelName);
        dynamicPaymentFields.appendChild(applicantName);
    }
}
