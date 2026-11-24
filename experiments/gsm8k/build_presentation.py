import sys
import os
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# 1. Initialize Presentation
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6] # completely blank layout

# Output paths
work_dir = Path(r"C:\Users\GC\.gemini\antigravity\scratch\hitl_mad_gsm8k")
fig_dir = work_dir / "figures"
pptx_path = work_dir / "Human_in_the_Loop_Multi_Agent_Debate_GSM8K.pptx"

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
    # Category tag
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

    # Main Title
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

# Decorative card
dec_card = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.5), Inches(0.12), Inches(4.5))
dec_card.fill.solid()
dec_card.fill.fore_color.rgb = C_BLUE_ACCENT
dec_card.line.fill.background()

tb = s1.shapes.add_textbox(Inches(1.2), Inches(1.4), Inches(11.0), Inches(4.8))
tf = tb.text_frame
tf.word_wrap = True

p_badge = tf.paragraphs[0]
p_badge.text = "RESEARCH PROJECT PRESENTATION"
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
p2.text = "Bottleneck Detection and Error Resolution on GSM8K"
p2.font.name = FONT_HEADING
p2.font.size = Pt(24)
p2.font.bold = True
p2.font.color.rgb = RGBColor(147, 197, 253) # Light Blue
p2.space_before = Pt(8)

p_author = tf.add_paragraph()
p_author.text = "Author: Min Jae Kang  |  Student ID: 202645469"
p_author.font.name = FONT_BODY
p_author.font.size = Pt(15)
p_author.font.color.rgb = RGBColor(226, 232, 240)
p_author.space_before = Pt(36)

p_affil = tf.add_paragraph()
p_affil.text = "Benchmark: GSM8K Math Reasoning  •  Multi-Agent Debate (MAD) Oversight"
p_affil.font.name = FONT_BODY
p_affil.font.size = Pt(13)
p_affil.font.color.rgb = C_TEXT_MUTED
p_affil.space_before = Pt(6)

# -------------------------------------------------------------
# SLIDE 2: Overview & Core Topic (Talk Roadmap & Central RQs)
# -------------------------------------------------------------
s2 = prs.slides.add_slide(blank_layout)
set_slide_background(s2)
add_header(s2, "Overview & Core Topic", "Talk Roadmap & Central Research Questions",
           "Investigating whether external human oversight can break closed-system debate bottlenecks")

# Central Research Question Banner
add_card(s2, Inches(0.8), Inches(1.5), Inches(11.73), Inches(1.15), bg_color=C_BLUE_LIGHT, border_color=C_BLUE_ACCENT)
tb_rq = s2.shapes.add_textbox(Inches(1.0), Inches(1.6), Inches(11.3), Inches(0.95))
tf_rq = tb_rq.text_frame
tf_rq.word_wrap = True
p = tf_rq.paragraphs[0]
p.text = "Core Question: Can Human Oversight Fix Closed Multi-Agent Debates?"
p.font.name = FONT_HEADING
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_NAVY_BRAND

p_sub = tf_rq.add_paragraph()
p_sub.text = "Testing Bottleneck Detection (RQ 1), Error Resolution (RQ 2), and Autonomous LLM Moderator Limits (RQ 3) on GSM8K."
p_sub.font.name = FONT_BODY
p_sub.font.size = Pt(12.5)
p_sub.font.color.rgb = C_TEXT_DARK
p_sub.space_before = Pt(4)

# 4 Roadmap Columns
roadmap = [
    ("01 Background", "MAD Bottlenecks", "Conformity bias and error propagation in autonomous multi-round debates.", C_NAVY_BRAND, C_BLUE_LIGHT),
    ("02 Method", "HITL Pipeline", "Turn-by-turn monitoring & non-invasive meta-level feedback protocol on GSM8K.", C_BLUE_ACCENT, C_BLUE_LIGHT),
    ("03 Results", "RQ 1–3 Findings", "Empirical validation: human detection, recovery rates, and moderator failure.", C_ORANGE_ACCENT, C_ORANGE_LIGHT),
    ("04 Conclusion", "Future Outlook", "Adaptive entropy triggers and scalable hybrid human-agent orchestration.", C_GREEN_ACCENT, C_GREEN_LIGHT)
]

col_w = Inches(2.76)
gap = Inches(0.23)
start_l = Inches(0.8)
top_y = Inches(2.9)
card_h = Inches(4.0)

for idx, (step_num, title, desc, col_c, bg_c) in enumerate(roadmap):
    cx = start_l + idx * (col_w + gap)
    add_card(s2, cx, top_y, col_w, card_h, bg_color=C_WHITE, border_color=C_BORDER)

    # Top accent bar
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
# SLIDE 3: Background 01: What is a Large Language Model (LLM)?
# -------------------------------------------------------------
s3 = prs.slides.add_slide(blank_layout)
set_slide_background(s3)
add_header(s3, "Background 01", "What is a Large Language Model (LLM)?",
           "Foundational capabilities and the core multi-step reasoning bottleneck")

