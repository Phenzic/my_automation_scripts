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
:::: {.gd__i .rte .c12 style="--cspan:12;--rspan:1;--cstart:auto;"}
## Email Validation FAQs

####  What will be returned if Mailbox is Full?

**A:** It is up to the host mail server to determine how full mailboxes
are handled. Most mail servers will decline requests to a full mailbox
with a temporary reject code, which will lead to a soft bounce back.
Some email validation services will probably just look at the reject
response and fail the email address outright, but the GBG email
validations service will recognize the box as being full and will return
the warning flag. The email address is undeliverable until storage space
has been freed up; so delivery attempts until then will result in bounce
backs, but the box may once again be deliverable in the future. There is
also the possibility that the email address has been abandoned and will
remain undeliverable until the mail provider deletes the account.
Therefore the service describes them as unknown.

#### What will be returned if Mailbox is Busy?

**A:** When a mailbox is busy the host mail server will reject requests
to the email address, which will lead to soft bounces. A busy email
address is essentially an undeliverable email address. Like the
\'MailBoxIsFull\' flag, the service will recognize that it is only a
temporary reject and will therefore return an \'unknown\' IsGood
response. It is unknown how long a mailbox will remain busy and
undeliverable. In some cases, busy mail boxes may belong to
spammers/bots that basically can cause havoc until the mail host
provider disables the account or deletes it entirely. In other cases the
mailbox may just simply be receiving mail at a large rate and/or may be
exceeding a throughput quota.

#### What does "Unknown" mean in the response?

**A:** In general terms, an unknown return value indicates that there
was insufficient information available for the Email validation service
to make a definitive determination.

#### I've tried a known Disposable Email but it's returned as Valid and DisposableEmail is false?

**A:** GBG are always improving the Email Validation service, as such we
are unable to detect every disposable email address created. It should
be noted that the Vulgar, Garbage and Bogus can often be attributed to
some disposable email addresses so can act as indicators.

#### What will the value of IsGood be if BlacklistedDomain and Alias email address are true?

**A:** A blacklist check is performed separately to the SMTP check, but
it alone is insufficient to return "Email is Bad" though it can reduce
to "Email is Probably Bad". Some MTA (Mail Transfer Agents) or firewalls
may prevent communications with blacklisted domains even via an email
address, with other MTA's they may allow an email to go to a blacklisted
domain but prevent any return. Hence the flag returned is a warning to
the user to indicate they may encounter some difficulty when attempting
to communicate with a black listed domain.

#### What is the difference between IsGood and ValidityFlag response?

**A:**  IsGood was primary flag GBG provided, so this has been retained
for existing users. ValidityFlag is the most recent encompassing flag.

#### What is the MisspelledSuggestion response for?

**A:**  MisspelledSuggestion could be populated where GBG have spotted a
potential typing mistake in say a domain. So for instance if the email
submitted was <Laura@hotmil.com>, MissspelledSuggestion could return
Hotmail.com

#### I know the email address exists, why is it saying it doesn't or unknown?

**A:**  Sometimes a domain can present a DNS error, depending upon the
DNS time-to-live of 24 hours, then that could have prevented the service
from establishing communication with the specific mail servers. However,
the service does not fail a server until after three consecutive days,
so unless the DNS error persisted the service should eventually
communicate with the mail servers and clear it.

#### I know the email address is definitely a Spammer/GreyListed/Complainer... but it's not flagged as such?

**A:**  No list is ever complete and it would not be that uncommon that
some lists lag behind what is really happening in the world, in both
adding and removing emails or domains to specific lists. GBG always
strive to ensure all the services are up to date and using the freshest
data, however in this example, it's not possible to have real time
updates to such lists.

::: subtle-wrap
:::
::::
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
