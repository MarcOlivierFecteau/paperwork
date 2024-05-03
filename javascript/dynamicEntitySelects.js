const entityTypes = ["", "Groupe Technique", "Groupe de l'AGEG", "Promotion",
    "CSG", "Événement"];
const groupesTechniques = ["Baja UdeS", "BIUS", "Canoë de béton", "EMUS",
    "Génie au Féminin", "JDIS", "PAUS", "Robotique Udes", "SCGCH",
    "Sherby Racing", "SIRIUS", "VAMUdeS"];
const groupesAGEG = ["AGEG Band", "CQI/CCI", "JDG"];
const promotions = ["Promo 66", "Promo 67", "Promo 68", "Promo 69", "Promo 70"];
const csg = ["CSG"];
const events = ["Oktoberfest", "Intégrations"];

let currentEntityType = document.getElementById("entityType");
let entityName = document.getElementById("entityName");

entityTypes.forEach(function (item) {
    let option = document.createElement("option");
    option.value = item;
    option.text = item;
    currentEntityType.appendChild(option);
});

currentEntityType.onchange = function () {
    entityName.innerHTML = "<option></option>";
    switch (this.value) {
        case "Groupe Technique":
            addToEntityName(groupesTechniques);
            break;
        case "Groupe de l'AGEG":
            addToEntityName(groupesAGEG);
            break;
        case "Promotion":
            addToEntityName(promotions);
            break;
        case "CSG":
            addToEntityName(csg);
            break;
        case "Événement":
            addToEntityName(events);
            break;
        default:
            addToEntityName("");
    }
}

function addToEntityName(items) {
    items.forEach(function (item) {
        let option = document.createElement("option");
        option.value = item;
        option.text = item;
        entityName.appendChild(option);
    });
}
