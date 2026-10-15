# 🏆 HackWithBangalore 4.0 — CraftifAI Track A Submission Guide

> **Submission Form Link:** [https://forms.gle/eJyeCKCG2UH757QZ8](https://forms.gle/eJyeCKCG2UH757QZ8)  
> **Project Name:** SentinelEye — Autonomous Industrial Workplace Safety Sentinel  
> **Chosen Track:** Track A — PipeGen (Perception)  
> **Bonus Track:** Edge Optimization (INT8 Post-Training Quantization with EntropyCalibratorV2)

---

## 📋 Copy-Paste Form Fields

### 1. Project Title
```text
SentinelEye — Autonomous Workplace Safety & Hazard Defense System
```

### 2. Track Selection
```text
Track A — PipeGen (Perception)
```

### 3. Project Description (Comprehensive & High Impact)
```text
SentinelEye is a multi-stage, high-throughput edge Physical AI system engineered for heavy industrial facilities, construction bays, and manufacturing plants. In high-risk environments, worker safety violations (missing helmets/high-vis vests) and unauthorized intrusions into heavy machinery exclusion zones (e.g., active forklift loading paths, overhead cranes) often go unnoticed until fatal incidents occur. 

Built end-to-end using CraftifAI PipeGen v0.5.1, SentinelEye constructs a 5-stage vision perception and spatial reasoning pipeline:
1. Requirement: Multi-hazard detection monitoring up to 4 concurrent 1080p RTSP camera streams at >= 60 FPS with sub-25ms latency.
2. Pipeline IR: A complete Directed Acyclic Graph (DAG) connecting multi-stream decoders, batched stream muxers, primary object detectors, NvDCF object tracking, secondary attribute classifiers, and spatial polygon geofencing.
3. Model: YOLOv8x fine-tuned for industrial PPE and equipment detection combined with a ResNet50 secondary PPE classifier and YOLOv8-pose keypoint fall detector.
4. Compiler: TensorRT 8.6 layer fusion and INT8 quantization using EntropyCalibratorV2, achieving a 3.71x throughput increase (141 FPS vs 38 FPS baseline) and 55% power reduction (20W vs 44W).
5. Run: An edge DeepStream execution pipeline that streams actionable MQTT alerts (topic: sentinel/workplace/incident_alerts), appends tamper-evident RFC7946 JSON incident audit logs, and powers a real-time web tactical operations dashboard.
```

### 4. PipeGen Pipeline Details
- **Inputs:** 1080p RTSP streams / V4L2 USB camera / Industrial CCTV video feeds.
- **Tasks:** 
  - Real-time worker and heavy machinery detection & multi-object tracking (NvDCF).
  - Multi-class PPE compliance verification (Hardhat, High-Vis Vest, Safety Goggles).
  - Spatial Geofencing with ray-casting polygon intersection for dynamic exclusion zones.
  - Worker fall posture and motionless distress detection.
- **Models:** YOLOv8x-Safety (Primary Detector) + ResNet50 (Secondary PPE Classifier) + YOLOv8-Pose (Fall Keypoint Detector).
- **Precision:** TensorRT INT8 (Quantized with PTQ EntropyCalibratorV2) & FP16.
- **Outputs (Actionable):**
  - Real-time MQTT telemetry feed (`sentinel/workplace/incident_alerts`).
  - Structured, tamper-evident JSON compliance audit log (`sentinel_incidents.json`).
  - Live Tactical Operator Dashboard with audible siren and zone perimeter breach alarms.

### 5. Bonus Track Claimed
```text
Edge Optimization (Track A Bonus):
We performed quantization trade-off analysis comparing FP32, FP16, and INT8:
- FP32 Baseline: 38 FPS | 26.5ms Latency | 44.2W Power | 94.2% mAP50
- FP16 Half: 84 FPS | 11.9ms Latency | 29.8W Power | 94.0% mAP50
- INT8 Calibrated: 141 FPS (3.71x boost) | 7.1ms Latency (-73%) | 20.1W Power (-55%) | 93.5% mAP50 (-0.7% drop)
This allows running 4 concurrent 1080p camera streams on an NVIDIA Jetson Orin Nano with minimal thermal and power footprint.
```

### 6. Evidence Files Included in Repo
1. **Pipeline IR Graph:** https://github.com/Mugilarasi04/SentinelEye-Physical-AI/blob/main/assets/pipeline_ir_graph.svg
2. **TensorRT Speed & Power Benchmark Report:** https://github.com/Mugilarasi04/SentinelEye-Physical-AI/blob/main/assets/tensorrt_benchmark_chart.svg
3. **DeepStream Config & Launch Script:** https://github.com/Mugilarasi04/SentinelEye-Physical-AI/blob/main/pipegen_export/deepstream_app_config.txt
4. **Actionable Output Logs:** https://github.com/Mugilarasi04/SentinelEye-Physical-AI/blob/main/sentinel_incidents.json

### 7. GitHub Repository URL
```text
https://github.com/Mugilarasi04/SentinelEye-Physical-AI
```

