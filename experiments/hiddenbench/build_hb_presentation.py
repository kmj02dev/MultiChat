import sys
import os
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# 1. Initialize Presentation
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

# Output paths
work_dir = Path(r"C:\Users\GC\.gemini\antigravity\scratch\hitl_mad_hiddenbench")
fig_dir = work_dir / "figures"
pptx_path = work_dir / "Human_in_the_Loop_Multi_Agent_Debate_HiddenBench.pptx"

# Color Palette Definitions
C_NAVY_DARK = RGBColor(15, 23, 42)       # #0F172A
C_NAVY_BRAND = RGBColor(30, 58, 138)     # #1E3A8A
C_BLUE_ACCENT = RGBColor(37, 99, 235)    # #2563EB
C_BLUE_LIGHT = RGBColor(239, 246, 255)   # #EFF6FF
C_ORANGE_ACCENT = RGBColor(234, 88, 12)  # #EA580C
C_ORANGE_LIGHT = RGBColor(254, 243, 199) # #FEF3C7
C_GREEN_ACCENT = RGBColor(16, 185, 129)  # #10B981
C_GREEN_LIGHT = RGBColor(236, 253, 245)  # #ECFDF5
C_RED_ACCENT = RGBColor(220, 38, 38)     # #DC2626
C_RED_LIGHT = RGBColor(254, 242, 242)    # #FEF2F2
C_TEXT_DARK = RGBColor(30, 41, 59)       # #1E293B
C_TEXT_MUTED = RGBColor(100, 116, 139)   # #64748B
C_BG_PAGE = RGBColor(248, 250, 252)      # #F8FAFC
C_WHITE = RGBColor(255, 255, 255)
C_BORDER = RGBColor(226, 232, 240)       # #E2E8F0

FONT_HEADING = "Segoe UI"
FONT_BODY = "Segoe UI"

def set_slide_background(slide, color=C_BG_PAGE):
    bg_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg_shape.fill.solid()
    bg_shape.fill.fore_color.rgb = color
    bg_shape.line.fill.background()
    return bg_shape

def add_header(slide, category_text, title_text, subtitle_text=None):
    tb_cat = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.35))
    tf_cat = tb_cat.text_frame
    tf_cat.word_wrap = True
    tf_cat.margin_left = tf_cat.margin_top = tf_cat.margin_right = tf_cat.margin_bottom = 0
    p_cat = tf_cat.paragraphs[0]
    p_cat.text = category_text.upper()
    p_cat.font.name = FONT_HEADING
    p_cat.font.size = Pt(11)
    p_cat.font.bold = True
    p_cat.font.color.rgb = C_BLUE_ACCENT

    tb_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.72), Inches(11.7), Inches(0.6))
    tf_title = tb_title.text_frame
    tf_title.word_wrap = True
    tf_title.margin_left = tf_title.margin_top = tf_title.margin_right = tf_title.margin_bottom = 0
    p_title = tf_title.paragraphs[0]
    p_title.text = title_text
    p_title.font.name = FONT_HEADING
    p_title.font.size = Pt(22)
    p_title.font.bold = True
    p_title.font.color.rgb = C_NAVY_DARK

    if subtitle_text:
        p_sub = tf_title.add_paragraph()
        p_sub.text = subtitle_text
        p_sub.font.name = FONT_BODY
        p_sub.font.size = Pt(12)
        p_sub.font.color.rgb = C_TEXT_MUTED
        p_sub.space_before = Pt(4)

def add_card(slide, left, top, width, height, bg_color=C_WHITE, border_color=C_BORDER):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    if border_color:
        card.line.color.rgb = border_color
        card.line.width = Pt(1.2)
    else:
        card.line.fill.background()
    return card

# -------------------------------------------------------------
# SLIDE 1: Title Slide
# -------------------------------------------------------------
s1 = prs.slides.add_slide(blank_layout)
set_slide_background(s1, C_NAVY_DARK)

dec_card = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.5), Inches(0.12), Inches(4.5))
dec_card.fill.solid()
dec_card.fill.fore_color.rgb = C_BLUE_ACCENT
dec_card.line.fill.background()

tb = s1.shapes.add_textbox(Inches(1.2), Inches(1.4), Inches(11.0), Inches(4.8))
tf = tb.text_frame
tf.word_wrap = True

p_badge = tf.paragraphs[0]
p_badge.text = "RESEARCH PROJECT PRESENTATION • ASYMMETRIC INFORMATION BENCHMARK"
p_badge.font.name = FONT_HEADING
p_badge.font.size = Pt(13)
p_badge.font.bold = True
p_badge.font.color.rgb = C_ORANGE_ACCENT

p1 = tf.add_paragraph()
p1.text = "Human-in-the-Loop Multi-Agent Debate"
p1.font.name = FONT_HEADING
p1.font.size = Pt(36)
p1.font.bold = True
p1.font.color.rgb = C_WHITE
p1.space_before = Pt(16)

p2 = tf.add_paragraph()
p2.text = "Overcoming Common Knowledge Bias and Information Asymmetry on HiddenBench"
p2.font.name = FONT_HEADING
p2.font.size = Pt(23)
p2.font.bold = True
p2.font.color.rgb = RGBColor(147, 197, 253)
p2.space_before = Pt(8)

p_author = tf.add_paragraph()
p_author.text = "Author: Min Jae Kang  |  Student ID: 202645469"
p_author.font.name = FONT_BODY
p_author.font.size = Pt(15)
p_author.font.color.rgb = RGBColor(226, 232, 240)
p_author.space_before = Pt(36)

p_affil = tf.add_paragraph()
p_affil.text = "Benchmark: HiddenBench (25 Tasks) • Asymmetric Hidden Profiles & Multi-Agent Oversight"
p_affil.font.name = FONT_BODY
p_affil.font.size = Pt(13)
p_affil.font.color.rgb = C_TEXT_MUTED
p_affil.space_before = Pt(6)

# -------------------------------------------------------------
# SLIDE 2: Overview & Research Questions
# -------------------------------------------------------------
s2 = prs.slides.add_slide(blank_layout)
set_slide_background(s2)
add_header(s2, "Overview & Core Topic", "Talk Roadmap & Central Research Questions",
           "Investigating whether external human oversight can break the Common Knowledge Effect in asymmetric debates")

add_card(s2, Inches(0.8), Inches(1.5), Inches(11.73), Inches(1.15), bg_color=C_BLUE_LIGHT, border_color=C_BLUE_ACCENT)
tb_rq = s2.shapes.add_textbox(Inches(1.0), Inches(1.6), Inches(11.3), Inches(0.95))
tf_rq = tb_rq.text_frame
tf_rq.word_wrap = True
p = tf_rq.paragraphs[0]
p.text = "Core Question: Can Human Oversight Solve the Hidden Profile Dilemma?"
p.font.name = FONT_HEADING
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_NAVY_BRAND

p_sub = tf_rq.add_paragraph()
p_sub.text = "Testing Bottleneck Detection (RQ 1), Private Constraint Pooling (RQ 2), and LLM Moderator Limits (RQ 3) on HiddenBench."
p_sub.font.name = FONT_BODY
p_sub.font.size = Pt(12.5)
p_sub.font.color.rgb = C_TEXT_DARK
p_sub.space_before = Pt(4)

roadmap = [
    ("01 Background", "Hidden Profiles", "Asymmetric information distribution and the classic Common Knowledge Effect.", C_NAVY_BRAND, C_BLUE_LIGHT),
    ("02 Method", "Epistemic Scaffolding", "Procedural constraint verification hints injected at Round 2 inflection points.", C_BLUE_ACCENT, C_BLUE_LIGHT),
    ("03 Results", "HiddenBench Findings", "Empirical proof: +88.0%p decision gain, 100% detection, and LLM moderator failure.", C_ORANGE_ACCENT, C_ORANGE_LIGHT),
    ("04 Synthesis", "GSM8K vs HiddenBench", "Cross-benchmark comparison proving human oversight is vital for asymmetric logic.", C_GREEN_ACCENT, C_GREEN_LIGHT)
]

