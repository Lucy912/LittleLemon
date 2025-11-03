# Module 2, Video 3: Advanced Prompting Techniques
## Tier 1 Quick Production Version

**Length:** 8 minutes
**Deliverable:** Advanced Techniques Quick Reference Guide (1-page PDF)
**Production Time:** 2-3 hours
**Note:** Takes students from basic framework to expert-level techniques

---

## Video Outline (Talking Points)

### [0:00-0:15] HOOK
"You know the framework. You've written 10 prompts. Now I'll show you 3 techniques that will make you better than 99% of AI users—and they're easier than you think."

**Visual:** Side-by-side comparison - basic prompt vs advanced prompt with dramatically better output

---

### [0:15-0:45] PROMISE

**What you'll learn:**
1. Chain-of-Thought: Make AI "show its work" for better reasoning
2. Few-Shot Learning: Train AI with examples in seconds
3. Iterative Refinement: Turn "good" into "perfect" in 2 iterations

**What you'll gain:**
- 10x better quality on complex tasks
- Ability to handle nuanced, sophisticated requests
- Confidence to tackle problems you thought AI couldn't solve
- Techniques used by AI researchers and power users

**Time to master:** Each technique takes 5 minutes to learn, lifetime to master.

---

### [0:45-1:30] THE PROBLEM WITH BASIC PROMPTS

**Why basic prompts fail on complex tasks:**

**Example - Basic Prompt:**
"Analyze this business strategy and tell me if it's good."

**What happens:**
- AI gives superficial answer
- Misses nuances
- No structured reasoning
- Generic advice

**Why it fails:**
- Too vague
- No thinking process required
- No examples of "good analysis"
- No iteration framework

**The solution:** 3 advanced techniques that solve each problem.

---

### [1:30-3:30] TECHNIQUE 1: CHAIN-OF-THOUGHT (CoT)

**What it is:** Ask AI to think step-by-step before answering.

**The magic phrase:** "Let's think through this step by step"

**Why it works:**
- Forces logical reasoning
- Catches mistakes mid-process
- Shows the "why" behind conclusions
- Dramatically improves accuracy on complex tasks

**BEFORE (without CoT):**
```
Prompt: "Should I invest €50K in expanding to Germany?"

Output: "Yes, it's a good market with strong economy."
(Generic, superficial, risky advice)
```

**AFTER (with CoT):**
```
Prompt: "Should I invest €50K in expanding to Germany? Let's think
through this step by step:
1. First, analyze market conditions
2. Then, assess competitive landscape
3. Then, evaluate our readiness
4. Finally, recommend a decision with reasoning"

Output:
"Step 1: Market Analysis - Germany's B2B services market is €X,
growing at Y%, but...
Step 2: Competitive Landscape - 3 major players dominate, our
differentiation is...
Step 3: Readiness Assessment - We lack German-speaking staff,
legal entity, and...
Step 4: Recommendation - WAIT. Instead, test with €5K pilot
targeting..."
(Structured, thorough, actionable)
```

**When to use CoT:**
- ✅ Complex decisions (investments, strategy, hiring)
- ✅ Multi-step analysis (data interpretation, problem-solving)
- ✅ Technical explanations (debugging, troubleshooting)
- ✅ Creative planning (campaigns, projects, content series)
- ❌ Simple tasks (basic writing, formatting, quick questions)

**Pro tip:** Number the steps (1, 2, 3...) to enforce structure.

**ChatGPT Example (show on screen):**
Run the Germany expansion prompt both ways, show the dramatic difference.

---

### [3:30-5:15] TECHNIQUE 2: FEW-SHOT LEARNING

**What it is:** Give AI 2-3 examples of what you want, then ask for more.

**Why it works:**
- Shows style, tone, format better than description
- AI pattern-matches your examples
- Captures nuances words can't describe
- Like showing a designer mockups vs describing your vision

**The formula:**
```
Here are examples of [what you want]:

Example 1: [your example]
Example 2: [your example]
Example 3: [your example]

Now create [number] more like these, for [your specific context].
```

**EXAMPLE 1: Email Style Training**

