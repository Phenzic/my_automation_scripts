::::::::::::::::::: {#mainBodyContent role="main" tabindex="-1"}
:::::::::::::::::: gd
::::::::::::::::: {.gd__c style="--cols:12"}
:::::::::::::::: {.gd__i .section .ptop--96 .c12 style=" --cspan:12; --rspan:1; --cstart:1;"}
::::::::::::::: {.section .gd__s}
:::::::::::::: {.gd__a style="--cols: 12;--cspan: 12; --rspan: 1;"}
::::::::::::: {.gd__c style="--cols:12"}
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

::::::::::: {.gd__i .section .c9 style=" --cspan:9; --rspan:1; --cstart:auto;"}
:::::::::: gd
::::::::: {.gd__c style="--cols:12"}
:::::::: {.gd__i .section .gd--cen .content .c12 style="--cspan:12;--rspan:1;--cstart:1;"}
::::::: {.section .gd__s}
:::::: {.gd__a style="--cols: 12;--cspan: 12; --rspan: 1;"}
::::: {.gd__c style="--cols:12"}
::: {.gd__i .rte .c12 style="--cspan:12;--rspan:1;--cstart:auto;"}
## Address Filters

Filtering provides a way to 'filter out' addresses, which have been
found by the web service, which match a particular kind of address.
Addresses which match an enabled filter are excluded from the IDM
results and are not returned in the overall response.

Each supported filter is identified by a code. To enable a particular
filter, a new element needs to be added to the "additionalData" of the
"requestData" of the IDM request. This element is a key-value pair,
whose key must be the filter code and whose value should be a "yes" or
"no" value. Providing "yes" informs the service that address types
covered by this filter should be returned, while providing "no" informs
the service that those addresses should not be returned (should be
filtered out).

Multiple filters may be specified in a request, if an address matches
any of the enabled filters, then the address is not returned.
:::

::: {.gd__i .rte .c12 style="--cspan:12;--rspan:1;--cstart:auto;"}
### Available Filters

Below are the available filters for use, some are only supported by
certain profiles and some are further only supported by certain datasets
used in conjunction with one of the profiles.

  Name          Notes                                                                           Profile(s) Supported                                                               Dataset(s) Supported
  ------------- ------------------------------------------------------------------------------- ---------------------------------------------------------------------------------- --------------------------------------------------------------------------
  ADDRPROV      Filter addresses with logical status of \'provisional\'                         Matchcode AddressBase, MultiDatabase                                               ABP, ABL
  ADDRAPPR      Filter addresses with logical status of \'approved\'                            Matchcode AddressBase, MultiDatabase                                               ABP, ABL 
  ADDRALT       Filter addresses with logical status of \'alternative\'                         Matchcode AddressBase, MultiDatabase                                               ABP, ABL
  ADDRHIST      Filter addresses with logical status of \'historical\'                          Matchcode AddressBase, MultiDatabase                                               ABP, ABL
  PREMCONSTR    Filter properties with state 'under construction'                               Matchcode AddressBase, MultiDatabase                                               ABP
  PREMINUSE     Filter properties with state \'in use\'                                         Matchcode AddressBase, MultiDatabase                                               ABP
  PREMUNOCC     Filter properties with state \'unoccupied\'                                     Matchcode AddressBase, MultiDatabase                                               ABP
  PREMDEM       Filter properties with state 'demolished' or 'no longer existing'               Matchcode AddressBase, MultiDatabase                                               ABP
  PREMPLAN      Filter properties with state \'planning permission granted\' or \'candidate\'   Matchcode AddressBase, MultiDatabase                                               ABP
  PREMUNKOWN    Filter properties with building state of \'unknown\'                            Matchcode AddressBase, MultiDatabase                                               ABP
  POSTADRCODE   Filter non-postal addresses                                                     Matchcode AddressBase, MultiDatabase                                               ABP
  ADDRBUS       Filter addresses showing those from business dataset                            MultiDatabase                                                                      N/A
  ADDROG        Filter business addresses from non-business-specific sources (e.g. PAF)         Matchcode AddressBase, Matchcode UK Address, Matchcode Eircode, Matchcode Global   ABP, ABL, NAMES, NOT_YET_BUILT, MULTI_RES, ECAF, ECAD, GLOBAL_ADDRESSING
:::
:::::
::::::
:::::::
::::::::
:::::::::
::::::::::
:::::::::::
:::::::::::::
::::::::::::::
:::::::::::::::
::::::::::::::::
:::::::::::::::::
::::::::::::::::::
:::::::::::::::::::
