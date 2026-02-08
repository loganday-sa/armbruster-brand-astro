#!/usr/bin/env python3
"""
Generate the AI Development & Deployment Governance Framework PDF.
Uses reportlab to create a branded PDF with compliance requirements and checklists.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, Image
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import os

# ── Branding Constants ──────────────────────────────────────────────
BRAND_NAME = "Scott Armbruster"
BRAND_TAGLINE = "AI Strategy & Systems at Every Level"
BRAND_TITLE = "AI Strategy & Systems Partner"
BRAND_WEBSITE = "scottarmbruster.com"
BRAND_LINKEDIN = "linkedin.com/in/scottrarmbruster"
BRAND_EMAIL = "info@scottarmbruster.com"

# Colors
DARK_BG = HexColor("#1e293b")       # slate-800
BLUE_ACCENT = HexColor("#3b82f6")   # blue-500
ORANGE_ACCENT = HexColor("#D97706")  # orange-600
LIGHT_TEXT = HexColor("#cbd5e1")     # slate-300
DARK_TEXT = HexColor("#1e293b")
WHITE = white
MEDIUM_TEXT = HexColor("#64748b")    # slate-500
GREEN = HexColor("#059669")
YELLOW = HexColor("#eab308")
RED = HexColor("#ef4444")

OUTPUT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "downloads", "ai-development-governance-framework.pdf")
HERO_IMG = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "images", "resources", "ai-development-governance.png")

# ── Page Template ───────────────────────────────────────────────────
def header_footer(canvas, doc):
    """Draw header and footer on every page."""
    width, height = letter
    page_num = canvas.getPageNumber()

    # Header background
    canvas.setFillColor(DARK_BG)
    canvas.rect(0, height - 50, width, 50, fill=1, stroke=0)

    # Orange accent line under header
    canvas.setFillColor(ORANGE_ACCENT)
    canvas.rect(0, height - 53, width, 3, fill=1, stroke=0)

    # Header text
    canvas.setFillColor(WHITE)
    canvas.setFont("Helvetica-Bold", 11)
    canvas.drawString(36, height - 35, BRAND_NAME)

    canvas.setFont("Helvetica", 9)
    canvas.drawRightString(width - 36, height - 35, BRAND_TAGLINE)

    # Footer background
    canvas.setFillColor(DARK_BG)
    canvas.rect(0, 0, width, 40, fill=1, stroke=0)

    # Footer text
    canvas.setFillColor(MEDIUM_TEXT)
    canvas.setFont("Helvetica", 7.5)
    footer_text = f"{BRAND_WEBSITE}  |  {BRAND_LINKEDIN}  |  {BRAND_EMAIL}"
    canvas.drawString(36, 16, footer_text)
    canvas.drawRightString(width - 36, 16, f"Page {page_num}")


# ── Styles ──────────────────────────────────────────────────────────
def get_styles():
    s = {}
    s["title"] = ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=24, leading=30, textColor=DARK_TEXT, spaceAfter=10)
    s["subtitle"] = ParagraphStyle("subtitle", fontName="Helvetica", fontSize=11, leading=16, textColor=MEDIUM_TEXT, spaceAfter=8)
    s["h2"] = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=18, leading=24, textColor=DARK_TEXT, spaceAfter=10, spaceBefore=4)
    s["h3"] = ParagraphStyle("h3", fontName="Helvetica-Bold", fontSize=12, leading=16, textColor=DARK_TEXT, spaceAfter=6, spaceBefore=8)
    s["h3orange"] = ParagraphStyle("h3orange", fontName="Helvetica-Bold", fontSize=12, leading=16, textColor=ORANGE_ACCENT, spaceAfter=6, spaceBefore=8)
    s["body"] = ParagraphStyle("body", fontName="Helvetica", fontSize=9.5, leading=13, textColor=DARK_TEXT, spaceAfter=5)
    s["bodysmall"] = ParagraphStyle("bodysmall", fontName="Helvetica", fontSize=8.5, leading=12, textColor=MEDIUM_TEXT, spaceAfter=3)
    s["bold"] = ParagraphStyle("bold", fontName="Helvetica-Bold", fontSize=9.5, leading=13, textColor=DARK_TEXT, spaceAfter=4)
    s["bullet"] = ParagraphStyle("bullet", fontName="Helvetica", fontSize=9, leading=13, textColor=DARK_TEXT, spaceAfter=2, leftIndent=18, bulletIndent=6)
    s["center"] = ParagraphStyle("center", fontName="Helvetica", fontSize=10, leading=15, textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=6)
    s["center_bold"] = ParagraphStyle("center_bold", fontName="Helvetica-Bold", fontSize=16, leading=22, textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=4)
    s["center_orange"] = ParagraphStyle("center_orange", fontName="Helvetica-Bold", fontSize=12, leading=16, textColor=ORANGE_ACCENT, alignment=TA_CENTER, spaceAfter=8)
    s["warning"] = ParagraphStyle("warning", fontName="Helvetica-Bold", fontSize=10, leading=14, textColor=RED, spaceAfter=6)
    return s


def build_pdf():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=letter,
        topMargin=72,
        bottomMargin=60,
        leftMargin=36,
        rightMargin=36
    )
    S = get_styles()
    story = []

    # ════════════════════════════════════════════════════════════════
    # PAGE 1: Title Page
    # ════════════════════════════════════════════════════════════════
    story.append(Spacer(1, 20))
    story.append(Paragraph("AI Development & Deployment<br/>Governance Framework", S["title"]))
    story.append(Spacer(1, 6))
    story.append(Paragraph("Navigate EU AI Act, state regulations, bias audits, and compliance requirements", S["subtitle"]))
    story.append(Spacer(1, 12))

    # Hero infographic
    if os.path.exists(HERO_IMG):
        img_width = 540
        img_height = img_width * 9 / 16
        story.append(Image(HERO_IMG, width=img_width, height=img_height))

    story.append(Spacer(1, 14))
    story.append(Paragraph(f"<b>{BRAND_NAME}</b>", ParagraphStyle("author", fontName="Helvetica-Bold", fontSize=14, leading=18, textColor=DARK_TEXT)))
    story.append(Paragraph(BRAND_TITLE, ParagraphStyle("authortitle", fontName="Helvetica", fontSize=11, leading=15, textColor=ORANGE_ACCENT, spaceAfter=4)))
    story.append(Paragraph("For organizations building AI-powered products, features, and automated decision systems", S["bodysmall"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph(f"{BRAND_WEBSITE}  |  {BRAND_LINKEDIN}  |  {BRAND_EMAIL}", S["bodysmall"]))
    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PAGE 2: Regulatory Overview
    # ════════════════════════════════════════════════════════════════
    story.append(Paragraph("The Regulatory Landscape (2025-2027)", S["h2"]))
    story.append(Paragraph(
        "AI governance isn't optional. Between the EU AI Act, state laws, and sector-specific regulations, ignorance is expensive. "
        "Here's what's actually enforceable.",
        S["body"]
    ))
    story.append(Spacer(1, 8))

    regulations = [
        ("EU AI Act", "Adopted April 2024 | Full enforcement by 2027",
         "• Risk classification (Unacceptable/High/Limited/Minimal)\n• Conformity assessments for high-risk AI\n• Technical documentation and audit trails\n• Fines up to €35M or 7% of global revenue",
         "Applies to ANY company offering AI in EU market"),

        ("Colorado SB 24-205", "Effective February 2026",
         "• Impact assessments for high-risk AI\n• Disclosure requirements\n• Risk management framework\n• Fines up to $20K per violation",
         "Applies to high-risk AI deployed in Colorado"),

        ("NYC Local Law 144", "Effective July 2023 (Active Now)",
         "• Annual bias audit for hiring AI\n• Published summary statistics\n• Candidate notification requirements\n• Daily fines for non-compliance",
         "Applies to automated employment decision tools in NYC"),

        ("GDPR Article 22", "Active since 2018",
         "• Right to explanation for automated decisions\n• Right to human review and contest\n• Data Protection Impact Assessments (DPIA)\n• Fines up to €20M or 4% of global revenue",
         "Applies to automated decisions affecting EU residents"),
    ]

    for title, status, reqs, scope in regulations:
        story.append(Paragraph(f"<b>{title}</b>", S["h3orange"]))
        story.append(Paragraph(status, S["bodysmall"]))
        story.append(Paragraph(reqs, S["body"]))
        story.append(Paragraph(f"<i>{scope}</i>", S["bodysmall"]))
        story.append(Spacer(1, 6))

    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PAGE 3: Risk Classification
    # ════════════════════════════════════════════════════════════════
    story.append(Paragraph("AI System Risk Classification", S["h2"]))
    story.append(Paragraph("First step: classify your AI system. This determines what documentation, testing, and oversight you need.", S["body"]))
    story.append(Spacer(1, 8))

    risk_tiers = [
        ("UNACCEPTABLE RISK (Banned)", RED,
         "Social scoring by governments, mass surveillance, subliminal manipulation, exploiting vulnerabilities",
         "Do not deploy. Stop development immediately."),

        ("HIGH RISK (Heavy Compliance)", ORANGE_ACCENT,
         "AI for hiring, lending, healthcare, law enforcement, education, insurance, housing",
         "Impact assessment + bias audit + technical docs + human oversight + logging required before deployment"),

        ("LIMITED RISK (Disclosure Required)", YELLOW,
         "Chatbots, AI-generated content, deepfakes, emotion recognition",
         "Disclose AI interaction to users. Label AI-generated content. Basic documentation."),

        ("MINIMAL RISK (Voluntary)", GREEN,
         "Spam filters, video games, inventory management, weather prediction",
         "No specific AI regulations apply. Follow general software best practices."),
    ]

    for tier, color, examples, requirement in risk_tiers:
        story.append(Paragraph(f'<font color="{color.hexval()}" size="11"><b>{tier}</b></font>', S["bold"]))
        story.append(Paragraph(f"<b>Examples:</b> {examples}", S["body"]))
        story.append(Paragraph(f"<b>Requirements:</b> {requirement}", S["bodysmall"]))
        story.append(Spacer(1, 8))

    story.append(Spacer(1, 6))
    story.append(Paragraph("<b>Quick Decision Tree:</b>", S["bold"]))
    story.append(Paragraph("1. Does your AI manipulate, exploit, or surveil people in prohibited ways? → UNACCEPTABLE", S["bullet"]))
    story.append(Paragraph("2. Does it make decisions about people in sensitive areas (hiring, lending, healthcare)? → HIGH RISK", S["bullet"]))
    story.append(Paragraph("3. Does it interact with users or generate content? → LIMITED RISK", S["bullet"]))
    story.append(Paragraph("4. Otherwise → MINIMAL RISK", S["bullet"]))

    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PAGES 4-6: 8-Step Compliance Checklist (High-Risk AI)
    # ════════════════════════════════════════════════════════════════
    story.append(Paragraph("High-Risk AI: 8-Step Pre-Deployment Checklist", S["h2"]))
    story.append(Paragraph(
        "All 8 must be complete before launching a high-risk AI system in regulated markets. "
        "One missing requirement = non-compliant.",
        S["body"]
    ))
    story.append(Spacer(1, 8))

    checklist = [
        ("1. Pre-Deployment Impact Assessment Completed",
         "Document intended use, potential harms, mitigation strategies, affected populations",
         "• System description and decision-making role\n• Data sources and training data\n• Reasonably foreseeable risks\n• Risk mitigation measures\n• Affected demographic groups\n• Human oversight mechanisms",
         "Required by: Colorado SB 24-205 (2026), EU AI Act Article 27"),

        ("2. Independent Bias Audit Conducted",
         "Third-party or internal audit testing for discriminatory outcomes across protected classes",
         "• Disparate impact analysis by race, gender, age\n• Selection rate ratios or impact ratios\n• Confusion matrix metrics by group\n• Statistical significance testing\n• Audit date, methodology, sample size",
         "Required by: NYC Local Law 144 (annual), EU AI Act (before deployment + major changes)"),

        ("3. Technical Documentation Package Created",
         "Comprehensive documentation of system design, training, testing, performance",
         "• System architecture and design specs\n• Training data description and methodology\n• Model performance metrics\n• Validation and testing results\n• Known limitations and failure modes\n• Cybersecurity measures\n• Change log and version control",
         "Required by: EU AI Act Annex IV. Retention: 10 years (EU), 3-7 years (US)"),

        ("4. Model Card Published",
         "Standardized ML model documentation (Mitchell et al. framework)",
         "• Model details (version, type, license)\n• Intended use and out-of-scope uses\n• Performance metrics by subgroup\n• Training and evaluation data\n• Ethical considerations\n• Caveats and recommendations",
         "Best practice (not legally required but recommended)"),
    ]

    for title, desc, bullets, reg in checklist[:4]:
        story.append(Paragraph(f"<b>{title}</b>", S["h3orange"]))
        story.append(Paragraph(desc, S["body"]))
        story.append(Paragraph(bullets, S["bodysmall"]))
        story.append(Paragraph(f"<i>{reg}</i>", S["bodysmall"]))
        story.append(Spacer(1, 6))

    story.append(PageBreak())

    # Continue checklist items 5-8
    checklist_cont = [
        ("5. Human Oversight Mechanism Implemented",
         "GDPR Article 22 and EU AI Act require human review capability",
         "• Human-in-the-loop (approves each decision)\n• Human-on-the-loop (monitors and can intervene)\n• Human-in-command (can override or shut down)\n• Document which model is used, who has authority, intervention triggers",
         "Required by: GDPR Article 22, EU AI Act"),

        ("6. Automated Logging and Audit Trails Active",
         "Enable traceability through comprehensive logging",
         "• Input data for each decision\n• Model output and confidence scores\n• Timestamp and system version\n• User who invoked the model\n• Human override events\n• Errors and exceptions",
         "Required by: EU AI Act Article 12. Retention: 3-10 years, protected from tampering"),

        ("7. User-Facing Transparency Disclosures",
         "Inform affected individuals that AI is used and provide meaningful information",
         "• Clear notice AI is making/assisting decisions\n• Purpose and general logic of the system\n• Right to contest or request human review\n• Contact for questions or complaints",
         "Required by: GDPR, NYC Local Law 144, California AB 2930"),

        ("8. Post-Deployment Monitoring Plan Established",
         "Continuous monitoring required for high-risk AI in operation",
         "• Performance metrics tracked\n• Drift detection (data and concept drift)\n• Bias metrics tracked over time\n• Incident reporting procedures\n• Review cadence and responsible team\n• Triggers for re-audit",
         "Required by: EU AI Act Article 61"),
    ]

    for title, desc, bullets, reg in checklist_cont:
        story.append(Paragraph(f"<b>{title}</b>", S["h3orange"]))
        story.append(Paragraph(desc, S["body"]))
        story.append(Paragraph(bullets, S["bodysmall"]))
        story.append(Paragraph(f"<i>{reg}</i>", S["bodysmall"]))
        story.append(Spacer(1, 6))

    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PAGE 7: AI System Inventory
    # ════════════════════════════════════════════════════════════════
    story.append(Paragraph("AI System Inventory Template", S["h2"]))
    story.append(Paragraph("You can't govern what you can't see. Maintain a living inventory of all AI systems in development or production.", S["body"]))
    story.append(Spacer(1, 8))

    story.append(Paragraph("<b>Track These Fields for Each AI System:</b>", S["bold"]))
    inventory_fields = [
        ("System Name", "Internal identifier"),
        ("Owner/Product Team", "Team responsible for system"),
        ("Risk Classification", "Unacceptable / High / Limited / Minimal"),
        ("Use Case", "What the system does"),
        ("Deployment Status", "Research / Dev / Staging / Production"),
        ("Deployment Date", "When system went live"),
        ("Affected Geographies", "EU / US (which states) / Other"),
        ("Impact Assessment", "Link to document or 'N/A'"),
        ("Last Bias Audit", "Date of most recent audit"),
        ("Technical Docs", "Link to documentation package"),
        ("Human Oversight Model", "In-loop / On-loop / In-command / None"),
        ("Logging Enabled", "Yes / No"),
        ("Next Review Date", "Scheduled re-audit or monitoring review"),
    ]
    for field, desc in inventory_fields:
        story.append(Paragraph(f"• <b>{field}:</b> {desc}", S["bullet"]))

    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "<b>Governance tip:</b> Store this inventory in a shared system (Airtable, Notion, internal wiki) accessible to "
        "Legal, Compliance, Product, and Engineering. Review quarterly. Add new systems as they move from dev to staging.",
        S["body"]
    ))

    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PAGE 8: Incident Response
    # ════════════════════════════════════════════════════════════════
    story.append(Paragraph("AI Incident Response: 5-Step Protocol", S["h2"]))
    story.append(Paragraph("When your AI system fails, discriminates, or causes harm, response speed matters. EU AI Act Article 62 requires reporting serious incidents to regulators within 15 days.", S["body"]))
    story.append(Spacer(1, 8))

    incident_steps = [
        ("1. Detect & Triage (Hour 0-2)",
         "• Log incident with timestamp\n• Assess severity (Critical / High / Medium / Low)\n• Notify AI system owner\n• Preliminary impact assessment (how many users affected?)\n• Critical severity: immediate halt/rollback if ongoing user harm"),

        ("2. Contain & Mitigate (Hour 2-24)",
         "• Decide system status (continue / modify / suspend / shut down)\n• If suspended: notify affected users\n• Preserve logs and evidence (do not delete)\n• Activate human oversight or fallback\n• Brief Legal and Compliance teams"),

        ("3. Investigate Root Cause (Day 1-7)",
         "• Review logs and system behavior\n• Reproduce issue in test environment\n• Identify root cause (model, data, code, process)\n• Document findings in incident report\n• Assess if similar issues exist in other AI systems"),

        ("4. Remediate & Test (Day 7-30)",
         "• Implement fix (retrain, update data, change logic)\n• Re-run bias audit and impact assessment if High Risk\n• Test fix in staging\n• Validate no new issues introduced\n• Update technical documentation"),

        ("5. Redeploy & Monitor (Day 30+)",
         "• Gradual rollout with enhanced monitoring\n• Communicate fix to affected users\n• Report to regulators if required (EU: serious incidents within 15 days)\n• Post-incident review with team\n• Update incident response procedures"),
    ]

    for title, steps in incident_steps:
        story.append(Paragraph(f"<b>{title}</b>", S["h3orange"]))
        story.append(Paragraph(steps, S["bodysmall"]))
        story.append(Spacer(1, 5))

    story.append(Spacer(1, 8))
    story.append(Paragraph(
        '<font color="#ef4444"><b>EU AI Act Reporting:</b></font> Providers of high-risk AI must report serious incidents '
        '(death, serious health issues, fundamental rights violations) to national authorities within 15 days. '
        'Establish your reporting chain now.',
        S["warning"]
    ))

    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PAGE 9: Regulatory Quick Reference
    # ════════════════════════════════════════════════════════════════
    story.append(Paragraph("Regulatory Compliance Quick Reference", S["h2"]))
    story.append(Paragraph("Map your AI system to applicable laws.", S["body"]))
    story.append(Spacer(1, 8))

    # Create table data
    table_data = [
        ["Regulation", "Applies To", "Key Requirement", "Deadline"],
        ["EU AI Act", "High-risk AI in EU market", "Conformity assessment, docs, logging", "Aug 2026 (high-risk)\nMay 2027 (all)"],
        ["Colorado\nSB 24-205", "High-risk AI in Colorado", "Impact assessments, disclosure", "Feb 2026"],
        ["NYC Local\nLaw 144", "Automated hiring tools (NYC)", "Annual bias audit, publish stats", "Effective\nJuly 2023"],
        ["GDPR\nArticle 22", "Automated decisions (EU residents)", "Right to review, explanation", "Active\nsince 2018"],
        ["ECOA", "AI credit decisions (US)", "Adverse action notices, non-discrimination", "Active"],
        ["FDA AI/ML", "AI medical devices (US)", "Premarket review, algorithm change protocol", "Active\n(evolving)"],
    ]

    table = Table(table_data, colWidths=[100, 130, 140, 70])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), DARK_BG),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#64748b")),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(table)

    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "<b>Not sure which applies?</b> Start with geography (where are your users?) and use case (what decisions does your AI make?). "
        "If you're making decisions about people in sensitive areas, assume multiple regulations apply.",
        S["body"]
    ))

    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PAGE 10: CTA / Contact
    # ════════════════════════════════════════════════════════════════
    story.append(Spacer(1, 100))
    story.append(Paragraph("Building AI Systems? Don't Navigate Compliance Alone.", S["center_bold"]))
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "The regulatory landscape is complex and penalties are severe. Whether you need help classifying your AI systems, "
        "running bias audits, building impact assessments, or preparing for EU AI Act compliance, I can help you get it right before launch.",
        S["center"]
    ))
    story.append(Spacer(1, 30))
    story.append(Paragraph(f"<b>{BRAND_NAME}</b>", S["center_bold"]))
    story.append(Paragraph(BRAND_TITLE, S["center_orange"]))
    story.append(Spacer(1, 8))
    story.append(Paragraph(f"<b>Website:</b> {BRAND_WEBSITE}", S["center"]))
    story.append(Paragraph(f"<b>LinkedIn:</b> {BRAND_LINKEDIN}", S["center"]))
    story.append(Paragraph(f"<b>Email:</b> {BRAND_EMAIL}", S["center"]))
    story.append(Paragraph(f"<b>Services:</b> {BRAND_WEBSITE}/agency", S["center"]))

    # ── Build ───────────────────────────────────────────────────────
    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    print(f"PDF generated: {OUTPUT_PATH}")


if __name__ == "__main__":
    build_pdf()
