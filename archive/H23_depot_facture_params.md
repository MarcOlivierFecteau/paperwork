# H23_depot_facture

## Form parameters

- groupName
- comboboxGroupType
  - GT
  - Groupe AGEG
  - Promo
- applicantName
- **applicant_CIP (new, probably violates "loi 25")**
- contactName
- contactEmail
- contactPhoneNumber
- comboboxPaymentType
  - AccesD
  - Cheque
- listCurrency
  - CAD (required)
  - USD (CAD entry must be added)
  - other (specify; CAD entry must be added)
    - entryboxOtherCurrency
- checkPhysicalProof
- checkFinancingEvent
- checkProfitEvent
- project_or_event_name
- purchaseDescription
- purchaseDate
- requestFilledDate
- requestDepositDate (permanence)
- signatureGroupPresident
- signatureGroupTresorer
- signaturePermanence

## Form documents

- request form
- physical proof (if physical)
  - digitalized physical proof
- digital purchase proof (Image --> PDF converter needed)
  - transaction proof

## Other parameters

- request_processing_date (Diane)
- request_ID
- hash?
- \[applicantCIP\]\_\[requestFilledDate\]\_\[requestID | rand | hash\]

*N.B.* \[requestID\] pour faciliter l'archivage des demandes (et potentiellement ID doublons)