**Prompt:**
```
I need 5 more customer follow-up emails in the same style as these:

Example 1:
Subject: Quick question about your onboarding
Hey Sarah - noticed you haven't logged in yet. Anything blocking you?
Happy to jump on a 10-min call to help. - Mike

Example 2:
Subject: How's it going?
Hi Tom - checking in on your first week. Questions? Bugs? Feature
requests? Reply with anything and I'll handle it. - Mike

Example 3:
Subject: You're quiet 🙂
Hey Lisa - you were active week 1, then went silent. Did we lose you?
What happened? Honest feedback helps us improve. - Mike

Now write 5 more follow-up emails in this same style for:
- User who viewed pricing but didn't buy
- User whose trial expires in 3 days
- User who canceled subscription
- User who completed onboarding but hasn't used key feature
- Power user we want to turn into case study
```

**Output:** 5 emails that perfectly match your voice, tone, length, and approach.

**EXAMPLE 2: Code Comment Style**

**Prompt:**
```
Here are examples of how I comment my code:

Example 1:
// HACK: This is ugly but works. Clean up after API v2 ships.
// Converts timestamps because backend returns inconsistent formats.

Example 2:
// PERF: Cached for 5 min because API is slow (avg 2s response).
// TODO: Move to real-time WebSocket when backend supports it.

Example 3:
// CONTEXT: Users expect instant feedback, so we fake success first
// then sync in background. See design doc in Notion.

Now write comments in this style for these 5 functions:
[paste your uncommented code]
```

**Output:** Comments matching your exact style—practical, context-rich, future-focused.

**When to use Few-Shot:**
- ✅ Matching specific writing style/voice
- ✅ Generating similar items (emails, social posts, code)
- ✅ When you can show examples but can't describe the pattern
- ✅ Maintaining consistency across content
- ❌ When you only have 1 example (need 2-3 minimum)
- ❌ When examples are too diverse (confuses the pattern)

**Pro tip:** 3 examples is the sweet spot. 2 is minimum, 4+ rarely helps.

---

### [5:15-7:00] TECHNIQUE 3: ITERATIVE REFINEMENT

**What it is:** Start with a good prompt, then improve the output through conversation.

**Why it works:**
- Faster than perfect first try
- You don't need to anticipate everything
- Allows course correction
- Builds on what's already good

**The 3-iteration formula:**

**Iteration 1: Generate (80% quality)**
Start with a solid prompt using the framework.

**Iteration 2: Refine (95% quality)**
"This is good, but [specific change]. Keep everything else the same."

**Iteration 3: Perfect (99% quality)**
"Almost perfect. Just change [tiny detail]."

**EXAMPLE: LinkedIn Post Refinement**

**Iteration 1:**
```
Prompt: Act as a LinkedIn ghostwriter known for viral B2B posts.

Task: Write a post about how we reduced customer churn by 40%.

Context: We implemented a new onboarding flow based on user research.
Want to share learnings with other product managers. Main insight:
we were teaching features when we should have been enabling outcomes.

Format: Hook + 3 bullet points with sub-bullets + conclusion with
question. 200 words.

Tone: Conversational but credible, humble about the journey,
genuinely helpful.
```

**Output 1:** (Good but not perfect)
"Last quarter we cut churn by 40%. Here's what we learned about
onboarding..." [continues with 3 learnings]

---

**Iteration 2:**
```
This is good, but the hook isn't surprising enough. Make it more
contrarian—something that makes people stop scrolling. Also add
specific numbers/examples to the bullet points. Keep everything
else the same.
```

**Output 2:** (Better, more specific)
"We spent 6 months perfecting our onboarding tutorial. Churn didn't
budge. Then we deleted it. Churn dropped 40%..." [continues with
specific examples and data]

---

**Iteration 3:**
```
Perfect. Just make the final question more action-oriented—instead
of "what do you think?" ask something that prompts specific advice
or stories.
```

**Output 3:** (Publication-ready)
"We spent 6 months perfecting our onboarding tutorial. Churn didn't
budge. Then we deleted it. Churn dropped 40%... [post content]...

What onboarding assumption did you have to completely reverse?
Drop your story below—trying to learn from the community."

---

**Iteration tips:**
- ✅ Be specific: "Make hook more contrarian" not "make it better"
- ✅ Keep what works: "Keep everything else the same"
- ✅ One change per iteration: Don't give 5 notes at once
- ✅ Build on previous output: Stay in same conversation thread
- ❌ Don't start over: "Actually, forget that" wastes context
- ❌ Don't be vague: "Make it more engaging" (how?)

