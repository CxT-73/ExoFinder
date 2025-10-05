**# NASA_SPACE_CHALLENGE-2025
#ExoFinder:

Summary:**
ExoFinder is a web application designed to provide users, scientists, and enthusiasts with the ability to explore new exoplanet datasets through an interactive visualization of the exoplanets detected by the ML models. It is designed to be user-friendly, yet it also includes advanced features for those deeply involved in the field.

**Project Demonstration:**
https://uab-my.sharepoint.com/:b:/g/personal/1666599_uab_cat/EboaFGqA9qlGqMImbE3pEZUBfxQfT-acZaVm0mrCXpjg-A?e=xXaBjB

**Project Details:**
This project simulates the Transit Method used in astrophysics to detect exoplanets via machine learning (ML). It allows users to adjust stellar and planetary parameters: such as radius, mass, orbital period, and temperature, and visually observe how an exoplanet transits across the star. As the planet passes in front of the star, the system dynamically calculates the drop in observed flux and generates a real-time light curve using Chart.js.

Beyond visualization, the simulation extracts scientifically relevant features, such as the impact parameter, planet-to-star radius ratio, and equilibrium temperature, which are displayed in formatted KOI (Kepler Object of Interest) style. These features can later be used for machine learning classification with Python in the second phase of the project, where datasets are uploaded and processed with models such as Random Forest, CatBoost, XGBoost, and ensemble methods.

The project was developed using HTML, CSS, and JavaScript for interactivity, with a modular structure split between UI handling and astrophysical calculations. One creative aspect of the project is the interactive control system: the exoplanet only appears when the user hovers over the star, allowing an intuitive understanding of transit geometry. Additionally, noise can be toggled on and off to simulate real telescope observations.

This tool is designed both for education and research prototyping, helping users understand how exoplanetary signals are formed and how machine learning can be applied to classify them.

**Use of Artificial Intelligence (AI):**
We made limited use of Artificial Intelligence tools to accelerate development efficiency. Specifically:

We used AI based code assistants (such as ChatGPT/Gemini) to help generate small UI interaction snippets and assist with frontend logic structuring (e.g., event handling and DOM manipulation to refresh the UI).
No AI generated images, videos, audio, or datasets were used. All visual or media elements were sourced from copyright-free resources.
All scientific formulas, simulations, and feature calculations were manually implemented and verified.
All AI generated code suggestions were reviewed, adapted, and validated by the team to ensure correctness and originality.

**NASA Data:**
Kepler Objects of Interest (KOI) (https://www.spaceappschallenge.org/2025/challenges/a-world-away-hunting-for-exoplanets-with-ai/?tab=resources)

**Space Agency Partner & Other Data:**
Exoplanet Detection Using Machine Learning (https://www.spaceappschallenge.org/2025/challenges/a-world-away-hunting-for-exoplanets-with-ai/?tab=resources)
Assessment of Ensemble-Based Machine Learning Algorithms for Exoplanet Identification (https://www.spaceappschallenge.org/2025/challenges/a-world-away-hunting-for-exoplanets-with-ai/?tab=resources)