llm_points = [
    ("Foundation Model", "Pretrained on Massive Text Corpora",
     "Trained via self-supervised learning on billions of tokens to capture linguistic syntax, common-sense facts, and generative flow.", C_NAVY_BRAND),
    ("Context Comprehension", "Complex Semantic Modeling",
     "In-context attention mechanisms extract subtle semantic nuances and multi-turn conversational instructions effectively.", C_BLUE_ACCENT),
    ("General-Purpose Generation", "Zero-Shot Breadth",
     "Excels at open-ended dialogue, summarization, qualitative comparison, and straightforward instruction-following.", C_GREEN_ACCENT),
    ("Multi-Step Bottleneck", "Arithmetic & Logical Brittleness",
     "Single LLMs struggle when tasks require error-intolerant, strict sequential math deductions where a single slip cascades into complete failure.", C_RED_ACCENT)
]

w3 = Inches(5.7)
h3 = Inches(2.4)
coords3 = [
    (Inches(0.8), Inches(1.6)),
    (Inches(6.8), Inches(1.6)),
    (Inches(0.8), Inches(4.3)),
    (Inches(6.8), Inches(4.3))
]

for idx, (t, sub, desc, col) in enumerate(llm_points):
    px, py = coords3[idx]
    add_card(s3, px, py, w3, h3, bg_color=C_WHITE, border_color=col if idx==3 else C_BORDER)

    # Accent stripe
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
# SLIDE 4: Background 02: From Single LLM to Multi-Agent Systems
# -------------------------------------------------------------
s4 = prs.slides.add_slide(blank_layout)
set_slide_background(s4)
add_header(s4, "Background 02", "From Single LLM to Multi-Agent Systems",
           "Overcoming individual model limitations through collaborative debate architecture")

# 2 Major Columns: Single LLM Limitations vs Multi-Agent Paradigm
add_card(s4, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.2), bg_color=C_WHITE, border_color=C_RED_ACCENT)
tb_l = s4.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.1), Inches(4.8))
tf_l = tb_l.text_frame
tf_l.word_wrap = True

p = tf_l.paragraphs[0]
p.text = "Previous Paradigm: Single LLM"
p.font.name = FONT_HEADING
p.font.size = Pt(18)
p.font.bold = True
p.font.color.rgb = C_RED_ACCENT

p_sub = tf_l.add_paragraph()
p_sub.text = "Structural Vulnerabilities in Multi-Step Tasks"
p_sub.font.name = FONT_BODY
p_sub.font.size = Pt(12)
p_sub.font.color.rgb = C_TEXT_MUTED
p_sub.space_before = Pt(4)

items_single = [
    ("Hallucination Cascades", "A subtle calculation slip in Step 1 compounds exponentially across subsequent derivation steps."),
    ("Self-Correction Rigidity", "Models rarely reverse erroneous initial assumptions during greedy autoregressive decoding."),
    ("Tunnel Vision", "Lacks alternative problem representations or counter-argument verification pathways.")
]

for title, d in items_single:
    p_t = tf_l.add_paragraph()
    p_t.text = "• " + title
    p_t.font.name = FONT_HEADING
    p_t.font.size = Pt(13.5)
    p_t.font.bold = True
    p_t.font.color.rgb = C_NAVY_DARK
    p_t.space_before = Pt(14)

    p_d = tf_l.add_paragraph()
    p_d.text = d
    p_d.font.name = FONT_BODY
    p_d.font.size = Pt(11.5)
    p_d.font.color.rgb = C_TEXT_DARK
    p_d.space_before = Pt(2)

# Multi-Agent Paradigm Card
add_card(s4, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2), bg_color=C_WHITE, border_color=C_BLUE_ACCENT)
tb_r = s4.shapes.add_textbox(Inches(7.1), Inches(1.8), Inches(5.1), Inches(4.8))
tf_r = tb_r.text_frame
tf_r.word_wrap = True

p = tf_r.paragraphs[0]
p.text = "Collaborative Shift: Multi-Agent Paradigm"
p.font.name = FONT_HEADING
p.font.size = Pt(18)
p.font.bold = True
p.font.color.rgb = C_BLUE_ACCENT

p_sub = tf_r.add_paragraph()
p_sub.text = "Structured Interaction & Distributed Verification"
p_sub.font.name = FONT_BODY
p_sub.font.size = Pt(12)
p_sub.font.color.rgb = C_TEXT_MUTED
p_sub.space_before = Pt(4)

items_multi = [
    ("Diverse Solution Paths", "Multiple autonomous agents generate independent interpretations and intermediate equations."),
    ("Peer Cross-Examination", "Agents actively inspect rival solutions, exposing arithmetic discrepancies and invalid bounds."),
    ("Collective Accuracy Gain", "Group synthesis filters individual blind spots, converging on validated mathematical ground truth.")
]

