#!/usr/bin/env python3
"""
Generate the AI Tool Governance Pipeline PDF.
Uses reportlab to create a branded PDF with the complete lifecycle framework.
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
PURPLE_ACCENT = HexColor("#7C3AED")  # purple-600
LIGHT_TEXT = HexColor("#cbd5e1")     # slate-300
DARK_TEXT = HexColor("#1e293b")
WHITE = white
MEDIUM_TEXT = HexColor("#64748b")    # slate-500
GREEN = HexColor("#059669")
YELLOW = HexColor("#eab308")
ORANGE = HexColor("#D97706")
RED = HexColor("#ef4444")

OUTPUT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "downloads", "ai-tool-governance-pipeline.pdf")
HERO_IMG = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "images", "resources", "governance-pipeline.png")

# ── Page Template ───────────────────────────────────────────────────
def header_footer(canvas, doc):
    """Draw header and footer on every page."""
    width, height = letter
    page_num = canvas.getPageNumber()

    # Header background
    canvas.setFillColor(DARK_BG)
    canvas.rect(0, height - 50, width, 50, fill=1, stroke=0)

    # Purple accent line under header
    canvas.setFillColor(PURPLE_ACCENT)
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
    s["title"] = ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=26, leading=32, textColor=DARK_TEXT, spaceAfter=10)
    s["subtitle"] = ParagraphStyle("subtitle", fontName="Helvetica", fontSize=12, leading=17, textColor=MEDIUM_TEXT, spaceAfter=8)
    s["h2"] = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=20, leading=26, textColor=DARK_TEXT, spaceAfter=10, spaceBefore=4)
    s["h3"] = ParagraphStyle("h3", fontName="Helvetica-Bold", fontSize=13, leading=17, textColor=DARK_TEXT, spaceAfter=6, spaceBefore=8)
    s["h3purple"] = ParagraphStyle("h3purple", fontName="Helvetica-Bold", fontSize=13, leading=17, textColor=PURPLE_ACCENT, spaceAfter=6, spaceBefore=8)
    s["body"] = ParagraphStyle("body", fontName="Helvetica", fontSize=10, leading=14, textColor=DARK_TEXT, spaceAfter=6)
    s["bodysmall"] = ParagraphStyle("bodysmall", fontName="Helvetica", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=4)
    s["bold"] = ParagraphStyle("bold", fontName="Helvetica-Bold", fontSize=10, leading=14, textColor=DARK_TEXT, spaceAfter=4)
    s["bullet"] = ParagraphStyle("bullet", fontName="Helvetica", fontSize=9.5, leading=14, textColor=DARK_TEXT, spaceAfter=2, leftIndent=18, bulletIndent=6)
    s["section_badge"] = ParagraphStyle("section_badge", fontName="Helvetica-Bold", fontSize=10, leading=14, textColor=WHITE, spaceAfter=0)
    s["center"] = ParagraphStyle("center", fontName="Helvetica", fontSize=10, leading=15, textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=6)
    s["center_bold"] = ParagraphStyle("center_bold", fontName="Helvetica-Bold", fontSize=16, leading=22, textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=4)
    s["center_purple"] = ParagraphStyle("center_purple", fontName="Helvetica-Bold", fontSize=12, leading=16, textColor=PURPLE_ACCENT, alignment=TA_CENTER, spaceAfter=8)
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
    story.append(Paragraph("AI Tool Governance Pipeline", S["title"]))
    story.append(Spacer(1, 6))
    story.append(Paragraph("Complete Lifecycle Framework: From Chaos to Optimization", S["subtitle"]))
    story.append(Spacer(1, 12))

    # Hero infographic
    if os.path.exists(HERO_IMG):
        img_width = 540
        img_height = img_width * 9 / 16
        story.append(Image(HERO_IMG, width=img_width, height=img_height))

    story.append(Spacer(1, 14))
    story.append(Paragraph(f"<b>{BRAND_NAME}</b>", ParagraphStyle("author", fontName="Helvetica-Bold", fontSize=14, leading=18, textColor=DARK_TEXT)))
    story.append(Paragraph(BRAND_TITLE, ParagraphStyle("authortitle", fontName="Helvetica", fontSize=11, leading=15, textColor=PURPLE_ACCENT, spaceAfter=4)))
    story.append(Paragraph("Maturity model, readiness assessment, KPIs, decision trees, and workshop guide", S["bodysmall"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph(f"{BRAND_WEBSITE}  |  {BRAND_LINKEDIN}  |  {BRAND_EMAIL}", S["bodysmall"]))
    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PAGE 2: Overview
    # ════════════════════════════════════════════════════════════════
    story.append(Paragraph("The Complete Governance Journey", S["h2"]))
    story.append(Paragraph(
        "Most organizations jump straight to implementation and wonder why governance fails. The ones that succeed follow this complete four-phase cycle.",
        S["body"]
    ))
    story.append(Spacer(1, 10))

    phases = [
        ("Phase 1: Assessment", "Pre-Week 1", "Maturity model, readiness checklist, stakeholder mapping"),
        ("Phase 2: Implementation", "Week 1-3", "Discovery, approved toolkit, deployment (see Shadow AI Toolkit)"),
        ("Phase 3: Operationalization", "Month 2-6", "KPIs, monthly reviews, feedback loops, cost optimization"),
        ("Phase 4: Optimization", "Ongoing", "Quarterly reviews, champions program, continuous improvement"),
    ]
    for title, timeline, desc in phases:
        story.append(Paragraph(f"<b>{title}</b> ({timeline})", S["h3purple"]))
        story.append(Paragraph(desc, S["body"]))
        story.append(Spacer(1, 4))

    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PAGE 3: Governance Maturity Model
    # ════════════════════════════════════════════════════════════════
    story.append(Paragraph("AI Tool Governance Maturity Model", S["h2"]))
    story.append(Paragraph("Find your current level, then use the recommended actions to move up.", S["body"]))
    story.append(Spacer(1, 10))

    maturity = [
        ("LEVEL 0: Chaos", RED, [
            "Zero visibility into AI tool usage",
            "No policies, no approved tools, no security controls",
            "IT discovers AI through expense reports or incidents"
        ], "→ Start with Shadow AI amnesty audit"),
        ("LEVEL 1: Reactive", ORANGE, [
            "Aware of shadow AI problem",
            "'Don't use ChatGPT' policy that nobody follows",
            "No approved alternatives provided"
        ], "→ Approved toolkit selection + amnesty program"),
        ("LEVEL 2: Managed", YELLOW, [
            "Approved AI tools in place",
            "Data classification policy exists (Green/Yellow/Red)",
            "DLP rules configured and monitoring"
        ], "→ Adoption metrics + quarterly tool evaluation"),
        ("LEVEL 3: Measured", GREEN, [
            "Tracking adoption, ROI, and compliance",
            "Feedback loops operational",
            "Champions program active"
        ], "→ Advanced use case enablement"),
        ("LEVEL 4: Optimized", BLUE_ACCENT, [
            "AI governance integrated into IT governance",
            "Continuous improvement culture",
            "Predictive cost management"
        ], "→ Publish best practices externally"),
    ]

    for level, color, chars, action in maturity:
        story.append(Paragraph(f'<font color="{color.hexval()}" size="11"><b>{level}</b></font>', S["bold"]))
        for char in chars:
            story.append(Paragraph(f"• {char}", S["bullet"]))
        story.append(Paragraph(f"<i>{action}</i>", S["bodysmall"]))
        story.append(Spacer(1, 6))

    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PAGE 4: Readiness Checklist
    # ════════════════════════════════════════════════════════════════
    story.append(Paragraph("Organizational Readiness Checklist", S["h2"]))
    story.append(Paragraph("Use this to identify blockers before you start. Four or more 'No' answers means you need executive alignment first.", S["body"]))
    story.append(Spacer(1, 8))

    checklist = [
        ("Executive sponsorship secured", "VP+ level champion with budget authority"),
        ("IT and Security aligned", "CIO/CISO on board with approved tool approach"),
        ("Budget allocated", "$20-50/user/month for enterprise AI tools"),
        ("Training capacity available", "2hr manager + 1hr IC training for entire org"),
        ("DLP/monitoring infrastructure exists", "Purview, Symantec, Forcepoint, or similar"),
        ("Compliance requirements documented", "Know which regulations apply (GDPR, HIPAA, SOC 2, etc.)"),
        ("Change management support available", "Resource for comms, training, adoption campaigns"),
    ]
    for title, desc in checklist:
        story.append(Paragraph(f"□ <b>{title}</b>", S["bold"]))
        story.append(Paragraph(desc, S["bodysmall"]))
        story.append(Spacer(1, 3))

    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PAGE 5: 6 KPIs to Track
    # ════════════════════════════════════════════════════════════════
    story.append(Paragraph("6 KPIs to Track (Month 2-6)", S["h2"]))
    story.append(Paragraph("Don't track everything. Track these six metrics and you'll catch 95% of problems early.", S["body"]))
    story.append(Spacer(1, 8))

    kpis = [
        ("Tool Adoption Rate", "% of employees who logged in last 30 days", "Target: 70%+ by Month 3"),
        ("DLP Incident Rate", "DLP flags per 1,000 employees per month", "Target: <5 by Month 4 (trending down)"),
        ("Cost Per Active User", "Total spend ÷ active users", "Target: Trending down as you consolidate"),
        ("Time Saved (Self-Reported)", "Avg hours saved per week via quarterly survey", "Target: 3+ hours/week/user"),
        ("Exception Request Volume", "Requests for non-approved tools per month", "Target: <10/month"),
        ("User Satisfaction Score", "1-10 rating via quarterly pulse survey", "Target: 7+ average"),
    ]
    for name, definition, target in kpis:
        story.append(Paragraph(f"<b>{name}</b>", S["h3purple"]))
        story.append(Paragraph(definition, S["body"]))
        story.append(Paragraph(f"<i>{target}</i>", S["bodysmall"]))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Monthly review agenda:</b> 30 minutes. Same time every month. Don't skip it.", S["bold"]))
    story.append(Paragraph("• 5 min: KPI dashboard review", S["bullet"]))
    story.append(Paragraph("• 5 min: DLP incident summary", S["bullet"]))
    story.append(Paragraph("• 10 min: Exception requests & user feedback", S["bullet"]))
    story.append(Paragraph("• 5 min: Cost analysis", S["bullet"]))
    story.append(Paragraph("• 5 min: Action items", S["bullet"]))

    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PAGE 6: Decision Trees
    # ════════════════════════════════════════════════════════════════
    story.append(Paragraph("Decision Framework: Can I Use This AI Tool?", S["h2"]))
    story.append(Paragraph("Print this. Make it accessible. Answers the most common governance question.", S["body"]))
    story.append(Spacer(1, 8))

    decision_steps = [
        ("1. Is it on the approved toolkit list?", "YES → Use it freely for Green/Yellow data", "NO → Continue to step 2"),
        ("2. Does an approved tool already cover this use case?", "YES → Use the approved alternative instead", "NO → Continue to step 3"),
        ("3. Will you only use it with Green data (public info)?", "YES → Proceed (but report usage to IT quarterly)", "NO → Continue to step 4"),
        ("4. Is this a one-time need or recurring?", "ONE-TIME → Submit exception request to your manager", "RECURRING → Submit new tool request with business case"),
    ]
    for question, yes_path, no_path in decision_steps:
        story.append(Paragraph(f"<b>{question}</b>", S["bold"]))
        story.append(Paragraph(yes_path, S["body"]))
        story.append(Paragraph(no_path, S["bodysmall"]))
        story.append(Spacer(1, 6))

    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PAGE 7: Champions Program
    # ════════════════════════════════════════════════════════════════
    story.append(Paragraph("AI Champions Program Structure", S["h2"]))
    story.append(Paragraph("Once governance is operational, shift from top-down enforcement to bottom-up enablement. Champions make this sustainable.", S["body"]))
    story.append(Spacer(1, 8))

    story.append(Paragraph("<b>What Champions Do:</b>", S["bold"]))
    champ_do = [
        "First point of contact for team questions about approved tools",
        "Share best practices and use case examples",
        "Surface feedback to governance team monthly",
        "Pilot new tools before broader rollout"
    ]
    for item in champ_do:
        story.append(Paragraph(f"• {item}", S["bullet"]))

    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>How to Select Champions:</b>", S["bold"]))
    champ_select = [
        "High engagement with approved tools (top 10% users)",
        "Respected by their teams (not necessarily senior)",
        "Volunteered during initial rollout",
        "One per department minimum (scale to 1 per 20 employees)"
    ]
    for item in champ_select:
        story.append(Paragraph(f"• {item}", S["bullet"]))

    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "<b>Time commitment:</b> 2 hours per month. 1-hour monthly champion sync call + 1 hour answering team questions. "
        "Recognize them—profile in company newsletter, annual award, resume/LinkedIn fodder.",
        S["body"]
    ))

    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PAGE 8: Workshop Facilitation Guide
    # ════════════════════════════════════════════════════════════════
    story.append(Paragraph("2-Hour AI Readiness Workshop Agenda", S["h2"]))
    story.append(Paragraph("Use this framework to run workshops with clients, leadership teams, or cross-functional stakeholders.", S["body"]))
    story.append(Spacer(1, 8))

    workshop = [
        ("0:00-0:15", "Opening: Why This Matters Now", "Set stage with real data: 75% of employees use AI, 78% use non-approved tools, $200K+ breach costs"),
        ("0:15-0:45", "Interactive: Maturity Assessment", "Walk through maturity model. Plot the organization's current state together. No shame—just facts."),
        ("0:45-1:05", "Breakout: Stakeholder Mapping", "Small groups assigned phases. Each uses RACI matrix to assign roles."),
        ("1:05-1:30", "Interactive: Readiness Checklist", "Go through checklist line by line. Vote: Yes/Partial/No. Assign owners for gaps."),
        ("1:30-1:50", "Planning: Next Steps & Timeline", "Build 90-day roadmap together with specific milestones based on maturity level."),
        ("1:50-2:00", "Closing: Commitment & Questions", "Each attendee commits to one action. Schedule 30-day check-in."),
    ]
    for time, section, desc in workshop:
        story.append(Paragraph(f"<b>{time}: {section}</b>", S["h3purple"]))
        story.append(Paragraph(desc, S["body"]))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "<b>Workshop tip:</b> Print the Maturity Model, Readiness Checklist, and RACI Matrix as handouts. "
        "Make the workshop tactile—people remember what they write down more than what they hear.",
        S["body"]
    ))

    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PAGE 9: CTA / Contact
    # ════════════════════════════════════════════════════════════════
    story.append(Spacer(1, 100))
    story.append(Paragraph("Ready to Build Your Governance Pipeline?", S["center_bold"]))
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "This framework has helped organizations from 50 to 5,000 employees move from chaos to optimized AI governance. "
        "Whether you need help running the assessment workshop, selecting tools, or building sustainable governance, I can guide you through it.",
        S["center"]
    ))
    story.append(Spacer(1, 30))
    story.append(Paragraph(f"<b>{BRAND_NAME}</b>", S["center_bold"]))
    story.append(Paragraph(BRAND_TITLE, S["center_purple"]))
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