**When to use Iteration:**
- ✅ Complex creative work (writing, design, strategy)
- ✅ When requirements aren't fully clear upfront
- ✅ When "perfect" is hard to describe but easy to recognize
- ✅ When you're exploring options
- ❌ Simple tasks that are one-and-done
- ❌ When you know exactly what you want (nail it in iteration 1)

---

### [7:00-7:45] COMBINING TECHNIQUES (Power Move)

**The ultimate prompt combines all 3:**

**Example: Business Strategy Analysis**
```
Act as a management consultant who specializes in market entry
strategy.

Task: Evaluate whether we should expand to the German market.

Context: We're a €2M/year B2B SaaS company, 15 people, serving
Dutch enterprises. Considering Germany for growth. Have €50K
budget for expansion.

Here are examples of the analysis format I want (FEW-SHOT):

Example 1: [Show a previous market analysis you liked]
Example 2: [Show another one]

Let's think through this step by step (CHAIN-OF-THOUGHT):
1. First, analyze market opportunity (size, growth, accessibility)
2. Then, evaluate competitive landscape and our differentiation
3. Then, assess our organizational readiness
4. Finally, provide Go/No-Go recommendation with risk mitigation

Format: Executive summary + detailed analysis for each step +
final recommendation table (Criteria, Score 1-10, Reasoning)

Tone: Data-driven but practical, acknowledging unknowns, focused
on decision-making not just analysis.
```

**Then iterate:**
- Iteration 1: Get the full analysis
- Iteration 2: "This is great, but add a 'test-before-bet' option—
a pilot approach that reduces risk. Keep everything else."
- Iteration 3: "Perfect. Just add 3 specific metrics we should
track in the pilot phase to determine if we should go full scale."

**Result:** Professional-grade strategic analysis in 3 iterations,
10 minutes total.

---

### [7:45-8:00] PRACTICE CHALLENGE & WRAP

**Your challenge:**
Pick one prompt from Video 2.2 (your library of 10) and upgrade it:

1. Add Chain-of-Thought if it's a complex decision
2. Add Few-Shot examples if you want specific style
3. Use Iteration to refine the output to perfection

**Before next video:**
- Try each technique once
- Note which technique helps most for YOUR work
- Add your favorite advanced prompts to your library

**Download:** Advanced Techniques Quick Reference Guide (1-page
cheat sheet with all 3 techniques + templates)

**Next video:** Industry-Specific Prompts (Marketing, Sales,
Product, Finance, Operations, HR - ready-made prompts for your role)

**The truth:** Master these 3 techniques and you'll be in the top
1% of AI users. Most people never get here. You just did.

---

## Deliverable: Advanced Techniques Quick Reference Guide

### Content to Create (1-page PDF, front and back):

