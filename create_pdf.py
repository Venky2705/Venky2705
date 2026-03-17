#!/usr/bin/env python3
"""
Generate GTM Tech Stack PDF Presentation
"""

from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT


DARK_BLUE = colors.HexColor('#003366')
LIGHT_BLUE = colors.HexColor('#0066CC')
ACCENT = colors.HexColor('#FF6600')
LIGHT_GRAY = colors.HexColor('#F5F5F5')
MID_GRAY = colors.HexColor('#CCCCCC')
WHITE = colors.white


def get_styles():
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'SlideTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=28,
        textColor=DARK_BLUE,
        spaceAfter=12,
        alignment=TA_CENTER,
    )

    slide_heading = ParagraphStyle(
        'SlideHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        textColor=DARK_BLUE,
        spaceBefore=6,
        spaceAfter=10,
    )

    subtitle_style = ParagraphStyle(
        'Subtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=16,
        textColor=LIGHT_BLUE,
        spaceAfter=6,
        alignment=TA_CENTER,
    )

    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        textColor=colors.HexColor('#333333'),
        spaceAfter=6,
        leftIndent=12,
    )

    bullet_style = ParagraphStyle(
        'Bullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        textColor=colors.HexColor('#444444'),
        spaceAfter=4,
        leftIndent=24,
        bulletIndent=12,
    )

    sub_bullet_style = ParagraphStyle(
        'SubBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        textColor=colors.HexColor('#666666'),
        spaceAfter=3,
        leftIndent=40,
    )

    label_style = ParagraphStyle(
        'Label',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        textColor=LIGHT_BLUE,
        spaceAfter=3,
        leftIndent=12,
    )

    return {
        'title': title_style,
        'heading': slide_heading,
        'subtitle': subtitle_style,
        'body': body_style,
        'bullet': bullet_style,
        'sub_bullet': sub_bullet_style,
        'label': label_style,
    }


def slide_divider():
    return [
        HRFlowable(width="100%", thickness=2, color=DARK_BLUE, spaceAfter=14),
    ]


def slide_footer_divider():
    return [
        Spacer(1, 0.15 * inch),
        HRFlowable(width="100%", thickness=1, color=MID_GRAY),
        Spacer(1, 0.1 * inch),
    ]


