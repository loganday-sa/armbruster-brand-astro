#!/usr/bin/env python3
"""
Generate Media Kit PDF for impact.com publisher profile
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.pdfgen import canvas

# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
OUTPUT_PATH = os.path.join(PROJECT_ROOT, "public", "downloads", "scott-armbruster-media-kit.pdf")

# Brand colors
BLUE_PRIMARY = colors.HexColor("#2563EB")
PURPLE_ACCENT = colors.HexColor("#7C3AED")
ORANGE_ACCENT = colors.HexColor("#D97706")
GREEN_ACCENT = colors.HexColor("#059669")
SLATE_900 = colors.HexColor("#0F172A")
SLATE_300 = colors.HexColor("#CBD5E1")

# Ensure output directory exists
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

# Custom page template with header/footer
class MediaKitTemplate(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self.pages = []

    def showPage(self):
        self.pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        page_count = len(self.pages)
        for i, page in enumerate(self.pages):
            self.__dict__.update(page)
            if i > 0:  # Skip footer on cover page
                self.draw_page_footer(i + 1, page_count)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_footer(self, page_num, page_count):
        self.saveState()
        self.setFont('Helvetica', 9)
        self.setFillColor(SLATE_300)
        footer_text = f"Scott Armbruster Media Kit | {page_num}"
        self.drawRightString(letter[0] - 0.75*inch, 0.5*inch, footer_text)
        self.restoreState()

# Create PDF
doc = SimpleDocTemplate(
    OUTPUT_PATH,
    pagesize=letter,
    topMargin=0.75*inch,
    bottomMargin=0.75*inch,
    leftMargin=0.75*inch,
    rightMargin=0.75*inch
)

# Styles
styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=36,
    textColor=BLUE_PRIMARY,
    spaceAfter=12,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold'
)

subtitle_style = ParagraphStyle(
    'CustomSubtitle',
    parent=styles['Normal'],
    fontSize=16,
    textColor=colors.HexColor("#475569"),  # Medium slate for readability
    spaceAfter=36,
    alignment=TA_CENTER,
    fontName='Helvetica'
)

heading1_style = ParagraphStyle(
    'CustomHeading1',
    parent=styles['Heading1'],
    fontSize=24,
    textColor=BLUE_PRIMARY,
    spaceAfter=18,
    spaceBefore=16,
    fontName='Helvetica-Bold',
    leading=28
)

heading2_style = ParagraphStyle(
    'CustomHeading2',
    parent=styles['Heading2'],
    fontSize=18,
    textColor=PURPLE_ACCENT,
    spaceAfter=14,
    spaceBefore=12,
    fontName='Helvetica-Bold',
    leading=22
)

body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['Normal'],
    fontSize=11,
    textColor=colors.HexColor("#1E293B"),  # Dark slate for readability
    spaceAfter=12,
    leading=16,
    fontName='Helvetica'
)

bullet_style = ParagraphStyle(
    'CustomBullet',
    parent=styles['Normal'],
    fontSize=11,
    textColor=colors.HexColor("#1E293B"),  # Dark slate for readability
    leftIndent=20,
    bulletIndent=10,
    spaceAfter=8,
    leading=16,
    fontName='Helvetica'
)

stat_number_style = ParagraphStyle(
    'StatNumber',
    parent=styles['Normal'],
    fontSize=32,
    textColor=BLUE_PRIMARY,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold',
    spaceAfter=6
)

stat_label_style = ParagraphStyle(
    'StatLabel',
    parent=styles['Normal'],
    fontSize=11,
    textColor=colors.HexColor("#475569"),  # Medium slate for readability
    alignment=TA_CENTER,
    fontName='Helvetica',
    spaceAfter=16
)

# Build content
story = []

# Cover page
story.append(Spacer(1, 1.5*inch))
story.append(Paragraph("MEDIA KIT", title_style))
story.append(Paragraph("Scott Armbruster", subtitle_style))
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph("AI Strategy & Systems Partner", body_style))
story.append(Paragraph("Content Creator | Thought Leader | Agency Owner", body_style))
story.append(Spacer(1, 1.5*inch))
story.append(Paragraph("scottarmbruster.com", body_style))
story.append(Paragraph("LinkedIn: linkedin.com/in/scottrarmbruster", body_style))

story.append(PageBreak())

# About section
story.append(Paragraph("About Scott Armbruster", heading1_style))
story.append(Spacer(1, 0.2*inch))

about_text = """Scott Armbruster is an AI strategy partner, agency owner, and content creator
specializing in helping mission-driven organizations deploy AI systems that deliver measurable ROI.
Through practical implementation guides, comprehensive governance frameworks, and strategic resources,
Scott reaches executives, operations leaders, and tech professionals navigating AI adoption."""

story.append(Paragraph(about_text, body_style))
story.append(Spacer(1, 0.3*inch))

story.append(Paragraph("Expertise & Focus Areas", heading2_style))
story.append(Paragraph("• AI strategy and readiness assessments", bullet_style))
story.append(Paragraph("• AI governance frameworks and EU AI Act compliance", bullet_style))
story.append(Paragraph("• Shadow AI management and security", bullet_style))
story.append(Paragraph("• Custom AI agents and automation systems", bullet_style))
story.append(Paragraph("• Career positioning and professional development in AI", bullet_style))

story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("Services Offered", heading2_style))
story.append(Paragraph("• AI Readiness Workshops (starting at $2,500)", bullet_style))
story.append(Paragraph("• AI Governance Frameworks (starting at $3,500)", bullet_style))
story.append(Paragraph("• Custom AI Agents - voice and chat (starting at $1,500)", bullet_style))
story.append(Paragraph("• AI Strategy & Advisory retainer ($3,000/month)", bullet_style))

story.append(PageBreak())

# Audience Demographics
story.append(Paragraph("Audience Demographics", heading1_style))
story.append(Spacer(1, 0.2*inch))

# Audience stats table
audience_stats = [
    [Paragraph("<b>Decision Makers</b>", body_style), Paragraph("<b>Organization Size</b>", body_style), Paragraph("<b>Industries</b>", body_style)],
    [Paragraph("Executive Directors<br/>COOs, CTOs<br/>Operations Leaders<br/>Tech Consultants", body_style),
     Paragraph("50-500 employees<br/><br/>Budget: $10K-$100K<br/>for AI implementation", body_style),
     Paragraph("Non-profits<br/>Social enterprises<br/>B2B SaaS<br/>Professional services", body_style)]
]
audience_table = Table(audience_stats, colWidths=[2*inch, 2.2*inch, 2*inch])
audience_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), BLUE_PRIMARY),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 10),
    ('TOPPADDING', (0, 0), (-1, -1), 14),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 14),
    ('LEFTPADDING', (0, 0), (-1, -1), 12),
    ('RIGHTPADDING', (0, 0), (-1, -1), 12),
    ('GRID', (0, 0), (-1, -1), 0.5, SLATE_300),
]))
story.append(audience_table)

story.append(Spacer(1, 0.4*inch))

story.append(Paragraph("Audience Characteristics", heading2_style))
story.append(Paragraph("• Budget-conscious but investment-ready for proven ROI", bullet_style))
story.append(Paragraph("• Values mission alignment over \"move fast and break things\"", bullet_style))
story.append(Paragraph("• Seeks practical implementation, not theoretical strategy", bullet_style))
story.append(Paragraph("• Tech-forward but not necessarily technical experts", bullet_style))
story.append(Paragraph("• High engagement with B2B SaaS, enterprise software, AI tools", bullet_style))

story.append(PageBreak())

# Content Overview
story.append(Paragraph("Content Overview", heading1_style))
story.append(Spacer(1, 0.3*inch))

story.append(Paragraph("Content Categories", heading2_style))
story.append(Paragraph("• <b>AI Strategy</b> - Business strategy, ROI analysis, AI adoption guidance", bullet_style))
story.append(Paragraph("• <b>Implementation</b> - How-to guides, automation walkthroughs, case studies", bullet_style))
story.append(Paragraph("• <b>Industry</b> - AI news analysis, market trends, regulatory updates", bullet_style))
story.append(Paragraph("• <b>Career</b> - Career positioning, side businesses, professional growth", bullet_style))

story.append(Spacer(1, 0.3*inch))

story.append(Paragraph("Flagship Resources (Free Downloads)", heading2_style))
story.append(Paragraph("• <b>AI Tool Governance Pipeline</b> - Complete lifecycle framework with maturity model, KPIs, decision trees", bullet_style))
story.append(Paragraph("• <b>AI Development Governance Framework</b> - EU AI Act compliance, bias audits, regulatory mapping", bullet_style))
story.append(Paragraph("• <b>Shadow AI Governance Toolkit</b> - 3-week tactical implementation guide", bullet_style))

story.append(Spacer(1, 0.3*inch))

story.append(Paragraph("Content Formats", heading2_style))
story.append(Paragraph("• Long-form blog posts (1,500-3,000 words)", bullet_style))
story.append(Paragraph("• Downloadable PDF resources and frameworks", bullet_style))
story.append(Paragraph("• Case studies with ROI metrics", bullet_style))
story.append(Paragraph("• Implementation guides and checklists", bullet_style))
story.append(Paragraph("• LinkedIn thought leadership", bullet_style))

story.append(Spacer(1, 0.3*inch))

story.append(Paragraph("Content Portfolio", heading2_style))
story.append(Paragraph("• <b>AI Tool Briefing</b> (aitoolbriefing.com) - Curated intelligence on AI tools with reviews, comparisons, and industry insights", bullet_style))
story.append(Paragraph("• <b>Scott Armbruster Blog</b> (scottarmbruster.com) - AI strategy, implementation guides, and professional development", bullet_style))

story.append(PageBreak())

# Sample Content Highlights
story.append(Paragraph("Sample Content Highlights", heading1_style))
story.append(Spacer(1, 0.2*inch))

sample_content = [
    ["Title", "Category", "Focus"],
    ["95% of AI Projects Fail: Here's How to Be in the 5%", "AI Strategy", "Project success"],
    ["Case Study: 10-Hour Automation That Freed Up 20% of Work Time", "Implementation", "ROI proof"],
    ["State AI Compliance Laws Crushing Small Businesses (2026)", "Industry", "Regulatory landscape"],
    ["How to Position Yourself for AI's Job Market Changes by 2030", "Career", "Future-proofing"],
    ["Shadow AI Costing More Than Productivity: How to Fix", "AI Strategy", "Governance urgency"],
]

sample_table = Table(sample_content, colWidths=[3.2*inch, 1.4*inch, 1.4*inch])
sample_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), PURPLE_ACCENT),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('TOPPADDING', (0, 0), (-1, -1), 14),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 14),
    ('LEFTPADDING', (0, 0), (-1, -1), 10),
    ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ('GRID', (0, 0), (-1, -1), 0.5, SLATE_300),
]))
story.append(sample_table)

story.append(PageBreak())

# Partnership Opportunities
story.append(Paragraph("Partnership Opportunities", heading1_style))
story.append(Spacer(1, 0.2*inch))

story.append(Paragraph("Why Partner With Scott Armbruster?", heading2_style))
story.append(Spacer(1, 0.1*inch))

partnership_benefits = [
    ["✓ High-ticket services = Higher commissions per conversion"],
    ["✓ 90-day cookie window = More attribution credit"],
    ["✓ Niche positioning = Less competition, higher trust"],
    ["✓ Multiple service tiers = Easy upsell path"],
    ["✓ Free downloadable resources = Lead generation hooks"],
    ["✓ Mission-driven positioning = Authentic promotion"],
    ["✓ Professional brand = High conversion from qualified traffic"],
]

benefits_table = Table(partnership_benefits, colWidths=[6*inch])
benefits_table.setStyle(TableStyle([
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('FONTSIZE', (0, 0), (-1, -1), 11),
    ('TOPPADDING', (0, 0), (-1, -1), 8),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ('LEFTPADDING', (0, 0), (-1, -1), 12),
    ('RIGHTPADDING', (0, 0), (-1, -1), 12),
]))
story.append(benefits_table)

story.append(Spacer(1, 0.3*inch))

story.append(Paragraph("Ideal Brand Partnerships", heading2_style))
story.append(Paragraph("• B2B SaaS tools (AI, automation, productivity)", bullet_style))
story.append(Paragraph("• Enterprise software and business operations platforms", bullet_style))
story.append(Paragraph("• Professional development and online courses", bullet_style))
story.append(Paragraph("• Tech consulting and implementation services", bullet_style))
story.append(Paragraph("• AI tools and APIs", bullet_style))

story.append(Spacer(1, 0.25*inch))

story.append(Paragraph("Suggested Commission Structure", heading2_style))
story.append(Paragraph("• $250 per qualified consultation booked", bullet_style))
story.append(Paragraph("• $500 bonus for closed project deals", bullet_style))
story.append(Paragraph("• $150/month for retainer clients (first 6 months)", bullet_style))
story.append(Paragraph("• Average order value: $2,500-$15,000 per engagement", bullet_style))

story.append(PageBreak())

# Contact & Links
story.append(Paragraph("Contact & Links", heading1_style))
story.append(Spacer(1, 0.3*inch))

contact_data = [
    [Paragraph("<b>Website</b>", body_style), Paragraph("scottarmbruster.com", body_style)],
    [Paragraph("<b>LinkedIn</b>", body_style), Paragraph("linkedin.com/in/scottrarmbruster", body_style)],
    [Paragraph("<b>Twitter</b>", body_style), Paragraph("@ScottArmbruster", body_style)],
    [Paragraph("<b>Email</b>", body_style), Paragraph("Contact via website", body_style)],
]

contact_table = Table(contact_data, colWidths=[1.5*inch, 4.5*inch])
contact_table.setStyle(TableStyle([
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 12),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ('LEFTPADDING', (0, 0), (-1, -1), 12),
    ('RIGHTPADDING', (0, 0), (-1, -1), 12),
    ('LINEBELOW', (0, 0), (-1, -2), 0.5, colors.HexColor("#CBD5E1")),
]))
story.append(contact_table)

story.append(Spacer(1, 0.6*inch))

story.append(Paragraph("Key Pages for Promotion", heading2_style))
story.append(Paragraph("• Homepage - Overview of services and latest content", bullet_style))
story.append(Paragraph("• /agency - Complete service descriptions with pricing", bullet_style))
story.append(Paragraph("• /resources - Free downloadable governance frameworks", bullet_style))
story.append(Paragraph("• /contact - Discovery call booking", bullet_style))
story.append(Paragraph("• Blog categories - AI Strategy, Implementation, Industry, Career", bullet_style))

story.append(Spacer(1, 0.6*inch))

closing = """Thank you for your interest in partnering with Scott Armbruster. For partnership inquiries,
media requests, or collaboration opportunities, please reach out via the website contact form."""

story.append(Paragraph(closing, body_style))

# Build PDF
doc.build(story, canvasmaker=MediaKitTemplate)

print(f"✓ Media kit generated: {OUTPUT_PATH}")
print(f"  File size: {os.path.getsize(OUTPUT_PATH) / 1024:.1f} KB")
