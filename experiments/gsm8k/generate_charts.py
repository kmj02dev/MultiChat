import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

out_dir = Path(r"C:\Users\GC\.gemini\antigravity\scratch\hitl_mad_gsm8k\figures")
out_dir.mkdir(parents=True, exist_ok=True)

# Set global styles
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.linewidth'] = 1.2

# 1. Fig RQ1: Detection Breakdown
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2), dpi=220)

categories = ['Conformity\nTraps', 'Cascading\nArithmetic', 'Constraint\nDeadlocks']
total_events = [12, 5, 2]
detected_events = [12, 5, 2]

x = np.arange(len(categories))
width = 0.35

rects1 = ax1.bar(x - width/2, total_events, width, label='Total Bottlenecks', color='#94A3B8', edgecolor='#475569')
rects2 = ax1.bar(x + width/2, detected_events, width, label='Human Detected', color='#2563EB', edgecolor='#1E3A8A')

ax1.set_ylabel('Number of Events', fontweight='bold', color='#1E293B')
ax1.set_title('Bottleneck Events by Type (N=19)', fontweight='bold', fontsize=12, color='#1E3A8A', pad=10)
ax1.set_xticks(x)
ax1.set_xticklabels(categories, fontweight='semibold')
ax1.set_ylim(0, 15)
ax1.legend(frameon=True, facecolor='#F8FAFC', edgecolor='none')
ax1.grid(axis='y', linestyle='--', alpha=0.4)

for r in rects2:
    h = r.get_height()
    ax1.annotate(f'{h}/{h}\n(100%)',
                 xy=(r.get_x() + r.get_width() / 2, h),
                 xytext=(0, 3), textcoords="offset points",
                 ha='center', va='bottom', fontsize=9, fontweight='bold', color='#1E3A8A')

# Detection Timing by Round
rounds = ['Round 1\n(Emergence)', 'Round 2\n(Inflection Pt)', 'Round 3\n(Consensus)']
timing = [0, 19, 0] # all 19 detected at inflection point Round 2
bars = ax2.bar(rounds, [0, 100, 0], color=['#CBD5E1', '#EA580C', '#CBD5E1'], edgecolor='#9A3412', width=0.5)
ax2.set_ylabel('% Bottlenecks Intervened', fontweight='bold', color='#1E293B')
ax2.set_title('Human Detection & Intervention Timing', fontweight='bold', fontsize=12, color='#EA580C', pad=10)
ax2.set_ylim(0, 120)
ax2.grid(axis='y', linestyle='--', alpha=0.4)
ax2.annotate('Optimal Inflection Point\nAvg Round: 2.0 (100% Interventions)',
             xy=(1, 100), xytext=(0.3, 107),
             ha='center', fontsize=9.5, fontweight='bold', color='#9A3412',
             arrowprops=dict(facecolor='#EA580C', shrink=0.08, width=1.5, headwidth=6))

plt.tight_layout()
fig.savefig(out_dir / "fig_rq1_detection.png")
plt.close(fig)

# 2. Fig RQ2: Accuracy & Error Resolution
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2), dpi=220)

conditions = ['Baseline\n(Pure MAD)', 'Human-in-the-Loop\n(HITL)']
acc = [36.67, 100.0]
colors = ['#EF4444', '#10B981']

bars1 = ax1.bar(conditions, acc, color=colors, width=0.45, edgecolor=['#B91C1C', '#047857'], linewidth=1.5)
ax1.set_ylabel('GSM8K Accuracy (%)', fontweight='bold', color='#1E293B')
ax1.set_title('Final Benchmark Accuracy (N=30)', fontweight='bold', fontsize=12, color='#1E3A8A', pad=10)
ax1.set_ylim(0, 120)
ax1.grid(axis='y', linestyle='--', alpha=0.4)

ax1.annotate('36.67%\n(11/30)', xy=(0, 36.67), xytext=(0, 5), textcoords='offset points', ha='center', fontweight='bold', color='#B91C1C')
ax1.annotate('100.0%\n(30/30)', xy=(1, 100.0), xytext=(0, 5), textcoords='offset points', ha='center', fontweight='bold', color='#047857')