for title, d in items_multi:
    p_t = tf_r.add_paragraph()
    p_t.text = "• " + title
    p_t.font.name = FONT_HEADING
    p_t.font.size = Pt(13.5)
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
# SLIDE 5: Background 03: How Multi-Agent Debate Works
# -------------------------------------------------------------
s5 = prs.slides.add_slide(blank_layout)
set_slide_background(s5)
add_header(s5, "Background 03", "How Multi-Agent Debate Works",
           "Standard 3-stage protocol: independent generation, cross-critique, and consensus formation")

steps = [
    ("Stage 1", "Initial Generation", "Each debater agent independently reads the problem prompt and generates a zero-shot step-by-step derivation without peer exposure.", C_NAVY_BRAND),
    ("Stage 2", "Iterative Critique", "Agents inspect peers' intermediate variables and equations in synchronized rounds, challenging discrepancies and defending arguments.", C_BLUE_ACCENT),
    ("Stage 3", "Consensus Formation", "Agents converge towards an agreed numerical result through majority consensus or unified revision across final debate rounds.", C_GREEN_ACCENT)
]

col_w5 = Inches(3.7)
gap5 = Inches(0.3)
start_l5 = Inches(0.8)

for idx, (stage, title, desc, col) in enumerate(steps):
    cx = start_l5 + idx * (col_w5 + gap5)
    add_card(s5, cx, Inches(1.8), col_w5, Inches(4.8), bg_color=C_WHITE, border_color=C_BORDER)

    # Header block inside card
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

    # Body
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
# SLIDE 6: Problem Statement: Two Bottlenecks in Closed Debates
# -------------------------------------------------------------
s6 = prs.slides.add_slide(blank_layout)
set_slide_background(s6)
add_header(s6, "Problem Statement", "Two Bottlenecks in Closed Multi-Agent Debates",
           "Systemic interaction failures identified in autonomous LLM collaboration (Guo et al., IJCAI 2024)")

# Prior literature banner
add_card(s6, Inches(0.8), Inches(1.6), Inches(11.73), Inches(0.85), bg_color=C_BLUE_LIGHT, border_color=C_BLUE_ACCENT)
tb_lit = s6.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(11.3), Inches(0.65))
tf_lit = tb_lit.text_frame
tf_lit.word_wrap = True
p = tf_lit.paragraphs[0]
p.text = "Theoretical Foundation: Guo et al. (IJCAI 2024)"
p.font.name = FONT_HEADING
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = C_NAVY_BRAND
p_sub = tf_lit.add_paragraph()
p_sub.text = "Prior empirical studies demonstrate that multi-agent debate often deteriorates into severe interaction pathology rather than truthful convergence."
p_sub.font.name = FONT_BODY
p_sub.font.size = Pt(11.5)
p_sub.font.color.rgb = C_TEXT_DARK

# 2 Bottlenecks Cards
bottlenecks = [
    ("Bottleneck 1: Error Propagation",
     "Early Hallucinations Infect the Closed System",
     "• When an agent introduces a plausible-sounding arithmetic error in Round 1, peer agents frequently adopt it without deep recalculation.\n• Flawed formulas replicate virally across turns, cementing incorrect intermediate premises.",
     C_RED_ACCENT, C_RED_LIGHT),
    ("Bottleneck 2: Conformity Bias",
     "Sycophancy & Majority Pressure Overpower Truth",
     "• Solitary agents holding mathematically sound minority solutions capitulate when confronted by a confident 2-agent majority.\n• Rational minority logic is systematically abandoned for false consensus (Social Proof trap).",
     C_ORANGE_ACCENT, C_ORANGE_LIGHT)
]

for idx, (b_title, b_sub, b_text, col, bg_c) in enumerate(bottlenecks):
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
# SLIDE 7: Motivation: Testing External Human Oversight
# -------------------------------------------------------------
s7 = prs.slides.add_slide(blank_layout)
set_slide_background(s7)
add_header(s7, "Motivation", "Testing External Human Oversight in Multi-Agent Debate",
           "Can an external observer recognize debate inflection points and break closed-system conformity?")

# Central Callout Card
add_card(s7, Inches(0.8), Inches(1.6), Inches(11.73), Inches(1.4), bg_color=C_NAVY_BRAND, border_color=C_BLUE_ACCENT)
tb_quote = s7.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(11.1), Inches(1.0))
tf_quote = tb_quote.text_frame
tf_quote.word_wrap = True
p = tf_quote.paragraphs[0]
p.text = '“When humans observe closed agent debates, can they recognize and break conformity loops?”'
p.font.name = FONT_HEADING
p.font.size = Pt(18)
p.font.bold = True
p.font.color.rgb = C_WHITE

p_qsub = tf_quote.add_paragraph()
p_qsub.text = "Investigating human intervention as a minimally intrusive, meta-level grounding signal against autonomous stagnation."
p_qsub.font.name = FONT_BODY
p_qsub.font.size = Pt(12.5)
p_qsub.font.color.rgb = RGBColor(191, 219, 254)
p_qsub.space_before = Pt(6)

