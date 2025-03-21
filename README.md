# 🎮 MemoryGame-javascript

Memory Game built with pure JavaScript, HTML and CSS – no frameworks!

## 🧠 About the Game

This is a classic memory card matching game. The goal is to find all matching pairs of cards with the fewest possible moves and in the shortest amount of time. When all cards are matched, your score (number of moves) is sent to the server.

## 🚀 Features

- Random card generation each time you play
- Real-time move and timer tracking
- Win detection and result display
- Animated card flip effect
- Reset and replay options
- Score submission to backend (`/score` endpoint)

## 🖼️ Card Data

All cards use image files located in `static/images/` folder. The game randomly selects half of them (e.g. 8 pairs for a 4x4 grid).

## 💡 How to Play

1. Click the **Start** button.
2. Try to find matching image pairs by flipping two cards at a time.
3. If the cards match – they stay visible.
4. If they don’t match – they flip back after 0.5 seconds.
5. Game ends when all pairs are matched.
6. Your move count and time are displayed at the end.

## 🧪 Technologies Used

- HTML5
- CSS3
- JavaScript

## 📦 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/aleTomasz/MemoryGame-javascript.git
