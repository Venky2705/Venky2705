#!/usr/bin/env python3
"""
Generate GTM Tech Stack Presentation
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

def create_title_slide(prs, title, subtitle):
    """Create a title slide"""
    slide = prs.slides.add_slide(prs.slide_layouts[0])
    title_shape = slide.shapes.title
    subtitle_shape = slide.placeholders[1]

    title_shape.text = title
    subtitle_shape.text = subtitle

    # Style the title
    title_shape.text_frame.paragraphs[0].font.size = Pt(44)
    title_shape.text_frame.paragraphs[0].font.bold = True
    title_shape.text_frame.paragraphs[0].font.color.rgb = RGBColor(0, 51, 102)

    return slide

def create_content_slide(prs, title, content_items):
    """Create a content slide with bullet points"""
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    title_shape = slide.shapes.title
    body_shape = slide.placeholders[1]

    title_shape.text = title
    title_shape.text_frame.paragraphs[0].font.size = Pt(36)
    title_shape.text_frame.paragraphs[0].font.bold = True
    title_shape.text_frame.paragraphs[0].font.color.rgb = RGBColor(0, 51, 102)

    text_frame = body_shape.text_frame
    text_frame.clear()

    for item in content_items:
        p = text_frame.add_paragraph()
        p.text = item
        p.level = 0
        p.font.size = Pt(18)
        p.space_after = Pt(12)

    return slide

def create_two_column_slide(prs, title, left_items, right_items):
    """Create a two-column slide"""
    slide = prs.slides.add_slide(prs.slide_layouts[5])  # Blank layout

    # Add title
    left = Inches(0.5)
    top = Inches(0.5)
    width = Inches(9)
    height = Inches(0.75)

    title_box = slide.shapes.add_textbox(left, top, width, height)
    title_frame = title_box.text_frame
    title_frame.text = title
    title_frame.paragraphs[0].font.size = Pt(36)
    title_frame.paragraphs[0].font.bold = True
    title_frame.paragraphs[0].font.color.rgb = RGBColor(0, 51, 102)

    # Left column
    left_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(4.25), Inches(5))
    left_frame = left_box.text_frame
    left_frame.word_wrap = True

    for item in left_items:
        p = left_frame.add_paragraph()
        p.text = item
        p.font.size = Pt(16)
        p.space_after = Pt(10)

    # Right column
    right_box = slide.shapes.add_textbox(Inches(5.25), Inches(1.5), Inches(4.25), Inches(5))
    right_frame = right_box.text_frame
    right_frame.word_wrap = True

    for item in right_items:
        p = right_frame.add_paragraph()
        p.text = item
        p.font.size = Pt(16)
        p.space_after = Pt(10)

    return slide

def main():
    # Create presentation
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)

    # Slide 1: Title
    create_title_slide(
        prs,
        "GTM Tech Stack Overview",
        "AI-Native Command Center for Revenue Operations\n2026"
    )

    # Slide 2: Executive Summary
    create_content_slide(
        prs,
        "Executive Summary",
        [
            "🎯 Unified GTM operations platform powering revenue growth",
            "🤖 AI-native architecture across all revenue touchpoints",
            "📊 Real-time intelligence from prospecting to customer success",
            "⚡ Automated workflows reducing manual effort by 60%",
            "🔗 Seamless integration across 15+ mission-critical tools"
        ]
    )

    # Slide 3: Core Revenue Platforms
    create_content_slide(
        prs,
        "Core Revenue Platforms",
        [
            "💼 Salesforce - CRM & Revenue Operations Hub",
            "  • Single source of truth for all customer data",
            "  • Custom automation for deal progression",
            "  • AI-powered forecasting and pipeline management",
            "",
            "📈 ChartMogul - Revenue Analytics & MRR Tracking",
            "  • Subscription metrics and cohort analysis",
            "  • Customer lifetime value modeling",
            "  • Churn prediction and retention insights",
            "",
            "🎙️ Gong - Conversation Intelligence",
            "  • AI-powered call analysis and coaching",
            "  • Deal risk detection and win/loss insights",
            "  • Rep performance benchmarking"
        ]
    )

    # Slide 4: GTM Enablement Stack
    create_content_slide(
        prs,
        "GTM Enablement Stack",
        [
            "🧠 GTMBuddy - Sales Enablement & Content AI",
            "  • Just-in-time content recommendations",
            "  • AI-generated battlecards and objection handling",
            "",
            "🔍 Clay - Data Enrichment & Prospecting",
            "  • Automated lead enrichment from 50+ data sources",
            "  • AI-powered ideal customer profile (ICP) scoring",
            "",
            "📞 JustCall - Cloud Contact Center",
            "  • Omnichannel customer communications",
            "  • Call recording and sentiment analysis",
            "",
            "📊 Amplitude - Product Analytics",
            "  • User behavior tracking and cohort analysis",
            "  • Product-led growth insights"
        ]
    )

    # Slide 5: AI-Native Command Center Architecture
    create_two_column_slide(
        prs,
        "AI-Native Command Center Architecture",
        [
            "🤖 AI Integration Layer:",
            "• Claude API for natural language processing",
            "• Custom AI agents for workflow automation",
            "• Real-time data synthesis across platforms",
            "",
            "🔄 Automation Framework:",
            "• Zapier/Make for no-code workflows",
            "• Custom API integrations",
            "• Event-driven triggers and actions"
        ],
        [
            "📡 Data Infrastructure:",
            "• Centralized data warehouse (Snowflake/BigQuery)",
            "• Real-time ETL pipelines",
            "• AI-ready data models",
            "",
            "🛡️ Security & Compliance:",
            "• SOC 2 Type II compliance",
            "• Role-based access controls",
            "• Encrypted data at rest and in transit"
        ]
    )

    # Slide 6: AI Automation Roadmap
    create_content_slide(
        prs,
        "AI Automation Roadmap",
        [
            "Q2 2026 - Foundation:",
            "  ✅ AI-powered lead scoring and routing",
            "  ✅ Automated email personalization at scale",
            "  ✅ Intelligent meeting scheduling and follow-ups",
            "",
            "Q3 2026 - Optimization:",
            "  🔄 Predictive deal scoring and risk alerts",
            "  🔄 AI-generated proposal and contract content",
            "  🔄 Automated competitive intelligence gathering",
            "",
            "Q4 2026 - Advanced Intelligence:",
            "  📅 Cross-platform revenue attribution",
            "  📅 AI-driven customer health scoring",
            "  📅 Autonomous renewal and expansion workflows"
        ]
    )

    # Slide 7: Strategic GTM Metrics Dashboard
    create_content_slide(
        prs,
        "Strategic GTM Metrics Dashboard",
        [
            "💰 Revenue Metrics:",
            "  • ARR Growth Rate | MRR Movement | Net Revenue Retention",
            "",
            "📈 Pipeline Health:",
            "  • Pipeline Coverage Ratio | Avg Deal Size | Win Rate by Segment",
            "",
            "⚡ Efficiency Metrics:",
            "  • Sales Cycle Length | CAC Payback Period | Magic Number",
            "",
            "👥 Team Performance:",
            "  • Quota Attainment | Ramp Time | Activity Metrics",
            "",
            "🎯 Customer Success:",
            "  • NPS Score | Customer Health Score | Expansion Rate"
        ]
    )

    # Slide 8: Technology Stack Summary
    create_two_column_slide(
        prs,
        "Complete Technology Stack",
        [
            "Revenue Operations:",
            "• Salesforce",
            "• ChartMogul",
            "• Gong",
            "",
            "Sales Enablement:",
            "• GTMBuddy",
            "• Clay",
            "• JustCall"
        ],
        [
            "Analytics & Intelligence:",
            "• Amplitude",
            "• Custom BI Dashboards",
            "",
            "AI & Automation:",
            "• Claude AI",
            "• Zapier/Make",
            "• Custom integrations"
        ]
    )

    # Slide 9: Key Success Metrics
    create_content_slide(
        prs,
        "Impact & Success Metrics",
        [
            "📊 Operational Efficiency:",
            "  • 60% reduction in manual data entry",
            "  • 45% faster lead response time",
            "  • 35% improvement in forecast accuracy",
            "",
            "💼 Revenue Impact:",
            "  • 25% increase in win rate",
            "  • 40% shorter sales cycles",
            "  • 20% higher average deal size",
            "",
            "🚀 Team Productivity:",
            "  • 50% more time spent on customer-facing activities",
            "  • 30% faster rep ramp time",
            "  • 85% user adoption rate across platforms"
        ]
    )

    # Slide 10: Closing
    create_title_slide(
        prs,
        "Building the Future of GTM",
        "AI-Powered • Data-Driven • Customer-Centric"
    )

    # Save presentation
    output_file = "GTM_Tech_Stack_Presentation.pptx"
    prs.save(output_file)
    print(f"✅ Presentation created successfully: {output_file}")
    print(f"📄 Total slides: {len(prs.slides)}")

if __name__ == "__main__":
    main()