# 3 Concrete Investigation Goals
goals = [
    ("1. Bottleneck Detection (RQ 1)", "Can human observers accurately spot conformity inflection points and cascading error propagation before consensus freezes?"),
    ("2. Error Resolution (RQ 2)", "Can non-invasive meta-level hints (without revealing answers) successfully rescue agents from false consensus?"),
    ("3. Moderator Comparison (RQ 3)", "How does external human grounding compare to an automated LLM moderator sharing the same underlying model biases?")
]

for idx, (gt, gd) in enumerate(goals):
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
add_header(s8, "Methodology", "Three-Condition Experimental Design",
           "Controlled benchmark comparison to isolate the causal impact of human oversight")

# Add Table for 3 Conditions
rows = 4
cols = 4
left_t = Inches(0.8)
top_t = Inches(1.7)
width_t = Inches(11.73)
height_t = Inches(4.9)

table_shape = s8.shapes.add_table(rows, cols, left_t, top_t, width_t, height_t)
table = table_shape.table

# Set Column Widths
table.columns[0].width = Inches(2.6)
table.columns[1].width = Inches(2.2)
table.columns[2].width = Inches(4.3)
table.columns[3].width = Inches(2.63)

headers = ["Experimental Condition", "Moderator / Observer", "Debate Protocol & Interaction Loop", "Primary Research Focus"]
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

data_conds = [
    ("Condition 1: Baseline\n(Pure MAD)", "None\n(Closed Loop)", "Autonomous multi-round agent debate with standard peer critique prompts.", "Baseline Conformity Rate &\nError Propagation (No guidance)"),
    ("Condition 2: HITL\n(Human-in-the-Loop)", "Human Observer\n(External Grounding)", "Targeted meta-level hints injected at Round 2 inflection points upon bottleneck detection.", "RQ 1 (Detection Rate) &\nRQ 2 (Conformity Resolution)"),
    ("Condition 3: Agent-Moderated\n(LLM Moderator)", "LLM Moderator\n(Automated Peer)", "Automated LLM prompt reviewing turn arguments, synthesizing consensus and nudging debaters.", "RQ 3 (Moderator Limits &\nShared Inductive Bias)")
]

for r_idx, row_data in enumerate(data_conds):
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
# SLIDE 9: Experimental Control: Controlled Human Protocol
# -------------------------------------------------------------
s9 = prs.slides.add_slide(blank_layout)
set_slide_background(s9)
add_header(s9, "Experimental Control", "Controlled Human Intervention Protocol",
           "Strict intervention constraints ensure humans do not solve the problem for the agents")

rules = [
    ("Rule 1: No Direct Answers", "Never Reveal Values or Equations",
     "The human monitor is strictly forbidden from providing numerical answers, intermediate calculations, or equation formulations. The goal is to stimulate agent self-reflection, not replace debater computation.", C_RED_ACCENT),
    ("Rule 2: Meta-Level Hints", "Focus on Assumptions & Minority Logic",
     "Feedback is confined to meta-cognitive prompts: pointing out unexamined constraints, conflicting assumptions between debaters, or prompting rigorous re-verification of the minority agent's logic from first principles.", C_BLUE_ACCENT),
    ("Rule 3: Inflection Point Trigger", "Intervene Only When Bottlenecks Emerge",
     "Interventions occur exclusively at Round 2 inflection points when divergence or conformity pressure is formally detected. Debates with natural consensus are left completely undisturbed.", C_ORANGE_ACCENT)
]

for idx, (rt, rsub, rdesc, col) in enumerate(rules):
    rx = Inches(0.8) + idx * Inches(3.98)
    add_card(s9, rx, Inches(1.8), Inches(3.75), Inches(4.8), bg_color=C_WHITE, border_color=col)

    # Top indicator
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
# SLIDE 10: Implementation 01: System Architecture & HITL Interface
# -------------------------------------------------------------
s10 = prs.slides.add_slide(blank_layout)
set_slide_background(s10)
add_header(s10, "Implementation 01", "System Architecture & HITL Interface",
           "Modular orchestrator supporting real-time turn monitoring and dual-mode intervention routing")

# Insert Architecture figure on left/center
fig_arch = fig_dir / "fig_architecture.png"
if fig_arch.exists():
    s10.shapes.add_picture(str(fig_arch), Inches(0.8), Inches(1.6), Inches(7.6), Inches(5.1))

# Right summary card
add_card(s10, Inches(8.6), Inches(1.6), Inches(3.93), Inches(5.1), bg_color=C_WHITE, border_color=C_BORDER)
tb_arch = s10.shapes.add_textbox(Inches(8.85), Inches(1.85), Inches(3.43), Inches(4.6))
tf_a = tb_arch.text_frame
tf_a.word_wrap = True

p = tf_a.paragraphs[0]
p.text = "Key System Modules"
p.font.name = FONT_HEADING
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_NAVY_BRAND