col_w = Inches(2.76)
gap = Inches(0.23)
start_l = Inches(0.8)
top_y = Inches(2.9)
card_h = Inches(4.0)

for idx, (step_num, title, desc, col_c, bg_c) in enumerate(roadmap):
    cx = start_l + idx * (col_w + gap)
    add_card(s2, cx, top_y, col_w, card_h, bg_color=C_WHITE, border_color=C_BORDER)

    top_bar = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, cx, top_y, col_w, Inches(0.1))
    top_bar.fill.solid()
    top_bar.fill.fore_color.rgb = col_c
    top_bar.line.fill.background()

    tb_card = s2.shapes.add_textbox(cx + Inches(0.2), top_y + Inches(0.25), col_w - Inches(0.4), card_h - Inches(0.5))
    tf_c = tb_card.text_frame
    tf_c.word_wrap = True

    p_s = tf_c.paragraphs[0]
    p_s.text = step_num
    p_s.font.name = FONT_HEADING
    p_s.font.size = Pt(12)
    p_s.font.bold = True
    p_s.font.color.rgb = col_c

    p_t = tf_c.add_paragraph()
    p_t.text = title
    p_t.font.name = FONT_HEADING
    p_t.font.size = Pt(16)
    p_t.font.bold = True
    p_t.font.color.rgb = C_NAVY_DARK
    p_t.space_before = Pt(8)

    p_d = tf_c.add_paragraph()
    p_d.text = desc
    p_d.font.name = FONT_BODY
    p_d.font.size = Pt(12)
    p_d.font.color.rgb = C_TEXT_DARK
    p_d.space_before = Pt(12)

# -------------------------------------------------------------
# SLIDE 3: Background 01: The Hidden Profile Paradigm
# -------------------------------------------------------------
s3 = prs.slides.add_slide(blank_layout)
set_slide_background(s3)
add_header(s3, "Background 01", "The Hidden Profile Paradigm in Multi-Agent Systems",
           "Foundational social psychology framework (Stasser & Titus, 1985) applied to collaborative LLMs")

hp_points = [
    ("Shared Information", "Common Knowledge Hub",
     "Information broadcasted to all participants prior to debate. Typically highlights superficial positive attributes of a suboptimal candidate (Distractor), creating false collective confidence.", C_BLUE_ACCENT),
    ("Hidden Information", "Asymmetric Private Silos",
     "Critical disqualifying facts or enabling conditions partitioned across agents. No individual agent holds enough private information alone to deduce the ground truth without pooling.", C_ORANGE_ACCENT),
    ("Collective Task", "Mandatory Information Integration",
     "Solving the task requires agents to actively exchange, validate, and integrate unshared private facts against shared distractor claims.", C_NAVY_BRAND),
    ("Systemic Pathology", "Common Knowledge Bias",
     "Human groups and LLM multi-agent systems systematically discuss shared facts 4x more frequently than unshared facts, prematurely eliminating optimal alternatives.", C_RED_ACCENT)
]

w3 = Inches(5.7)
h3 = Inches(2.4)
coords3 = [(Inches(0.8), Inches(1.6)), (Inches(6.8), Inches(1.6)), (Inches(0.8), Inches(4.3)), (Inches(6.8), Inches(4.3))]

for idx, (t, sub, desc, col) in enumerate(hp_points):
    px, py = coords3[idx]
    add_card(s3, px, py, w3, h3, bg_color=C_WHITE, border_color=col if idx==3 else C_BORDER)
    stripe = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, px, py, Inches(0.12), h3)
    stripe.fill.solid()
    stripe.fill.fore_color.rgb = col
    stripe.line.fill.background()

    tb = s3.shapes.add_textbox(px + Inches(0.28), py + Inches(0.2), w3 - Inches(0.4), h3 - Inches(0.4))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = t
    p.font.name = FONT_HEADING
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = col

    p_sub = tf.add_paragraph()
    p_sub.text = sub
    p_sub.font.name = FONT_BODY
    p_sub.font.size = Pt(12)
    p_sub.font.bold = True
    p_sub.font.color.rgb = C_NAVY_DARK
    p_sub.space_before = Pt(4)

    p_desc = tf.add_paragraph()
    p_desc.text = desc
    p_desc.font.name = FONT_BODY
    p_desc.font.size = Pt(11.5)
    p_desc.font.color.rgb = C_TEXT_DARK
    p_desc.space_before = Pt(8)

# -------------------------------------------------------------
# SLIDE 4: Background 02: Why Closed Debates Fail on Asymmetric Info
# -------------------------------------------------------------
s4 = prs.slides.add_slide(blank_layout)
set_slide_background(s4)
add_header(s4, "Background 02", "Why Closed Multi-Agent Debates Fail on Asymmetric Info",
           "The toxic interaction between Common Knowledge Sampling and Conformity Pressure")

add_card(s4, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.2), bg_color=C_WHITE, border_color=C_RED_ACCENT)
tb_l = s4.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.1), Inches(4.8))
tf_l = tb_l.text_frame
tf_l.word_wrap = True
p = tf_l.paragraphs[0]
p.text = "Mechanism 1: Common Knowledge Bias"
p.font.name = FONT_HEADING
p.font.size = Pt(17)
p.font.bold = True
p.font.color.rgb = C_RED_ACCENT
p_sub = tf_l.add_paragraph()
p_sub.text = "Sampling Bias in Shared Message Pools"
p_sub.font.name = FONT_BODY
p_sub.font.size = Pt(12)
p_sub.font.color.rgb = C_TEXT_MUTED
p_sub.space_before = Pt(4)

items_ckb = [
    ("Echo Chamber Reinforcement", "Because 4 out of 4 agents possess the shared positive notes, these claims dominate the opening round of discourse."),
    ("Dismissal of Unshared Vetoes", "When a single agent raises an unshared constraint (e.g., 'tunnel fire'), peers treat it as an unverified rumor or local irregularity."),
    ("Sycophantic Convergence", "Language models are heavily tuned to be agreeable, rapidly abandoning unshared truths to match peer sentiment.")
]
for title, d in items_ckb:
    p_t = tf_l.add_paragraph()
    p_t.text = "• " + title
    p_t.font.name = FONT_HEADING
    p_t.font.size = Pt(13)
    p_t.font.bold = True
    p_t.font.color.rgb = C_NAVY_DARK
    p_t.space_before = Pt(14)
    p_d = tf_l.add_paragraph()
    p_d.text = d
    p_d.font.name = FONT_BODY
    p_d.font.size = Pt(11.5)
    p_d.font.color.rgb = C_TEXT_DARK
    p_d.space_before = Pt(2)

add_card(s4, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2), bg_color=C_WHITE, border_color=C_BLUE_ACCENT)
tb_r = s4.shapes.add_textbox(Inches(7.1), Inches(1.8), Inches(5.1), Inches(4.8))
tf_r = tb_r.text_frame
tf_r.word_wrap = True
p = tf_r.paragraphs[0]
p.text = "Mechanism 2: The Conformity Collapse"
p.font.name = FONT_HEADING
p.font.size = Pt(17)
p.font.bold = True
p.font.color.rgb = C_BLUE_ACCENT
p_sub = tf_r.add_paragraph()
p_sub.text = "Peer Pressure Overpowers Ground Truth"
p_sub.font.name = FONT_BODY
p_sub.font.size = Pt(12)
p_sub.font.color.rgb = C_TEXT_MUTED
p_sub.space_before = Pt(4)

