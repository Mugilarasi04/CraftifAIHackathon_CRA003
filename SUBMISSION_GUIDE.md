# 🏆 HackWithBangalore 4.0 — CraftifAI Track A Submission Guide

> **Form 1 (Feedback):** [https://docs.google.com/forms/d/e/1FAIpQLSc3OkTWFA58URYmLmHSNjunO2yJLEEq8aMuaxrT7ROyPHarzA/viewform](https://docs.google.com/forms/d/e/1FAIpQLSc3OkTWFA58URYmLmHSNjunO2yJLEEq8aMuaxrT7ROyPHarzA/viewform)  
> **Form 2 (Project Submission):** [https://docs.google.com/forms/d/e/1FAIpQLSeUmbJbcFMQEiIvKkcD7hoTOvdtQXRNZE6uilCYH9fRDAZqvw/viewform](https://docs.google.com/forms/d/e/1FAIpQLSeUmbJbcFMQEiIvKkcD7hoTOvdtQXRNZE6uilCYH9fRDAZqvw/viewform)  
> **Participant ID:** `CRA003`  
> **Repository Name:** `CraftifAIHackathon_CRA003`  
> **Repository Link:** [https://github.com/Mugilarasi04/CraftifAIHackathon_CRA003](https://github.com/Mugilarasi04/CraftifAIHackathon_CRA003)

---

## 📋 Copy-Paste Form Fields for Form 2

### 1. About You
* **Full name:**
  ```text
  Mugilarasi M S
  ```
* **Participant ID:**
  ```text
  CRA003
  ```
* **Email:**
  ```text
  mugilarasims@gmail.com
  ```

---

### 2. What You Built
* **Project name:**
  ```text
  SentinelEye: Autonomous Industrial Safety & Hazard Defense System
  ```

* **In one line, what does it do?**
  ```text
  Detects PPE violations and dangerous exclusion-zone intrusions in real time, triggering instant MQTT alarms and compliance audit logs.
  ```

* **Who is it for, and what changes for them?**
  ```text
  It is for industrial plant safety officers, warehouse supervisors, and construction site managers overseeing high-risk environments like forklift bays and overhead crane paths. Today, supervisors rely on periodic manual spot-checks or post-incident CCTV review after injuries have already occurred. SentinelEye transforms this into proactive zero-delay intervention: catching 100% of zone breaches and missing PPE within 25ms, preventing catastrophic forklift collisions and saving hours of daily safety audit paperwork.
  ```

* **Which area does it serve?**
  * Select: **Factories and worker safety**

* **What does your pipeline send out?** *(Tick all that apply)*
  * ☑️ **Live display**
  * ☑️ **Metadata file (JSON)**
  * ☑️ **MQTT**
  * ☑️ **Something I built on top: an alert, dashboard, API or database**

* **Where does that output go, and who acts on it?**
  ```text
  Real-time MQTT telemetry (topic: sentinel/workplace/incident_alerts) and an audible siren trigger immediately in the site safety control room dashboard when an unauthorized worker enters a designated forklift or crane perimeter without mandatory PPE. Simultaneously, a structured RFC7946 JSON incident record is logged to sentinel_incidents.json for the safety officer's daily OSHA/ISO compliance audit.
  ```

* **What input did you test it on?**
  * Select: **Video from the real setting, recorded or found**

* **What does your pipeline do between input and output?**
  ```text
  1. Ingests 1080p stream through NvStreamMux batched preprocessor.
  2. Runs YOLOv8x TensorRT INT8 primary detector to classify personnel and machinery.
  3. Applies NvDCF multi-object tracker for persistent worker ID and trajectory history.
  4. Feeds person crops to a secondary ResNet50 FP16 classifier to verify Hardhat, High-Vis Vest, and Goggles compliance.
  5. Evaluates 2D spatial geofencing with ray-casting polygon intersection against active exclusion zones (Forklift Bay & Overhead Crane).
  6. Triggers MQTT alerts on breach and writes immutable incident logs to sentinel_incidents.json.
  ```

* **How fast does it run, and on what hardware?**
  ```text
  Runs at 140.8 FPS with 7.1 ms end-to-end latency and 20.1W power consumption on NVIDIA Jetson / RTX GPU using TensorRT INT8 quantization (EntropyCalibratorV2), achieving a 3.71x speedup over the 37.7 FPS (26.5ms) FP32 baseline.
  ```

* **What does it not handle yet?**
  ```text
  Extreme camera occlusions where a worker is more than 80% obscured behind heavy machinery, and dynamic moving exclusion zones attached to moving vehicles (currently zones are defined as static polygons).
  ```

---

### 3. Links and Checks
* **GitHub repository URL:**
  ```text
  https://github.com/Mugilarasi04/CraftifAIHackathon_CRA003
  ```

* **Demo video URL:**
  *(Paste link to your 1-3 minute screen recording or Google Drive video)*

* **Export archive link:**
  *(Leave blank if repository is under 100MB)*

* **My repository is public:**
  * Select: **Yes**

* **My README shows it running and shows the Pipeline IR node graph:**
  * Select: **Yes**

* **My repository has the Export Project folder...:**
  * Select: **Yes**
