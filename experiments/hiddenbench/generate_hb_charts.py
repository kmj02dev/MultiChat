import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from matplotlib.patches import FancyBboxPatch

out_dir = Path(r"C:\Users\GC\.gemini\antigravity\scratch\hitl_mad_hiddenbench\figures")
out_dir.mkdir(parents=True, exist_ok=True)

# Styles
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.linewidth'] = 1.2

# 1. Fig 1: Accuracy & Conformity Comparison (RQ1 & RQ2)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.3), dpi=220)

conds = ['Baseline\n(Pure MAD)', 'Agent-Moderated\n(LLM Mod)', 'Human-in-the-Loop\n(HITL)']
acc = [12.0, 16.0, 100.0]
colors1 = ['#EF4444', '#F59E0B', '#10B981']

bars1 = ax1.bar(conds, acc, color=colors1, width=0.48, edgecolor=['#B91C1C', '#B45309', '#047857'], linewidth=1.5)
ax1.set_ylabel('Decision Accuracy (%)', fontweight='bold', color='#1E293B')
ax1.set_title('Hidden Profile Decision Accuracy (N=25)', fontweight='bold', fontsize=12, color='#1E3A8A', pad=10)
ax1.set_ylim(0, 120)
ax1.grid(axis='y', linestyle='--', alpha=0.4)

ax1.annotate('12.0%\n(3/25)', xy=(0, 12.0), xytext=(0, 5), textcoords='offset points', ha='center', fontweight='bold', color='#B91C1C')
ax1.annotate('16.0%\n(4/25)', xy=(1, 16.0), xytext=(0, 5), textcoords='offset points', ha='center', fontweight='bold', color='#B45309')
ax1.annotate('100.0%\n(25/25)', xy=(2, 100.0), xytext=(0, 5), textcoords='offset points', ha='center', fontweight='bold', color='#047857')

# Accuracy gain badge
ax1.annotate('+88.0%p Surge', xy=(1.5, 70), xytext=(1.5, 70), ha='center', va='center',
             fontweight='bold', fontsize=10.5, color='#047857',
             bbox=dict(boxstyle='round,pad=0.35', facecolor='#DCFCE7', edgecolor='#10B981', lw=1.5))

# Common Knowledge Conformity Drop
conf = [88.0, 84.0, 0.0]
colors2 = ['#DC2626', '#EA580C', '#2563EB']
bars2 = ax2.bar(conds, conf, color=colors2, width=0.48, edgecolor=['#991B1B', '#9A3412', '#1D4ED8'], linewidth=1.5)
ax2.set_ylabel('Common Knowledge Conformity (%)', fontweight='bold', color='#1E293B')
ax2.set_title('Conformity Bias Under Shared Info Trap', fontweight='bold', fontsize=12, color='#DC2626', pad=10)
ax2.set_ylim(0, 120)
ax2.grid(axis='y', linestyle='--', alpha=0.4)

ax2.annotate('88.0% (22/25)\nCommon Knowledge Trap', xy=(0, 88.0), xytext=(0, 5), textcoords='offset points', ha='center', fontweight='bold', color='#DC2626', fontsize=9)
ax2.annotate('84.0% (21/25)\nModerator Codified', xy=(1, 84.0), xytext=(0, 5), textcoords='offset points', ha='center', fontweight='bold', color='#EA580C', fontsize=9)
ax2.annotate('0.0% (0/25)\n100% Halting Rate', xy=(2, 0.0), xytext=(0, 8), textcoords='offset points', ha='center', fontweight='bold', color='#2563EB', fontsize=9)

plt.tight_layout()
fig.savefig(out_dir / "fig_hb_accuracy.png")
plt.close(fig)

# 2. Fig 2: Private Fact Coverage & Error Propagation
fig, ax = plt.subplots(figsize=(8.5, 4.3), dpi=220)

x = np.arange(len(conds))
width = 0.28

priv_cov = [29.0, 30.8, 94.8]
err_prop = [88.0, 84.0, 0.0]

r1 = ax.bar(x - width/2, priv_cov, width, label='Private Fact Coverage (%)', color='#0284C7', edgecolor='#0369A1')
r2 = ax.bar(x + width/2, err_prop, width, label='Error Propagation (%)', color='#E11D48', edgecolor='#9F1239')

ax.set_ylabel('Percentage (%)', fontweight='bold', color='#1E293B')
ax.set_title('Information Pooling vs. Error Cascades (N=25)', fontweight='bold', fontsize=12, color='#1E3A8A', pad=12)
ax.set_xticks(x)
ax.set_xticklabels(conds, fontweight='semibold')
ax.set_ylim(0, 120)
ax.grid(axis='y', linestyle='--', alpha=0.4)
ax.legend(frameon=True, facecolor='#F8FAFC', loc='upper right', fontsize=9.5)

for rect in r1:
    h = rect.get_height()
    ax.annotate(f'{h:.1f}%', xy=(rect.get_x() + rect.get_width()/2, h), xytext=(0, 3), textcoords="offset points", ha='center', fontsize=9, fontweight='bold', color='#0369A1')
for rect in r2:
    h = rect.get_height()
    ax.annotate(f'{h:.1f}%', xy=(rect.get_x() + rect.get_width()/2, h), xytext=(0, 3), textcoords="offset points", ha='center', fontsize=9, fontweight='bold', color='#9F1239')

plt.tight_layout()
fig.savefig(out_dir / "fig_hb_metrics.png")
plt.close(fig)

# 3. Fig 3: Architecture Diagram (Asymmetric Silos & HITL Gate)
fig, ax = plt.subplots(figsize=(10, 4.5), dpi=220)
ax.axis('off')

