#!/usr/bin/env python3
"""
Generate the Shadow AI Governance Toolkit PDF.
Uses reportlab to create a branded 12-page PDF matching the website content.
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
LIGHT_TEXT = HexColor("#cbd5e1")     # slate-300
DARK_TEXT = HexColor("#1e293b")
WHITE = white
MEDIUM_TEXT = HexColor("#64748b")    # slate-500
GREEN = HexColor("#22c55e")
YELLOW = HexColor("#eab308")
RED = HexColor("#ef4444")
SECTION_NUM = HexColor("#3b82f6")

OUTPUT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "downloads", "shadow-ai-governance-toolkit.pdf")
ROADMAP_IMG = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "images", "shadow-ai-governance-roadmap.png")

# ── Page Template ───────────────────────────────────────────────────
def header_footer(canvas, doc):
    """Draw header and footer on every page."""
    width, height = letter
    page_num = canvas.getPageNumber()

    # Header background
    canvas.setFillColor(DARK_BG)
    canvas.rect(0, height - 50, width, 50, fill=1, stroke=0)

    # Blue accent line under header
    canvas.setFillColor(BLUE_ACCENT)
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
    s["title"] = ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=28, leading=34, textColor=DARK_TEXT, spaceAfter=12)
    s["subtitle"] = ParagraphStyle("subtitle", fontName="Helvetica", fontSize=13, leading=18, textColor=MEDIUM_TEXT, spaceAfter=8)
    s["h2"] = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=22, leading=28, textColor=DARK_TEXT, spaceAfter=10, spaceBefore=4)
    s["h3"] = ParagraphStyle("h3", fontName="Helvetica-Bold", fontSize=14, leading=18, textColor=DARK_TEXT, spaceAfter=6, spaceBefore=8)
    s["h3blue"] = ParagraphStyle("h3blue", fontName="Helvetica-Bold", fontSize=14, leading=18, textColor=BLUE_ACCENT, spaceAfter=6, spaceBefore=8)
    s["body"] = ParagraphStyle("body", fontName="Helvetica", fontSize=10, leading=15, textColor=DARK_TEXT, spaceAfter=6)
    s["bodysmall"] = ParagraphStyle("bodysmall", fontName="Helvetica", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=4)
    s["italic"] = ParagraphStyle("italic", fontName="Helvetica-Oblique", fontSize=10, leading=15, textColor=MEDIUM_TEXT, spaceAfter=6, leftIndent=18, rightIndent=18)
    s["bold"] = ParagraphStyle("bold", fontName="Helvetica-Bold", fontSize=10, leading=15, textColor=DARK_TEXT, spaceAfter=4)
    s["mono"] = ParagraphStyle("mono", fontName="Courier", fontSize=8, leading=12, textColor=MEDIUM_TEXT, spaceAfter=2, leftIndent=18)
    s["bullet"] = ParagraphStyle("bullet", fontName="Helvetica", fontSize=10, leading=15, textColor=DARK_TEXT, spaceAfter=3, leftIndent=18, bulletIndent=6)
    s["section_num"] = ParagraphStyle("section_num", fontName="Helvetica-Bold", fontSize=36, leading=40, textColor=BLUE_ACCENT, spaceAfter=0)
    s["center"] = ParagraphStyle("center", fontName="Helvetica", fontSize=10, leading=15, textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=6)
    s["center_bold"] = ParagraphStyle("center_bold", fontName="Helvetica-Bold", fontSize=16, leading=22, textColor=DARK_TEXT, alignment=TA_CENTER, spaceAfter=4)
    s["center_blue"] = ParagraphStyle("center_blue", fontName="Helvetica-Bold", fontSize=12, leading=16, textColor=BLUE_ACCENT, alignment=TA_CENTER, spaceAfter=8)
    s["green_header"] = ParagraphStyle("green_header", fontName="Helvetica-Bold", fontSize=13, leading=17, textColor=GREEN, spaceAfter=6)
    s["yellow_header"] = ParagraphStyle("yellow_header", fontName="Helvetica-Bold", fontSize=13, leading=17, textColor=YELLOW, spaceAfter=6)
    s["red_header"] = ParagraphStyle("red_header", fontName="Helvetica-Bold", fontSize=13, leading=17, textColor=RED, spaceAfter=6)
    s["blue_header"] = ParagraphStyle("blue_header", fontName="Helvetica-Bold", fontSize=13, leading=17, textColor=BLUE_ACCENT, spaceAfter=6)
    s["tip"] = ParagraphStyle("tip", fontName="Helvetica-Bold", fontSize=10, leading=15, textColor=DARK_TEXT, spaceAfter=4, spaceBefore=8)
    s["toc_item"] = ParagraphStyle("toc_item", fontName="Helvetica-Bold", fontSize=11, leading=16, textColor=DARK_TEXT, spaceAfter=1)
    s["toc_desc"] = ParagraphStyle("toc_desc", fontName="Helvetica", fontSize=9, leading=13, textColor=MEDIUM_TEXT, spaceAfter=10, leftIndent=0)
    s["rule_title"] = ParagraphStyle("rule_title", fontName="Helvetica-Bold", fontSize=11, leading=15, textColor=DARK_TEXT, spaceAfter=3, spaceBefore=10)
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
    story.append(Spacer(1, 30))
    story.append(Paragraph("Shadow AI<br/>Governance Toolkit", S["title"]))
    story.append(Spacer(1, 8))
    story.append(Paragraph("The complete framework to map, manage, and govern shadow AI usage.<br/>7 templates. 3-week deployment. Proven across organizations.", S["subtitle"]))
    story.append(Spacer(1, 16))

    # Roadmap infographic
    if os.path.exists(ROADMAP_IMG):
        img_width = 540  # full available width (letter - 36pt margins each side)
        img_height = img_width * 9 / 16  # maintain ~16:9 aspect ratio
        story.append(Image(ROADMAP_IMG, width=img_width, height=img_height))

    story.append(Spacer(1, 16))
    story.append(Paragraph(f"<b>{BRAND_NAME}</b>", ParagraphStyle("author", fontName="Helvetica-Bold", fontSize=14, leading=18, textColor=DARK_TEXT)))
    story.append(Paragraph(BRAND_TITLE, ParagraphStyle("authortitle", fontName="Helvetica", fontSize=11, leading=15, textColor=BLUE_ACCENT, spaceAfter=4)))
    story.append(Paragraph("23+ years in technology | 10+ years Fortune 500 consulting", S["bodysmall"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph(f"{BRAND_WEBSITE}  |  {BRAND_LINKEDIN}  |  {BRAND_EMAIL}", S["bodysmall"]))
    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PAGE 2: Table of Contents
    # ════════════════════════════════════════════════════════════════
    story.append(Spacer(1, 20))
    story.append(Paragraph("What's Inside", S["h2"]))
    story.append(Spacer(1, 12))

    toc = [
        ("1", "Shadow AI Amnesty Audit Template", "Employee disclosure form for Week 1"),
        ("2", "IT Discovery Checklist", "Network log domains, extension audit, finance search terms"),
        ("3", "Approved AI Toolkit Matrix", "5 use cases with ranked recommendations and evaluation checklists"),
        ("4", "Data Classification Policy", "Green / Yellow / Red system for AI data handling"),
        ("5", "DLP Rules for AI Traffic", "4 pre-configured rules for your DLP system"),
        ("6", "Training Session Outlines", "Manager (2hr) and IC (1hr) agendas"),
        ("7", "Rollout Communication Scripts", "Week 1/2/3 copy-paste announcements"),
    ]
    for num, title, desc in toc:
        story.append(Paragraph(f'<font color="#3b82f6" size="18"><b>{num}.</b></font>  <font size="12"><b>{title}</b></font>', S["toc_item"]))
        story.append(Paragraph(desc, S["toc_desc"]))

    story.append(Spacer(1, 4))
    story.append(Paragraph('<font color="#3b82f6" size="18"><b>+</b></font>  <font size="12"><b>3-Week Deployment Timeline</b></font>', S["toc_item"]))
    story.append(Paragraph("Day-by-day implementation schedule", S["toc_desc"]))
    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PAGE 3: Template 1 - Amnesty Audit
    # ════════════════════════════════════════════════════════════════
    story.append(Paragraph('<font color="#3b82f6">1</font>', S["section_num"]))
    story.append(Paragraph("Shadow AI Amnesty Audit Template", S["h2"]))
    story.append(Paragraph("Send this to all employees during Week 1. The amnesty framing is critical -- punitive language kills participation.", S["body"]))
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "We're building an AI toolkit for the company. To make sure we choose the right tools, we need to understand what's already working. "
        "This is a no-penalty disclosure -- we want to learn from your experience, not restrict it.",
        S["italic"]
    ))
    story.append(Spacer(1, 8))

    questions = [
        ("1. What AI tools do you currently use for work?", "(List all tools (ChatGPT, Claude, Copilot, Midjourney, browser extensions, etc.))"),
        ("2. What tasks do you use them for?", "(Content writing, code review, data analysis, research, email drafting, meeting notes, etc.)"),
        ("3. How often do you use each tool?", "(Daily / Several times per week / Weekly / Occasionally)"),
        ("4. Are you using a personal account or company account?", None),
        ("5. Roughly how much time does this save you per week?", None),
        ("6. What types of data do you typically share with AI tools?", "(Public info / Internal docs / Customer data / Source code / Financial data)"),
        ("7. What AI tool do you wish the company officially supported?", None),
    ]
    for q, hint in questions:
        story.append(Paragraph(f"<b>{q}</b>", S["body"]))
        if hint:
            story.append(Paragraph(f"<i>{hint}</i>", S["bodysmall"]))
        story.append(Spacer(1, 4))
    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PAGE 4: Template 2 - IT Discovery
    # ════════════════════════════════════════════════════════════════
    story.append(Paragraph('<font color="#3b82f6">2</font>', S["section_num"]))
    story.append(Paragraph("IT Discovery Checklist", S["h2"]))
    story.append(Paragraph("Run this in parallel with the amnesty audit. Employees won't report everything -- network logs fill the gaps.", S["body"]))
    story.append(Spacer(1, 8))

    story.append(Paragraph("<b>Proxy/Firewall Log Domains to Search:</b>", S["body"]))
    domains = [
        ("*.openai.com", "ChatGPT, DALL-E, API"),
        ("*.anthropic.com", "Claude"),
        ("*.google.com/ai*", "Gemini"),
        ("*.cohere.ai", "Cohere models"),
        ("*.huggingface.co", "Open-source models"),
        ("*.replicate.com", "Model hosting"),
        ("*.midjourney.com", "Image generation"),
        ("*.perplexity.ai", "AI search"),
        ("*.jasper.ai", "AI writing"),
        ("*.copy.ai", "AI copywriting"),
        ("*.cursor.sh", "AI code editor"),
        ("*.replit.com", "AI code assistant"),
        ("*.otter.ai", "Meeting transcription"),
        ("*.fireflies.ai", "Meeting transcription"),
    ]
    for domain, desc in domains:
        story.append(Paragraph(f"{domain}  -- {desc}", S["mono"]))
    story.append(Spacer(1, 10))

    story.append(Paragraph("<b>Browser Extension Audit Keywords:</b>", S["body"]))
    story.append(Paragraph("Search managed browser extension lists for: <b>AI, GPT, assistant, copilot, writer, summarize, transcribe</b>", S["body"]))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Finance Audit:</b>", S["body"]))
    story.append(Paragraph("Pull expense reports and corporate card transactions containing: <b>OpenAI, Anthropic, Jasper, Copy.ai, Midjourney, Otter, Fireflies, Cursor, Replit, Perplexity</b>", S["body"]))
    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PAGE 5: Template 3 - Approved AI Toolkit Matrix
    # ════════════════════════════════════════════════════════════════
    story.append(Paragraph('<font color="#3b82f6">3</font>', S["section_num"]))
    story.append(Paragraph("Approved AI Toolkit Matrix", S["h2"]))
    story.append(Paragraph("The goal is to cover 80% of use cases with 5 or fewer tools. Consolidating tools reduces cost, simplifies security, and makes training easier.", S["body"]))
    story.append(Spacer(1, 8))

    tools = [
        ("General AI Assistant", "FOUNDATION TOOL",
         "Recommended (in order): 1. Claude Team, 2. Gemini Business, 3. ChatGPT Team, 4. M365 Copilot, 5. Local open-source",
         "SOC 2 compliant on Team/Business plans. No training on your data. This is your most important choice -- it will also serve as your document analysis and potentially image generation tool.",
         "Every business is different. Your industry, existing tech stack, compliance requirements, and team size all affect which tool is the best fit. See the General AI Assistant Checklist to evaluate your options."),
        ("Code Assistant", "DEV TEAMS ONLY",
         "Recommended (in order): 1. Claude Code, 2. Codex, 3. GitHub Copilot, 4. Cursor Team",
         "Price is the biggest variable. Costs range from usage-based to $40+/user/month depending on tool and plan. No code sent to third parties on enterprise plans, local processing available on some.",
         "Every business is different. Your language stack, repo size, security posture, and budget all matter. Pricing models vary significantly. See the Code Assistant Checklist to figure out which fits your team."),
        ("Document Analysis", "REUSE OPPORTUNITY",
         "Recommended (in order): 1. Your General AI Assistant, 2. Perplexity Pro",
         "Keep your tool count low. Whichever General AI Assistant you chose above likely handles document analysis well. Perplexity adds source citations for research-heavy workflows. Every new tool is another license, security review, and training session.",
         "Every business is different. Your document types, compliance needs, and volume should drive this decision. See the Document Analysis Checklist to evaluate whether you need a dedicated tool."),
        ("Image Generation", "REUSE OPPORTUNITY",
         "Recommended (in order): 1. Your General AI Assistant (ChatGPT or Gemini), 2. MidJourney, 3. Gemini",
         "Reuse first. ChatGPT and Gemini both have image generation built in. If your team needs higher-fidelity creative output, MidJourney is the next step. Commercial usage rights on all recommended options.",
         "Every business is different. Your creative volume, brand guidelines, and quality bar all affect this choice. See the Image Generation Checklist to decide if built-in is enough."),
        ("Meeting Transcription", "CHECK EXISTING TOOLS",
         "Recommended (in order): 1. Your existing meeting platform, 2. Your General AI Assistant, 3. Otter.ai Business, 4. Fireflies.ai",
         "Check what you already have first. Zoom, Teams, and Google Meet all have built-in AI transcription now. Only add a dedicated tool if your existing stack falls short. Critical: validate the Enterprise Data Protection policy of any transcription tool -- meetings often contain sensitive data.",
         "Every business is different. Your meeting platform, recording policies, and data sensitivity should guide this choice. See the Meeting Transcription Checklist to audit what you already have."),
    ]
    for name, badge, rec, desc, note in tools:
        story.append(Paragraph(f"<b>{name}</b>  <font size='7' color='#64748b'>{badge}</font>", S["h3"]))
        story.append(Paragraph(f"<b>{rec}</b>", S["bodysmall"]))
        story.append(Paragraph(desc, S["body"]))
        story.append(Paragraph(f"<i>{note}</i>", S["bodysmall"]))
        story.append(Spacer(1, 6))

    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PAGE 6: 80% Rule + Negotiation Tip
    # ════════════════════════════════════════════════════════════════
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "<b>The 80% rule:</b> These 5 use cases cover the vast majority of what your team needs. "
        "There are hundreds of AI tools on the market, but every tool you add is another license, security review, and training burden. "
        "Start here, measure adoption, and expand deliberately. Review the Use Case Checklists if you want to dive deeper into any category.",
        S["body"]
    ))
    story.append(Spacer(1, 12))
    story.append(Paragraph(
        "<b>Negotiation tip:</b> Contact vendors directly and reference that you're consolidating from multiple individual accounts to one enterprise agreement. Most will offer annual discounts of 40-60%.",
        S["body"]
    ))
    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PAGE 7: Template 4 - Data Classification
    # ════════════════════════════════════════════════════════════════
    story.append(Paragraph('<font color="#3b82f6">4</font>', S["section_num"]))
    story.append(Paragraph("Data Classification Policy for AI Usage", S["h2"]))
    story.append(Paragraph("Print this. Hang it in every team area. Three colors, three rules.", S["body"]))
    story.append(Spacer(1, 10))

    # Green
    story.append(Paragraph("GREEN -- Use Freely", S["green_header"]))
    for item in ["Public information", "Marketing copy and blog drafts", "General research questions",
                  "Code from open-source projects", "Meeting agenda planning", "Email drafting (non-sensitive)"]:
        story.append(Paragraph(f"\u2022 {item}", S["bullet"]))
    story.append(Paragraph("<b>Rule:</b> Any approved tool. No restrictions.", S["bodysmall"]))
    story.append(Spacer(1, 10))

    # Yellow
    story.append(Paragraph("YELLOW -- Business Tools Only", S["yellow_header"]))
    for item in ["Internal process documentation", "Non-sensitive business data", "Aggregated (anonymized) metrics",
                  "Internal presentations", "Product feature brainstorming", "Competitive analysis"]:
        story.append(Paragraph(f"\u2022 {item}", S["bullet"]))
    story.append(Paragraph("<b>Rule:</b> Enterprise-grade tools only (Team/Business plans). No personal accounts.", S["bodysmall"]))
    story.append(Spacer(1, 10))

    # Red
    story.append(Paragraph("RED -- Approval Required", S["red_header"]))
    for item in ["Customer PII or data", "Financial records", "Strategic plans and roadmaps",
                  "Proprietary source code", "Legal documents", "Employee records"]:
        story.append(Paragraph(f"\u2022 {item}", S["bullet"]))
    story.append(Paragraph("<b>Rule:</b> Written approval from department head + IT. Full audit trail required.", S["bodysmall"]))
    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PAGE 8: Template 5 - DLP Rules
    # ════════════════════════════════════════════════════════════════
    story.append(Paragraph('<font color="#3b82f6">5</font>', S["section_num"]))
    story.append(Paragraph("DLP Rules for AI Traffic", S["h2"]))
    story.append(Paragraph("Configure these in your existing DLP system (Microsoft Purview, Symantec, Forcepoint, etc.). Flag first, block later. Blocking on day one creates workarounds.", S["body"]))
    story.append(Spacer(1, 8))

    dlp_rules = [
        ("Rule 1: PII Detection on AI Domains",
         "SSN patterns (XXX-XX-XXXX), credit card numbers (16-digit), email addresses in bulk (10+)",
         "Flag + notify security team. Do not block.",
         "All AI-related domains from the discovery checklist"),
        ("Rule 2: Source Code Exfiltration",
         "Files with extensions .py, .js, .ts, .java, .go, .rb sent to non-approved AI domains",
         "Block + notify both user and IT",
         "Exception: Approved code assistants (GitHub Copilot, Cursor Team)"),
        ("Rule 3: Confidential Document Upload",
         'Documents containing "Confidential," "Internal Only," or "Restricted" in headers/footers',
         "Block + redirect to policy page explaining approved alternatives",
         None),
        ("Rule 4: Bulk Data Transfer",
         "CSV, XLSX, JSON files over 1MB sent to any AI endpoint",
         "Flag + require manager approval within 24 hours",
         None),
    ]
    for title, trigger, action, scope in dlp_rules:
        story.append(Paragraph(f"<b>{title}</b>", S["rule_title"]))
        story.append(Paragraph(f"<b>Trigger:</b> {trigger}", S["body"]))
        story.append(Paragraph(f"<b>Action:</b> {action}", S["body"]))
        if scope:
            story.append(Paragraph(f"<b>Scope:</b> {scope}", S["body"]))
        story.append(Spacer(1, 4))
    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PAGE 9: Template 6 - Training Outlines
    # ════════════════════════════════════════════════════════════════
    story.append(Paragraph('<font color="#3b82f6">6</font>', S["section_num"]))
    story.append(Paragraph("Training Session Outlines", S["h2"]))
    story.append(Paragraph("Two sessions cover the entire organization. Run the manager session first.", S["body"]))
    story.append(Spacer(1, 8))

    story.append(Paragraph("Manager Training -- 2 hours", S["blue_header"]))
    mgr_items = [
        ("1. Why shadow AI happens (15 min)", "Employees trying to be productive, not malicious. Show the 75%/78% stats."),
        ("2. The real risks (20 min)", "Data leaks, compliance fines, IP exposure. Use the $200K breach cost stat."),
        ("3. How to spot shadow AI (15 min)", "Sudden productivity jumps, new expenses, unfamiliar browser extensions."),
        ("4. Response framework (20 min)", "Educate, don't punish. Redirect to approved tools. Escalate only for Red data."),
        ("5. Approved toolkit walkthrough (30 min)", "Live demo of each approved tool. Show managers how to use them first."),
        ("6. Q&A + scenarios (20 min)", 'Walk through 5 real scenarios. "What do you do when..." format.'),
    ]
    for title, desc in mgr_items:
        story.append(Paragraph(f"<b>{title}</b>", S["body"]))
        story.append(Paragraph(desc, S["bodysmall"]))

    story.append(Spacer(1, 12))
    story.append(Paragraph("Individual Contributor Training -- 1 hour", S["blue_header"]))
    ic_items = [
        ("1. Your approved tools (15 min)", "Here's what you have access to. Here's how to get accounts set up."),
        ("2. Getting the most out of them (15 min)", "Top 5 prompts per tool for your department. Live examples."),
        ("3. The Green/Yellow/Red system (10 min)", "What data goes where. When in doubt, ask. No penalties for asking."),
        ("4. What NOT to do (10 min)", "No customer data in personal accounts. No confidential docs. No shadow extensions."),
        ("5. Who to contact + Q&A (10 min)", "AI help desk contact. How to request new tools. Feedback channel."),
    ]
    for title, desc in ic_items:
        story.append(Paragraph(f"<b>{title}</b>", S["body"]))
        story.append(Paragraph(desc, S["bodysmall"]))
    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PAGE 10: Template 7 - Rollout Scripts
    # ════════════════════════════════════════════════════════════════
    story.append(Paragraph('<font color="#3b82f6">7</font>', S["section_num"]))
    story.append(Paragraph("Rollout Communication Scripts", S["h2"]))
    story.append(Paragraph("Copy, customize, send. Tone matters -- these build buy-in, not compliance fear.", S["body"]))
    story.append(Spacer(1, 8))

    story.append(Paragraph("Week 1: Amnesty Announcement", S["blue_header"]))
    week1 = [
        '"Team -- we\'re going all-in on AI. Not banning it. Embracing it."',
        '"Over the next three weeks, we\'re building an official AI toolkit that gives everyone access to powerful, secure AI tools. To make sure we pick the right ones, I need your help."',
        '"Starting today, we\'re running a two-week AI usage survey. This is a no-penalty disclosure. I don\'t care what you\'ve been using -- I care about what\'s been working. Your input directly shapes which tools we officially support."',
        '"Please fill out the survey by [DATE]. The more honest you are, the better your toolkit will be."',
    ]
    for line in week1:
        story.append(Paragraph(line, S["italic"]))

    story.append(Spacer(1, 8))
    story.append(Paragraph("Week 2: Toolkit Announcement", S["blue_header"]))
    week2 = [
        '"Thanks to everyone who participated in the AI survey. We heard you."',
        '"Based on your feedback and our security review, here are the official AI tools now available to the entire team: [LIST TOOLS]. Accounts are being provisioned this week -- you\'ll get setup instructions by [DATE]."',
        '"These tools cover the use cases you told us about. They\'re enterprise-grade, meaning your data stays private and we maintain compliance. If you need something not on the list, there\'s a request process -- we\'ll evaluate new tools quarterly."',
    ]
    for line in week2:
        story.append(Paragraph(line, S["italic"]))

    story.append(Spacer(1, 8))
    story.append(Paragraph("Week 3: Training + Go-Live", S["blue_header"]))
    week3 = [
        '"Your AI training sessions are scheduled for [DATES]. Attendance is required -- but I promise it\'s the most useful hour you\'ll spend this month."',
        '"You\'ll learn exactly how to get the most out of your new tools, including specific prompts for your role. You\'ll also learn the simple Green/Yellow/Red system for knowing what data is safe to use with AI."',
        '"After training, you\'re free to use approved tools without restrictions for Green and Yellow data. Questions? Reach out to [AI HELP DESK CONTACT]."',
    ]
    for line in week3:
        story.append(Paragraph(line, S["italic"]))
    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PAGE 11: 3-Week Timeline
    # ════════════════════════════════════════════════════════════════
    story.append(Paragraph("3-Week Deployment Timeline", S["h2"]))
    story.append(Paragraph("Day-by-day implementation schedule. Run IT discovery and amnesty audit in parallel during Week 1.", S["body"]))
    story.append(Spacer(1, 8))

    # Week 1
    story.append(Paragraph("Week 1: Discovery", S["blue_header"]))
    story.append(Paragraph("<b>Days 1-2</b>", S["body"]))
    for item in ["IT/Security/HR alignment meeting", "Send amnesty audit to all employees", "IT begins network log analysis"]:
        story.append(Paragraph(f"\u2022 {item}", S["bullet"]))
    story.append(Paragraph("<b>Days 3-5</b>", S["body"]))
    for item in ["Finance pulls AI-related expenses", "Collect and analyze survey responses", "Identify top shadow AI tools in use"]:
        story.append(Paragraph(f"\u2022 {item}", S["bullet"]))
    story.append(Spacer(1, 8))

    # Week 2
    story.append(Paragraph("Week 2: Build", S["blue_header"]))
    story.append(Paragraph("<b>Days 1-3</b>", S["body"]))
    for item in ["Select and approve toolkit (use matrix above)", "Negotiate enterprise licenses", "Configure DLP rules (flag mode)"]:
        story.append(Paragraph(f"\u2022 {item}", S["bullet"]))
    story.append(Paragraph("<b>Days 4-5</b>", S["body"]))
    for item in ["Provision accounts for all employees", "Create data classification poster", "Prepare training materials"]:
        story.append(Paragraph(f"\u2022 {item}", S["bullet"]))
    story.append(Spacer(1, 8))

    # Week 3
    story.append(Paragraph("Week 3: Deploy", S["blue_header"]))
    story.append(Paragraph("<b>Days 1-3</b>", S["body"]))
    for item in ["Run manager training sessions", "Send toolkit announcement", "Run IC training sessions"]:
        story.append(Paragraph(f"\u2022 {item}", S["bullet"]))
    story.append(Paragraph("<b>Days 4-5</b>", S["body"]))
    for item in ["Go live with approved tools", "Monitor DLP flags (first 48 hours critical)", "Establish AI help desk channel"]:
        story.append(Paragraph(f"\u2022 {item}", S["bullet"]))
    story.append(PageBreak())

    # ════════════════════════════════════════════════════════════════
    # PAGE 12: CTA / Contact
    # ════════════════════════════════════════════════════════════════
    story.append(Spacer(1, 80))
    story.append(Paragraph("Need Help Deploying This?", S["center_bold"]))
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "This framework has been implemented across organizations of all sizes -- from 50-person startups to "
        "5,000-employee enterprises -- and consistently turns shadow AI from a risk into a competitive advantage. "
        "If you want hands-on help running the audit, selecting tools, or training your team, let's talk.",
        S["center"]
    ))
    story.append(Spacer(1, 30))
    story.append(Paragraph(f"<b>{BRAND_NAME}</b>", S["center_bold"]))
    story.append(Paragraph(BRAND_TITLE, S["center_blue"]))
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
