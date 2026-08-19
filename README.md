# from-signal-to-reviving
Analyse et traitement des signaux phonocardiographiques (PCG) pour l’étude de la stationnarité, la segmentation S1/S2 et l’extraction de caractéristiques temporelles et temps-fréquentielles à des fins de détection des pathologies cardiaques.

# 🫀 Interpretable Artificial Intelligence for Heart Sound Analysis

## Informational Signature Extraction and Cardiac Pathology Detection Using Phonocardiogram Databases

---

## 🎓 Project Information

**Type:** Projet de Fin d'Études (PFE)

**Field:** Artificial Intelligence, Signal Processing & Biomedical Signal Analysis

**University:** Université Mohammed V de Rabat

### Supervisors

- **Khalid MINAOUI**
- **BELMAJDOUB Hanae**
- **Reda BEKKALI**

### Author

- **EZZERROUTI Salwa**

---

# 📌 1. Introduction

Cardiovascular diseases are among the leading causes of mortality worldwide. Early detection of cardiac abnormalities, such as heart murmurs, is essential for timely clinical intervention.

The **Phonocardiogram (PCG)** records the acoustic activity of the heart and provides a non-invasive source of information for cardiac analysis.

Traditional cardiac auscultation is highly dependent on the physician's expertise and may suffer from inter-observer variability. Recent advances in **signal processing, machine learning, deep learning, and explainable artificial intelligence** provide new opportunities for automated heart sound analysis.

However, high classification performance alone is not sufficient for clinical applications. AI systems should also provide **interpretable and clinically meaningful explanations**.

This project therefore aims to develop an **interpretable AI framework for PCG analysis**, from signal processing and informational signature extraction to cardiac pathology detection and model explanation.

---

# 🎯 2. Research Objectives

The project is structured around **three main objectives**.

---

## 🔵 Objective 1 — Informational Signature Extraction

### Goal

Identify the signal characteristics and acoustic signatures that contain relevant information for distinguishing normal and pathological heart sounds.

### Main Components

#### Signal Preprocessing

- Noise reduction
- Signal normalization
- DC offset correction
- Baseline correction
- Artifact analysis

#### Cardiac Cycle Analysis

- Cardiac cycle segmentation
- S1 detection
- S2 detection
- Systole identification
- Diastole identification

#### Time-Frequency Analysis

Different representations will be investigated:

- Short-Time Fourier Transform (STFT)
- Continuous Wavelet Transform (CWT)
- Stockwell Transform

#### Informational Signatures

The analysis will focus on:

- Spectral energy distribution
- Dominant frequencies
- Frequency-band characteristics
- Frequency modulation patterns
- Temporal envelope characteristics
- Energy variations
- Pathology-related acoustic biomarkers

### Research Question

> **What are the most informative signal signatures that differentiate normal from pathological heart sounds?**

---

# 🟠 Objective 2 — Development of Interpretable AI Models

### Goal

Develop and evaluate machine learning and deep learning models for automatic cardiac pathology detection.

## Machine Learning

The following approaches will be investigated:

- Support Vector Machine (SVM)
- Random Forest
- Gradient Boosting

These models will use features extracted from PCG signals and their time-frequency representations.

## Deep Learning

The following architectures will be investigated:

### 1D CNN

Applied to raw or preprocessed PCG signals.

### 2D CNN

Applied to time-frequency representations such as:

- STFT spectrograms
- CWT scalograms
- Stockwell representations

### Attention-Based Models

Attention mechanisms will be investigated to identify important temporal and frequency regions.

### Transformer Models

Transformer-based architectures may be explored for learning temporal dependencies within PCG recordings.

### Research Question

> **Can time-frequency representations and AI models improve the robustness and generalization of cardiac pathology detection?**

---

# 🟢 Objective 3 — Interpretability and Clinical Reliability

### Goal

Understand the reasoning behind AI predictions and evaluate whether the information used by the models corresponds to meaningful cardiac characteristics.

The project will investigate several Explainable AI (XAI) techniques.

## SHAP

Used to explain predictions from classical machine learning models.

## Grad-CAM

Used with CNN models to identify important regions of time-frequency representations.

## Saliency Maps

Used to identify important regions of the input PCG signal.

## Attention Visualization

Used to analyze which temporal and frequency regions receive the highest attention.

### Interpretability Analysis

The explanations will be analyzed to determine:

- Which cardiac cycles influence predictions?
- Which temporal regions are important?
- Which frequency bands contribute to classification?
- Which acoustic features influence the prediction?
- Whether the learned representations are consistent with known clinical markers.

### Research Question

> **How can AI predictions be made interpretable and clinically reliable?**

---

# 🔬 3. Overall Methodology

The proposed framework follows three main stages:

```text
                    PCG DATABASE
                         │
                         ▼
              ┌─────────────────────┐
              │     OBJECTIVE 1     │
              │ Informational       │
              │ Signature Extraction│
              └──────────┬──────────┘
                         │
                         ▼
                Signal Preprocessing
                         │
                         ▼
               Cardiac Cycle Analysis
                         │
                         ▼
              Time-Frequency Analysis
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
             STFT       CWT     Stockwell
              │          │          │
              └──────────┼──────────┘
                         ▼
                 Feature Extraction
                         │
                         ▼
              ┌─────────────────────┐
              │     OBJECTIVE 2     │
              │   AI Development    │
              └──────────┬──────────┘
                         │
                 ┌───────┴───────┐
                 ▼               ▼
          Machine Learning   Deep Learning
          SVM / RF / GB      CNN / Attention
                 │               │
                 └───────┬───────┘
                         ▼
                    Prediction
                         │
                         ▼
              ┌─────────────────────┐
              │     OBJECTIVE 3     │
              │ Interpretability &  │
              │ Clinical Reliability│
              └──────────┬──────────┘
                         │
                ┌────────┼────────┐
                ▼        ▼        ▼
               SHAP   Grad-CAM  Saliency
                │        │        │
                └────────┼────────┘
                         ▼
                Clinical Interpretation