# Bracket for gain
ax1.annotate('+63.33%p Gain', xy=(0.5, 75), xytext=(0.5, 75), ha='center', va='center',
             fontweight='bold', fontsize=11, color='#047857',
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#DCFCE7', edgecolor='#10B981', lw=1.5))

# Wrong conformity rate drop
conf_rates = [100.0, 0.0]
bars2 = ax2.bar(conditions, conf_rates, color=['#F97316', '#3B82F6'], width=0.45, edgecolor=['#C2410C', '#1D4ED8'], linewidth=1.5)
ax2.set_ylabel('Wrong Conformity Rate (%)', fontweight='bold', color='#1E293B')
ax2.set_title('Conformity Bias Under Peer Pressure', fontweight='bold', fontsize=12, color='#C2410C', pad=10)
ax2.set_ylim(0, 120)
ax2.grid(axis='y', linestyle='--', alpha=0.4)

ax2.annotate('100.0% (17/17)\nConformed to Error', xy=(0, 100.0), xytext=(0, 5), textcoords='offset points', ha='center', fontweight='bold', color='#C2410C')
ax2.annotate('0.0% (0/17)\n100% Halting Rate', xy=(1, 0.0), xytext=(0, 8), textcoords='offset points', ha='center', fontweight='bold', color='#1D4ED8')

plt.tight_layout()
fig.savefig(out_dir / "fig_rq2_accuracy.png")
plt.close(fig)

# 3. Fig RQ3: Three-Condition Benchmark
fig, ax = plt.subplots(figsize=(8.5, 4.3), dpi=220)

conds = ['Baseline\n(Pure MAD)', 'Agent-Moderated\n(LLM Moderator)', 'Human-in-the-Loop\n(HITL)']
x = np.arange(len(conds))
width = 0.26

acc_vals = [36.67, 36.67, 100.0]
conf_vals = [100.0, 100.0, 0.0]
err_vals = [63.33, 63.33, 0.0]

r1 = ax.bar(x - width, acc_vals, width, label='Final Accuracy (%)', color='#2563EB', edgecolor='#1E3A8A')
r2 = ax.bar(x, conf_vals, width, label='Wrong Conformity (%)', color='#DC2626', edgecolor='#991B1B')
r3 = ax.bar(x + width, err_vals, width, label='Error Propagation (%)', color='#F59E0B', edgecolor='#B45309')

ax.set_ylabel('Percentage (%)', fontweight='bold', color='#1E293B')
ax.set_title('Quantitative Comparison Across 3 Experimental Conditions (N=30)', fontweight='bold', fontsize=12, color='#1E3A8A', pad=12)
ax.set_xticks(x)
ax.set_xticklabels(conds, fontweight='semibold')
ax.set_ylim(0, 125)
ax.grid(axis='y', linestyle='--', alpha=0.4)
ax.legend(frameon=True, facecolor='#F8FAFC', loc='upper right', ncol=3, fontsize=9.5)

for rect in r1:
    h = rect.get_height()
    ax.annotate(f'{h:.1f}%', xy=(rect.get_x() + rect.get_width()/2, h), xytext=(0, 3), textcoords="offset points", ha='center', fontsize=8.5, fontweight='bold', color='#1E3A8A')
for rect in r2:
    h = rect.get_height()
    ax.annotate(f'{h:.0f}%', xy=(rect.get_x() + rect.get_width()/2, h), xytext=(0, 3), textcoords="offset points", ha='center', fontsize=8.5, fontweight='bold', color='#991B1B')
for rect in r3:
    h = rect.get_height()
    ax.annotate(f'{h:.1f}%', xy=(rect.get_x() + rect.get_width()/2, h), xytext=(0, 3), textcoords="offset points", ha='center', fontsize=8.5, fontweight='bold', color='#B45309')

plt.tight_layout()
fig.savefig(out_dir / "fig_rq3_comparison.png")
plt.close(fig)

# 4. Fig Architecture: System Architecture & Dual-Mode UI
fig, ax = plt.subplots(figsize=(10, 4.4), dpi=220)
ax.axis('off')

from matplotlib.patches import FancyBboxPatch

# Draw boxes
def draw_card(ax, xy, w, h, title, lines, color='#F8FAFC', border='#CBD5E1', title_color='#1E3A8A'):
    card = FancyBboxPatch(xy, w, h, boxstyle="round,pad=0.02,rounding_size=0.02", fc=color, ec=border, lw=1.5, zorder=2)
    ax.add_patch(card)
    ax.text(xy[0] + 0.02, xy[1] + h - 0.06, title, fontsize=10.5, fontweight='bold', color=title_color, zorder=3)
    y_text = xy[1] + h - 0.12
    for line in lines:
        ax.text(xy[0] + 0.02, y_text, line, fontsize=8.2, color='#334155', zorder=3)
        y_text -= 0.055

# Column 1: Multi-Agent Orchestrator
draw_card(ax, (0.02, 0.45), 0.28, 0.50,
          "Multi-Agent Orchestrator",
          ["• Synchronous turn-by-turn loop",
           "• Agent A: Independent derivation",
           "• Agent B: Cross-examination",
           "• Agent C: Boundary verification",
           "• Structured JSON round logs"],
          color='#EFF6FF', border='#3B82F6', title_color='#1E40AF')

# Column 2: Dual Mode Switch
draw_card(ax, (0.36, 0.54), 0.28, 0.41,
          "Condition 2: Human Observer",
          ["• Live inflection point monitor",
           "• Non-invasive Meta-Hints only",
           "• Triggers at Round 2 divergence",
           "• Strict no-answer protocol"],
          color='#FEF3C7', border='#F59E0B', title_color='#B45309')

draw_card(ax, (0.36, 0.05), 0.28, 0.41,
          "Condition 3: LLM Moderator",
          ["• Automated round synthesis",
           "• Heuristic peer vote weight",
           "• Fast, zero-overhead critique",
           "• Shared inductive bias risk"],
          color='#FEE2E2', border='#EF4444', title_color='#B91C1C')

# Column 3: Real-Time Monitoring UI & Results
draw_card(ax, (0.70, 0.28), 0.28, 0.48,
          "Real-Time Monitoring UI",
          ["• Round-by-round consensus radar",
           "• Discrepancy & slip alerts",
           "• Interactive intervention prompt",
           "• Final convergence validator"],
          color='#ECFDF5', border='#10B981', title_color='#047857')

# Draw arrows
def draw_arrow(ax, start, end, label=""):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(facecolor='#64748B', edgecolor='#475569', arrowstyle="-|>", lw=1.5, mutation_scale=14),
                zorder=4)
    if label:
        mid = ((start[0]+end[0])/2, (start[1]+end[1])/2 + 0.03)
        ax.text(mid[0], mid[1], label, fontsize=8, ha='center', color='#475569', fontweight='semibold')

