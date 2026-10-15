# 🛡️ SentinelEye — Autonomous Industrial Workplace Safety Sentinel

[![Hackathon](https://img.shields.io/badge/HackWithBangalore%204.0-CraftifAI%20Physical%20AI-blue)](https://luma.com/5z8w42mq)
[![Track](https://img.shields.io/badge/Track%20A-PipeGen%20(Perception)-cyan)](https://developer.craftifai.com)
[![TensorRT](https://img.shields.io/badge/TensorRT-8.6.2%20INT8-green)](https://developer.nvidia.com/tensorrt)
[![DeepStream](https://img.shields.io/badge/NVIDIA-DeepStream%206.3%2F7.0-brightgreen)](https://developer.nvidia.com/deepstream-sdk)
[![Actionable](https://img.shields.io/badge/Actionable%20Output-MQTT%20%2B%20JSON%20Logs-orange)](#actionable-outputs)

> **CraftifAI Physical AI Hackathon (Embedded SF / HackWithBangalore 4.0)**  
> **Theme:** Building Physical AI Systems That See, Decide, and Act  
> **Track:** Track A — PipeGen (Perception)  
> **Bonus Prize Claim:** Edge Optimization (INT8 Post-Training Quantization on Jetson/RTX)

---

## 📌 Executive Summary

Industrial manufacturing floors, loading docks, and construction yards are high-velocity, hazardous environments. Every year, thousands of severe injuries occur due to two preventable causes:
1. **Unchecked PPE Non-Compliance:** Workers entering hazardous zones without hardhats, high-visibility vests, or protective eye gear.
2. **Exclusion Zone Breaches:** Personnel crossing into blind spots of moving forklifts or beneath suspended crane loads.

**SentinelEye** solves this with an edge Physical AI perception pipeline built using **CraftifAI PipeGen v0.5.1**. SentinelEye processes live high-definition RTSP camera feeds, accelerates multi-task neural networks with **TensorRT INT8**, evaluates spatial polygon geofencing in real time, and broadcasts actionable alarms over **MQTT** and tamper-evident **JSON compliance audit logs**.

---

## 🏗️ The 5-Stage PipeGen Architecture

In compliance with Track A mandatory requirements, SentinelEye implements the full 5-stage PipeGen lifecycle:

```
[Camera / RTSP / Video]
          │
          ▼
┌──────────────────┐
│ STAGE 1: INGEST  │  NvMultiStreamInput (1080p @ 30 FPS) + NvStreamMux
└─────────┬────────┘
          │
          ▼
┌──────────────────┐
│ STAGE 2: IR DAG  │  Pipeline IR specification linking detectors, trackers & spatial analytics
└─────────┬────────┘
          │
          ▼
┌──────────────────┐
│ STAGE 3: MODELS  │  Primary: YOLOv8x | Secondary: ResNet50 PPE | Pose: YOLOv8-Pose
└─────────┬────────┘
          │
          ▼
┌──────────────────┐
│ STAGE 4: COMPILE │  TensorRT 8.6 INT8 Calibration (EntropyCalibratorV2) & Layer Fusion
└─────────┬────────┘
          │
          ▼
┌──────────────────┐
│ STAGE 5: RUN     │  DeepStream edge container emitting MQTT alerts, JSON logs & Web HUD
└──────────────────┘
```

---

## 🚀 Edge Optimization Benchmark (Bonus Prize)

SentinelEye is optimized for embedded edge deployment on **NVIDIA Jetson Orin Nano** and **RTX Ada Lovelace** architectures. Through PipeGen's Compiler stage, we performed comprehensive quantization trade-off analysis:

| Precision Mode | Inference Latency | Throughput (FPS) | GPU Memory | Power Draw | Accuracy (mAP@50) | Concurrent 1080p Streams |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **FP32 (Baseline)** | 26.5 ms | 37.7 FPS | 1,840 MB | 44.2 W | 94.2% | 1 Stream |
| **FP16 (Half)** | 11.9 ms | 84.0 FPS | 960 MB | 29.8 W | 94.0% | 2 Streams |
| **INT8 (Quantized)** 🏆 | **7.1 ms (-73%)** | **140.8 FPS (3.7x)** | **512 MB (-72%)** | **20.1 W (-55%)** | **93.5% (-0.7%)** | **4 Streams** |

*Key Takeaway:* Quantizing from FP32 to INT8 yields a **3.71x throughput increase** with only a negligible **0.7% drop in detection accuracy**, enabling multi-camera edge inference under 20W.

---

## 📡 Actionable Outputs

Unlike simple visual demos that only draw boxes on a screen, SentinelEye generates **direct actionable outputs**:

### 1. Real-Time MQTT Telemetry
High-priority incident events are published to MQTT topic `sentinel/workplace/incident_alerts`:
```json
{
  "incident_id": "INC-1792076087587",
  "timestamp": "2026-10-15T14:54:47.587Z",
  "incident_type": "ZONE_INTRUSION",
  "severity": "CRITICAL",
  "worker_tracker_id": "W-102",
  "zone_id": "ZONE_OVERHEAD_CRANE_2",
  "bounding_box": [653, 221, 50, 120],
  "compliance_details": {
    "violations": [
      "NO_HELMET",
      "HAZARD_ZONE_BREACH: Overhead Crane Exclusion Area"
    ]
  },
  "action_taken": "DISPATCH_AUDIO_ALARM_AND_BROADCAST_MQTT"
}
```

### 2. Tamper-Evident JSON Audit Logs
All violations are persisted to `sentinel_incidents.json` with microsecond timestamps, worker tracker tracking IDs, spatial coordinates, and supervisor resolution status for regulatory compliance (OSHA / ISO 45001).

### 3. Live Web Tactical Operations Dashboard
An interactive operations dashboard (`http://localhost:8080`) providing:
* Real-time canvas tracking overlay with animated geofence exclusion perimeters.
* Live FPS, Latency (ms), and Power (W) readouts.
* Instant audio alarm siren synthesizer.
* One-click JSON audit log export.

---

## 📂 Project Structure

```
.
├── SUBMISSION_GUIDE.md               # Quick copy-paste guide for Google Form submission
├── README.md                         # Project documentation and benchmarks
├── sentinel_incidents.json           # Actionable output: structured compliance audit trail
├── pipegen_export/                   # Complete CraftifAI PipeGen export package
│   ├── pipeline_ir.json              # Stage 2: Pipeline IR graph DAG definition
│   ├── deepstream_app_config.txt     # Stage 5: DeepStream multi-stream pipeline config
│   ├── run.sh                        # Stage 5: Production execution script
│   ├── models/
│   │   ├── model_catalog.json        # Stage 3: Model definitions and tensor layouts
│   │   ├── labels_primary.txt        # Primary detector classes (person, forklift, etc.)
│   │   └── labels_ppe.txt            # PPE classifier labels (helmet, vest, goggles)
│   └── compiler/
│       ├── trt_compiler_config.json  # Stage 4: TensorRT INT8 calibration configuration
│       ├── config_infer_primary.txt  # DeepStream nvinfer primary config
│       ├── config_infer_ppe.txt      # DeepStream nvinfer secondary PPE config
│       └── speed_benchmark_report.json # Detailed TensorRT speed, latency, power benchmarks
├── src/
│   ├── sentinel_engine.py            # Core edge perception & spatial reasoning engine
│   ├── mqtt_publisher.py             # Actionable MQTT broker client
│   └── incident_logger.py            # JSON compliance audit logger
├── dashboard/                        # Tactical Operations Web Control Center
│   ├── index.html                    # Glassmorphic dark-mode tactical interface
│   ├── style.css                     # High-tech design tokens and animations
│   └── app.js                        # Canvas renderer, Web Audio alarm & telemetry poller
└── assets/
    ├── pipeline_ir_graph.svg         # Evidence: PipeGen Pipeline IR DAG Diagram
    └── tensorrt_benchmark_chart.svg  # Evidence: TensorRT Speed/Latency/Power Chart
```

---

## ⚡ Quickstart & Live Run

### 1. Launch the Live Engine & Tactical Dashboard
```bash
python3 src/sentinel_engine.py --port 8080
```
Open your browser to:
👉 **[http://localhost:8080](http://localhost:8080)**

### 2. Run with Native DeepStream & TensorRT (on Linux / Jetson with GPU)
```bash
bash pipegen_export/run.sh deepstream
```

---

## 👥 HackWithBangalore 4.0 Team Submission
- **Track:** Track A — PipeGen (Perception)
- **Submission Form:** [https://forms.gle/eJyeCKCG2UH757QZ8](https://forms.gle/eJyeCKCG2UH757QZ8)