def draw_card(ax, xy, w, h, title, lines, color='#F8FAFC', border='#CBD5E1', title_color='#1E3A8A'):
    card = FancyBboxPatch(xy, w, h, boxstyle="round,pad=0.02,rounding_size=0.02", fc=color, ec=border, lw=1.5, zorder=2)
    ax.add_patch(card)
    ax.text(xy[0] + 0.02, xy[1] + h - 0.06, title, fontsize=10.5, fontweight='bold', color=title_color, zorder=3)
    y_text = xy[1] + h - 0.12
    for line in lines:
        ax.text(xy[0] + 0.02, y_text, line, fontsize=8.2, color='#334155', zorder=3)
        y_text -= 0.055

# Col 1: 4 Asymmetric Silos
draw_card(ax, (0.02, 0.52), 0.28, 0.44,
          "Shared Knowledge Hub",
          ["• Broadcasted to all 4 agents",
           "• Mayor endorsement (East Town)",
           "• Accommodations & volunteers",
           "• Superficial consensus bias"],
          color='#EFF6FF', border='#3B82F6', title_color='#1E40AF')

draw_card(ax, (0.02, 0.04), 0.28, 0.44,
          "Private Information Silos",
          ["• Agent 1: Supply truck stuck",
           "• Agent 2: Massive tunnel fire",
           "• Agent 3: Trail trees blocked",
           "• Agent 4: Driveway mudslide"],
          color='#FEF3C7', border='#F59E0B', title_color='#B45309')

# Col 2: Multi-Agent Debate Room
draw_card(ax, (0.36, 0.28), 0.28, 0.50,
          "Collaborative Debate Room",
          ["• 4 Synchronous Agents",
           "• Round 1: Divergent dispatches",
           "• Round 2: Majority pressure",
           "• Baseline failure: Tunnel fire",
           "  dismissed as localized anomaly"],
          color='#F8FAFC', border='#94A3B8', title_color='#334155')

# Col 3: HITL Scaffolding vs LLM Moderator
draw_card(ax, (0.70, 0.52), 0.28, 0.44,
          "Human-in-the-Loop (HITL)",
          ["• Monitors constraint neglect",
           "• Meta-Hint at Round 2:",
           "  'Verify physical route access'",
           "• Unlocks cross-agent pooling",
           "• 100% Ground Truth recovery"],
          color='#ECFDF5', border='#10B981', title_color='#047857')

draw_card(ax, (0.70, 0.04), 0.28, 0.44,
          "LLM Moderator (Closed)",
          ["• Evaluates vote majorities",
           "• Inductive bias amplification",
           "• Pressures minority to yield",
           "• Institutionalizes error (16%)"],
          color='#FEE2E2', border='#EF4444', title_color='#B91C1C')

# Arrows
def draw_arrow(ax, start, end, label=""):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(facecolor='#64748B', edgecolor='#475569', arrowstyle="-|>", lw=1.5, mutation_scale=14),
                zorder=4)
    if label:
        mid = ((start[0]+end[0])/2, (start[1]+end[1])/2 + 0.03)
        ax.text(mid[0], mid[1], label, fontsize=8, ha='center', color='#475569', fontweight='semibold')

draw_arrow(ax, (0.30, 0.72), (0.36, 0.60), "Common Info")
draw_arrow(ax, (0.30, 0.26), (0.36, 0.40), "Private Notes")
draw_arrow(ax, (0.64, 0.60), (0.70, 0.72), "Monitor")
draw_arrow(ax, (0.70, 0.65), (0.64, 0.55), "Meta-Hint")
draw_arrow(ax, (0.64, 0.35), (0.70, 0.24), "Synthesize")

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.tight_layout()
fig.savefig(out_dir / "fig_hb_architecture.png")
plt.close(fig)

# 4. Fig 4: Case Study Flowchart (Task #1 Evacuation)
fig, ax = plt.subplots(figsize=(10, 4.2), dpi=220)
ax.axis('off')

# Options comparison cards
draw_card(ax, (0.03, 0.15), 0.29, 0.72,
          "East Town (Shared Distractor)",
          ["• Shared: Mayor guarantees beds",
           "  and volunteer assistance",
           "• Agent 1: Supply truck stuck",
           "• Agent 2: Massive tunnel fire",
           "• Verdict: 100% IMPASSABLE",
           "• Baseline: 4 votes (DISASTER)",
           "• HITL: 0 votes (ELIMINATED)"],
          color='#FEF2F2', border='#EF4444', title_color='#B91C1C')

draw_card(ax, (0.355, 0.15), 0.29, 0.72,
          "North Hill (Secondary Trap)",
          ["• Shared: School gym has 2-week",
           "  supplies, lacks privacy",
           "• Agent 3: Walking trails closed",
           "  due to fallen trees",
           "• Agent 4: Driveway mudslide",
           "• Verdict: IMPASSABLE (Car/Foot)",
           "• Baseline: Eliminated in R2",
           "• HITL: Rapidly vetoed"],
          color='#FFFBEB', border='#F59E0B', title_color='#B45309')

draw_card(ax, (0.68, 0.15), 0.29, 0.72,
          "West City (Ground Truth)",
          ["• Shared: Hotels fully stocked",
           "  with food (lacks med supplies)",
           "• Bridge: River below crest level",
           "• Road Access: OPEN & VIABLE",
           "• Verdict: SAFEST ROUTE",
           "• Baseline: Abandoned (0 votes)",
           "• HITL: 4 votes (100% ACCURACY)"],
          color='#ECFDF5', border='#10B981', title_color='#047857')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.tight_layout()
fig.savefig(out_dir / "fig_hb_case_study.png")
plt.close(fig)

print("All 4 high-resolution HiddenBench figures generated successfully!")