draw_arrow(ax, (0.30, 0.72), (0.36, 0.72), "Inspect")
draw_arrow(ax, (0.36, 0.65), (0.30, 0.65), "Meta-Hint")
draw_arrow(ax, (0.30, 0.50), (0.36, 0.25), "Auto-Route")
draw_arrow(ax, (0.64, 0.72), (0.70, 0.60), "Stream UI")
draw_arrow(ax, (0.64, 0.25), (0.70, 0.45), "Critique")

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.tight_layout()
fig.savefig(out_dir / "fig_architecture.png")
plt.close(fig)

# 5. Fig Case Study: Trajectory Comparison
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.0), dpi=220)

rounds = [1, 2, 3]
# Baseline: A starts at 403.2, B starts at 403.2, C starts at 453.6 (Correct), then C conforms to 403.2
# Let's plot answer values for Agent A, B, C
ax1.plot(rounds, [403.2, 403.2, 403.2], 'o--', color='#EF4444', lw=2, label='Agent A (Wrong)')
ax1.plot(rounds, [403.2, 403.2, 403.2], 's--', color='#F97316', lw=2, label='Agent B (Wrong)')
ax1.plot(rounds, [453.6, 403.2, 403.2], '^--', color='#2563EB', lw=2.5, label='Agent C (Conforms!)')
ax1.axhline(453.6, color='#10B981', linestyle=':', lw=2, label='Ground Truth (453.6)')

ax1.set_title('Baseline Trajectory (Conformity Collapse)', fontweight='bold', fontsize=11, color='#DC2626')
ax1.set_xlabel('Debate Round', fontweight='bold')
ax1.set_ylabel('Calculated Price ($)', fontweight='bold')
ax1.set_xticks(rounds)
ax1.set_xticklabels(['Round 1\n(Independent)', 'Round 2\n(Peer Critique)', 'Round 3\n(Consensus)'])
ax1.set_ylim(380, 480)
ax1.grid(True, linestyle='--', alpha=0.4)
ax1.legend(loc='upper right', fontsize=8.5, frameon=True, facecolor='#FEF2F2')
ax1.annotate('Agent C Capitulates\nto Wrong Majority!', xy=(2, 403.2), xytext=(1.5, 435),
             arrowprops=dict(facecolor='#DC2626', shrink=0.08, width=1.5, headwidth=6),
             fontweight='bold', color='#DC2626', fontsize=8.5)

# HITL Trajectory
ax2.plot(rounds, [403.2, 403.2, 453.6], 'o-', color='#10B981', lw=2, label='Agent A (Corrected)')
ax2.plot(rounds, [403.2, 403.2, 453.6], 's-', color='#3B82F6', lw=2, label='Agent B (Corrected)')
ax2.plot(rounds, [453.6, 453.6, 453.6], '^-', color='#047857', lw=2.5, label='Agent C (Maintained)')
ax2.axhline(453.6, color='#10B981', linestyle=':', lw=2, label='Ground Truth (453.6)')

ax2.set_title('HITL Trajectory (Recovery via Meta-Hint)', fontweight='bold', fontsize=11, color='#047857')
ax2.set_xlabel('Debate Round', fontweight='bold')
ax2.set_ylabel('Calculated Price ($)', fontweight='bold')
ax2.set_xticks(rounds)
ax2.set_xticklabels(['Round 1\n(Independent)', 'Round 2\n(Meta-Hint)', 'Round 3\n(Consensus)'])
ax2.set_ylim(380, 480)
ax2.grid(True, linestyle='--', alpha=0.4)
ax2.legend(loc='lower right', fontsize=8.5, frameon=True, facecolor='#ECFDF5')
ax2.annotate('Human Meta-Hint\nFlags Constraint!', xy=(2, 403.2), xytext=(1.4, 435),
             arrowprops=dict(facecolor='#047857', shrink=0.08, width=1.5, headwidth=6),
             fontweight='bold', color='#047857', fontsize=8.5)

plt.tight_layout()
fig.savefig(out_dir / "fig_case_study.png")
plt.close(fig)

print("All 5 high-resolution figures generated successfully!")
