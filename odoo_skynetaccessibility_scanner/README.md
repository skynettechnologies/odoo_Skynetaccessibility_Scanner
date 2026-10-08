SkynetAccessibility Scanner is a powerful Odoo accessibility testing and scanning module designed to help organizations identify, monitor, and fix accessibility issues across their websites. It enables businesses, agencies, and government organizations to maintain compliance with global accessibility standards while improving user experience for all visitors.

Built for Odoo 20.0, this module provides automated scanning, detailed reporting, and continuous monitoring - making accessibility management simple and scalable.

[**Start 10-Days Free Trial!**](https://skynetaccessibilityscan.com/trial-subscription)

## Why use Automated Odoo accessibility monitoring plugin - SkynetAccessibility Scanner?

Accessibility is not a one-time task. With evolving standards and legal requirements, websites require continuous monitoring and improvements. This module helps you:

- Detect accessibility issues automatically
- Track compliance across multiple pages
- Prioritize fixes with actionable recommendations
- Maintain long-term accessibility compliance

It acts as both an accessibility checker and compliance testing tool, helping teams proactively manage accessibility risks.

## Features

- Automated Accessibility Scanning.
- Detailed Automated generated reports with severity levels, issues descriptions, and clear remediation guidance.
- Sitemap-Based Scanning and Monitoring
- Multi Resolution Monitoring
- Set up weekly, monthly, or quarterly scheduled ongoing accessibility compliance monitoring
- Supports scanning in 190+ languages, making it ideal for global websites.
- Seamlessly integrates with the All in One Accessibility dashboard for centralized management.

### Supported Global Accessibility Compliance Standards

- WCAG 2.0, 2.1, 2.2
- ADA
- Section 508
- EAA EN 301 549 (EU)
- UK Equality Act
- Australian DDA
- Canada ACA
- Ontario AODA
- California Unruh
- Israeli Standard 5568
- Germany BITV 2.0
- France RGAA
- Spain UNE 139803
- Italy Stanca Act
- Indian RPD Act
- GIGW 3.0
- Brazilian Inclusion law LBI 13.146/2015
- Japan JIS X 8341

### Key Benefits for Odoo Users

- Works directly within the Odoo ecosystem
- Reduces manual accessibility testing efforts
- Helps improve user experience for people with disabilities
- Supports legal and compliance requirements
- Scales across multiple Odoo websites and projects

Explore the full capabilities of the accessibility monitoring Odoo module. Flexible plans allow to evaluate website accessibility requirements.

### Pricing

- 10 Days free trial

#### Single Site

- Small Site (Up to 25 pages): $9 Per Month
- Medium Site (Up to 250 pages): $19 per month
- Large Site (Up to 1000 pages): $89 per month
- Extra Large Site (Up to 2500 pages): $199 per month

#### Multi-site

- Silver (3 websites up to 1500 pages): $129 per month
- Gold (5 websites up to 2500 pages): $219 per month
- Platinum (10 websites up to 5000 pages): $399 per month

### Paid Add-ons

- Manual Accessibility Audit Report
- Manual Accessibility Remediation
- PDF/Document Accessibility Remediation
- VPAT Report/Accessibility Conformance Report (ACR)

## How does Odoo accessibility scanning and monitoring work?

- **Scan Your Website** – Run automated scans to detect accessibility issues with our Accessibility Testing Tool.
- **Review Reports** – Access prioritized issue lists with remediation recommendations.
- **Monitor & Maintain** – Keep your website accessible with ongoing monitoring using the Accessibility Scanning Monitoring Application.

## Getting Started with SkynetAccessibility Scanner

- Visit [WCAG Accessibility Scanning and Monitoring](https://www.skynettechnologies.com/accessibility-scanning-and-monitoring)
- Request a demo or [sign up for a free trial](https://skynetaccessibilityscan.com/trial-subscription) to explore accessibility scanning features.
- Configure website domains and customize accessibility scan settings.
- Start monitoring WCAG compliance, track accessibility issues, and download detailed audit report.

## Compatibility

### Version Support

| **Requirement** | **Supported Versions**        |
|-----------------|-------------------------------|
| Odoo            | 20.0 (Community & Enterprise) |
| Python          | 3.12 or newer (Odoo 20 requirement) |
| Module Version  | 1.0.0                         |

> **Note:** This module depends only on Odoo's `base` and `web` apps. Missing dependencies are installed automatically when you install the module. The Odoo server and your browser need internet access to reach the Skynet scanning platform.

## Installation

### Prerequisites

- Odoo 20.0
- An administrator login
- The file `odoo_skynetaccessibility_scanner.zip`

### Steps

To install the module, follow these instructions.

## Using the addons folder

1. Find your addons folder: open `odoo.conf` and look at the `addons_path` line.

2. Extract the zip into that folder so this file exists: `<addons_path>/odoo_skynetaccessibility_scanner/__manifest__.py`

> The folder must sit **directly** inside the addons path. If `__manifest__.py` is one level deeper, move the inner folder up.

3. Restart the Odoo server (or the Odoo Windows service).

4. Turn on Developer Mode: **Settings → General Settings → Developer Tools → Activate the developer mode**.

5. Go to **Apps**, click **Update Apps List**, then confirm.

6. Remove the **Apps** filter, search for **SkynetAccessibility Scanner**, and click **Activate** (or **Install**).

7. Open the main app menu (the grid icon at the top-left), click **SkynetAccessibility Scanner**, then **My Scans**.

## Using Import Module (zip upload)

No server access is needed for this option.

1. Turn on Developer Mode: **Settings → General Settings → Developer Tools → Activate the developer mode**.

2. Go to **Apps → Import Module**.

3. Click **Module file (.zip)** and choose `odoo_skynetaccessibility_scanner.zip`.

4. Click **Install**.

5. Wait for the "installed" message, then click **Close**.

6. Open the main app menu (the grid icon at the top-left), click **SkynetAccessibility Scanner**, then **My Scans**.

> Import Module requires an administrator user. Upload the original zip as it is; do not re-zip it.

## Activation and Deactivation

1. Navigate to **Apps** in Odoo.
2. Search for *SkynetAccessibility Scanner* (remove the **Apps** filter if it does not appear).
3. Click **Activate** (or **Install**) to enable the module, or open the **⋮** menu on the module card and click **Uninstall** to deactivate it.

### Upgrade

1. Replace the `odoo_skynetaccessibility_scanner` folder with the new version (or re-import the zip).
2. Restart Odoo, then go to **Apps → SkynetAccessibility Scanner → Upgrade**.

## CORS Policy Configuration

To avoid CORS policy issues, ensure the following URLs are allowed in your website. These URLs should be added to your CORS configuration or trusted domains list.

| **Domain** | **Description** | **Usage** |
|------------|-----------------|-----------|
| `https://skynetaccessibilityscan.com` | Skynet Accessibility Scan (Global Domain) | API access and resources |
| `https://*.skynettechnologies.com` | Skynet Technologies (Global Domain) | API access and resources |
| `https://*.skynettechnologies.us` | Skynet Technologies (US Domain) | API access and resources |
| `https://*.googleapis.com` | Google APIs | Services like Fonts, Translation |
| `https://*.gstatic.com` | Fonts APIs | Custom Fonts |

## Instructions

1. Update your server's CORS configuration to include these URLs.
2. Ensure wildcard subdomains (`*`) are supported where necessary.
3. Verify the application functionality by testing requests to these domains.
4. If issues persist, consult the documentation for CORS configuration guidance.

## Screenshots

![SkynetAccessibility_Scanner_Image_1](https://www.skynettechnologies.com/sites/default/files/SkynetAccessibilityScanner/SkynetAccessibility_Scanner_Image_1.jpg)
![SkynetAccessibility_Scanner_Image_2](https://www.skynettechnologies.com/sites/default/files/SkynetAccessibilityScanner/SkynetAccessibility_Scanner_Image_2.jpg)
![SkynetAccessibility_Scanner_Image_3](https://www.skynettechnologies.com/sites/default/files/SkynetAccessibilityScanner/SkynetAccessibility_Scanner_Image_3.jpg)
![SkynetAccessibility_Scanner_Image_4](https://www.skynettechnologies.com/sites/default/files/SkynetAccessibilityScanner/SkynetAccessibility_Scanner_Image_4.jpg)

## Video

[![SkynetAccessibility Scanner](https://img.youtube.com/vi/g0RNlTOQImY/0.jpg)](https://www.youtube.com/watch?v=g0RNlTOQImY)

## Submit a Support Request

Please visit our **[support page](https://www.skynettechnologies.com/report-accessibility-problem)** and fill out the form. Our team will get back to you as soon as possible.

## Send Us an Email

Alternatively, you can send an email to our support team:
**[hello@skynettechnologies.com](mailto:hello@skynettechnologies.com)**

## Accessibility Partnership Opportunities

### **[Accessibility Agency Partnership](https://www.skynettechnologies.com/agency-partners)**

Partner with us as an agency to provide comprehensive accessibility solutions to your existing clients. Get access to exclusive resources, training, and support to help you implement and manage accessibility features effectively.

### **[Accessibility Affiliate Partnership](https://www.skynettechnologies.com/affiliate-partner)**

Join our affiliate program and earn hefty commissions by promoting SkynetAccessibility Scanner. Share our accessibility solution within your network and help businesses improve their website accessibility while generating additional revenue.

For more details, please visit **[Accessibility Partnership Opportunities Page](https://www.skynettechnologies.com/partner-program)**.

## Credits

This **Accessibility Scanning Monitoring Application** is developed and maintained by **[Skynet Technologies USA LLC](https://www.skynettechnologies.com)**