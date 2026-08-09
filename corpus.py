"""Support corpus data for the three ecosystems."""

HACKERRANK_CORPUS = """
=== HACKERRANK SUPPORT KNOWLEDGE BASE ===

PRODUCT AREAS: Screen, Interviews, Settings, Integrations, General Help, Library, SkillUp, Engage, Chakra

--- SCREEN (Tests & Candidates) ---
- Tests remain active indefinitely unless start/end times are set.
- To set expiration: Go to test Settings > General > Update Start/End date & time. Clear fields (X) for indefinite.
- Candidates CANNOT reschedule tests themselves. They must contact the company that invited them for a new link.
- Companies can extend deadlines or re-invite candidates via their admin dashboard.
- Time Accommodation: Tests tab > Select test > Candidates tab > Select candidate > More > Add Time Accommodation > Enter % in multiples of five > Save.
- Add Extra Time (during/after test): Tests tab > Select test > Candidates tab > Select candidate > More > Add Time > Enter minutes > Confirm.
- Test timer runs continuously; does not pause for technical issues.
- Supported browsers: Chrome (recommended), Edge, Firefox, Safari.
- Common issues: test links expiring, browser compatibility, unsupported browsers, network issues.
- Troubleshooting: Clear browser cache, disable extensions, use Chrome, check internet connection.

--- TEST INTEGRITY ---
- Impersonation Detection features: Photo Identification, Image Proctoring, Multiple Monitor Detection, Webcam Switch Detection, Image Analysis (AI).
- Photo ID: captures candidate photo before test. Hiring team must manually verify.
- Image Proctoring: captures images at 1-minute intervals. Disabled by default.
- Multiple Monitor Detection: detects external monitors. Supported on Edge/Chrome/Chromium.
- Image Analysis (AI): categorizes proctoring images into Multiple Faces, Secondary Faces, No Faces, Static Faces.
- Suspicion scores: High (8-10), Medium (5-7), Low (<5).
- HackerRank does NOT review or change candidate scores. Only the hiring company can do that.
- HackerRank does NOT intervene in hiring decisions.

--- INTERVIEWS ---
- Interview product supports live coding interviews with candidates.
- Zoom connectivity is required for some interview-based tests.
- Inactivity timeouts may disconnect users; settings are configurable per account.
- Troubleshoot Zoom: ensure Zoom installed/updated, try different network, clear browser cache.

--- SETTINGS & ACCOUNT MANAGEMENT ---
- Team Management: Settings > Team > Find user > Click Remove. Only admins with permissions can add/remove.
- Roles Management: Admin roles control access levels.
- Company Level Admin Settings: manage company-wide configurations.
- User Account Settings: manage individual preferences.
- GDPR and NYC AI Laws compliance available.
- To delete HackerRank account (Google login): Reset password first via "Forgot your password", then Settings > Delete Account.
- SOC 2 Type II certification, GDPR compliance available. Visit security.hackerrank.com for infosec.

--- BILLING ---
- Subscription changes (upgrades, downgrades, pauses, cancellations) must be handled by account admins or HackerRank sales support.
- For billing inquiries: contact billing@hackerrank.com.
- Refund policies vary by contract.

--- COMMUNITY ---
- HackerRank Community is for practice and learning.
- Account deletion requires setting a password first if using Google login.
"""

CLAUDE_CORPUS = """
=== CLAUDE HELP CENTER KNOWLEDGE BASE ===

PRODUCT AREAS: Claude (chat), Pro/Max plans, Team/Enterprise plans, API/Console, Claude Code, Claude Desktop, Mobile apps, Connectors, Claude for Education, Privacy/Legal, Safeguards, Amazon Bedrock

--- ACCOUNT MANAGEMENT ---
- Get support: Log in > Click initials (lower left) > "Get help" > Chat with Fin (AI bot) or search help.
- No phone or live chat support. Product Support team assists through support messenger.
- Free users: access to help docs, Fin AI bot, and account deletion support.
- Team/Enterprise non-Owners: chat with Fin only. Escalation requires Owner/Admin to contact support.
- Enterprise Owners: can submit Enterprise Support form at claude.ai/support/enterprise.
- Subscription support: help locating login info, cancellations, refund eligibility (requires account validation).
- Change email: available through account settings.
- Delete account: available through account settings. Permanent and cannot be undone.
- Export data: available through account settings.
- Log out all sessions: available through security settings.

--- CONVERSATION MANAGEMENT ---
- Delete/rename conversation: Click conversation name at top > Select Delete or Rename.
- Sharing/unsharing chats: available through conversation options.
- Incognito chats: for temporary conversations not saved to history.
- Chat search and memory: build on previous context.

--- TEAM & ENTERPRISE PLANS ---
- Team plan: collaborative workspace for organizations.
- Enterprise plan: advanced features, SSO, SCIM, audit logs, compliance.
- Workspace access managed by Owners and Admins.
- Non-owner/non-admin users should contact their workspace Owner for access issues.
- Roles and permissions: Owner, Admin, Member (varying access levels).
- Seat management: Admins can purchase/manage seats.
- When user removed from org: their data handling depends on org settings.
- Billing: Team plan calculated per seat. Annual/monthly billing options.
- Cancel Team plan: available through subscription settings.

--- PRIVACY & DATA ---
- Free plan: conversations MAY be used to improve models. Users can opt out in settings.
- Team/Enterprise: conversations NOT used for model training by default.
- Data retention policies vary by plan.
- Anthropic acts as Data Processor for Team/Enterprise.
- Users can export data or delete account at any time.
- Web crawling: Block ClaudeBot by adding to robots.txt: User-agent: ClaudeBot, Disallow: /
- Responsible Disclosure Policy: report security vulnerabilities via responsible-disclosure-policy page.

--- SAFEGUARDS ---
- Model Safety Bug Bounty Program: for reporting security vulnerabilities in Claude.
- Report vulnerabilities: visit Anthropic's Responsible Disclosure Policy page.
- Public Vulnerability Reporting available.
- Usage Policy governs acceptable use.
- Content filtering may block certain outputs.

--- AMAZON BEDROCK ---
- Claude available through AWS Bedrock in multiple regions.
- For Bedrock support: contact AWS support, not Anthropic.
- Common issues: IAM permissions, region availability, model access requests, rate limits.

--- CLAUDE FOR EDUCATION ---
- Claude for Education: available for universities.
- LTI integration: Set up Claude LTI in Canvas by Instructure (documented).
- Getting Started guide available for university Owners/Admins.
- Contact Anthropic's education team or visit Claude for Education documentation.
"""

