# 📐 R.S. Aggarwal Class 9 Mathematics MCQ Revision Portal

> Interactive, web-based mathematics MCQ practice companion covering all 17 chapters of CBSE Class 9 R.S. Aggarwal Mathematics, featuring instant KaTeX formula typesetting, click-to-reveal solutions, and integrated AI search.

[![React](https://img.shields.io/badge/React-18.2.0-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev/)
[![Vite](https://img.shields.io/badge/Vite-7.2.4-646CFF?style=for-the-badge&logo=vite&logoColor=white)](https://vite.dev/)
[![KaTeX](https://img.shields.io/badge/KaTeX-LaTeX_Math-00D084?style=for-the-badge&logo=latex&logoColor=white)](https://katex.org/)
[![React Router](https://img.shields.io/badge/React_Router-7.11-CA4245?style=for-the-badge&logo=react-router&logoColor=white)](https://reactrouter.com/)
[![Framer Motion](https://img.shields.io/badge/Framer_Motion-12.23-0055FF?style=for-the-badge&logo=framer&logoColor=white)](https://www.framer.com/motion/)
[![Status](https://img.shields.io/badge/Status-Maintained-success?style=for-the-badge)]()

---

## 📖 Overview

**MCQ-RS-Aggrawal-Class-9-Website** is a focused study and revision platform built specifically for students preparing for CBSE Class 9 Mathematics exams using the standard **R.S. Aggarwal** textbook. It features extensive multiple-choice question banks spanning all 17 textbook chapters, rendered with crisp mathematical typography via KaTeX.

The web app is optimized for rapid self-assessment with interactive click-to-reveal answers, memoized question rows for lag-free scrolling, and a custom context menu enabling instant one-click solution lookup on Google or ChatGPT.

---

## ✨ Features

- **Full Curriculum Coverage (17 Chapters)**:
  1. *Number Systems*
  2. *Polynomials*
  3. *Factorisation of Polynomials*
  4. *Linear Equations in Two Variables*
  5. *Coordinate Geometry*
  6. *Introduction to Euclid’s Geometry*
  7. *Lines and Angles*
  8. *Triangles*
  9. *Congruence of Triangles and Inequalities in a Triangle*
  10. *Quadrilaterals*
  11. *Areas of Parallelograms and Triangles*
  12. *Circles*
  13. *Areas of Triangles and Quadrilaterals (Heron's Formula)*
  14. *Volume and Surface Area of Solids*
  15. *Presentation of Data in Tabular Form*
  16. *Mean, Median and Mode of Ungrouped Data*
  17. *Probability*
- **Interactive Click-to-Reveal**: Tap or click any question to toggle the correct answer key in vivid emerald green (`#4ade80`).
- **Instant AI & Web Solution Lookup**: Right-click on any question row to bring up a custom context menu that automatically formats the question and options for immediate search via **Google Search** or **ChatGPT**.
- **High-Fidelity KaTeX Math Rendering**: Integrated `react-latex-next` with KaTeX engine ensuring sharp exponents, radicals, fractions, and Greek symbols.
- **Optimized Rendering**: `React.memo` question row components with custom shallow equality checks prevent full-list re-renders upon individual answer reveals.
- **Fluid Navigation**: Built with React Router 7 and Framer Motion transitions between the chapter index and practice views.

---

## 🛠️ Tech Stack

- **UI Framework**: React 18.2.0 & React DOM
- **Build Tool**: Vite 7.2.4 (Hot Module Replacement & Rolldown/ESBuild)
- **Math Formatting**: `katex` 0.16.27 & `react-latex-next` 3.0.0
- **Routing**: `react-router-dom` 7.11.0
- **Animations**: `framer-motion` 12.23.26
- **Language / Runtime**: Modern JavaScript (ES Modules), Node.js 20.x

---

## 🚀 Getting Started

### Prerequisites
- **Node.js**: v18.0.0+ (Node.js 20.x recommended)
- **npm** or **yarn** / **pnpm**

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AryansDevStudios/MCQ-RS-Aggrawal-Class-9-Website.git
   cd MCQ-RS-Aggrawal-Class-9-Website
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

### Running the App

- **Development server**:
  ```bash
  npm run dev
  ```
  Open [http://localhost:5173](http://localhost:5173) in your browser.

- **Production build & preview**:
  ```bash
  npm run build
  npm run preview
  ```

---

## 📁 Project Structure

```plaintext
MCQ-RS-Aggrawal-Class-9-Website/
├── index.html                   # HTML entry point with viewport configuration
├── package.json                 # Project dependencies & build scripts
├── vite.config.js               # Vite bundler configuration
├── public/                      # Static assets & icons
└── src/
    ├── App.css                  # Global layout styles & theme tokens
    ├── App.jsx                  # Main router setup & layout wrapping
    ├── data.js                  # Complete question bank database for all 17 chapters
    ├── index.css                # Base typography & KaTeX styling
    ├── main.jsx                 # React root DOM mounting
    └── pages/
        ├── Home.jsx             # Chapter catalog grid with question counters
        └── Chapter.jsx          # Interactive test runner, KaTeX viewer & AI context menu
```

---

## 💡 How to Use

1. **Browse Chapters**: Select any chapter from the homepage grid.
2. **Attempt Questions**: Read the mathematical problem and select your answer mentally.
3. **Verify Instantly**: Click on the question card to reveal the correct option highlighted in green.
4. **Get AI Explanations**: Right-click on any tricky problem and select *"Search on ChatGPT"* or *"Search on Google"* to view detailed step-by-step derivation.

---

## 🤝 Contributing

Suggestions for new questions, typo fixes in equations, or UI enhancements are warmly welcomed!
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/FixChapter4Equations`)
3. Commit your Changes (`git commit -m 'Fix LaTeX syntax in Chapter 4 Q12'`)
4. Push to the Branch (`git push origin feature/FixChapter4Equations`)
5. Open a Pull Request

---

## 📄 License

This repository is maintained for educational purposes under the [MIT License](LICENSE). Educational textbook problems are reference material from R.S. Aggarwal Mathematics (Bharati Bhawan Publishers & Distributors).
