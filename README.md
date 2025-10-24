![UAV Battery Efficiency Estimator](banner.PNG)

## 🌟 Highlights  

**Aerospace-grade physics**  
ISA density, bounded fixed-wing drag polar, rotor induced-power scaling, gust/terrain penalties, and climb/descent energy.  

---

**🔋 Battery:**  
Temperature derating, usable capacity, and a live battery gauge/timer.  

**⛽ ICE (MQ-1 / MQ-9):**  
BSFC fuel burn, climb fuel, usable fuel fraction, and **Hybrid Assist** (battery substitution).  

---

**🥷 Stealth & Detectability:**  
AI-visual and IR-thermal scores (0–100), factoring cloud cover, altitude, speed, gusts, and stealth-load penalties with color-coded risk badges.  

**🤖 LLM Mission Advisor:**  
3–5 concise tactical recommendations (graceful fallback if no API key).  

---

**🐝 Swarm Advisor (Multi-Agent):**  
Multi-role UAV agents with proposals, LEAD fusion, Stealth Ingress logic, in-zone auto-assist, and conversation log.  

**🎞️ Mission Playback:**  
Waypoint following, per-agent state timeline, mission map plot, and CSV exports.  

---

**📊 Individual UAV Detailed Results:**  
Replaces “Quick Look” with a full, copy-ready panel and machine-readable JSON.  

**📱 Mobile-friendly UX:**  
Auto-select inputs on focus, clear gauges, and clean layout.  

**📤 One-click Exports:**  
Scenario Summary + Detailed Results (CSV/JSON) and Swarm/Waypoint CSV.

No API key? No problem — the app automatically switches to heuristic (non-LLM) mission logic.

⸻

🧭 Workflow Overview

1️⃣ Select a UAV → Choose from fixed-wing or rotorcraft (Battery or ICE).

2️⃣ Set mission parameters → Payload, speed, altitude, wind, terrain, stealth, and waypoints.

3️⃣ Estimate → Endurance, ranges (best/upwind), draw/fuel use, ΔT, detectability badges.

4️⃣ Plan → Receive LLM mission tips or heuristic alternatives.

5️⃣ Playback & Export → Replay the mission, visualize the swarm, and export results as CSV/JSON.

⸻

📦 Included UAV Profiles

Small multirotors / COTS:
Generic Quad, DJI Phantom, Skydio 2+, Freefly Alta 8

Small tactical / fixed-wing:
RQ-11 Raven, RQ-20 Puma, Teal Golden Eagle, Quantum Systems Vector

MALE (ICE):
MQ-1 Predator, MQ-9 Reaper

Sandbox:
Custom Build (user-tunable)

⸻

🛠️ Inputs & Controls

Flight Parameters:
Battery Wh, Payload (g), Speed (km/h), Wind (km/h), Temperature (°C), Altitude (m), Elevation gain (m), Flight Mode.

Environment:
Cloud cover (%), Gust factor, Terrain complexity (×), Stealth drag factor (×).

ICE Panel (MQ-1 / MQ-9):
S, b, CₙD₀, e, ηₚ, BSFC, fuel density, tank size, Hybrid Assist (% & duration).

Swarm & Stealth:
Swarm size, conversation rounds, Stealth Ingress toggle, Threat-zone radius.

Waypoints:
(x,y) in km (e.g., 2,2; 5,0; 8,-3).

Debug:
Enable Debug Mode; optional battery override clamp.

⸻

📊 Key Outputs

Atmospheric Data:
Air density (ρ) and density ratio (ρ/ρ₀).

Power & Draw:
	•	Fixed-wing: bounded aero + hotel + install losses (+ gust/terrain/stealth penalties).
	•	Rotorcraft: mass & density scaling + parasitic ∝ V² (+ gust penalties).

Endurance & Range:
Dispatchable endurance (with reserve), total distance, and heading-dependent range (best vs upwind).

Thermal Model:
ΔT computed via convective + radiative sink; color-coded risk levels.

Detectability Scores:
AI-visual / IR-thermal (0–100) + overall LOW / MODERATE / HIGH tag.

ICE Metrics:
Total shaft+hotel power, L/h, climb fuel, usable fuel after assist.

Live Simulation:
Animated battery/fuel gauge with elapsed and remaining time indicators.

Detailed Results:
Full UAV parameters in human-readable bullets and machine JSON format.

Swarm Advisor:
Multi-agent states, LEAD actions, playback map, and CSV exports.

⸻

🧠 LLM Mission Advisor (Optional)
	•	Uses OpenAI GPT-4o-mini for tactical suggestions and optimization insights.
	•	Outputs concise, scenario-specific mission guidance.
	•	Gracefully falls back to heuristic logic when no API key is found.

⸻

🕵️ Stealth & Detectability
	•	AI-Visual: Affected by altitude, speed, platform type, gustiness, cloud cover, and stealth factor.
	•	IR-Thermal: ΔT from waste-heat vs convective/radiative sink; attenuated by cloud/altitude; ICE adds small bias.
	•	Hybrid Assist (ICE): Reduces IR signature during stealth ingress; energy tradeoffs modeled dynamically.

⸻

🐝 Swarm Advisor (Multi-Agent)
	•	Each UAV acts as an autonomous agent proposing actions (e.g., RTB, LOITER, HYBRID_ASSIST, RELAY_COMMS).
	•	LEAD agent fuses decisions using environmental and mission context.
	•	Stealth Ingress Mode: Automatically enables Hybrid Assist inside threat zones for ICE-class UAVs.
	•	Playback Timeline: Simulated agent evolution with plotted mission paths and exportable logs.

⸻

📤 Export Options
	•	Scenario Summary: mission_results.csv / mission_results.json
	•	Detailed UAV Results: *_detailed_results.csv / *_detailed_results.json
	•	Swarm Playback: swarm_mission_playback.csv
	•	Mission Waypoints: mission_waypoints.csv

⸻

🧪 Physics & Realism
	•	ISA Atmosphere: Up to 11 km, density applied in aerodynamic + rotor calculations.
	•	Fixed-wing: Drag polar (CₙD₀, e), AR = b²/S, Power = D·V / ηₚ.
	•	Rotorcraft: Induced power ∝ 1/√ρ; parasitic ∝ V²; gust penalty based on WL proxy.
	•	Reserves: 30% dispatch reserve, 85% usable battery, 90% usable fuel.
	•	Thermals: ΔT = waste heat / (convective + radiative sink).
	•	Climb/Descent: mgh in Wh (battery) or via BSFC for ICE; 20% descent recovery modeled.

This is an educational, planning-grade estimator — realistic, not tactical. Validate results before deployment.

⸻

🧩 FAQ

Do I need an API key?
No — LLM features automatically revert to heuristic logic when unavailable.

Can I add new UAVs?
Yes — simply extend the UAV_PROFILES dictionary with your platform data.

Why is endurance lower than manufacturer specs?
The estimator includes dispatch reserves, hotel loads, gust/terrain drag, and temperature derates for realism.

⸻

🗺️ Roadmap
	•	Optional 3D flight-path animation & terrain tiles.
	•	Expanded hybrid fuel-mapping and pack health analytics.
	•	Import/export full mission plans (JSON schema).