```
═══════════════════════════════════════════════════
ADVANCED PROMPTING TECHNIQUES
Quick Reference Guide
═══════════════════════════════════════════════════

Use these 3 techniques to 10x your prompt quality

═══════════════════════════════════════════════════
TECHNIQUE 1: CHAIN-OF-THOUGHT (CoT)
═══════════════════════════════════════════════════

⚡ WHAT: Ask AI to think step-by-step before answering

🎯 WHEN TO USE:
✅ Complex decisions (investments, strategy, hiring)
✅ Multi-step analysis (data interpretation, problem-solving)
✅ Technical explanations (debugging, troubleshooting)
❌ Simple tasks (basic writing, quick questions)

🔧 HOW TO USE:

OPTION 1: Magic phrase
Add: "Let's think through this step by step:"

OPTION 2: Numbered steps (better)
Add:
"Let's approach this systematically:
1. First, [step 1]
2. Then, [step 2]
3. Then, [step 3]
4. Finally, [conclusion with reasoning]"

📝 TEMPLATE:
──────────────────────────────────────────────────
[Your 5-Part Framework Prompt]

Let's approach this systematically:
1. First, [analyze/identify/evaluate] __________
2. Then, [assess/compare/examine] __________
3. Then, [consider/calculate/determine] __________
4. Finally, [recommend/conclude/decide] with reasoning
──────────────────────────────────────────────────

💡 EXAMPLE:

❌ WITHOUT CoT:
"Should I hire a senior or junior developer?"
→ Superficial answer

✅ WITH CoT:
"Should I hire a senior or junior developer? Let's think this
through step by step:
1. First, analyze my current team's skill gaps
2. Then, compare the value each brings in year 1
3. Then, consider budget impact and growth trajectory
4. Finally, recommend which hire with clear reasoning"
→ Structured, thorough analysis

🎁 RESULT: 10x better reasoning, catches errors, shows the "why"

═══════════════════════════════════════════════════
TECHNIQUE 2: FEW-SHOT LEARNING
═══════════════════════════════════════════════════

⚡ WHAT: Give AI 2-3 examples, then ask for more like them

🎯 WHEN TO USE:
✅ Matching specific writing style/voice
✅ Generating similar items (emails, posts, code)
✅ When you can show examples but can't describe the pattern
❌ When you only have 1 example (need 2-3 minimum)

🔧 HOW TO USE:

The formula:
1. Provide 2-3 high-quality examples
2. Point out what they have in common (optional but helpful)
3. Ask for more in the same style

📝 TEMPLATE:
──────────────────────────────────────────────────
I need [number] more [type of content] in the same style as these:

Example 1:
[Your first example - paste the actual content]

Example 2:
[Your second example - paste the actual content]

Example 3:
[Your third example - paste the actual content]

These examples share: [optional: what pattern you want preserved]

Now create [number] more like these for:
- [Scenario 1]
- [Scenario 2]
- [Scenario 3]
──────────────────────────────────────────────────

💡 EXAMPLE:

"I need 5 customer emails in the same style as these:

Example 1:
Subject: Quick question
Hey Tom - noticed you're stuck on setup. 10-min call? I'll
drive. - Mike

Example 2:
Subject: How's it going?
Hi Sarah - first week check-in. Questions? Bugs? Hit reply. - Mike

Example 3:
Subject: You're quiet 🙂
Hey Lisa - went from active to silent. What happened? - Mike

Now write 5 more for: [different scenarios]"

🎁 RESULT: Perfect style match, captures nuances words can't describe

🎯 PRO TIP: 3 examples is the sweet spot

═══════════════════════════════════════════════════
TECHNIQUE 3: ITERATIVE REFINEMENT
═══════════════════════════════════════════════════

⚡ WHAT: Start good, then improve through conversation

🎯 WHEN TO USE:
✅ Complex creative work (writing, strategy, design)
✅ When requirements aren't fully clear upfront
✅ When "perfect" is easy to recognize but hard to describe
❌ Simple one-and-done tasks
❌ When you know exactly what you want (nail it first try)

🔧 THE 3-ITERATION FORMULA:

ITERATION 1: Generate (80% quality)
→ Use solid 5-Part Framework prompt
→ Get first version

ITERATION 2: Refine (95% quality)
→ "This is good, but [specific change]. Keep everything else."
→ One major improvement

ITERATION 3: Perfect (99% quality)
→ "Almost perfect. Just change [tiny detail]."
→ Final polish

📝 ITERATION TEMPLATES:

ITERATION 2 (Refine):
"This is good, but [specific improvement]. Keep everything
else the same."

Examples:
- "...but make the hook more surprising"
- "...but add specific numbers/examples"
- "...but make it more concise"
- "...but adjust tone to be more [adjective]"

ITERATION 3 (Perfect):
"Perfect. Just [one small change]."

Examples:
- "Just make the CTA more action-oriented"
- "Just fix the formatting in bullet 2"
- "Just make the conclusion stronger"

💡 ITERATION RULES:

✅ DO:
• Be specific: "Make hook more contrarian" not "better"
• Keep what works: "Keep everything else the same"
• One change per iteration
• Build on previous output (stay in conversation)

❌ DON'T:
• Don't restart: "Actually, forget that" (wastes context)
• Don't be vague: "Make it more engaging" (how?)
• Don't give 5 notes at once (AI gets confused)

🎁 RESULT: Fast 80% → slow perfection, saves time

═══════════════════════════════════════════════════
POWER MOVE: COMBINE ALL 3 TECHNIQUES
═══════════════════════════════════════════════════

For expert-level results, stack techniques:

📝 THE ULTIMATE PROMPT FORMAT:
──────────────────────────────────────────────────
[5-Part Framework Prompt: Role, Task, Context, Format, Tone]

[FEW-SHOT: Here are 2-3 examples of what I want...]

[CHAIN-OF-THOUGHT: Let's approach this step by step:
1. First, [step]
2. Then, [step]
3. Finally, [step]]

[Then use ITERATION to refine the output]
──────────────────────────────────────────────────

💡 EXAMPLE: Strategic Business Analysis

Iteration 1: Get analysis using Framework + Few-Shot + CoT
Iteration 2: "Add a 'test-before-bet' pilot option"
Iteration 3: "Add 3 metrics to track pilot success"

Result: Professional-grade strategic analysis in 10 minutes

═══════════════════════════════════════════════════
QUICK DECISION GUIDE
═══════════════════════════════════════════════════

"Which technique should I use?"

CHAIN-OF-THOUGHT → Complex reasoning, decisions, analysis
FEW-SHOT → Style matching, pattern replication
ITERATION → Creative work, unclear requirements, polish
ALL THREE → High-stakes complex work (strategy, planning)

═══════════════════════════════════════════════════
PRACTICE EXERCISES
═══════════════════════════════════════════════════

□ Exercise 1: Take a prompt from your library (Video 2.2)
  Add Chain-of-Thought steps. Compare outputs.

□ Exercise 2: Find 3 examples of content you like (emails,
  posts, etc). Use Few-Shot to generate 5 more.

□ Exercise 3: Write a complex prompt (strategy, analysis).
  Use all 3 iterations to refine to perfection.

□ Exercise 4: Combine all techniques on a real work task.
  Track time saved vs doing it manually.

═══════════════════════════════════════════════════

📚 NEXT STEP: Watch Video 2.4 - Industry-Specific Prompts
Ready-made prompts for Marketing, Sales, Product, Finance,
Operations, and HR roles.

Created by Lucy's AI Training | lucyworks.com
```