arch_items = [
    ("Multi-Agent Orchestrator", "Coordinates synchronous turn-by-turn agent responses across 3 distinct debater agents with isolated context windows."),
    ("Real-Time Monitoring UI", "Visualizes answer trajectories, flags mathematical discrepancy spikes, and alerts the observer to conformity traps."),
    ("Dual-Mode Switch", "Instantly routes identical round states to either human meta-injection or automated LLM moderator critique for direct A/B testing.")
]

for at, ad in arch_items:
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
# SLIDE 11: Implementation 02: Prompt Engineering & Feedback Injection
# -------------------------------------------------------------
s11 = prs.slides.add_slide(blank_layout)
set_slide_background(s11)
add_header(s11, "Implementation 02", "Prompt Engineering & Feedback Injection",
           "Standardized prompt templates governing agent critique and external intervention routing")

prompts = [
    ("Debate Prompt: Peer Critique Template",
     'System: "You are a competitive debater in a multi-agent mathematics committee. Review the arguments and final numbers submitted by your peers in the previous round. Carefully verify their mathematical calculations. If you detect errors or oversights, state them clearly and revise your own derivation if needed."',
     C_BLUE_LIGHT, C_BLUE_ACCENT),
    ("HITL Injection: Human Hint Wrapper",
     'Observation Wrapper: "[Human Monitor Intervention]: Notice that Agent A and Agent B share an assumption, while Agent C highlights a distinct constraint in the problem text. Do not rely on vote count; explicitly verify the exact wording and calculate each step independently without assuming majority correctness."',
     C_ORANGE_LIGHT, C_ORANGE_ACCENT),
    ("Moderator Prompt: LLM Moderator Role",
     'Moderator System: "You are the debate moderator. Synthesize the current arguments across all debater agents. Identify emerging consensus, critique divergent minority outliers, and provide guidance to help the group reach a reliable final answer before Round 3 closes."',
     C_RED_LIGHT, C_RED_ACCENT)
]

for idx, (p_title, p_code, bg_c, col) in enumerate(prompts):
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
# SLIDE 12: Dataset & Setup: GSM8K Math Reasoning Benchmark
# -------------------------------------------------------------
s12 = prs.slides.add_slide(blank_layout)
set_slide_background(s12)
add_header(s12, "Dataset & Setup", "GSM8K Math Reasoning Benchmark Setup",
           "Rigorous multi-step arithmetic reasoning benchmark for unambiguous error tracking")

# 3 Big Stat Cards at Top
stats = [
    ("30 Items", "GSM8K Benchmark Subset", "Multi-step word problems (rates, discounts, work, mixtures)", C_NAVY_BRAND),
    ("3 Agents", "Multi-Agent Committee", "3 Debaters (Agent A, B, C) + LLM Moderator / Human", C_BLUE_ACCENT),
    ("3 Rounds", "Debate Depth", "R1: Generation, R2: Critique/Intervene, R3: Consensus", C_ORANGE_ACCENT)
]

for idx, (num, lbl, desc, col) in enumerate(stats):
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

# Bottom Card: Logged Metrics Breakdown
add_card(s12, Inches(0.8), Inches(3.6), Inches(11.73), Inches(3.2), bg_color=C_WHITE, border_color=C_BORDER)
tb_met = s12.shapes.add_textbox(Inches(1.1), Inches(3.8), Inches(11.1), Inches(2.8))
tf_m = tb_met.text_frame
tf_m.word_wrap = True

p = tf_m.paragraphs[0]
p.text = "Evaluation Criteria & Turn-by-Turn Logging Protocol"
p.font.name = FONT_HEADING
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_NAVY_BRAND

metric_bullets = [
    ("Turn-by-Turn State Tracking: ", "Logs exact numerical outputs, formulas, and confidence statements for each agent per round."),
    ("Conformity Emergence Metric: ", "Identifies whenever a correct minority agent (1 vs 2) switches allegiance to an incorrect majority in R2/R3."),
    ("Cascading Error Propagation: ", "Detects when an initial arithmetic error made by one agent is unthinkingly copied by peers."),
    ("Intervention Efficacy: ", "Measures whether the human meta-hint successfully arrests wrong consensus without answer leakage.")
]

for title, desc in metric_bullets:
    p_b = tf_m.add_paragraph()
    p_b.text = "• " + title + desc
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(12)
    p_b.font.color.rgb = C_TEXT_DARK
    p_b.space_before = Pt(8)

# -------------------------------------------------------------
# SLIDE 13: Result 01 — RQ 1: Humans Spot Bottlenecks Clearly
# -------------------------------------------------------------
s13 = prs.slides.add_slide(blank_layout)
set_slide_background(s13)
add_header(s13, "Result 01 — RQ 1", "RQ 1: Humans Spot Bottlenecks Clearly",
           "100.0% of debate bottlenecks detected at the optimal Round 2 inflection point")

# Left Chart
fig_rq1 = fig_dir / "fig_rq1_detection.png"
if fig_rq1.exists():
    s13.shapes.add_picture(str(fig_rq1), Inches(0.8), Inches(1.6), Inches(7.0), Inches(5.1))

# Right Narrative Cards
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