items_conf = [
    ("Asymmetrical Majority Pressure", "A 3-against-1 majority forms instantly in Round 1 based on shared information."),
    ("Coordination Bonus Trap", "Agents prioritize group consensus to maximize cooperative rewards, sacrificing factual accuracy."),
    ("Capitulation in Round 2", "The dissenting agent surrenders: 'Since all 3 of you agree on East Town, I align with group consensus.'")
]
for title, d in items_conf:
    p_t = tf_r.add_paragraph()
    p_t.text = "• " + title
    p_t.font.name = FONT_HEADING
    p_t.font.size = Pt(13)
    p_t.font.bold = True
    p_t.font.color.rgb = C_NAVY_DARK
    p_t.space_before = Pt(14)
    p_d = tf_r.add_paragraph()
    p_d.text = d
    p_d.font.name = FONT_BODY
    p_d.font.size = Pt(11.5)
    p_d.font.color.rgb = C_TEXT_DARK
    p_d.space_before = Pt(2)

# -------------------------------------------------------------
# SLIDE 5: Background 03: Multi-Agent Debate Workflow
# -------------------------------------------------------------
s5 = prs.slides.add_slide(blank_layout)
set_slide_background(s5)
add_header(s5, "Background 03", "Multi-Agent Debate Protocol on HiddenBench",
           "Synchronized 3-round interaction architecture across 4 collaborative decision-makers")

steps5 = [
    ("Stage 1", "Siloed Deliberation", "Each of the 4 agents reads the shared scenario plus their private dispatch. Agents state their initial preferred candidate.", C_NAVY_BRAND),
    ("Stage 2", "Cross-Turn Critique", "Agents evaluate peers' recommendations. In baseline, majority pressure suppresses minority private facts.", C_BLUE_ACCENT),
    ("Stage 3", "Consensus Voting", "Agents cast their final votes. The group succeeds only if all 4 agents converge onto the true optimal choice.", C_GREEN_ACCENT)
]

col_w5 = Inches(3.7)
gap5 = Inches(0.3)
start_l5 = Inches(0.8)

for idx, (stage, title, desc, col) in enumerate(steps5):
    cx = start_l5 + idx * (col_w5 + gap5)
    add_card(s5, cx, Inches(1.8), col_w5, Inches(4.8), bg_color=C_WHITE, border_color=C_BORDER)

    hblock = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, cx, Inches(1.8), col_w5, Inches(0.9))
    hblock.fill.solid()
    hblock.fill.fore_color.rgb = col
    hblock.line.fill.background()

    tb_h = s5.shapes.add_textbox(cx + Inches(0.2), Inches(1.9), col_w5 - Inches(0.4), Inches(0.7))
    tf_h = tb_h.text_frame
    tf_h.word_wrap = True
    p_st = tf_h.paragraphs[0]
    p_st.text = stage.upper()
    p_st.font.name = FONT_HEADING
    p_st.font.size = Pt(11)
    p_st.font.bold = True
    p_st.font.color.rgb = RGBColor(241, 245, 249)

    p_tt = tf_h.add_paragraph()
    p_tt.text = title
    p_tt.font.name = FONT_HEADING
    p_tt.font.size = Pt(16)
    p_tt.font.bold = True
    p_tt.font.color.rgb = C_WHITE

    tb_b = s5.shapes.add_textbox(cx + Inches(0.25), Inches(2.9), col_w5 - Inches(0.5), Inches(3.4))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True
    p_bd = tf_b.paragraphs[0]
    p_bd.text = desc
    p_bd.font.name = FONT_BODY
    p_bd.font.size = Pt(12.5)
    p_bd.font.color.rgb = C_TEXT_DARK
    p_bd.line_spacing = 1.25

# -------------------------------------------------------------
# SLIDE 6: Problem Statement: Two Fatal Bottlenecks
# -------------------------------------------------------------
s6 = prs.slides.add_slide(blank_layout)
set_slide_background(s6)
add_header(s6, "Problem Statement", "Two Fatal Bottlenecks on HiddenBench",
           "Empirical failure patterns observed in closed autonomous multi-agent coordination")

add_card(s6, Inches(0.8), Inches(1.6), Inches(11.73), Inches(0.85), bg_color=C_BLUE_LIGHT, border_color=C_BLUE_ACCENT)
tb_lit = s6.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(11.3), Inches(0.65))
tf_lit = tb_lit.text_frame
tf_lit.word_wrap = True
p = tf_lit.paragraphs[0]
p.text = "Benchmark Vulnerability: Stasser & Stewart (1992) Replicated in AI"
p.font.name = FONT_HEADING
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = C_NAVY_BRAND
p_sub = tf_lit.add_paragraph()
p_sub.text = "Without external intervention, multi-agent systems fail 88.0% of hidden profile tasks, actively walking into disaster zones."
p_sub.font.name = FONT_BODY
p_sub.font.size = Pt(11.5)
p_sub.font.color.rgb = C_TEXT_DARK

bottlenecks6 = [
    ("Bottleneck 1: Private Fact Dismissal",
     "Unshared Vetoes Ignored in Favor of Common Positive Notes",
     "• When Agent 2 reports a severe route obstacle (tunnel fire), peers disregard it because their shared briefing describes the Mayor's volunteer program favorably.\n• Unshared facts suffer an 71% neglect rate (only 29.0% private coverage in Baseline).",
     C_RED_ACCENT, C_RED_LIGHT),
    ("Bottleneck 2: Sycophantic Consensus Lock",
     "Consensus Incentives Paralyze Truth Verification",
     "• In 22 out of 25 tasks (88.0%), the solitary agent holding the true disqualifier capitulated by Round 2.\n• The entire 4-agent committee unanimously chose the catastrophic distractor route.",
     C_ORANGE_ACCENT, C_ORANGE_LIGHT)
]