---

## ChatGPT Examples (Prepare These)

**Example 1: Chain-of-Thought Comparison**
- Show Germany expansion prompt without CoT → superficial answer
- Show same prompt with CoT → detailed step-by-step analysis
- Highlight how reasoning catches issues basic prompt missed

**Example 2: Few-Shot Email Style**
- Show 3 example emails in a specific voice
- Run the prompt asking for 5 more
- Show how output perfectly matches the style

**Example 3: Live Iteration**
- Start with LinkedIn post prompt (iteration 1)
- Refine with specific note (iteration 2)
- Final polish (iteration 3)
- Show side-by-side of all 3 versions

**Example 4: Combined Techniques**
- Use real business problem
- Build prompt with all 3 techniques
- Show the professional-grade output
- Emphasize: "This took 10 minutes, would take consultants hours"

---

## Production Notes

### Recording Tips:
- Show actual ChatGPT screen for every example
- Type out the advanced prompts on screen
- Use split-screen to compare basic vs advanced outputs
- Pause to highlight which part of technique created the improvement

### Visual Elements:
- Technique comparison table (when to use each)
- Before/after output comparisons
- Progressive improvement in iteration examples (v1 → v2 → v3)
- Decision tree: "Which technique should I use?"

### Editing Focus:
- Fast cuts between examples
- Highlight key phrases ("Let's think step by step", "Here are examples")
- Show full ChatGPT outputs (actual screenshots, not mockups)
- Add captions for key learnings

### Engagement Hooks:
- "Pause and try this technique on your own prompt"
- "Screenshot this template"
- "Which technique will save you the most time?"

---

## Key Messages

1. **These 3 techniques = top 1% of AI users:** Most people never learn advanced prompting
2. **Start with one technique:** Don't need to use all at once
3. **Iteration is underused:** Most people give up after first try
4. **Combining = expert level:** Stack techniques for professional results

---

**PRODUCTION TARGET: 2-3 hours**
- Prep: 30 min (prepare ChatGPT examples showing all techniques)
- Record: 60 min (show live examples with outputs)
- Edit: 45 min (split screens for comparisons)
- Deliverable (quick reference): 45 min (1-page double-sided PDF)

**OUTCOME: Students understand and can apply advanced prompting techniques for expert-level results**