findings_rq1 = [
    ("100% Detection Rate (19/19 Events)", "Human observers flawlessly detected all 12 conformity traps, 5 cascading arithmetic errors, and 2 constraint deadlocks."),
    ("Optimal Timing (Avg Round 2.0)", "Interventions were systematically delivered at Round 2 before the solitary correct debater conformed to majority peer pressure."),
    ("Error Traceability Advantage", "External humans immediately recognized when debaters shared a flawed heuristic vs when an agent maintained strict ground truth.")
]

for ft, fd in findings_rq1:
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
# SLIDE 14: Result 02 — RQ 2: Human Feedback Breaks Conformity
# -------------------------------------------------------------
s14 = prs.slides.add_slide(blank_layout)
set_slide_background(s14)
add_header(s14, "Result 02 — RQ 2", "RQ 2: Human Feedback Breaks Conformity",
           "Meta-level hints achieve 100% conformity halting rate, lifting accuracy from 36.7% to 100.0%")

# Left Chart
fig_rq2 = fig_dir / "fig_rq2_accuracy.png"
if fig_rq2.exists():
    s14.shapes.add_picture(str(fig_rq2), Inches(0.8), Inches(1.6), Inches(7.0), Inches(5.1))

# Right Narrative Cards
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

findings_rq2 = [
    ("+63.33%p Benchmark Accuracy Gain", "Accuracy surged from 36.67% (Baseline) to 100.0% (HITL) across the entire 30-problem test suite."),
    ("100% Conformity Halting Rate", "17 out of 17 conformity traps were halted; no correct minority agent capitulated after receiving a meta-hint."),
    ("Zero Answer Leakage", "Because hints only prompted re-examination of clauses, self-correction was accomplished through agents' own internal reasoning.")
]

for ft, fd in findings_rq2:
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
# SLIDE 15: Case Study: GSM8K Debate Log: Conformity vs. Recovery
# -------------------------------------------------------------
s15 = prs.slides.add_slide(blank_layout)
set_slide_background(s15)
add_header(s15, "Case Study", "GSM8K Debate Log: Conformity vs. Recovery",
           "Problem #1 (Clothing Store Sale): Comparing Baseline conformity collapse against HITL recovery")

# Left Column: Trajectory Chart & Problem Text
fig_cs = fig_dir / "fig_case_study.png"
if fig_cs.exists():
    s15.shapes.add_picture(str(fig_cs), Inches(0.8), Inches(1.6), Inches(5.7), Inches(2.6))

# Problem text box
add_card(s15, Inches(0.8), Inches(4.35), Inches(5.7), Inches(2.35), bg_color=C_WHITE, border_color=C_BORDER)
tb_pt = s15.shapes.add_textbox(Inches(0.95), Inches(4.45), Inches(5.4), Inches(2.15))
tf_pt = tb_pt.text_frame
tf_pt.word_wrap = True
p = tf_pt.paragraphs[0]
p.text = "Problem #1 Excerpt & Ground Truth ($453.60)"
p.font.name = FONT_HEADING
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = C_NAVY_BRAND
p_body = tf_pt.add_paragraph()
p_body.text = '"A clothing store sells jackets for $120. Buying one gets you 20% off the second. Maria buys 4 jackets + 5% sales tax on discounted price. How much does she pay?"\n• Gold: 2 full ($240) + 2 discounted ($192) = $432 * 1.05 = $453.60\n• Trap: Applying 20% to all 4 jackets yields $403.20'
p_body.font.name = FONT_BODY
p_body.font.size = Pt(10.5)
p_body.font.color.rgb = C_TEXT_DARK
p_body.space_before = Pt(4)

# Right Column: Side-by-Side Debate Transcripts
add_card(s15, Inches(6.8), Inches(1.6), Inches(5.73), Inches(2.55), bg_color=C_RED_LIGHT, border_color=C_RED_ACCENT)
tb_b = s15.shapes.add_textbox(Inches(6.95), Inches(1.7), Inches(5.43), Inches(2.35))
tf_b = tb_b.text_frame
tf_b.word_wrap = True
p = tf_b.paragraphs[0]
p.text = "Baseline (Without Human): Sycophancy & Collapse"
p.font.name = FONT_HEADING
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = C_RED_ACCENT
p_log1 = tf_b.add_paragraph()
p_log1.text = "• Round 1: Agent A: 403.2, Agent B: 403.2 | Agent C: 453.6 (Correct)\n• Round 2: A & B insist on 403.2; pressure C as an outlier.\n• Round 3: Agent C concedes: 'Seeing both agree on 403.2, I align with majority.'\n-> Final Outcome: FAILED (403.2 vs GT 453.6)"
p_log1.font.name = FONT_BODY
p_log1.font.size = Pt(10)
p_log1.font.color.rgb = C_TEXT_DARK
p_log1.space_before = Pt(2)

