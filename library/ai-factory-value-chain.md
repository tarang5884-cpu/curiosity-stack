# AI Factory Value Chain Module

**Version**: 1.0  
**Last Updated**: 01 August 2026  
**Purpose**: Complete reference of every physical component and software layer required to design, build, and operate a modern AI Factory (Hyperscale AI Data Center).

---

## 1. Power Infrastructure Layer

| Component | Description | Role in AI Factory |
|-----------|-------------|--------------------|
| Grid Connection / Substation | High-voltage interconnection to utility | Primary power intake |
| HV / EHV Transformers | Step-down from 220/400 kV to 33/11 kV | Voltage transformation |
| Gas-Insulated Switchgear (GIS) / AIS | High & Medium voltage switchgear | Protection & switching |
| Medium Voltage Switchgear | 11–33 kV distribution | Campus-level power distribution |
| Low Voltage Switchgear | 415V / 480V boards | Final distribution |
| Busways / Bus Ducts | High-current power bars | Efficient delivery to rows/racks |
| Uninterruptible Power Supply (UPS) | Double-conversion or modular UPS | Clean continuous power |
| Battery Energy Storage (BESS) | Lithium-ion or alternative chemistries | Short-duration backup + peak shaving |
| Diesel / Gas Generators | Large backup gensets | Long-duration backup |
| Power Distribution Units (PDUs) | Rack-level and row-level | Final power delivery to servers |
| Automatic Transfer Switches (ATS) | Seamless source switching | Reliability |
| Power Monitoring & SCADA | Electrical monitoring systems | Visibility and control |

---

## 2. Cooling Infrastructure Layer

| Component | Description | Role in AI Factory |
|-----------|-------------|--------------------|
| CRAH / CRAC Units | Computer Room Air Handlers | Legacy air cooling |
| Chillers | Water or air-cooled | Primary heat rejection |
| Cooling Towers / Dry Coolers | Atmospheric heat rejection | Final heat dump |
| Rear-Door Heat Exchangers | Water-cooled rack doors | Transitional liquid cooling |
| Direct-to-Chip Cold Plates | Liquid cold plates on GPUs/CPUs | Mainstream for high-density AI |
| Coolant Distribution Units (CDUs) | Pumps, heat exchangers, controls | Heart of liquid cooling loop |
| Secondary Fluid Network | Pipes, manifolds, hoses | Coolant distribution |
| Immersion Cooling Tanks | Single-phase or two-phase | Extreme density cooling |
| Dielectric Fluid | Non-conductive cooling fluid | Used in immersion systems |
| Facility Water Loop | Building-level chilled water | Connects CDUs to chillers |
| Leak Detection & Monitoring | Sensors + control systems | Safety-critical |

---

## 3. Physical Facility & Structure Layer

| Component | Description |
|-----------|-------------|
| Building Shell / White Space | Data halls |
| Raised Floor or Slab Design | Airflow or liquid-ready design |
| Racks / Cabinets | High-power, liquid-ready (42U–52U) |
| Hot/Cold Aisle Containment | Airflow management |
| Fire Suppression Systems | Clean agent or water mist |
| Security Systems | Access control, CCTV, biometrics |
| Cable Management | Overhead or underfloor trays |
| Prefabricated Modules / Skids | Factory-built power & cooling modules |

---

## 4. Compute & Networking Hardware Layer

| Component | Description | Key Global Players |
|-----------|-------------|--------------------|
| AI Accelerators (GPUs) | High-performance training/inference chips | NVIDIA (dominant), AMD, Broadcom, Custom ASICs |
| CPUs | Host processors | Intel, AMD, NVIDIA Grace |
| High Bandwidth Memory (HBM) | HBM3e / HBM4 | SK Hynix, Samsung, Micron |
| Server Motherboards | Multi-GPU baseboards | Various ODMs |
| NVLink / NVSwitch | High-speed GPU interconnect | NVIDIA |
| Networking ASICs | High-speed Ethernet / InfiniBand | Broadcom, NVIDIA, Marvell |
| Network Interface Cards (NICs) | 400G/800G SmartNICs / DPUs | NVIDIA BlueField, Broadcom, AMD |
| Optical Transceivers | 400G/800G/1.6T optics | Coherent, Lumentum, Innolight |
| Fiber Cabling | Single-mode & multi-mode | Corning + others |
| High-Performance Storage | NVMe, object storage | Various |
| DPUs / IPUs | Data Processing Units | NVIDIA, AMD, Intel |

---

## 5. Software & Orchestration Stack

### 5.1 Low-Level / Firmware
- GPU Firmware & Drivers
- BMC (Baseboard Management Controller)
- Networking Operating Systems (SONiC, NVIDIA Cumulus, etc.)

### 5.2 Cluster Management & Orchestration
| Layer | Examples | Purpose |
|-------|----------|--------|
| Cluster Scheduler | Kubernetes + NVIDIA GPU Operator, Slurm, Run:ai | Job scheduling |
| Container Runtime | Docker, containerd, NVIDIA Container Toolkit | Packaging |
| Resource Manager | Kubernetes, Ray, Volcano | Multi-tenant allocation |
| Fabric Manager | NVIDIA Fabric Manager, NCCL | Multi-GPU / multi-node communication |

### 5.3 AI Frameworks & Libraries
- CUDA + cuDNN + TensorRT (NVIDIA)
- ROCm (AMD)
- PyTorch, TensorFlow, JAX
- Hugging Face, vLLM, TensorRT-LLM
- DeepSpeed, Megatron-LM, NeMo
- Triton Inference Server

### 5.4 MLOps / Platform Layer
- Experiment Tracking (Weights & Biases, MLflow)
- Model Registry
- Feature Store
- Pipeline Orchestration (Kubeflow, Airflow, Flyte)
- Monitoring & Observability (Prometheus, Grafana, NVIDIA DCGM)

### 5.5 Data & Storage Software
- Distributed File Systems (Lustre, GPFS, BeeGFS)
- Object Storage (Ceph, MinIO)
- High-performance data loading (NVIDIA DALI, WebDataset)

### 5.6 Security & Governance
- Identity & Access Management
- Confidential Computing (where required)
- Audit & Compliance tooling

---

## 6. Full Stack Hierarchy (Bottom → Top)

**Physical**
1. Power Generation / Grid Connection
2. Substation + Transformers + Switchgear
3. UPS + Generators + Busways
4. Cooling Plant (Chillers → CDUs → Liquid loops)
5. Data Hall + Racks
6. Servers (CPU + GPU + HBM + Networking)
7. Optical & Copper Fabric

**Software**
1. Firmware / Drivers
2. Operating System + Container Runtime
3. Cluster Orchestrator
4. Communication Libraries (NCCL etc.)
5. AI Frameworks
6. Model Serving & Inference Engines
7. MLOps Platform
8. Observability & Security

---

## 7. Usage Notes for Curiosity Stack

- Use this module as the master reference when analysing any company claiming AI Data Center exposure.
- Map Indian listed companies against specific components (especially Power, Cooling, Cabling, and EPC layers).
- Distinguish clearly between:
  - Component suppliers (transformers, switchgear, cooling, cables)
  - Systems integrators / EPC
  - Operators / Developers
  - Compute / Silicon plays

**Related Modules / Commands**
- `commands/morning-brief.md`
- Watchlist tracking for Power T&D + Cooling names

---

*This module is a living reference. Update as new cooling architectures, power densities, or software stacks become standard.*