VISA_CORPUS = """
=== VISA CONSUMER SUPPORT KNOWLEDGE BASE ===

PRODUCT AREAS: Credit Cards, Security/Fraud, Travel Support, 3-D Secure/Verified by Visa, Merchant Issues, General Support

--- CREDIT CARDS ---
- Log in to account: Visit your issuer/bank website. Website and phone number on your card.
- Dispute a charge: Contact your issuer/bank using phone number on card. Provide detailed transaction info.
- Common dispute reasons: unauthorized charges, wrong amounts, merchandise not received, duplicate charges.
- Card declined: Contact issuer/bank for specific decline reason and guidance.

--- LOST OR STOLEN CARD ---
- Report lost/stolen card from India: Call 000-800-100-1219.
- Global Customer Assistance Service (GCAS): +1 303 967 1090 (24/7).
- Reverse charge calls: +1 303 967 1096.
- GCAS can: block card within ~30 minutes, arrange emergency cash, provide replacement card (1-3 days).
- Have ready: card number, when/where lost, issuer name.

--- IDENTITY THEFT ---
- If identity theft involves Visa card: visit Lost or Stolen card page to cancel card or get emergency replacement.
- This is HIGH RISK and should be escalated to human support.

--- SECURITY & FRAUD ---
- Visa does NOT call or email cardholders to request personal information.
- If contacted by someone claiming to be Visa requesting info: do NOT provide it. Report via contact form.
- Visa does not set up, service or have access to cardholder or merchant accounts (done through banks).

--- TRAVEL SUPPORT ---
- Before travel: confirm card activated for overseas use, know daily ATM withdrawal limit, know expiry dates/balance.
- Sign up for SMS transaction alerts.
- Know your credit card PIN before travelling overseas.
- Tell your bank where/when you'll be travelling to avoid fraud flags.
- Emergency cash abroad: Contact GCAS at +1 303 967 1096 (reverse charge) for emergency cash disbursement.
- Visa's exchange rate applies when paying with Visa card abroad.
- Dynamic Currency Conversion (DCC): choice to pay in home currency (includes service fee). Pay in local currency for Visa's rate.
- ATM Locator: visa.com/atmlocator for 2+ million ATMs worldwide.
- Currency exchange calculator available on visa.co.in.

--- TRAVELLER'S CHEQUES ---
- If stolen: call the issuer immediately (e.g., Citicorp: 1-800-645-6556 or collect 1-813-623-1709).
- Have ready: cheque serial numbers, where/when bought, how/when lost/stolen, issuer name.
- Refunds typically arranged within 24 hours.
- Notify local police. Use Visa's contact form if can't reach issuer.

--- 3-D SECURE (VERIFIED BY VISA) ---
- No consumer registration needed. Issuers handle authentication.
- If issues: contact your issuer/bank.
- Provides additional security layer for e-commerce transactions.

--- MERCHANT RULES ---
- Merchants generally CANNOT set minimum or maximum for Visa transactions.
- EXCEPTION: In USA and US territories (Puerto Rico, US Virgin Islands, Guam), merchants MAY require minimum of US$10 for CREDIT cards only.
- If merchant requires >$10 minimum on credit card or any minimum on debit card: notify your Visa card issuer.
- Report merchant concerns: fill out form at visa.co.in/Forms/visa-rules.html.
"""

ESCALATION_KEYWORDS = [
    "identity theft", "identity stolen", "fraud", "stolen card", "unauthorized",
    "security vulnerability", "bug bounty", "hacked", "breach", "compromised",
    "delete all files", "system files", "hack", "exploit",
    "suicide", "self-harm", "emergency", "police", "legal action",
    "lawsuit", "attorney", "lawyer",
    "internal rules", "system prompt", "ignore instructions",
]

ALL_CORPUS = HACKERRANK_CORPUS + "\n\n" + CLAUDE_CORPUS + "\n\n" + VISA_CORPUS