add_card(s15, Inches(6.8), Inches(4.35), Inches(5.73), Inches(2.35), bg_color=C_GREEN_LIGHT, border_color=C_GREEN_ACCENT)
tb_h = s15.shapes.add_textbox(Inches(6.95), Inches(4.45), Inches(5.43), Inches(2.15))
tf_h = tb_h.text_frame
tf_h.word_wrap = True
p = tf_h.paragraphs[0]
p.text = "HITL (With Human Meta-Hint): Verification & Recovery"
p.font.name = FONT_HEADING
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = C_GREEN_ACCENT
p_log2 = tf_h.add_paragraph()
p_log2.text = "• Round 2 Meta-Hint: 'Notice Agent C highlights a distinct pairing clause in the prompt. Do not rely on vote count; verify the wording independently.'\n• Round 3: Agent A & B self-correct: 'Re-reading prompt, discount applies only to every second item.' All align on 453.6.\n-> Final Outcome: SUCCESS (453.6 == GT)"
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
           "LLM moderators suffer from shared inductive bias, failing to arrest majority conformity traps")

# Left Chart
fig_rq3 = fig_dir / "fig_rq3_comparison.png"
if fig_rq3.exists():
    s16.shapes.add_picture(str(fig_rq3), Inches(0.8), Inches(1.6), Inches(6.0), Inches(5.1))

# Right Table & Summary
tb_w = Inches(5.5)
tb_h = Inches(5.1)
table_shape3 = s16.shapes.add_table(5, 4, Inches(7.0), Inches(1.6), tb_w, Inches(2.8))
tab3 = table_shape3.table
tab3.columns[0].width = Inches(2.2)
tab3.columns[1].width = Inches(1.1)
tab3.columns[2].width = Inches(1.1)
tab3.columns[3].width = Inches(1.1)

headers3 = ["Metric", "Baseline", "LLM Mod", "HITL"]
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
    ("Final Accuracy (%)", "36.67%", "36.67%", "100.0%"),
    ("Conformity Rate (%)", "100.0%", "100.0%", "0.0%"),
    ("Error Propagation (%)", "63.33%", "63.33%", "0.0%"),
    ("Intervention Freq.", "0 / prob", "1.0 / prob", "0.63 / prob")
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
        p.font.color.rgb = C_GREEN_ACCENT if c_idx == 3 and r_idx in [0, 1] else C_TEXT_DARK

# Explanatory card below table
add_card(s16, Inches(7.0), Inches(4.6), tb_w, Inches(2.1), bg_color=C_WHITE, border_color=C_BORDER)
tb_q3 = s16.shapes.add_textbox(Inches(7.15), Inches(4.7), tb_w - Inches(0.3), Inches(1.9))
tf_q3 = tb_q3.text_frame
tf_q3.word_wrap = True
p = tf_q3.paragraphs[0]
p.text = "Key Quantitative Insight (RQ 3)"
p.font.name = FONT_HEADING
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = C_NAVY_BRAND

p_body = tf_q3.add_paragraph()
p_body.text = "• The LLM Moderator yielded 0% net gain over baseline (36.67% accuracy).\n• In all 19 bottleneck scenarios, the LLM moderator favored the fluent, 2-agent majority rather than validating the solitary correct agent.\n• External human grounding provides an indispensable epistemic anchor."
p_body.font.name = FONT_BODY
p_body.font.size = Pt(11)
p_body.font.color.rgb = C_TEXT_DARK
p_body.space_before = Pt(4)

# -------------------------------------------------------------
# SLIDE 17: Result 03 — RQ 3 (Qualitative): Why LLM Moderators Struggle
# -------------------------------------------------------------
s17 = prs.slides.add_slide(blank_layout)
set_slide_background(s17)
add_header(s17, "Result 03 — RQ 3 (Qualitative)", "Why LLM Moderators Struggle to Break Loops",
           "Epistemic vulnerabilities inherent to in-distribution language model moderation")

reasons = [
    ("Shared Inductive Bias", "Susceptible to Identical Reasoning Pitfalls",
     "• Debaters and moderators share similar pretraining corpora and heuristic tendencies.\n• When an arithmetic shortcut seems superficially plausible, the moderator validates the trap instead of spotting the violation.", C_RED_ACCENT),
    ("Moderator Conformity", "Prioritizing Agreement Over Ground Truth",
     "• Standard LLM objective functions reward agreeable, coherent consensus building.\n• The moderator frequently dismisses rigorous minority derivations as 'deviations from majority consensus,' accelerating sycophancy.", C_ORANGE_ACCENT),
    ("Human Epistemic Advantage", "True External Grounding & Common Sense",
     "• Human observers possess out-of-distribution physical intuition and semantic grounding.\n• Humans readily distinguish between confident superficial rhetoric and rigorous step-by-step arithmetic truth.", C_GREEN_ACCENT)
]

for idx, (rt, rsub, rdesc, col) in enumerate(reasons):
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
# SLIDE 18: Error Analysis: Failure Cases & Study Limitations
# -------------------------------------------------------------
s18 = prs.slides.add_slide(blank_layout)
set_slide_background(s18)
add_header(s18, "Error Analysis", "Failure Cases & Practical Study Limitations",
           "Analyzing edge-case resistance and scalability boundaries in human-in-the-loop systems")

