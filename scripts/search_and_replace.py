#!/usr/bin/env python3.12
import re
import typing

def search_and_replace(template, results: typing.Dict[str, typing.Union[str, float, int]]) -> None:
	with open(template, 'r') as template_file:
		content = template_file.read()
		for field, value in results.items():
			content = re.sub(f'\\[\\[{field}\\]\\]', value, content)
	with open("output.tex", 'w') as output:
		output.write(content)

test_results = {
	"groupName": "Paperwork",
	"groupType": "Groupe de l'AGEG",
	"contactName": "Fecteau, Marc-Olivier",
	"contactEmail": "fecm0701@usherbrooke.ca",
	"contactPhone": "418-225-4387",
	"applicantName": "Fecteau, Marc-Olivier",
	"supplier": "Non",
	"purchaseAmount": "42,69",
	"currency": "CAD",
	"purchaseAmountCAD": "",
	"paymentMethod": "Chèque",
	"physicalProof": "Non",
	"financingActivity": "Non",
	"forProfit": "Non",
	"activityName": "Paperwork",
	"purchaseDescription": "Développement de l'application",
	"purchaseDate": "2024-07-06",
}

if __name__ == "__main__":
	search_and_replace("template_reimbursement_E24.tex", test_results)
	print("Done.")