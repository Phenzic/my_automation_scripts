:::::::::::::::::::::::: {#mainBodyContent role="main" tabindex="-1"}
::::::::::::::::::::::: gd
:::::::::::::::::::::: {.gd__c style="--cols:12"}
::::::::::::::::::::: {.gd__i .section .ptop--96 .c12 style=" --cspan:12; --rspan:1; --cstart:1;"}
:::::::::::::::::::: {.section .gd__s}
::::::::::::::::::: {.gd__a style="--cols: 12;--cspan: 12; --rspan: 1;"}
:::::::::::::::::: {.gd__c style="--cols:12"}
::: {.gd__i .section .c3 .t-hide style=" --cspan:3; --rspan:1; --cstart:auto;"}
- [Loqate Basics](#){aria-expanded="false" toggle="dropdown"
  role="button"}

  ::: dd
  - [Start Here](/developers/getting-started/)
  - [Ways To Integrate](/developers/getting-started/ways-to-integrate/)
  - [Creating API Keys](/developers/getting-started/creating-api-keys/)
  - [List Of Endpoints](/developers/getting-started/list-of-endpoints/)
  - [API Security](/developers/getting-started/api-security/)
  - [Monitoring Account
    Usage](/developers/getting-started/monitoring-account-usage/)
  :::
- [Product support](#){aria-expanded="false" toggle="dropdown"
  role="button"}

  ::: dd
  - [Address Capture](/developers/address-capture/)
  - [Address Verify](/developers/address-verify/)
  - [Store Finder](/developers/store-finder/)
  - [Email Validation](/developers/email-validation/)
  - [Phone Validation](/developers/phone-verification/)
  - [Bank Validation](/developers/bank-verification/)
  - [Geocode](/developers/geocode/)
  - [Matchcode (legacy)](/developers/matchcode/)
  :::
- [Guides](#){aria-expanded="false" toggle="dropdown" role="button"}

  ::: {.dd .nav__side-menu}
  - [Address, Email and Phone Validation](#){aria-expanded="false"
    toggle="dropdown" role="button"}

    ::: dd
    - [Quick setup guide -- Address, Email and Phone
      Validation](/developers/guides/quick/)
    - [Advanced Setup Guide](/developers/guides/advanced-setup-guide/)
    - [Address Capture Integration Best
      Practice](/developers/guides/address-capture-integration-best-practice/)
    - [Enabling new Capture
      features](/developers/guides/enabling-new-capture-features/)
    - [SaaS Platform: Setting up a new
      service](/developers/guides/saas-platform-setting-up/)
    - [SaaS Platform: Integration
      options](/developers/guides/saas-platform-integration-options/)
    - [SaaS Platform: SDK](/developers/guides/saas-platform-sdk/)
    - [The Loqate Saas
      Platform](/developers/guides/the-loqate-saas-platform/)
    :::
  - [Data Maintenance](#){aria-expanded="false" toggle="dropdown"
    role="button"}

    ::: dd
    - [Data Maintenance - Post
      Processing](/developers/guides/data-maintenance-post-processing/)
    :::
  - [Data Sets](#){aria-expanded="false" toggle="dropdown"
    role="button"}

    ::: dd
    - [Consuming Premium Data
      Sets](/developers/guides/consuming-premium-data-sets/)
    - [Property Intelligence User
      Guide](/developers/guides/property-intelligence-user-guide/)
    - [Property Intelligence Data
      Directory](/developers/guides/property-intelligence-data-directory/)
    :::
  - [Integrations by platform](#){aria-expanded="false"
    toggle="dropdown" role="button"}

    ::: dd
    - [Adobe Commerce
      (Magento)](/developers/guides/adobe-commerce-magento-integration-guide/)
    - [BigCommerce](/developers/guides/bigcommerce/)
    - [commercetools](/developers/guides/commercetools-integration/)
    - [Microsoft Dynamics
      365](/developers/guides/loqate-for-microsoft-dynamics-365/)
    - [Shopify
      Plus](/developers/guides/the-loqate-shopify-integration-guide/)
    - [Shopware
      6](/developers/guides/loqate-plugin-for-shopware-6-configuration-guide/)
    :::
  - [Store Finder](#){aria-expanded="false" toggle="dropdown"
    role="button"}

    ::: dd
    - [How Does a Store Finder
      Work?](/developers/guides/how-does-a-store-finder-work/)
    - [Creating and Managing Location
      Lists](/developers/guides/creating-and-managing-location-lists/)
    - [How To Implement a Store
      Finder](/developers/guides/how-to-implement-a-store-finder/)
    - [Setting Up Store Finder
      Keys](/developers/guides/setting-up-store-finder-keys/)
    :::
  - [Utilities Register](#){aria-expanded="false" toggle="dropdown"
    role="button"}

    ::: dd
    - [Loqate Utilities Register
      2.0](/developers/guides/loqate-utilities-register/)
    :::
  :::
- [APIs](/developers/api/){aria-expanded="false" toggle="dropdown"
  role="button"}

  ::: dd
  - [Address Capture](/developers/api/capture/)
  - [Address Verify](/developers/api/cleanseplus/)
  - [Store Finder](/developers/apis/location-services/)
  - [Email Validation](/developers/api/emailvalidation/)
  - [Phone Validation](/developers/api/phonenumbervalidation/)
  - [Bank Validation](/developers/api/bankaccountvalidation/)
  - [Geocode](/developers/api/distancesanddirections/)
  - [Generic Errors](/developers/api/generic-errors/)
  :::
- [Sandbox](/developers/sandbox/)
- [FAQs](#){aria-expanded="false" toggle="dropdown" role="button"}

  ::: dd
  - [Address Capture](/developers/faqs/Address-Capture)
  - [Address Verification](/developers/faqs/Address-Verification)
  - [Bank Account
    Verification](/developers/faqs/Bank-Account-Verification)
  - [Common account errors](/developers/faqs/Common-account-errors)
  - [Data Maintenance Annual
    Subscription](/developers/faqs/Data-Maintenance-Annual-Subscription)
  - [Email Verification](/developers/faqs/Email-Verification)
  - [General](/developers/faqs/General)
  - [Geocoding](/developers/faqs/Geocoding)
  - [Geolocation](/developers/faqs/Geolocation)
  - [Phone Verification](/developers/faqs/Phone-Verification)
  - [Technical](/developers/faqs/Technical)
  :::
:::

:::::::::::::::: {.gd__i .section .c9 style=" --cspan:9; --rspan:1; --cstart:auto;"}
::::::::::::::: gd
:::::::::::::: {.gd__c style="--cols:12"}
::::::::::::: {.gd__i .section .gd--cen .content .c12 style="--cspan:12;--rspan:1;--cstart:1;"}
:::::::::::: {.section .gd__s}
::::::::::: {.gd__a style="--cols: 12;--cspan: 12; --rspan: 1;"}
:::::::::: {.gd__c style="--cols:12"}
::: {.gd__i .rte .c12 style="--cspan:12;--rspan:1;--cstart:auto;"}
## MultiDatabase Related Data Codes

#####   

##### AddressBase Premium Fields

+-----------------------+-----------------------+-----------------------+
| Related Data Field in | Description           | Return Field          |
| Request               |                       | response.address      |
+=======================+=======================+=======================+
| UDPRN                 | Royal Mail Unique     | address.              |
|                       | Delivery Point        | additionalItems.UDPRN |
|                       | Reference Number      | and\                  |
|                       |                       | address.rmUDPRN       |
+-----------------------+-----------------------+-----------------------+
| UPRN                  | UPRN (Unique Property | address               |
|                       | Reference Number)     | .additionalItems.UPRN |
|                       |                       | and\                  |
|                       |                       | address.uprn          |
+-----------------------+-----------------------+-----------------------+
| LPI_KEY               | LPI Key               | address.ad            |
|                       |                       | ditionalItems.LPI_KEY |
|                       |                       | and\                  |
|                       |                       | address.lpi.LPIKey    |
+-----------------------+-----------------------+-----------------------+
| LPI_STATUS            | LPI Logical Status    | address               |
|                       |                       | .lpi.LPILogicalStatus |
+-----------------------+-----------------------+-----------------------+
| USRN                  | USRN (Unique Street   | address.lpi.USRN      |
|                       | Reference Number)     |                       |
+-----------------------+-----------------------+-----------------------+
| USRN_MATCH_INDI       | USRN Match Indicator  | address.l             |
|                       |                       | pi.USRNMatchIndicator |
+-----------------------+-----------------------+-----------------------+
| LEVEL                 | Memorandum of         | address.lpi.level     |
|                       | Vertical Position     |                       |
+-----------------------+-----------------------+-----------------------+
| OFFICIAL_FLAG         | Status of the Address | add                   |
|                       |                       | ress.lpi.OfficialFlag |
+-----------------------+-----------------------+-----------------------+
| BLPU_STATUS           | BLPU Logical Status   | address.b             |
|                       |                       | lpu.BLPULogicalStatus |
+-----------------------+-----------------------+-----------------------+
| BLPU_STATE            | BLPU State            | a                     |
|                       |                       | ddress.blpu.BLPUState |
+-----------------------+-----------------------+-----------------------+
| PARENT_UPRN           | Parent UPRN           | address.addit         |
|                       |                       | ionalItems.ParentUPRN |
|                       |                       | and                   |
|                       |                       |                       |
|                       |                       | ad                    |
|                       |                       | dress.blpu.ParentUPRN |
+-----------------------+-----------------------+-----------------------+
| X_COORDINATE          | Easting               | address.blpu.Easting  |
+-----------------------+-----------------------+-----------------------+
| Y_COORDINATE          | Northing              | address.blpu.Northing |
+-----------------------+-----------------------+-----------------------+
| RPC                   | Representative Point  | address.blpu.RPC      |
|                       | Code                  |                       |
+-----------------------+-----------------------+-----------------------+
| BLPU_CUSTODIAN        | LLPG Custodian        | address.bl            |
|                       |                       | pu.LocalCustodianCode |
+-----------------------+-----------------------+-----------------------+
| BLPU_END_DATE         | BLPU End Date         | add                   |
|                       |                       | ress.blpu.BLPUEndDate |
+-----------------------+-----------------------+-----------------------+
| POSTAL_ADDRESS        | Postal Address        | address.b             |
|                       |                       | lpu.PostalAddressable |
+-----------------------+-----------------------+-----------------------+
| MULTI_OCC_COUNT       | Multi-Occupancy Count | addre                 |
|                       |                       | ss.blpu.MultiOccCount |
+-----------------------+-----------------------+-----------------------+
| BLPU_STATE_DATE       | BLPU State Date       | addre                 |
|                       |                       | ss.blpu.BLPUStateDate |
+-----------------------+-----------------------+-----------------------+
| BLPU_START_DATE       | BLPU Start Date       | addre                 |
|                       |                       | ss.blpu.BLPUStartDate |
+-----------------------+-----------------------+-----------------------+
| BLPU_UPDATE_DATE      | BLPU Update Date      | address.bl            |
|                       |                       | pu.BLPULastUpdateDate |
+-----------------------+-----------------------+-----------------------+
| BLPU_ENTRY_DATE       | BLPU Entry Date       | addre                 |
|                       |                       | ss.blpu.BLPUEntryDate |
+-----------------------+-----------------------+-----------------------+
| CLASS_CODE            | Class Code            | address.classificati  |
|                       |                       | on,ClassificationCode |
+-----------------------+-----------------------+-----------------------+
| CLASS_PRIMARY         | Class Primary         | a                     |
|                       |                       | ddress.classification |
|                       |                       | ClassPrimaryText      |
+-----------------------+-----------------------+-----------------------+
| CLASS_SECONDARY       | Class Secondary       | a                     |
|                       |                       | ddress.classification |
|                       |                       | ClassPrimaryText      |
+-----------------------+-----------------------+-----------------------+
| CLASS_TERTIARY        | Class Tertiary        | a                     |
|                       |                       | ddress.classification |
|                       |                       | ClassTertiaryText     |
+-----------------------+-----------------------+-----------------------+
| CLASS_QUATERNARY      | Class Quaternary      | address.classificatio |
|                       |                       | n.ClassQuaternaryText |
+-----------------------+-----------------------+-----------------------+
| CLASS_END_DATE        | Class End Date        | address.classi        |
|                       |                       | fication.ClassEndDate |
+-----------------------+-----------------------+-----------------------+
| CLASS_START_DATE      | Class Start Date      | address.classifi      |
|                       |                       | cation.ClassStartDate |
+-----------------------+-----------------------+-----------------------+
| CLASS_UDPATE_DATE     | Class Update Date     | address.classificatio |
|                       |                       | n.ClassLastUpdateDate |
+-----------------------+-----------------------+-----------------------+
| CLASS_ENTRY_DATE      | Class Entry Date      | address.cla           |
|                       |                       | ssification.EntryDate |
+-----------------------+-----------------------+-----------------------+
| CLASS_SCHEME          | Scheme                | address.class         |
|                       |                       | ification.ClassScheme |
+-----------------------+-----------------------+-----------------------+
| ORG_KEY               | Unique Key for        | address.ad            |
|                       | Organisation Record   | ditionalItems.ORG_KEY |
|                       |                       | and                   |
|                       |                       |                       |
|                       |                       | address.companyInform |
|                       |                       | ation.organisationKey |
+-----------------------+-----------------------+-----------------------+
| ORG_ORGANISATION      | ABP Organisation Name | a                     |
|                       |                       | ddress.companyInforma |
|                       |                       | tion.organisationName |
+-----------------------+-----------------------+-----------------------+
| ORG_LEGAL_NAME        | Organisation          | address.com           |
|                       | Registered Legal Name | panyInformation.legal |
|                       |                       | OrganisationLegalName |
+-----------------------+-----------------------+-----------------------+
| ORG_START_DATE        | Organisation Start    | addres                |
|                       | Date                  | s.companyInformation. |
|                       |                       | organisationStartDate |
+-----------------------+-----------------------+-----------------------+
| ORG_END_DATE          | Organisation End Date | addre                 |
|                       |                       | ss.companyInformation |
|                       |                       | .organisationEndDate  |
+-----------------------+-----------------------+-----------------------+
| ORG_UPDATE_DATE       | Organisation Update   | address.com           |
|                       | Date                  | panyInformation.organ |
|                       |                       | isationLastUpdateDate |
+-----------------------+-----------------------+-----------------------+
| ORG_ENTRY_DATE        | Organisation Entry    | addres                |
|                       | Date                  | s.companyInformation. |
|                       |                       | organisationEntryDate |
+-----------------------+-----------------------+-----------------------+
| XREFMA                | XREFMA Address Layer  | address.osAl2Toid     |
|                       | 2 TOID                |                       |
+-----------------------+-----------------------+-----------------------+
| XREFMI                | XREFMI Transport      | address.osItnToid     |
|                       | Network TOID          |                       |
+-----------------------+-----------------------+-----------------------+
| XREFMT                | XREFMT Topography     | address.osTopoToid    |
|                       | Layer TOID            |                       |
+-----------------------+-----------------------+-----------------------+
| XREFVC                | XREFVC Council Tax    | address.voaCtRecord   |
+-----------------------+-----------------------+-----------------------+
| XREFVN                | XREFVN Non-Domestic   | address.voaNdrRecord  |
|                       | Rates                 |                       |
+-----------------------+-----------------------+-----------------------+
| CLASS_KEY             | Class Key             | address.cl            |
|                       |                       | assification.ClassKey |
+-----------------------+-----------------------+-----------------------+
| SAO_START_NUMBER      | SAO Start Number      | addre                 |
|                       |                       | ss.lpi.SAOStartNumber |
+-----------------------+-----------------------+-----------------------+
| SAO_START_SUFFIX      | SAO Start Suffix      | addre                 |
|                       |                       | ss.lpi.SAOStartSuffix |
+-----------------------+-----------------------+-----------------------+
| SAO_END_NUMBER        | SAO End Number        | add                   |
|                       |                       | ress.lpi.SAOEndNumber |
+-----------------------+-----------------------+-----------------------+
| SAO_END_SUFFIX        | SAO End Suffix        | add                   |
|                       |                       | ress.lpi.SAOEndSuffix |
+-----------------------+-----------------------+-----------------------+
| PAO_START_NUMBER      | PAO Start Number      | addre                 |
|                       |                       | ss.lpi.PAOStartNumber |
+-----------------------+-----------------------+-----------------------+
| PAO_START_SUFFIX      | PAO Start Suffix      | addre                 |
|                       |                       | ss.lpi.PAOStartSuffix |
+-----------------------+-----------------------+-----------------------+
| PAO_END_NUMBER        | PAO End Number        | add                   |
|                       |                       | ress.lpi.PAOEndNumber |
+-----------------------+-----------------------+-----------------------+
| PAO_END_SUFFIX        | PAO End Suffix        | add                   |
|                       |                       | ress.lpi.PAOEndSuffix |
+-----------------------+-----------------------+-----------------------+
| LANGUAGE              | Language              | ad                    |
|                       |                       | dress.lpi.LPILanguage |
+-----------------------+-----------------------+-----------------------+
| LPI_START_DATE        | LPI Start Date        | add                   |
|                       |                       | ress.lpi.LPIStartDate |
+-----------------------+-----------------------+-----------------------+
| LPI_END_DATE          | LPI End Date          | a                     |
|                       |                       | ddress.lpi.LPIEndDate |
+-----------------------+-----------------------+-----------------------+
| LPI_UPDATE_DATE       | LPI Update Date       | address.              |
|                       |                       | lpi.LPILastUpdateDate |
+-----------------------+-----------------------+-----------------------+
| LPI_ENTRY_DATE        | LPI Entry Date        | add                   |
|                       |                       | ress.lpi.LPIEntryDate |
+-----------------------+-----------------------+-----------------------+
| AREA_NAME             | Area Name             | address.lpi.AreaName  |
+-----------------------+-----------------------+-----------------------+
| SAO_TEXT              | SAO Text              | address.lpi.SAOText   |
+-----------------------+-----------------------+-----------------------+
| PAO_TEXT              | PAO Text              | address.lpi.PAOText   |
+-----------------------+-----------------------+-----------------------+
| ST_TYPE               | Street Type           | address.streetI       |
|                       |                       | nformation.StreetType |
+-----------------------+-----------------------+-----------------------+
| ST_STATE              | Street State          | address.streetIn      |
|                       |                       | formation.StreetState |
+-----------------------+-----------------------+-----------------------+
| ST_SURFACE            | Street Surface Finish | address.streetInfo    |
|                       |                       | rmation.StreetSurface |
+-----------------------+-----------------------+-----------------------+
| ST_CLASS              | Street Class          | addr                  |
|                       |                       | ess.streetInformation |
|                       |                       | .StreetClassification |
+-----------------------+-----------------------+-----------------------+
| ST_VERSION            | Street Version        | address.streetInfo    |
|                       |                       | rmation.StreetVersion |
+-----------------------+-----------------------+-----------------------+
| ST_END_DATE           | Street End Date       | address.streetInfo    |
|                       |                       | rmation.StreetEndDate |
+-----------------------+-----------------------+-----------------------+
| ST_START_X            | Street Start X        | ad                    |
|                       | (Easting)             | dress.streetInformati |
|                       |                       | on.StreetStartEasting |
+-----------------------+-----------------------+-----------------------+
| ST_START_Y            | Street Start Y        | add                   |
|                       | (Northing)            | ress.streetInformatio |
|                       |                       | n.StreetStartNorthing |
+-----------------------+-----------------------+-----------------------+
| ST_END_X              | Street End X          | address.streetInforma |
|                       | (Easting)             | tion.StreetEndEasting |
+-----------------------+-----------------------+-----------------------+
| ST_END_Y              | Street End Y          | a                     |
|                       | (Northing)            | ddress.streetInformat |
|                       |                       | ion.StreetEndNorthing |
+-----------------------+-----------------------+-----------------------+
| ST_TOLERANCE          | Street Tolerance      | address.streetInform  |
|                       |                       | ation.StreetTolerance |
+-----------------------+-----------------------+-----------------------+
| ST_STATE_DATE         | Street State Date     | address.street        |
|                       |                       | Information.StateDate |
+-----------------------+-----------------------+-----------------------+
| ST_START_DATE         | Street Start Date     | address.streetInform  |
|                       |                       | ation.StreetStartDate |
+-----------------------+-----------------------+-----------------------+
| ST_UPDATE_DATE        | Street Update Date    | addr                  |
|                       |                       | ess.streetInformation |
|                       |                       | .StreetLastUpdateDate |
+-----------------------+-----------------------+-----------------------+
| ST_ENTRY_DATE         | Street Entry Date     | address.streetInform  |
|                       |                       | ation.StreetEntryDate |
+-----------------------+-----------------------+-----------------------+
| ST_DESCRIPTION        | Street Name           | address.streetDescrip |
|                       |                       | tor.StreetDescription |
+-----------------------+-----------------------+-----------------------+
| ST_LOCALITY           | Street Locality Name  | address.stre          |
|                       |                       | etDescriptor.Locality |
+-----------------------+-----------------------+-----------------------+
| ST_TOWN               | Street Town Name      | address.stre          |
|                       |                       | etDescriptor.TownName |
+-----------------------+-----------------------+-----------------------+
| ST_ADMIN_AREA         | Highway Authority     | a                     |
|                       | Name                  | ddress.streetDescript |
|                       |                       | or.AdministrativeArea |
+-----------------------+-----------------------+-----------------------+
| ST_LANGUAGE           | Street Descriptor     | address.streetDesc    |
|                       | Language              | riptor.StreetLanguage |
+-----------------------+-----------------------+-----------------------+
:::

::: {.gd__i .rte .c12 style="--cspan:12;--rspan:1;--cstart:auto;"}
##### Multiple Residence Fields

  Related Data Field in Request   Description               Return Field response.address
  ------------------------------- ------------------------- -------------------------------------
  UMRRN                           UMRRN                     address.additionalItems.UMRRN
  Owning UDPRN                    OwningUDPRN               address.additionalItems.OwningUDPRN
  OwningAK                        Owning Address Key        address.additionalItems.OwningAK
  OwningOK                        Owning Organisation Key   address.additionalItems.OwningOK
:::

::: {.gd__i .rte .c12 style="--cspan:12;--rspan:1;--cstart:auto;"}
##### Business Fields

+-----------------------+-----------------------+-----------------------+
| Related Data Field in | Description           | Return Field          |
| Request               |                       | response.address      |
+=======================+=======================+=======================+
| TEL                   | Telephone Number      | address.gro           |
|                       |                       | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"TEL\"               |
+-----------------------+-----------------------+-----------------------+
| FAX                   | Fax Number            | address.gro           |
|                       |                       | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"FAX\"               |
+-----------------------+-----------------------+-----------------------+
| SIC03                 | UK 2003 SIC Code      | address.gro           |
|                       |                       | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"SIC03\"             |
+-----------------------+-----------------------+-----------------------+
| NUMEMPCO              | Employees at Company  | address.gro           |
|                       |                       | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"NUMEMPCO\"          |
+-----------------------+-----------------------+-----------------------+
| NUMEMP                | Employees at Site     | address.gro           |
|                       |                       | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"NUMEMP\"            |
+-----------------------+-----------------------+-----------------------+
| HOF                   | Head Office Flag      | address.gro           |
|                       |                       | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"HOF\"               |
+-----------------------+-----------------------+-----------------------+
| TO                    | Turnover              | address.gro           |
|                       |                       | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"TO\"                |
+-----------------------+-----------------------+-----------------------+
| YEARSTAR              | Year Started          | address.gro           |
|                       |                       | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"YEARSTAR\"          |
+-----------------------+-----------------------+-----------------------+
| SIC03TEXT             | 2003 SIC Description  | address.gro           |
|                       |                       | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"SIC03TEXT\"         |
+-----------------------+-----------------------+-----------------------+
| ExecutiveCount        | Count of named        | address.gro           |
|                       | executives            | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"ExecutiveCount\"    |
+-----------------------+-----------------------+-----------------------+
| Ex1_Function          | Executive 1 function  | address.gro           |
|                       |                       | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex1_Function\"      |
+-----------------------+-----------------------+-----------------------+
| Ex1_FirstName         | Executive 1 first     | address.gro           |
|                       | name                  | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex1_FirstName\"     |
+-----------------------+-----------------------+-----------------------+
| Ex1_Surname           | Executive 1 surname   | address.gro           |
|                       |                       | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex1_Surname\"       |
+-----------------------+-----------------------+-----------------------+
| Ex1_Salutation        | Executive 1           | address.gro           |
|                       | salutation            | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex1_Salutation\"    |
+-----------------------+-----------------------+-----------------------+
| Ex1_Sex               | Executive 1 gender    | address.gro           |
|                       |                       | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex1_Sex\"           |
+-----------------------+-----------------------+-----------------------+
| Ex2_Function          | Executive 2 function  | address.gro           |
|                       |                       | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex2_Function\"      |
+-----------------------+-----------------------+-----------------------+
| Ex2_FirstName         | Executive 2 first     | address.gro           |
|                       | name                  | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex2_FirstName\"     |
+-----------------------+-----------------------+-----------------------+
| Ex2_Surname           | Executive 2 surname   | address.gro           |
|                       |                       | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex2_Surname\"       |
+-----------------------+-----------------------+-----------------------+
| Ex2_Salutation        | Executive 2           | address.gro           |
|                       | salutation            | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex2_Salutation\"    |
+-----------------------+-----------------------+-----------------------+
| Ex2_Sex               | Executive 2 gender    | address.gro           |
|                       |                       | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex2_Sex\"           |
+-----------------------+-----------------------+-----------------------+
| Ex3_Function          | Executive 3 function  | address.gro           |
|                       |                       | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex3_Function\"      |
+-----------------------+-----------------------+-----------------------+
| Ex3_Function          | Executive 3 function  | address.gro           |
|                       |                       | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex1_Surname\"       |
+-----------------------+-----------------------+-----------------------+
| Ex3_FirstName         | Executive 3 first     | address.gro           |
|                       | name                  | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex3_FirstName\"     |
+-----------------------+-----------------------+-----------------------+
| Ex3_Surname           | Executive 3 surname   | address.gro           |
|                       |                       | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex3_Surname\"       |
+-----------------------+-----------------------+-----------------------+
| Ex3_Salutation        | Executive 3           | address.gro           |
|                       | salutation            | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex3_Salutation\"    |
+-----------------------+-----------------------+-----------------------+
| Ex3_Sex               | Executive 3 gender    | address.gro           |
|                       |                       | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex3_Sex\"           |
+-----------------------+-----------------------+-----------------------+
| Ex4_Function          | Executive 4 function  | address.gro           |
|                       |                       | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex4_Function\"      |
+-----------------------+-----------------------+-----------------------+
| Ex4_FirstName         | Executive 4 first     | address.gro           |
|                       | name                  | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex4_FirstName\"     |
+-----------------------+-----------------------+-----------------------+
| Ex4_Surname           | Executive 4 surname   | address.gro           |
|                       |                       | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex4_Surname\"       |
+-----------------------+-----------------------+-----------------------+
| Ex4_Salutation        | Executive 4           | address.gro           |
|                       | salutation            | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex4_Salutation\"    |
+-----------------------+-----------------------+-----------------------+
| Ex4_Sex               | Executive 4 gender    | address.gro           |
|                       |                       | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex4_Sex\"           |
+-----------------------+-----------------------+-----------------------+
| Ex5_Function          | Executive 5 function  | address.gro           |
|                       |                       | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex5_Function\"      |
+-----------------------+-----------------------+-----------------------+
| Ex5_FirstName         | Executive 5 first     | address.gro           |
|                       | name                  | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex5_FirstName\"     |
+-----------------------+-----------------------+-----------------------+
| Ex5_Surname           | Executive 5 surname   | address.gro           |
|                       |                       | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex5_Surname\"       |
+-----------------------+-----------------------+-----------------------+
| Ex5_Salutation        | Executive 5           | address.gro           |
|                       | salutation            | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex5_Salutation\"    |
+-----------------------+-----------------------+-----------------------+
| Ex5_Sex               | Executive 5 gender    | address.gro           |
|                       |                       | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex5_Sex\"           |
+-----------------------+-----------------------+-----------------------+
| Ex6_Function          | Executive 6 function  | address.gro           |
|                       |                       | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex6_Function\"      |
+-----------------------+-----------------------+-----------------------+
| Ex6_FirstName         | Executive 6 first     | address.gro           |
|                       | name                  | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex6_FirstName\"     |
+-----------------------+-----------------------+-----------------------+
| Ex6_Surname           | Executive 6 surname   | address.gro           |
|                       |                       | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex6_Surname\"       |
+-----------------------+-----------------------+-----------------------+
| Ex6_Salutation        | Executive 6           | address.gro           |
|                       | salutation            | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex6_Salutation\"    |
+-----------------------+-----------------------+-----------------------+
| Ex6_Sex               | Executive 6 gender    | address.gro           |
|                       |                       | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"Ex6_Sex\"           |
+-----------------------+-----------------------+-----------------------+
| DecsFunction          | Decisions             | address.gro           |
|                       | responsibility        | upedAdditionalItems - |
|                       | function              | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"DecsFunction\"      |
+-----------------------+-----------------------+-----------------------+
| DecsFirstName         | Decisions             | address.gro           |
|                       | responsibility first  | upedAdditionalItems - |
|                       | name                  | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"DecsFirstName\"     |
+-----------------------+-----------------------+-----------------------+
| DecsSurname           | Decisions             | address.gro           |
|                       | responsibility        | upedAdditionalItems - |
|                       | surname               | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"DecsSurname\"       |
+-----------------------+-----------------------+-----------------------+
| DecsSalutation        | Decisions             | address.gro           |
|                       | responsibility        | upedAdditionalItems - |
|                       | salutation            | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"DecsSalutation\"    |
+-----------------------+-----------------------+-----------------------+
| DecsGender            | Decisions             | address.gro           |
|                       | responsibility gender | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"DecsGender\"        |
+-----------------------+-----------------------+-----------------------+
| CRONUMBER             | Company Registration  | address.gro           |
|                       | Number                | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"CRONUMBER\"         |
+-----------------------+-----------------------+-----------------------+
| UCRN                  | Unique Company        | address.gro           |
|                       | Registration Number   | upedAdditionalItems - |
|                       |                       | keyed on              |
|                       |                       | \"BusinessData\"      |
|                       |                       |                       |
|                       |                       | item - keyed on       |
|                       |                       | \"UCRN\"              |
+-----------------------+-----------------------+-----------------------+
:::

::: {.gd__i .rte .c12 style="--cspan:12;--rspan:1;--cstart:auto;"}
##### Not Yet Built Specific Fields

  Related Data Field in Request   Description     Return Field response.address
  ------------------------------- --------------- -------------------------------------
  NOTYETBUILT                     Not Yet Built   address.additionalItems.NOTYETBUILT
:::

::: {.gd__i .rte .c12 style="--cspan:12;--rspan:1;--cstart:auto;"}
##### LPS Pointer Specific Fields

+-----------------------+-----------------------+-----------------------+
| Related Data Field in | Description           | Return Field          |
| Request               |                       | response.address      |
+=======================+=======================+=======================+
| TOWNLAND              | The town allocated as | address.OnsPointerInf |
|                       | the main postal       | ormation.Ptr.Townland |
|                       | centre for an area.   |                       |
|                       | May differ from the   |                       |
|                       | TOWN field in the     |                       |
|                       | main address          |                       |
+-----------------------+-----------------------+-----------------------+
| UNIQUE_BUILDING_ID    | 12-digit identifying  | address.additionalI   |
|                       | a Primary Addressable | tems.UniqueBuildingId |
|                       | Object defined by the | and                   |
|                       | \'physical            |                       |
|                       | footprint\' of the    | address               |
|                       | building shell        | .OnsPointerInformatio |
|                       |                       | n.PtrUniqueBuildingId |
+-----------------------+-----------------------+-----------------------+
| LOCAL_COUNCIL         | The name of the       | add                   |
|                       | administrative area   | ress.OnsPointerInform |
|                       | (local council) in    | ation.PtrLocalCouncil |
|                       | which the building    |                       |
|                       | exists                |                       |
+-----------------------+-----------------------+-----------------------+
| X_COR                 | 1m accurate easting   | address.onsPoint      |
|                       | coordinate based on   | erInformation.PtrXcor |
|                       | the Irish Grid        |                       |
+-----------------------+-----------------------+-----------------------+
| Y_COR                 | 1m accurate northing  | address.OnsPoint      |
|                       | coordinate based on   | erInformation.PtrYcor |
|                       | the Irish Grid        |                       |
+-----------------------+-----------------------+-----------------------+
| TEMP_COORDS           | If \"Y\", then        | address.OnsPointerInf |
|                       | indicates that        | ormation.PtrTempCoord |
|                       | PrtXcor and PtrYcor   |                       |
|                       | are temporary         |                       |
|                       | coordinates. Null     |                       |
|                       | indicates that        |                       |
|                       | PtrXcor and PtrYcor   |                       |
|                       | are permanent         |                       |
+-----------------------+-----------------------+-----------------------+
| BUILDING_STATUS       | The current physical  | addre                 |
|                       | status of the         | ss.OnsPointerInformat |
|                       | building. See         | ion.PtrBuildingStatus |
|                       | codelist:             |                       |
|                       | LPS_BUILDING_STATUS   |                       |
+-----------------------+-----------------------+-----------------------+
| ADDRESS_STATUS        | The current logical   | addr                  |
|                       | status of the         | ess.OnsPointerInforma |
|                       | address. See          | tion.PtrAddressStatus |
|                       | codelist:             |                       |
|                       | LPS_ADDRESS_STATUS    |                       |
+-----------------------+-----------------------+-----------------------+
| CLASSIFICATION        | A code signifying the | address.OnsPointerInf |
|                       | current use of the    | ormation.PtrClassCode |
|                       | building e.g.         |                       |
|                       | \"ND_culture\"        |                       |
+-----------------------+-----------------------+-----------------------+
| CREATION_DATE         | The date when an      | add                   |
|                       | address was first     | ress.OnsPointerInform |
|                       | entered into the      | ation.PtrCreationDate |
|                       | system by the local   |                       |
|                       | council               |                       |
+-----------------------+-----------------------+-----------------------+
| COMMENCEMENT_DATE     | The date when the     | address               |
|                       | construction of the   | .OnsPointerInformatio |
|                       | property began        | n.PtrCommencementDate |
+-----------------------+-----------------------+-----------------------+
| ARCHIVED_DATE         | The date when an      | add                   |
|                       | address is deemed to  | ress.OnsPointerInform |
|                       | be no longer in use   | ation.PtrArchivedDate |
+-----------------------+-----------------------+-----------------------+
:::

::: {.gd__i .rte .c12 style="--cspan:12;--rspan:1;--cstart:auto;"}
##### Geographic Fields

  Related Data Field in Request   Description                               Return Field response.address
  ------------------------------- ----------------------------------------- -----------------------------------------
  EASTING                         6-digit grid co-ordinate e.g. 341449.21   address.geographicInformation.easting
  NORTHING                        6-digit grid co-ordinate e.g. 368192.68   address.geographicInformation.northing
  LATITUDE                        Digital latitude value (future use)       address.geographicInformation.latitude
  LONGITUDE                       Digital longitude value (future use)      address.geographicInformation.longitude
:::

::: {.gd__i .rte .c12 style="--cspan:12;--rspan:1;--cstart:auto;"}
##### GBG and RM Unique IDs

  Related Data Field in Request   Description                            Return Field response.address
  ------------------------------- -------------------------------------- ---------------------------------------
  GBGURN_1                        Unique address key                     address.additionalItems.GBGURN_1
  GBGURN_2                        Unique key (future use)                address.additionalItems.GBGURN_2
  ADDRESSSOURCE                   Data source for the returned address   address.additionalItems.ADDRESSSOURCE
  ORGKEY                          Royal Mail Organisation Key            address.additionalItems.ORGKEY
  ADDKEY                          Royal Mail Address Key                 address.additionalItems.ADDKEY
:::
::::::::::
:::::::::::
::::::::::::
:::::::::::::
::::::::::::::
:::::::::::::::
::::::::::::::::
::::::::::::::::::
:::::::::::::::::::
::::::::::::::::::::
:::::::::::::::::::::
::::::::::::::::::::::
:::::::::::::::::::::::
::::::::::::::::::::::::