limits = [
    ("Failure Mode: Stubborn Deadlocks", "Residual Resistance to Meta-Hints",
     "• In 2 edge-case problems involving nested fractional remainders, agents required multiple hint turns because both sides defended mutually incompatible mathematical axioms.\n• Highly convoluted phrasing occasionally required more specific clause referencing.", C_RED_ACCENT),
    ("Practical Constraint: Monitoring Overhead", "Scalability Limits of Continuous Human Oversight",
     "• Requiring continuous turn-by-turn human reading introduces latency and high human labor costs, making brute-force HITL infeasible for massive inference pipelines.\n• Highlights the urgent requirement for selective, uncertainty-triggered interventions.", C_ORANGE_ACCENT)
]

for idx, (lt, lsub, ldesc, col) in enumerate(limits):
    lx = Inches(0.8) + idx * Inches(5.95)
    add_card(s18, lx, Inches(1.8), Inches(5.75), Inches(4.8), bg_color=C_WHITE, border_color=col)

    top_ind = s18.shapes.add_shape(MSO_SHAPE.RECTANGLE, lx, Inches(1.8), Inches(5.75), Inches(0.12))
    top_ind.fill.solid()
    top_ind.fill.fore_color.rgb = col
    top_ind.line.fill.background()

    tb = s18.shapes.add_textbox(lx + Inches(0.3), Inches(2.1), Inches(5.15), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = lt
    p.font.name = FONT_HEADING
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = col

    p_s = tf.add_paragraph()
    p_s.text = lsub
    p_s.font.name = FONT_BODY
    p_s.font.size = Pt(12)
    p_s.font.bold = True
    p_s.font.color.rgb = C_NAVY_DARK
    p_s.space_before = Pt(4)

    p_d = tf.add_paragraph()
    p_d.text = ldesc
    p_d.font.name = FONT_BODY
    p_d.font.size = Pt(12)
    p_d.font.color.rgb = C_TEXT_DARK
    p_d.space_before = Pt(12)
    p_d.line_spacing = 1.3

# -------------------------------------------------------------
# SLIDE 19: Summary: Key Takeaways Across RQ 1–3
# -------------------------------------------------------------
s19 = prs.slides.add_slide(blank_layout)
set_slide_background(s19)
add_header(s19, "Summary", "Key Takeaways Across RQ 1–3",
           "Core experimental conclusions validating human oversight in multi-agent reasoning")

takeaways = [
    ("RQ 1: Bottleneck Detection", "Visible Bottlenecks (100% Detection)",
     "Human observers reliably detect conformity emergence, cascading arithmetic errors, and sycophantic peer pressure at the Round 2 inflection point before consensus freezes.", C_BLUE_ACCENT),
    ("RQ 2: Error Resolution", "Effective Meta-Level Correction (+63.3%p)",
     "Non-invasive meta-hints successfully halt conformity and re-engage internal agent deduction, lifting overall accuracy from 36.7% to 100.0% without leaking answers.", C_GREEN_ACCENT),
    ("RQ 3: Moderator Limits", "LLM Bias Inherent (Human Superiority)",
     "Autonomous LLM moderators fall prey to the same shared inductive majority bias as debaters, proving that external human grounding cannot be trivially substituted by LLMs.", C_NAVY_BRAND)
]

for idx, (tt, tsub, tdesc, col) in enumerate(takeaways):
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
p_fw1.text = "1. Adaptive Uncertainty Triggers for Scalable HITL"
p_fw1.font.name = FONT_HEADING
p_fw1.font.size = Pt(18)
p_fw1.font.bold = True
p_fw1.font.color.rgb = C_WHITE
p_fw1.space_before = Pt(12)

p_fw1_d = tf_end.add_paragraph()
p_fw1_d.text = "Incorporate semantic entropy and inter-agent divergence metrics to automatically flag bottleneck inflection points, paging humans only when anomaly scores exceed critical confidence thresholds."
p_fw1_d.font.name = FONT_BODY
p_fw1_d.font.size = Pt(12.5)
p_fw1_d.font.color.rgb = RGBColor(203, 213, 225)
p_fw1_d.space_before = Pt(4)

p_fw2 = tf_end.add_paragraph()
p_fw2.text = "2. Hybrid Human-Agent Teaming Across Complex Domains"
p_fw2.font.name = FONT_HEADING
p_fw2.font.size = Pt(18)
p_fw2.font.bold = True
p_fw2.font.color.rgb = C_WHITE
p_fw2.space_before = Pt(16)

p_fw2_d = tf_end.add_paragraph()
p_fw2_d.text = "Extend controlled meta-level intervention protocols beyond arithmetic to complex multi-hop formal verification, legal contract analysis, and scientific hypothesis generation."
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

# Save Presentation
prs.save(str(pptx_path))
print(f"Presentation saved successfully to: {pptx_path}")
print(f"Total slides created: {len(prs.slides)}")