for idx, (b_title, b_sub, b_text, col, bg_c) in enumerate(bottlenecks6):
    bx = Inches(0.8) + idx * Inches(5.95)
    add_card(s6, bx, Inches(2.65), Inches(5.75), Inches(4.2), bg_color=C_WHITE, border_color=col)
    tb = s6.shapes.add_textbox(bx + Inches(0.3), Inches(2.85), Inches(5.15), Inches(3.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = b_title
    p.font.name = FONT_HEADING
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = col

    p_s = tf.add_paragraph()
    p_s.text = b_sub
    p_s.font.name = FONT_BODY
    p_s.font.size = Pt(12)
    p_s.font.bold = True
    p_s.font.color.rgb = C_NAVY_DARK
    p_s.space_before = Pt(4)

    p_body = tf.add_paragraph()
    p_body.text = b_text
    p_body.font.name = FONT_BODY
    p_body.font.size = Pt(12)
    p_body.font.color.rgb = C_TEXT_DARK
    p_body.space_before = Pt(12)
    p_body.line_spacing = 1.3

# -------------------------------------------------------------
# SLIDE 7: Motivation: Epistemic Scaffolding
# -------------------------------------------------------------
s7 = prs.slides.add_slide(blank_layout)
set_slide_background(s7)
add_header(s7, "Motivation", "Testing Human Epistemic Scaffolding",
           "Can an external observer rescue agents from the Common Knowledge Trap without leaking answers?")

add_card(s7, Inches(0.8), Inches(1.6), Inches(11.73), Inches(1.4), bg_color=C_NAVY_BRAND, border_color=C_BLUE_ACCENT)
tb_quote = s7.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(11.1), Inches(1.0))
tf_quote = tb_quote.text_frame
tf_quote.word_wrap = True
p = tf_quote.paragraphs[0]
p.text = '“Can humans scaffold multi-agent deliberations to pool unshared facts without giving away the solution?”'
p.font.name = FONT_HEADING
p.font.size = Pt(18)
p.font.bold = True
p.font.color.rgb = C_WHITE

p_qsub = tf_quote.add_paragraph()
p_qsub.text = "Validating minimal, procedural meta-interventions against autonomous common-knowledge paralysis."
p_qsub.font.name = FONT_BODY
p_qsub.font.size = Pt(12.5)
p_qsub.font.color.rgb = RGBColor(191, 219, 254)
p_qsub.space_before = Pt(6)

goals7 = [
    ("1. Bottleneck Detection (RQ 1)", "Can human observers accurately recognize when an unshared constraint is being suppressed by a confident majority?"),
    ("2. Information Pooling (RQ 2)", "Can procedural meta-hints force agents to synthesize siloed private facts (elevating fact coverage from 29% to 95%)?"),
    ("3. Moderator Failure (RQ 3)", "Why does an automated LLM moderator accelerate common-knowledge conformity instead of resolving it?")
]

for idx, (gt, gd) in enumerate(goals7):
    gx = Inches(0.8) + idx * Inches(3.98)
    add_card(s7, gx, Inches(3.2), Inches(3.75), Inches(3.7), bg_color=C_WHITE, border_color=C_BORDER)
    tb_g = s7.shapes.add_textbox(gx + Inches(0.25), Inches(3.4), Inches(3.25), Inches(3.3))
    tf_g = tb_g.text_frame
    tf_g.word_wrap = True
    p = tf_g.paragraphs[0]
    p.text = gt
    p.font.name = FONT_HEADING
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = C_BLUE_ACCENT

    p_desc = tf_g.add_paragraph()
    p_desc.text = gd
    p_desc.font.name = FONT_BODY
    p_desc.font.size = Pt(12)
    p_desc.font.color.rgb = C_TEXT_DARK
    p_desc.space_before = Pt(12)
    p_desc.line_spacing = 1.3

# -------------------------------------------------------------
# SLIDE 8: Methodology: Three-Condition Experimental Design
# -------------------------------------------------------------
s8 = prs.slides.add_slide(blank_layout)
set_slide_background(s8)
add_header(s8, "Methodology", "Three-Condition Experimental Design on HiddenBench",
           "Rigorous controlled benchmark evaluating 25 complex hidden profile scenarios")

rows = 4
cols = 4
table_shape = s8.shapes.add_table(rows, cols, Inches(0.8), Inches(1.7), Inches(11.73), Inches(4.9))
table = table_shape.table
table.columns[0].width = Inches(2.6)
table.columns[1].width = Inches(2.2)
table.columns[2].width = Inches(4.3)
table.columns[3].width = Inches(2.63)

headers = ["Experimental Condition", "Moderator / Observer", "Information Interaction Loop", "Primary Research Focus"]
for c_idx, h_text in enumerate(headers):
    cell = table.cell(0, c_idx)
    cell.fill.solid()
    cell.fill.fore_color.rgb = C_NAVY_BRAND
    p = cell.text_frame.paragraphs[0]
    p.text = h_text
    p.font.name = FONT_HEADING
    p.font.size = Pt(12.5)
    p.font.bold = True
    p.font.color.rgb = C_WHITE

data_conds8 = [
    ("Condition 1: Baseline\n(Pure MAD)", "None\n(Autonomous Loop)", "4 agents deliberate freely with shared + private notes. Majority vote.", "Baseline Common Knowledge\nBias & Conformity Collapse"),
    ("Condition 2: HITL\n(Human-in-the-Loop)", "Human Observer\n(External Scaffolding)", "Meta-hint injected at Round 2 upon detecting unshared constraint dismissal.", "RQ 1 (Detection Rate) &\nRQ 2 (Cross-Pooling Recovery)"),
    ("Condition 3: Agent-Moderated\n(LLM Moderator)", "LLM Moderator\n(Automated Peer)", "LLM synthesizes Round 1 & Round 2 transcripts, guiding group to consensus.", "RQ 3 (Inductive Bias Amplification\n& Moderator Failure)")
]

for r_idx, row_data in enumerate(data_conds8):
    for c_idx, val in enumerate(row_data):
        cell = table.cell(r_idx + 1, c_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_BLUE_LIGHT if r_idx == 1 else C_WHITE
        p = cell.text_frame.paragraphs[0]
        p.text = val
        p.font.name = FONT_BODY
        p.font.size = Pt(11.5)
        p.font.color.rgb = C_TEXT_DARK

# -------------------------------------------------------------
# SLIDE 9: Experimental Control: Controlled Protocol
# -------------------------------------------------------------
s9 = prs.slides.add_slide(blank_layout)
set_slide_background(s9)
add_header(s9, "Experimental Control", "Controlled Human Intervention Protocol",
           "Strict non-invasive rules prevent human observers from solving the hidden profile")

rules9 = [
    ("Rule 1: No Candidate Naming", "Never Reveal the Ground Truth",
     "The human monitor is strictly forbidden from naming West City, East Town, or North Hill, or expressing preference for any option. The observer must not act as an oracle.", C_RED_ACCENT),
    ("Rule 2: Procedural Scaffolding", "Direct Attention to Verification Criteria",
     "Hints are strictly procedural: 'Notice Agent X raised an unshared constraint regarding road access. Verify physical blockages before deciding on capacity.'", C_BLUE_ACCENT),
    ("Rule 3: Inflection Point Trigger", "Intervene Only at Round 2 Convergence",
     "Intervention occurs exclusively at Round 2 when majority consensus around the distractor begins to crush the dissenting private fact holder.", C_ORANGE_ACCENT)
]

for idx, (rt, rsub, rdesc, col) in enumerate(rules9):
    rx = Inches(0.8) + idx * Inches(3.98)
    add_card(s9, rx, Inches(1.8), Inches(3.75), Inches(4.8), bg_color=C_WHITE, border_color=col)
    top_ind = s9.shapes.add_shape(MSO_SHAPE.RECTANGLE, rx, Inches(1.8), Inches(3.75), Inches(0.12))
    top_ind.fill.solid()
    top_ind.fill.fore_color.rgb = col
    top_ind.line.fill.background()

    tb = s9.shapes.add_textbox(rx + Inches(0.25), Inches(2.1), Inches(3.25), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = rt
    p.font.name = FONT_HEADING
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = col

    p_sub = tf.add_paragraph()
    p_sub.text = rsub
    p_sub.font.name = FONT_BODY
    p_sub.font.size = Pt(12)
    p_sub.font.bold = True
    p_sub.font.color.rgb = C_NAVY_DARK
    p_sub.space_before = Pt(4)

    p_d = tf.add_paragraph()
    p_d.text = rdesc
    p_d.font.name = FONT_BODY
    p_d.font.size = Pt(12)
    p_d.font.color.rgb = C_TEXT_DARK
    p_d.space_before = Pt(12)
    p_d.line_spacing = 1.3

# -------------------------------------------------------------
# SLIDE 10: Implementation 01: System Architecture
# -------------------------------------------------------------
s10 = prs.slides.add_slide(blank_layout)
set_slide_background(s10)
add_header(s10, "Implementation 01", "Asymmetric Architecture & HITL Interface",
           "Information routing hub orchestrating shared knowledge, private dispatches, and human scaffolding")

fig_arch10 = fig_dir / "fig_hb_architecture.png"
if fig_arch10.exists():
    s10.shapes.add_picture(str(fig_arch10), Inches(0.8), Inches(1.6), Inches(7.6), Inches(5.1))

add_card(s10, Inches(8.6), Inches(1.6), Inches(3.93), Inches(5.1), bg_color=C_WHITE, border_color=C_BORDER)
tb_arch = s10.shapes.add_textbox(Inches(8.85), Inches(1.85), Inches(3.43), Inches(4.6))
tf_a = tb_arch.text_frame
tf_a.word_wrap = True
p = tf_a.paragraphs[0]
p.text = "Key System Components"
p.font.name = FONT_HEADING
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_NAVY_BRAND

arch_items10 = [
    ("Asymmetric Knowledge Hub", "Injects shared context to all 4 agents while strictly partitioning private dispatch facts into isolated context windows."),
    ("Turn-by-Turn Monitor", "Calculates real-time Private Fact Coverage and alerts the human monitor when a critical private constraint is dismissed."),
    ("Dual Intervention Router", "Directs identical Round 2 state streams to either procedural human meta-prompts or automated LLM moderator summaries.")
]

for at, ad in arch_items10:
    p_t = tf_a.add_paragraph()
    p_t.text = "• " + at
    p_t.font.name = FONT_HEADING
    p_t.font.size = Pt(12.5)
    p_t.font.bold = True
    p_t.font.color.rgb = C_BLUE_ACCENT
    p_t.space_before = Pt(12)

    p_d = tf_a.add_paragraph()
    p_d.text = ad
    p_d.font.name = FONT_BODY
    p_d.font.size = Pt(11)
    p_d.font.color.rgb = C_TEXT_DARK
    p_d.space_before = Pt(2)

# -------------------------------------------------------------
# SLIDE 11: Implementation 02: Prompt Engineering
# -------------------------------------------------------------
s11 = prs.slides.add_slide(blank_layout)
set_slide_background(s11)
add_header(s11, "Implementation 02", "Prompt Engineering & Epistemic Scaffolding",
           "Standardized prompts governing collaborative deliberation, human scaffolding, and LLM moderation")

prompts11 = [
    ("Debate Prompt: Collaborative Leader",
     'System: "You are acting as a community leader in a critical decision committee. You have shared announcements and private dispatch notes. Deliberate with peers to reach unanimous agreement on the safest option. Scrutinize all potential hazards before finalizing your choice."',
     C_BLUE_LIGHT, C_BLUE_ACCENT),
    ("HITL Injection: Procedural Scaffolding",
     'Observation Wrapper: "[Human Monitor Intervention - Round 2]: Notice that Agent 2 raised an unshared operational constraint regarding a massive tunnel fire, and Agent 4 holds private status on driveway access. Do not decide based only on shared capacity notes; verify all physical route blockages and road access before eliminating viable options."',
     C_ORANGE_LIGHT, C_ORANGE_ACCENT),
    ("Moderator Prompt: Consensus Synthesizer",
     'Moderator System: "You are the debate moderator. Synthesize the recommendations of all 4 community leaders. Identify emerging majority consensus, assess feasibility, and guide the committee toward a unified final decision before Round 3 closes."',
     C_RED_LIGHT, C_RED_ACCENT)
]

for idx, (p_title, p_code, bg_c, col) in enumerate(prompts11):
    py = Inches(1.6) + idx * Inches(1.75)
    add_card(s11, Inches(0.8), py, Inches(11.73), Inches(1.6), bg_color=bg_c, border_color=col)
    tb = s11.shapes.add_textbox(Inches(1.05), py + Inches(0.12), Inches(11.23), Inches(1.36))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = p_title
    p.font.name = FONT_HEADING
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = col

    p_code_p = tf.add_paragraph()
    p_code_p.text = p_code
    p_code_p.font.name = "Consolas"
    p_code_p.font.size = Pt(10.5)
    p_code_p.font.color.rgb = C_NAVY_DARK
    p_code_p.space_before = Pt(4)

# -------------------------------------------------------------
# SLIDE 12: Dataset & Setup: HiddenBench Benchmark Profile
# -------------------------------------------------------------
s12 = prs.slides.add_slide(blank_layout)
set_slide_background(s12)
add_header(s12, "Dataset & Setup", "HiddenBench Asymmetric Decision Benchmark",
           "25 complex multi-agent hidden profile scenarios across disaster logistics, psychology, and security")

stats12 = [
    ("25 Tasks", "High-Stakes Scenarios", "Evacuation, medical transfer, Stasser & Stewart, Antarctic storm", C_NAVY_BRAND),
    ("4 Agents", "Asymmetric Silos", "Agents 1-4 with 1 shared briefing + 4 partitioned private notes", C_BLUE_ACCENT),
    ("3 Rounds", "Synchronous Debate", "R1: Opening, R2: Scaffolding / Intervention, R3: Final vote", C_ORANGE_ACCENT)
]

for idx, (num, lbl, desc, col) in enumerate(stats12):
    sx = Inches(0.8) + idx * Inches(3.98)
    add_card(s12, sx, Inches(1.6), Inches(3.75), Inches(1.8), bg_color=C_WHITE, border_color=col)
    tb = s12.shapes.add_textbox(sx + Inches(0.25), Inches(1.75), Inches(3.25), Inches(1.5))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = num
    p.font.name = FONT_HEADING
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = col

    p_l = tf.add_paragraph()
    p_l.text = lbl
    p_l.font.name = FONT_HEADING
    p_l.font.size = Pt(13)
    p_l.font.bold = True
    p_l.font.color.rgb = C_NAVY_DARK
    p_l.space_before = Pt(2)

    p_d = tf.add_paragraph()
    p_d.text = desc
    p_d.font.name = FONT_BODY
    p_d.font.size = Pt(10.5)
    p_d.font.color.rgb = C_TEXT_MUTED
    p_d.space_before = Pt(2)

add_card(s12, Inches(0.8), Inches(3.6), Inches(11.73), Inches(3.2), bg_color=C_WHITE, border_color=C_BORDER)
tb_met = s12.shapes.add_textbox(Inches(1.1), Inches(3.8), Inches(11.1), Inches(2.8))
tf_m = tb_met.text_frame
tf_m.word_wrap = True
p = tf_m.paragraphs[0]
p.text = "Asymmetric Information Metrics & Logging Pipeline"
p.font.name = FONT_HEADING
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_NAVY_BRAND

metric_bullets12 = [
    ("Private Fact Coverage (%): ", "Measures the fraction of unshared private facts successfully introduced and actively cited in the collective transcript."),
    ("Common Knowledge Conformity (%): ", "Quantifies instances where an agent holding a private veto capitulates to a distractor favored by the uninformed majority."),
    ("Error Propagation Rate (%): ", "Tracks whether false assurances from shared notes cascade across rounds to blind the entire committee."),
    ("Human Bottleneck Detection (%): ", "Evaluates human precision in detecting when an unshared constraint is actively dismissed.")
]

for title, desc in metric_bullets12:
    p_b = tf_m.add_paragraph()
    p_b.text = "• " + title + desc
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(12)
    p_b.font.color.rgb = C_TEXT_DARK
    p_b.space_before = Pt(8)

# -------------------------------------------------------------
# SLIDE 13: Result 01 — RQ 1: Humans Spot Information Bottlenecks
# -------------------------------------------------------------
s13 = prs.slides.add_slide(blank_layout)
set_slide_background(s13)
add_header(s13, "Result 01 — RQ 1", "RQ 1: Humans Spot Information Bottlenecks Flawlessly",
           "100.0% of unshared constraint neglect events detected at Round 2 inflection points")

fig_rq1_13 = fig_dir / "fig_hb_metrics.png"
if fig_rq1_13.exists():
    s13.shapes.add_picture(str(fig_rq1_13), Inches(0.8), Inches(1.6), Inches(7.0), Inches(5.1))

add_card(s13, Inches(8.0), Inches(1.6), Inches(4.53), Inches(5.1), bg_color=C_WHITE, border_color=C_BORDER)
tb_r1 = s13.shapes.add_textbox(Inches(8.25), Inches(1.85), Inches(4.03), Inches(4.6))
tf_r1 = tb_r1.text_frame
tf_r1.word_wrap = True
p = tf_r1.paragraphs[0]
p.text = "Key RQ 1 Empirical Findings"
p.font.name = FONT_HEADING
p.font.size = Pt(17)
p.font.bold = True
p.font.color.rgb = C_NAVY_BRAND

findings_rq1_13 = [
    ("100% Bottleneck Detection (25/25)", "Human observers flawlessly spotted every instance where agents dismissed private dispatches as localized noise."),
    ("Cross-Pooling Catalysis (+65.8%p)", "Private Fact Coverage surged from 29.0% in Baseline to 94.8% in HITL, forcing all hidden notes onto the table."),
    ("Optimal Epistemic Scaffolding", "Intervening at Round 2 arrested conformity right as the minority agent began to express doubt about their private data.")
]

for ft, fd in findings_rq1_13:
    p_t = tf_r1.add_paragraph()
    p_t.text = "• " + ft
    p_t.font.name = FONT_HEADING
    p_t.font.size = Pt(13)
    p_t.font.bold = True
    p_t.font.color.rgb = C_BLUE_ACCENT
    p_t.space_before = Pt(14)
    p_d = tf_r1.add_paragraph()
    p_d.text = fd
    p_d.font.name = FONT_BODY
    p_d.font.size = Pt(11.5)
    p_d.font.color.rgb = C_TEXT_DARK
    p_d.space_before = Pt(3)

# -------------------------------------------------------------
# SLIDE 14: Result 02 — RQ 2: Human Scaffolding Breaks Traps
# -------------------------------------------------------------
s14 = prs.slides.add_slide(blank_layout)
set_slide_background(s14)
add_header(s14, "Result 02 — RQ 2", "RQ 2: Human Scaffolding Breaks Common Knowledge Traps",
           "Accuracy skyrockets from 12.0% to 100.0% (+88.0%p) while conformity drops to 0.0%")

fig_rq2_14 = fig_dir / "fig_hb_accuracy.png"
if fig_rq2_14.exists():
    s14.shapes.add_picture(str(fig_rq2_14), Inches(0.8), Inches(1.6), Inches(7.0), Inches(5.1))

add_card(s14, Inches(8.0), Inches(1.6), Inches(4.53), Inches(5.1), bg_color=C_WHITE, border_color=C_BORDER)
tb_r2 = s14.shapes.add_textbox(Inches(8.25), Inches(1.85), Inches(4.03), Inches(4.6))
tf_r2 = tb_r2.text_frame
tf_r2.word_wrap = True
p = tf_r2.paragraphs[0]
p.text = "Key RQ 2 Empirical Findings"
p.font.name = FONT_HEADING
p.font.size = Pt(17)
p.font.bold = True
p.font.color.rgb = C_NAVY_BRAND

findings_rq2_14 = [
    ("+88.0%p Ground Truth Surge", "Decision accuracy leapt from 12.0% (3/25) in Baseline to 100.0% (25/25) under HITL scaffolding."),
    ("100% Halting of Conformity", "Common Knowledge Conformity plummeted from 88.0% to 0.0%; zero agents capitulated to false distractor routes."),
    ("Pure Procedural Epistemics", "Because no candidates or answers were leaked, success was driven entirely by agents synthesizing their own distributed facts.")
]

for ft, fd in findings_rq2_14:
    p_t = tf_r2.add_paragraph()
    p_t.text = "• " + ft
    p_t.font.name = FONT_HEADING
    p_t.font.size = Pt(13)
    p_t.font.bold = True
    p_t.font.color.rgb = C_GREEN_ACCENT
    p_t.space_before = Pt(14)
    p_d = tf_r2.add_paragraph()
    p_d.text = fd
    p_d.font.name = FONT_BODY
    p_d.font.size = Pt(11.5)
    p_d.font.color.rgb = C_TEXT_DARK
    p_d.space_before = Pt(3)

# -------------------------------------------------------------
# SLIDE 15: Case Study: Task #1 (Evacuation Route Viability)
# -------------------------------------------------------------
s15 = prs.slides.add_slide(blank_layout)
set_slide_background(s15)
add_header(s15, "Case Study", "Task #1: Evacuation Route Viability Decision",
           "Comparing Baseline catastrophe (East Town trap) against HITL cross-pooling recovery (West City)")

fig_cs15 = fig_dir / "fig_hb_case_study.png"
if fig_cs15.exists():
    s15.shapes.add_picture(str(fig_cs15), Inches(0.8), Inches(1.6), Inches(5.7), Inches(2.6))

add_card(s15, Inches(0.8), Inches(4.35), Inches(5.7), Inches(2.35), bg_color=C_WHITE, border_color=C_BORDER)
tb_pt = s15.shapes.add_textbox(Inches(0.95), Inches(4.45), Inches(5.4), Inches(2.15))
tf_pt = tb_pt.text_frame
tf_pt.word_wrap = True
p = tf_pt.paragraphs[0]
p.text = "Task #1 Scenario Profile & Ground Truth: West City"
p.font.name = FONT_HEADING
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = C_NAVY_BRAND
p_body = tf_pt.add_paragraph()
p_body.text = '• Shared Distractor (East Town): Mayor offers shelter & volunteers. West City flagged for lacking medical supplies.\n• Hidden Vetoes: Agent 1 (truck stuck in tunnel), Agent 2 (massive tunnel fire), Agent 3 (trails closed), Agent 4 (driveway mudslide).\n• Ground Truth: West City bridge is open and river below crest level!'
p_body.font.name = FONT_BODY
p_body.font.size = Pt(10.5)
p_body.font.color.rgb = C_TEXT_DARK
p_body.space_before = Pt(4)

add_card(s15, Inches(6.8), Inches(1.6), Inches(5.73), Inches(2.55), bg_color=C_RED_LIGHT, border_color=C_RED_ACCENT)
tb_b = s15.shapes.add_textbox(Inches(6.95), Inches(1.7), Inches(5.43), Inches(2.35))
tf_b = tb_b.text_frame
tf_b.word_wrap = True
p = tf_b.paragraphs[0]
p.text = "Baseline Deliberation: Catastrophic Conformity"
p.font.name = FONT_HEADING
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = C_RED_ACCENT
p_log1 = tf_b.add_paragraph()
p_log1.text = "• Round 1: Agent 2 mentions tunnel fire. Agents 1, 3, 4 favor East Town.\n• Round 2: Agents dismiss fire as a 'local rumor' and cite Mayor's guarantee.\n• Round 3: Agent 2 concedes: 'Since all 3 favor East Town, I align.'\n-> Outcome: FAILED (Villagers evacuated directly into a burning tunnel!)."
p_log1.font.name = FONT_BODY
p_log1.font.size = Pt(10)
p_log1.font.color.rgb = C_TEXT_DARK
p_log1.space_before = Pt(2)

add_card(s15, Inches(6.8), Inches(4.35), Inches(5.73), Inches(2.35), bg_color=C_GREEN_LIGHT, border_color=C_GREEN_ACCENT)
tb_h = s15.shapes.add_textbox(Inches(6.95), Inches(4.45), Inches(5.43), Inches(2.15))
tf_h = tb_h.text_frame
tf_h.word_wrap = True
p = tf_h.paragraphs[0]
p.text = "HITL Scaffolding: Cross-Pooling Ground Truth Recovery"
p.font.name = FONT_HEADING
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = C_GREEN_ACCENT
p_log2 = tf_h.add_paragraph()
p_log2.text = "• Round 2 Meta-Hint: 'Notice Agent 2 raised a tunnel fire. Verify physical route access before deciding on shared capacity.'\n• Round 2 Pooling: Agent 1 combines stuck truck with fire -> East Town impassable! Agent 4 reveals driveway mudslide -> North Hill blocked!\n• Round 3: All 4 agents unanimously converge on West City (Bridge open!)."
p_log2.font.name = FONT_BODY
p_log2.font.size = Pt(10)
p_log2.font.color.rgb = C_TEXT_DARK
p_log2.space_before = Pt(2)

# -------------------------------------------------------------
# SLIDE 16: Result 03 — RQ 3 (Quantitative): Oversight vs Moderator
# -------------------------------------------------------------
s16 = prs.slides.add_slide(blank_layout)
set_slide_background(s16)
add_header(s16, "Result 03 — RQ 3 (Quantitative)", "Human Oversight vs. Autonomous LLM Moderator",
           "LLM moderators suffer from Common Knowledge Bias, codifying majority sycophancy")

# Table
table_shape3 = s16.shapes.add_table(6, 4, Inches(0.8), Inches(1.6), Inches(6.5), Inches(5.1))
tab3 = table_shape3.table
tab3.columns[0].width = Inches(2.6)
tab3.columns[1].width = Inches(1.3)
tab3.columns[2].width = Inches(1.3)
tab3.columns[3].width = Inches(1.3)

headers3 = ["Performance Metric", "Baseline", "LLM Mod", "HITL"]
for c, h in enumerate(headers3):
    cell = tab3.cell(0, c)
    cell.fill.solid()
    cell.fill.fore_color.rgb = C_NAVY_BRAND
    p = cell.text_frame.paragraphs[0]
    p.text = h
    p.font.name = FONT_HEADING
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_WHITE

data_tab3 = [
    ("Decision Accuracy (%)", "12.0%", "16.0%", "100.0%"),
    ("Conformity Bias (%)", "88.0%", "84.0%", "0.0%"),
    ("Private Fact Coverage (%)", "29.0%", "30.8%", "94.8%"),
    ("Error Propagation (%)", "88.0%", "84.0%", "0.0%"),
    ("Intervention Freq.", "0 / task", "1.0 / task", "0.96 / task")
]

for r_idx, row in enumerate(data_tab3):
    for c_idx, val in enumerate(row):
        cell = tab3.cell(r_idx + 1, c_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_GREEN_LIGHT if c_idx == 3 else C_WHITE
        p = cell.text_frame.paragraphs[0]
        p.text = val
        p.font.name = FONT_BODY
        p.font.size = Pt(10.5)
        p.font.bold = (c_idx == 3 or c_idx == 0)
        p.font.color.rgb = C_GREEN_ACCENT if c_idx == 3 and r_idx in [0, 2] else C_TEXT_DARK

# Right Narrative Card
add_card(s16, Inches(7.6), Inches(1.6), Inches(4.93), Inches(5.1), bg_color=C_WHITE, border_color=C_BORDER)
tb_q3 = s16.shapes.add_textbox(Inches(7.85), Inches(1.85), Inches(4.43), Inches(4.6))
tf_q3 = tb_q3.text_frame
tf_q3.word_wrap = True
p = tf_q3.paragraphs[0]
p.text = "Quantitative RQ 3 Analysis"
p.font.name = FONT_HEADING
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_NAVY_BRAND

insights_q3 = [
    ("Marginal 4.0%p LLM Gain", "The autonomous LLM moderator produced virtually zero benefit (16.0% accuracy vs 12.0% baseline)."),
    ("Institutionalized Sycophancy", "In 21 out of 25 tasks (84.0%), the moderator actively scolded minority dissenters for deviating from the 'majority consensus'."),
    ("The Need for External Grounding", "Because LLM moderators cannot escape their in-distribution sampling bias, human oversight remains irreplaceable.")
]

for it, id_text in insights_q3:
    p_t = tf_q3.add_paragraph()
    p_t.text = "• " + it
    p_t.font.name = FONT_HEADING
    p_t.font.size = Pt(12.5)
    p_t.font.bold = True
    p_t.font.color.rgb = C_RED_ACCENT if "Sycophancy" in it else C_BLUE_ACCENT
    p_t.space_before = Pt(12)
    p_d = tf_q3.add_paragraph()
    p_d.text = id_text
    p_d.font.name = FONT_BODY
    p_d.font.size = Pt(11)
    p_d.font.color.rgb = C_TEXT_DARK
    p_d.space_before = Pt(2)

# -------------------------------------------------------------
# SLIDE 17: Result 03 — RQ 3 (Qualitative): Why LLM Moderators Fail
# -------------------------------------------------------------
s17 = prs.slides.add_slide(blank_layout)
set_slide_background(s17)
add_header(s17, "Result 03 — RQ 3 (Qualitative)", "Why LLM Moderators Institutionalize Common Bias",
           "Epistemic vulnerabilities inherent to language model summarization and vote weighting")

reasons17 = [
    ("Frequency Heuristic", "Mistaking Mention Count for Epistemic Truth",
     "• LLM attention weights correlate strongly with token frequency across dialogue turns.\n• Because 3 agents repeat shared claims, the moderator scores the distractor as mathematically more probable.", C_RED_ACCENT),
    ("Authority Bias", "Over-Weighting Official Municipal Statements",
     "• Shared briefings often feature formal language ('The Mayor officially guarantees accommodations').\n• The moderator treats official rhetoric as infallible while discounting field dispatches.", C_ORANGE_ACCENT),
    ("Human Epistemic Grounding", "Independent Causal Modeling",
     "• Humans model physical causality: 'If a tunnel is on fire, no amount of volunteer support can make it passable.'\n• External humans recognize that physical constraints invalidate social consensus.", C_GREEN_ACCENT)
]

for idx, (rt, rsub, rdesc, col) in enumerate(reasons17):
    rx = Inches(0.8) + idx * Inches(3.98)
    add_card(s17, rx, Inches(1.8), Inches(3.75), Inches(4.8), bg_color=C_WHITE, border_color=col)
    top_ind = s17.shapes.add_shape(MSO_SHAPE.RECTANGLE, rx, Inches(1.8), Inches(3.75), Inches(0.12))
    top_ind.fill.solid()
    top_ind.fill.fore_color.rgb = col
    top_ind.line.fill.background()

    tb = s17.shapes.add_textbox(rx + Inches(0.25), Inches(2.1), Inches(3.25), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = rt
    p.font.name = FONT_HEADING
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = col

    p_sub = tf.add_paragraph()
    p_sub.text = rsub
    p_sub.font.name = FONT_BODY
    p_sub.font.size = Pt(11.5)
    p_sub.font.bold = True
    p_sub.font.color.rgb = C_NAVY_DARK
    p_sub.space_before = Pt(4)

    p_d = tf.add_paragraph()
    p_d.text = rdesc
    p_d.font.name = FONT_BODY
    p_d.font.size = Pt(12)
    p_d.font.color.rgb = C_TEXT_DARK
    p_d.space_before = Pt(12)
    p_d.line_spacing = 1.3

# -------------------------------------------------------------
# SLIDE 18: Cross-Benchmark Synthesis: GSM8K vs HiddenBench
# -------------------------------------------------------------
s18 = prs.slides.add_slide(blank_layout)
set_slide_background(s18)
add_header(s18, "Cross-Benchmark Synthesis", "Comparative Analysis: GSM8K vs. HiddenBench",
           "Comparing human oversight across internal arithmetic vs. asymmetric information silos")

# Two Comparison Cards
add_card(s18, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.2), bg_color=C_WHITE, border_color=C_BLUE_ACCENT)
tb_gsm = s18.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.1), Inches(4.8))
tf_g = tb_gsm.text_frame
tf_g.word_wrap = True
p = tf_g.paragraphs[0]
p.text = "GSM8K: Internal Calculation Slippage"
p.font.name = FONT_HEADING
p.font.size = Pt(17)
p.font.bold = True
p.font.color.rgb = C_BLUE_ACCENT
p_gsub = tf_g.add_paragraph()
p_gsub.text = "Arithmetic Brittleness in Symmetric Settings"
p_gsub.font.name = FONT_BODY
p_gsub.font.size = Pt(12)
p_gsub.font.color.rgb = C_TEXT_MUTED
p_gsub.space_before = Pt(4)

gsm_points = [
    ("Baseline Accuracy: 36.7%", "Debaters make calculation slips (e.g. discounting all jackets instead of pairs)."),
    ("HITL Accuracy: 100.0% (+63.3%p)", "A simple prompt to re-check Step 2 allows agents to re-compute correctly."),
    ("Symmetric Context", "All agents see the exact same prompt; failure is purely computational.")
]
for title, d in gsm_points:
    p_t = tf_g.add_paragraph()
    p_t.text = "• " + title
    p_t.font.name = FONT_HEADING
    p_t.font.size = Pt(13)
    p_t.font.bold = True
    p_t.font.color.rgb = C_NAVY_DARK
    p_t.space_before = Pt(14)
    p_d = tf_g.add_paragraph()
    p_d.text = d
    p_d.font.name = FONT_BODY
    p_d.font.size = Pt(11.5)
    p_d.font.color.rgb = C_TEXT_DARK
    p_d.space_before = Pt(2)

add_card(s18, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2), bg_color=C_WHITE, border_color=C_ORANGE_ACCENT)
tb_hb = s18.shapes.add_textbox(Inches(7.1), Inches(1.8), Inches(5.1), Inches(4.8))
tf_h = tb_hb.text_frame
tf_h.word_wrap = True
p = tf_h.paragraphs[0]
p.text = "HiddenBench: Epistemic Asymmetry"
p.font.name = FONT_HEADING
p.font.size = Pt(17)
p.font.bold = True
p.font.color.rgb = C_ORANGE_ACCENT
p_hsub = tf_h.add_paragraph()
p_hsub.text = "Sociological Bottlenecks in Asymmetric Settings"
p_hsub.font.name = FONT_BODY
p_hsub.font.size = Pt(12)
p_hsub.font.color.rgb = C_TEXT_MUTED
p_hsub.space_before = Pt(4)

hb_points = [
    ("Baseline Accuracy: 12.0%", "Catastrophic collapse; 88% conformity to fatal distractor routes."),
    ("HITL Accuracy: 100.0% (+88.0%p)", "Human procedural scaffolding forces cross-silo fact integration."),
    ("Asymmetric Context", "Information is partitioned; failure is epistemic and sociological, making human oversight far more vital!")
]
for title, d in hb_points:
    p_t = tf_h.add_paragraph()
    p_t.text = "• " + title
    p_t.font.name = FONT_HEADING
    p_t.font.size = Pt(13)
    p_t.font.bold = True
    p_t.font.color.rgb = C_NAVY_DARK
    p_t.space_before = Pt(14)
    p_d = tf_h.add_paragraph()
    p_d.text = d
    p_d.font.name = FONT_BODY
    p_d.font.size = Pt(11.5)
    p_d.font.color.rgb = C_TEXT_DARK
    p_d.space_before = Pt(2)

# -------------------------------------------------------------
# SLIDE 19: Summary: Key Takeaways Across RQ 1–3
# -------------------------------------------------------------
s19 = prs.slides.add_slide(blank_layout)
set_slide_background(s19)
add_header(s19, "Summary", "Key Takeaways Across RQ 1–3 on HiddenBench",
           "Core empirical conclusions validating human oversight in asymmetric multi-agent coordination")

takeaways19 = [
    ("RQ 1: Flawless Bottleneck Detection", "100% Precision at Round 2",
     "Human observers reliably detect unshared fact neglect and sycophantic capitulation before consensus freezes, achieving optimal intervention timing.", C_BLUE_ACCENT),
    ("RQ 2: Massive Cross-Pooling Gain", "+88.0%p Decision Accuracy Surge",
     "Procedural scaffolding boosts private fact coverage from 29% to 95%, completely eliminating common-knowledge conformity without answer disclosure.", C_GREEN_ACCENT),
    ("RQ 3: Indispensable Human Grounding", "In-Distribution LLM Moderators Fail",
     "Autonomous LLM moderators fall prey to the exact same frequency heuristic, proving that external human grounding is structurally irreplaceable.", C_NAVY_BRAND)
]

for idx, (tt, tsub, tdesc, col) in enumerate(takeaways19):
    tx = Inches(0.8) + idx * Inches(3.98)
    add_card(s19, tx, Inches(1.8), Inches(3.75), Inches(4.8), bg_color=C_WHITE, border_color=col)
    top_ind = s19.shapes.add_shape(MSO_SHAPE.RECTANGLE, tx, Inches(1.8), Inches(3.75), Inches(0.12))
    top_ind.fill.solid()
    top_ind.fill.fore_color.rgb = col
    top_ind.line.fill.background()

    tb = s19.shapes.add_textbox(tx + Inches(0.25), Inches(2.1), Inches(3.25), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = tt
    p.font.name = FONT_HEADING
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = col

    p_s = tf.add_paragraph()
    p_s.text = tsub
    p_s.font.name = FONT_BODY
    p_s.font.size = Pt(12)
    p_s.font.bold = True
    p_s.font.color.rgb = C_NAVY_DARK
    p_s.space_before = Pt(4)

    p_d = tf.add_paragraph()
    p_d.text = tdesc
    p_d.font.name = FONT_BODY
    p_d.font.size = Pt(12)
    p_d.font.color.rgb = C_TEXT_DARK
    p_d.space_before = Pt(12)
    p_d.line_spacing = 1.3

# -------------------------------------------------------------
# SLIDE 20: Future Work & Q&A
# -------------------------------------------------------------
s20 = prs.slides.add_slide(blank_layout)
set_slide_background(s20, C_NAVY_DARK)

tb_end = s20.shapes.add_textbox(Inches(1.0), Inches(1.2), Inches(11.3), Inches(5.0))
tf_end = tb_end.text_frame
tf_end.word_wrap = True

p_f = tf_end.paragraphs[0]
p_f.text = "FUTURE RESEARCH DIRECTIONS"
p_f.font.name = FONT_HEADING
p_f.font.size = Pt(13)
p_f.font.bold = True
p_f.font.color.rgb = C_ORANGE_ACCENT

p_fw1 = tf_end.add_paragraph()
p_fw1.text = "1. Information-Gap Uncertainty Gates for Automated HITL Paging"
p_fw1.font.name = FONT_HEADING
p_fw1.font.size = Pt(18)
p_fw1.font.bold = True
p_fw1.font.color.rgb = C_WHITE
p_fw1.space_before = Pt(12)

p_fw1_d = tf_end.add_paragraph()
p_fw1_d.text = "Develop semantic novelty and unshared token coverage estimators (Counterfactual Grounding Gates) that automatically page human supervisors only when private fact suppression exceeds anomaly thresholds."
p_fw1_d.font.name = FONT_BODY
p_fw1_d.font.size = Pt(12.5)
p_fw1_d.font.color.rgb = RGBColor(203, 213, 225)
p_fw1_d.space_before = Pt(4)

p_fw2 = tf_end.add_paragraph()
p_fw2.text = "2. High-Stakes Real-World Crisis Teaming"
p_fw2.font.name = FONT_HEADING
p_fw2.font.size = Pt(18)
p_fw2.font.bold = True
p_fw2.font.color.rgb = C_WHITE
p_fw2.space_before = Pt(16)

p_fw2_d = tf_end.add_paragraph()
p_fw2_d.text = "Deploy procedural HITL scaffolding in multi-agency disaster response, cyber-incident triage, and intelligence fusion where asymmetric data silos are standard."
p_fw2_d.font.name = FONT_BODY
p_fw2_d.font.size = Pt(12.5)
p_fw2_d.font.color.rgb = RGBColor(203, 213, 225)
p_fw2_d.space_before = Pt(4)

p_qa = tf_end.add_paragraph()
p_qa.text = "Thank you!  •  Questions & Discussion"
p_qa.font.name = FONT_HEADING
p_qa.font.size = Pt(26)
p_qa.font.bold = True
p_qa.font.color.rgb = RGBColor(147, 197, 253)
p_qa.space_before = Pt(32)

prs.save(str(pptx_path))
print(f"Presentation saved successfully to: {pptx_path}")
print(f"Total slides created: {len(prs.slides)}")