def build_pdf(output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=landscape(letter),
        rightMargin=0.75 * inch,
        leftMargin=0.75 * inch,
        topMargin=0.6 * inch,
        bottomMargin=0.5 * inch,
    )

    s = get_styles()
    story = []

    # ── SLIDE 1: Title ──────────────────────────────────────────────
    story.append(Spacer(1, 0.6 * inch))
    story.append(Paragraph("GTM Tech Stack Overview", s['title']))
    story.append(Spacer(1, 0.15 * inch))
    story.append(Paragraph("AI-Native Command Center for Revenue Operations", s['subtitle']))
    story.append(Paragraph("2026", s['subtitle']))
    story += slide_footer_divider()
    story.append(Paragraph("Confidential · LambdaTest GTM Operations", ParagraphStyle(
        'footer', fontName='Helvetica', fontSize=9,
        textColor=MID_GRAY, alignment=TA_CENTER)))
    story.append(PageBreak())

    # ── SLIDE 2: Executive Summary ──────────────────────────────────
    story.append(Paragraph("Executive Summary", s['heading']))
    story += slide_divider()
    items = [
        ("🎯 Unified GTM Operations", "Single AI-native platform powering all revenue touchpoints and growth motions."),
        ("🤖 AI-First Architecture", "Claude-powered agents embedded across prospecting, enablement, and customer success."),
        ("📊 Real-Time Intelligence", "Live insights from pipeline to product usage—no data silos."),
        ("⚡ Automated Workflows", "60 % reduction in manual effort through end-to-end automation."),
        ("🔗 15 + Integrated Tools", "Seamless data flow across every mission-critical GTM platform."),
    ]
    for icon_label, desc in items:
        story.append(Paragraph(f"<b>{icon_label}</b>", s['label']))
        story.append(Paragraph(desc, s['sub_bullet']))
        story.append(Spacer(1, 0.05 * inch))
    story.append(PageBreak())

    # ── SLIDE 3: Core Revenue Platforms ─────────────────────────────
    story.append(Paragraph("Core Revenue Platforms", s['heading']))
    story += slide_divider()

    platforms = [
        ("💼 Salesforce — CRM & Revenue Operations Hub", [
            "Single source of truth for all customer data",
            "Custom automation for deal progression & pipeline hygiene",
            "AI-powered forecasting and territory management",
        ]),
        ("📈 ChartMogul — Revenue Analytics & MRR Tracking", [
            "Subscription metrics, cohort analysis, and LTV modeling",
            "Churn prediction and real-time retention insights",
        ]),
        ("🎙️ Gong — Conversation Intelligence", [
            "AI-powered call analysis and rep coaching",
            "Deal risk detection and win/loss pattern recognition",
            "Competitive intelligence extracted from every call",
        ]),
    ]
    for title, bullets in platforms:
        story.append(Paragraph(title, s['label']))
        for b in bullets:
            story.append(Paragraph(f"• {b}", s['bullet']))
        story.append(Spacer(1, 0.1 * inch))
    story.append(PageBreak())

    # ── SLIDE 4: GTM Enablement Stack ───────────────────────────────
    story.append(Paragraph("GTM Enablement Stack", s['heading']))
    story += slide_divider()

    enablement = [
        ("🧠 GTMBuddy — Sales Enablement & Content AI", [
            "Just-in-time content recommendations during live calls",
            "AI-generated battlecards and objection-handling playbooks",
        ]),
        ("🔍 Clay — Data Enrichment & Prospecting", [
            "Automated lead enrichment from 50 + data sources",
            "AI-powered ICP scoring and waterfall enrichment",
        ]),
        ("📞 JustCall — Cloud Contact Center", [
            "Omnichannel communications (voice, SMS, WhatsApp)",
            "Call recording, transcription, and sentiment analysis",
        ]),
        ("📊 Amplitude — Product Analytics", [
            "User-behavior tracking and funnel analysis",
            "Product-led growth signals surfaced to sales",
        ]),
    ]
    for title, bullets in enablement:
        story.append(Paragraph(title, s['label']))
        for b in bullets:
            story.append(Paragraph(f"• {b}", s['bullet']))
        story.append(Spacer(1, 0.08 * inch))
    story.append(PageBreak())

    # ── SLIDE 5: AI-Native Command Center Architecture ───────────────
    story.append(Paragraph("AI-Native Command Center Architecture", s['heading']))
    story += slide_divider()

    col_data = [
        [
            Paragraph("<b>AI Integration Layer</b>", s['label']),
            Paragraph("<b>Data Infrastructure</b>", s['label']),
        ],
        [
            Paragraph("• Claude API — NLP & agentic workflows\n• Custom AI agents for task automation\n• Real-time synthesis across platforms", s['bullet']),
            Paragraph("• Centralised warehouse (Snowflake/BigQuery)\n• Real-time ETL pipelines\n• AI-ready semantic data models", s['bullet']),
        ],
        [
            Paragraph("<b>Automation Framework</b>", s['label']),
            Paragraph("<b>Security & Compliance</b>", s['label']),
        ],
        [
            Paragraph("• Zapier / Make for no-code workflows\n• Custom REST/GraphQL integrations\n• Event-driven triggers and webhooks", s['bullet']),
            Paragraph("• SOC 2 Type II compliant\n• Role-based access controls (RBAC)\n• Encryption at rest and in transit", s['bullet']),
        ],
    ]
    tbl = Table(col_data, colWidths=[4.75 * inch, 4.75 * inch], hAlign='LEFT')
    tbl.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BACKGROUND', (0, 0), (-1, 0), LIGHT_GRAY),
        ('BACKGROUND', (0, 2), (-1, 2), LIGHT_GRAY),
        ('GRID', (0, 0), (-1, -1), 0.5, MID_GRAY),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(tbl)
    story.append(PageBreak())

    # ── SLIDE 6: AI Automation Roadmap ──────────────────────────────
    story.append(Paragraph("AI Automation Roadmap", s['heading']))
    story += slide_divider()

    roadmap = [
        ("Q2 2026 — Foundation", LIGHT_BLUE, [
            "✅ AI-powered lead scoring and intelligent routing",
            "✅ Automated email personalisation at scale",
            "✅ Smart meeting scheduling and follow-up generation",
        ]),
        ("Q3 2026 — Optimisation", colors.HexColor('#008800'), [
            "🔄 Predictive deal scoring and real-time risk alerts",
            "🔄 AI-generated proposals and contract drafting",
            "🔄 Automated competitive intelligence gathering",
        ]),
        ("Q4 2026 — Advanced Intelligence", ACCENT, [
            "📅 Cross-platform multi-touch revenue attribution",
            "📅 AI-driven customer health scoring and forecasting",
            "📅 Autonomous renewal and expansion workflows",
        ]),
    ]
    for quarter, color, bullets in roadmap:
        story.append(Paragraph(quarter, ParagraphStyle(
            'qtr', fontName='Helvetica-Bold', fontSize=13,
            textColor=color, spaceAfter=4, leftIndent=8)))
        for b in bullets:
            story.append(Paragraph(b, s['bullet']))
        story.append(Spacer(1, 0.1 * inch))
    story.append(PageBreak())

    # ── SLIDE 7: Strategic GTM Metrics Dashboard ─────────────────────
    story.append(Paragraph("Strategic GTM Metrics Dashboard", s['heading']))
    story += slide_divider()

    metrics = [
        ("💰 Revenue Metrics", "ARR Growth Rate | MRR Movement | Net Revenue Retention (NRR)"),
        ("📈 Pipeline Health", "Pipeline Coverage Ratio | Avg. Deal Size | Win Rate by Segment"),
        ("⚡ Efficiency Metrics", "Sales Cycle Length | CAC Payback Period | SaaS Magic Number"),
        ("👥 Team Performance", "Quota Attainment | Ramp Time | Daily Activity Metrics"),
        ("🎯 Customer Success", "NPS Score | Customer Health Score | Expansion Revenue Rate"),
    ]
    metric_data = [[Paragraph(f"<b>{cat}</b>", s['label']), Paragraph(val, s['body'])] for cat, val in metrics]
    tbl2 = Table(metric_data, colWidths=[2.8 * inch, 6.7 * inch], hAlign='LEFT')
    tbl2.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BACKGROUND', (0, 0), (0, -1), LIGHT_GRAY),
        ('GRID', (0, 0), (-1, -1), 0.5, MID_GRAY),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('ROWBACKGROUNDS', (0, 0), (-1, -1), [WHITE, LIGHT_GRAY]),
    ]))
    story.append(tbl2)
    story.append(PageBreak())

    # ── SLIDE 8: Technology Stack Summary ───────────────────────────
    story.append(Paragraph("Complete Technology Stack", s['heading']))
    story += slide_divider()

    stack_data = [
        [Paragraph("<b>Category</b>", s['label']), Paragraph("<b>Tools</b>", s['label'])],
        [Paragraph("Revenue Operations", s['body']), Paragraph("Salesforce · ChartMogul · Gong", s['body'])],
        [Paragraph("Sales Enablement", s['body']), Paragraph("GTMBuddy · Clay · JustCall", s['body'])],
        [Paragraph("Analytics & Intelligence", s['body']), Paragraph("Amplitude · Custom BI Dashboards", s['body'])],
        [Paragraph("AI & Automation", s['body']), Paragraph("Claude AI · Zapier/Make · Custom integrations", s['body'])],
        [Paragraph("Data Infrastructure", s['body']), Paragraph("Snowflake / BigQuery · Real-time ETL", s['body'])],
        [Paragraph("Security & Compliance", s['body']), Paragraph("SOC 2 Type II · RBAC · Encrypted data layer", s['body'])],
    ]
    tbl3 = Table(stack_data, colWidths=[2.8 * inch, 6.7 * inch], hAlign='LEFT')
    tbl3.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), DARK_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, MID_GRAY),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_GRAY]),
    ]))
    story.append(tbl3)
    story.append(PageBreak())

    # ── SLIDE 9: Impact & Success Metrics ───────────────────────────
    story.append(Paragraph("Impact & Success Metrics", s['heading']))
    story += slide_divider()

    impact_data = [
        [Paragraph("<b>Area</b>", s['label']), Paragraph("<b>Metric</b>", s['label']), Paragraph("<b>Impact</b>", s['label'])],
        [Paragraph("Operational Efficiency", s['body']), Paragraph("Manual data entry", s['body']), Paragraph("▼ 60%", ParagraphStyle('imp', fontName='Helvetica-Bold', fontSize=12, textColor=colors.green))],
        [Paragraph("Operational Efficiency", s['body']), Paragraph("Lead response time", s['body']), Paragraph("▼ 45%", ParagraphStyle('imp', fontName='Helvetica-Bold', fontSize=12, textColor=colors.green))],
        [Paragraph("Operational Efficiency", s['body']), Paragraph("Forecast accuracy", s['body']), Paragraph("▲ 35%", ParagraphStyle('imp2', fontName='Helvetica-Bold', fontSize=12, textColor=LIGHT_BLUE))],
        [Paragraph("Revenue Impact", s['body']), Paragraph("Win rate", s['body']), Paragraph("▲ 25%", ParagraphStyle('imp2', fontName='Helvetica-Bold', fontSize=12, textColor=LIGHT_BLUE))],
        [Paragraph("Revenue Impact", s['body']), Paragraph("Sales cycle length", s['body']), Paragraph("▼ 40%", ParagraphStyle('imp', fontName='Helvetica-Bold', fontSize=12, textColor=colors.green))],
        [Paragraph("Revenue Impact", s['body']), Paragraph("Average deal size", s['body']), Paragraph("▲ 20%", ParagraphStyle('imp2', fontName='Helvetica-Bold', fontSize=12, textColor=LIGHT_BLUE))],
        [Paragraph("Team Productivity", s['body']), Paragraph("Customer-facing time", s['body']), Paragraph("▲ 50%", ParagraphStyle('imp2', fontName='Helvetica-Bold', fontSize=12, textColor=LIGHT_BLUE))],
        [Paragraph("Team Productivity", s['body']), Paragraph("Rep ramp time", s['body']), Paragraph("▼ 30%", ParagraphStyle('imp', fontName='Helvetica-Bold', fontSize=12, textColor=colors.green))],
    ]
    tbl4 = Table(impact_data, colWidths=[2.5 * inch, 4 * inch, 3 * inch], hAlign='LEFT')
    tbl4.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), DARK_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (2, 0), (2, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 0.5, MID_GRAY),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_GRAY]),
    ]))
    story.append(tbl4)
    story.append(PageBreak())

    # ── SLIDE 10: Closing ────────────────────────────────────────────
    story.append(Spacer(1, 0.8 * inch))
    story.append(Paragraph("Building the Future of GTM", s['title']))
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph("AI-Powered  ·  Data-Driven  ·  Customer-Centric", s['subtitle']))
    story.append(Spacer(1, 0.4 * inch))
    story.append(HRFlowable(width="60%", thickness=3, color=ACCENT, hAlign='CENTER', spaceAfter=20))
    story.append(Paragraph(
        "LambdaTest GTM Operations · 2026",
        ParagraphStyle('closing', fontName='Helvetica', fontSize=11,
                       textColor=MID_GRAY, alignment=TA_CENTER)))

    doc.build(story)
    print(f"✅ PDF created: {output_path}")
    print(f"   Pages: 10")


if __name__ == "__main__":
    build_pdf("/home/user/Venky2705/GTM_Tech_Stack_Presentation.pdf")
