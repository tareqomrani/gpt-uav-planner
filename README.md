![UAV Battery Efficiency Estimator](banner.PNG)

Aerospace-grade physics + LLM Advisor + Swarm Logic + Stealth/Detectability + Mission Playback + CSV/JSON Exports

Live app script: Final_Full_App.py • Framework: Streamlit • Author: Tareq Omrani (2025)

⸻

🌟 Highlights
	•	Aerospace-grade physics: ISA density, bounded fixed-wing drag polar, rotor induced-power scaling, gust/terrain penalties, climb/descent energy.
	•	Battery & ICE support:
	•	🔋 Battery: temp derating, usable capacity, live battery gauge/timer.
	•	⛽ ICE (MQ-1/MQ-9): BSFC fuel burn, climb fuel, usable fuel fraction, Hybrid Assist (battery substitution) option.
	•	Stealth & Detectability: AI-visual and IR-thermal scores (0–100), cloud/altitude/speed/gust/stealth-load factors with color badges.
	•	LLM Mission Advisor: 3–5 concise tactics (graceful fallback if no API key).
	•	Swarm Advisor (Multi-Agent): roles, proposals, LEAD fusion, Stealth Ingress logic, in-threat-zone auto-assist, conversation log.
	•	Mission Playback: waypoint following, per-agent state timeline, map plot, CSV exports.
	•	Individual UAV Detailed Results: replaces “Quick Look” table with a rich, copy-ready panel + machine-readable JSON.
	•	Mobile-friendly UX: auto-select inputs on focus; clean gauges; clear warnings.
	•	One-click Exports: Scenario Summary + Detailed Results (CSV/JSON) and Swarm Playback/Waypoints CSV.

🧭 Workflow (at a glance)
	1.	Pick a UAV → fixed-wing or rotorcraft (battery or ICE).
	2.	Set mission → payload, speed, altitude, wind/gusts, terrain & stealth factors, waypoints, mode.
	3.	Estimate → endurance, ranges (best/upwind), draw/fuel, ΔT, detectability badges.
	4.	Plan → LLM Advisor tips + Swarm Advisor actions (RTB/Loiter/Hybrid Assist/etc.).
	5.	Playback & Export → step through mission frames, download CSV/JSON.

⸻

📦 Included UAV Profiles

Small multirotors / COTS: Generic Quad, DJI Phantom, Skydio 2+, Freefly Alta 8
Small tactical / fixed-wing: RQ-11 Raven, RQ-20 Puma, Teal Golden Eagle, Quantum Systems Vector
MALE (ICE): MQ-1 Predator, MQ-9 Reaper
Sandbox: Custom Build (user-tunable)

⸻

🔧 Inputs & Controls
	•	Flight Parameters: Battery Wh, Payload (g), Speed (km/h), Wind (km/h), Temperature (°C), Altitude (m), Elevation gain (m), Mode.
	•	Environment: Cloud cover, Gust factor, Terrain complexity (×), Stealth drag factor (×).
	•	ICE Panel (MQ-1/MQ-9): S, b, CD0, e, ηp, BSFC, fuel density, tank size, Hybrid Assist (% & minutes).
	•	Swarm & Stealth: Swarm size & rounds, Stealth Ingress toggle, Threat-zone radius.
	•	Waypoints: (x,y) in km (e.g., 2,2; 5,0; 8,-3).
	•	Debug: Enable Debug Mode; optional battery override clamp.

⸻

📊 Key Outputs
	•	Atmosphere: ρ and density ratio ρ/ρ₀.
	•	Power/Draw:
	•	Fixed-wing: bounded aero + hotel + install losses (+ gust/terrain/stealth penalties).
	•	Rotor: mass & density scaling + parasitic ∝ V² (+ gust penalties).
	•	Endurance & Range: Dispatchable endurance (with reserve), total distance, best heading vs upwind range.
	•	Thermals: ΔT via convection+radiation sink; risk level tags.
	•	Detectability: AI-visual & IR-thermal scores with colored badges and overall LOW/MODERATE/HIGH.
	•	ICE Metrics: total shaft+hotel power, L/h, climb fuel, usable fuel after assist.
	•	Live Gauges: animated Fuel or Battery gauge with elapsed/remaining timers.
	•	Detailed Results: human-readable bullets and JSON blob.
	•	Swarm: per-agent states, LEAD actions, Mission Playback map.
	•	Exports: Scenario Summary (CSV/JSON), Detailed Results (CSV/JSON), Swarm Playback CSV, Waypoints CSV.

⸻

🧠 LLM Mission Advisor (optional)
	•	Set OPENAI_API_KEY to enable targeted, concise mission recommendations.
	•	If unavailable, the app switches to heuristic guidance automatically.

⸻

🕵️ Stealth & Detectability
	•	AI-Visual: altitude, speed, platform type, gustiness, cloud cover, stealth factor.
	•	IR-Thermal: ΔT from waste-heat vs convective/radiative sink; altitude/cloud attenuation; ICE bias.
	•	Hybrid Assist (ICE): reduces IR signature for ingress windows (with energy tradeoffs).

⸻

🐝 Swarm Advisor (Multi-Agent)
	•	Agents propose actions (e.g., RTB, LOITER, HYBRID_ASSIST, RELAY_COMMS, etc.).
	•	LEAD fuses proposals with mission/environment rules and threat-zone logic.
	•	Auto Hybrid Assist inside threat-zone for MQ-1/MQ-9 when Stealth Ingress is active.
	•	Playback: timeline of agent states; map plot; CSV export.

⸻

📤 Exports (one-click)
	•	Scenario Summary: mission_results.csv / .json
	•	Detailed Results (Selected UAV): *_detailed_results.csv / .json
	•	Swarm Playback: swarm_mission_playback.csv
	•	Mission Waypoints: mission_waypoints.csv

⸻

🧪 Physics & Realism Notes
	•	ISA troposphere up to ~11 km; density used directly in aero/rotor models.
	•	Fixed-wing: drag polar with CD0, Oswald e, aspect ratio from b²/S; power = D·V/ηp.
	•	Rotorcraft: induced power scaling ∝ 1/√ρ; parasitic ~ V²; gust penalty vs wing/loading proxy.
	•	Reserves: 30% dispatch reserve; battery usable fraction 85%; fuel usable fraction 90%.
	•	Thermals: ΔT from waste heat over convection+radiation sink (emissivity & surface area).
	•	Climb/Descent: mgh in Wh (battery) or converted via BSFC (ICE); 20% descent recovery.

This is an educational, planning-grade estimator. Tune profiles to your platform; validate before operations.

⸻

🧩 FAQ

Q: Do I need an API key?
A: No. Without it, the LLM features gracefully fall back to heuristics.

Q: Can I add new UAVs?
A: Yes — extend the UAV_PROFILES dict with your platform specs.

Q: Why is endurance lower than spec sheets?
A: The app enforces reserves, hotel loads, penalties, and temperature derates for realism.

⸻

🗺️ Roadmap (short)
	•	Optional 3D path animation and georeferenced tiles.
	•	Expanded hybrid fuel-map modeling and pack health modeling.
	•	Import/export full mission plans (JSON schema).
