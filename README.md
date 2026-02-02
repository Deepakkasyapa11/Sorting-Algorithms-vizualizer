# Sorting Algorithm Visualizer

A modular Python-based visualization suite designed to demonstrate the mechanical efficiency and time complexity of various sorting algorithms. This project utilizes a **Generator-based architecture** to decouple sorting logic from the rendering thread, ensuring smooth UI performance.
<img width="796" height="493" alt="Screenshot (140)" src="https://github.com/user-attachments/assets/db748a81-c0bb-421c-8cc1-6c4b6419f28b" />

# Architectural Overview

Unlike standard linear implementations, this visualizer treats each sorting algorithm as a **state-machine**. 

# Key Design Patterns:
* **Generator-Driven Updates:** Leveraging Python's `yield` keyword to pause algorithm execution for frame rendering, preventing UI blocking without the overhead of multi-threading.
* **Decoupled Rendering:** The `Visualizer` class remains agnostic of the sorting logic, adhering to the **Single Responsibility Principle**.
* **Asymptotic Analysis:** Integrated visual markers for comparisons ($O(1)$ space) and recursive depth.

# Algorithms Implemented

| Algorithm | Best Case | Average Case | Worst Case | Space Complexity |
| :--- | :--- | :--- | :--- | :--- |
| **Quick Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ |
| **Merge Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ |
| **Selection Sort** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ |
| **Bubble Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ |

# Tech Stack
* **Language:** Python 3.x
* **Engine:** Pygame (Hardware-accelerated rendering)
* **Math:** NumPy (Optional for dataset generation)

# Installation & Usage

1. **Clone the repository:**
   git clone 
   cd sorting-visualizer-pro
