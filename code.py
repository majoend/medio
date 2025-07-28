
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Juego de Coches Simple</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');

        body {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background-color: #2c3e50; /* Fondo oscuro */
            font-family: 'Inter', sans-serif;
            color: #ecf0f1;
            overflow: hidden; /* Evita barras de desplazamiento */
        }

        h1 {
            color: #f1c40f; /* Amarillo brillante */
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }

        #game-container {
            position: relative;
            background-color: #34495e; /* Un poco más claro que el fondo */
            border-radius: 15px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.7);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px;
            max-width: 90vw; /* Ajuste para pantallas pequeñas */
            max-height: 90vh;
            box-sizing: border-box;
        }

        canvas {
            background-color: #2ecc71; /* Verde carretera */
            display: block;
            border-radius: 10px;
            box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.5);
            touch-action: none; /* Deshabilita el desplazamiento táctil predeterminado */
        }

        #score-board {
            margin-top: 15px;
            font-size: 1.5em;
            font-weight: bold;
            color: #ecf0f1;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
        }

        #game-over-screen {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.8);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: #e74c3c; /* Rojo de peligro */
            font-size: 2em;
            font-weight: bold;
            border-radius: 15px;
            text-align: center;
            padding: 20px;
            box-sizing: border-box;
            z-index: 10;
        }

        #game-over-screen p {
            margin: 10px 0;
            color: #ecf0f1;
        }

        .button-container {
            margin-top: 20px;
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
            justify-content: center;
        }

        button {
            background: linear-gradient(145deg, #3498db, #2980b9); /* Degradado azul */
            color: white;
            border: none;
            padding: 12px 25px;
            font-size: 1.1em;
            font-weight: bold;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        button:hover {
            background: linear-gradient(145deg, #2980b9, #3498db);
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
        }

        button:active {
            transform: translateY(0);
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.2);
        }

        /* Controles táctiles */
        #touch-controls {
            display: flex;
            justify-content: space-around;
            width: 100%;
            margin-top: 20px;
        }

        .touch-button {
            background: rgba(46, 204, 113, 0.7); /* Verde semitransparente */
            color: white;
            border: none;
            padding: 20px 30px;
            font-size: 2em;
            border-radius: 50%; /* Botones redondos */
            cursor: pointer;
            user-select: none; /* Evita la selección de texto al tocar */
            transition: background 0.2s ease;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
            width: 80px; /* Tamaño fijo para botones táctiles */
            height: 80px;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .touch-button:active {
            background: rgba(39, 174, 96, 0.9);
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        }

        @media (max-width: 600px) {
            h1 {
                font-size: 1.8em;
            }
            #score-board {
                font-size: 1.2em;
            }
            #game-over-screen {
                font-size: 1.5em;
            }
            button {
                padding: 10px 20px;
                font-size: 1em;
            }
            .touch-button {
                width: 60px;
                height: 60px;
                font-size: 1.5em;
            }
        }
    </style>
</head>
<body>
    <h1>Juego de Coches</h1>
    <div id="game-container">
        <canvas id="gameCanvas"></canvas>
        <div id="score-board">Puntuación: 0</div>
        <div id="game-over-screen" style="display: none;">
            <h2>¡Juego Terminado!</h2>
            <p>Tu puntuación final: <span id="final-score">0</span></p>
            <button id="restartButton">Reiniciar Juego</button>
        </div>
    </div>
    <div class="button-container">
        <button id="startButton">Iniciar Juego</button>
    </div>
    <div id="touch-controls" style="display: none;">
        <button class="touch-button" id="leftButton">◀</button>
        <button class="touch-button" id="rightButton">▶</button>
    </div>

    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        const scoreBoard = document.getElementById('score-board');
        const startButton = document.getElementById('startButton');
        const gameOverScreen = document.getElementById('game-over-screen');
        const finalScoreSpan = document.getElementById('final-score');
        const restartButton = document.getElementById('restartButton');
        const touchControls = document.getElementById('touch-controls');
        const leftButton = document.getElementById('leftButton');
        const rightButton = document.getElementById('rightButton');

        let gameRunning = false;
        let animationFrameId;

        // Configuración del juego
        const gameWidth = 300;
        const gameHeight = 500;
        const roadLineColor = '#bdc3c7'; // Gris claro para las líneas de la carretera
        const roadLineThickness = 5;
        const roadLineLength = 40;
        const roadLineGap = 60;

        // Coche del jugador
        const playerCar = {
            width: 30,
            height: 50,
            color: '#3498db', // Azul
            x: gameWidth / 2 - 15,
            y: gameHeight - 70,
            speed: 5,
        };

        // Obstáculos
        let obstacles = [];
        const obstacleWidth = 30;
        const obstacleHeight = 50;
        const obstacleColors = ['#e74c3c', '#f39c12', '#9b59b6', '#1abc9c']; // Rojo, Naranja, Púrpura, Turquesa
        let obstacleSpeed = 3;
        let obstacleSpawnInterval = 1500; // ms

        let score = 0;
        let lastObstacleSpawnTime = 0;

        // Estado de las teclas
        const keys = {
            left: false,
            right: false
        };

        // Función para dibujar el coche del jugador
        function drawPlayerCar() {
            ctx.fillStyle = playerCar.color;
            ctx.fillRect(playerCar.x, playerCar.y, playerCar.width, playerCar.height);

            // Detalles del coche (ventanas)
            ctx.fillStyle = '#ecf0f1'; // Blanco para las ventanas
            ctx.fillRect(playerCar.x + 5, playerCar.y + 10, playerCar.width - 10, 10); // Ventana delantera
            ctx.fillRect(playerCar.x + 5, playerCar.y + 30, playerCar.width - 10, 10); // Ventana trasera
        }

        // Función para dibujar un obstáculo
        function drawObstacle(obstacle) {
            ctx.fillStyle = obstacle.color;
            ctx.fillRect(obstacle.x, obstacle.y, obstacle.width, obstacle.height);

            // Detalles del obstáculo (luces)
            ctx.fillStyle = '#f1c40f'; // Amarillo para las luces
            ctx.fillRect(obstacle.x + 5, obstacle.y + 5, 5, 5); // Luz izquierda
            ctx.fillRect(obstacle.x + obstacle.width - 10, obstacle.y + 5, 5, 5); // Luz derecha
        }

        // Función para dibujar las líneas de la carretera
        function drawRoadLines() {
            ctx.fillStyle = roadLineColor;
            for (let i = 0; i < gameHeight / (roadLineLength + roadLineGap); i++) {
                ctx.fillRect(gameWidth / 2 - roadLineThickness / 2, (i * (roadLineLength + roadLineGap) + score * 0.1) % (gameHeight + roadLineLength) - roadLineLength, roadLineThickness, roadLineLength);
            }
        }

        // Función para actualizar el juego
        function update(currentTime) {
            if (!gameRunning) return;

            // Mover el coche del jugador
            if (keys.left) {
                playerCar.x = Math.max(0, playerCar.x - playerCar.speed);
            }
            if (keys.right) {
                playerCar.x = Math.min(gameWidth - playerCar.width, playerCar.x + playerCar.speed);
            }

            // Mover y generar obstáculos
            obstacles.forEach(obstacle => {
                obstacle.y += obstacleSpeed;
            });

            // Eliminar obstáculos fuera de la pantalla
            obstacles = obstacles.filter(obstacle => obstacle.y < gameHeight);

            // Generar nuevos obstáculos
            if (currentTime - lastObstacleSpawnTime > obstacleSpawnInterval) {
                const randomX = Math.floor(Math.random() * (gameWidth - obstacleWidth));
                const randomColor = obstacleColors[Math.floor(Math.random() * obstacleColors.length)];
                obstacles.push({
                    x: randomX,
                    y: -obstacleHeight, // Aparece desde arriba
                    width: obstacleWidth,
                    height: obstacleHeight,
                    color: randomColor
                });
                lastObstacleSpawnTime = currentTime;

                // Aumentar dificultad gradualmente
                obstacleSpeed += 0.005;
                obstacleSpawnInterval = Math.max(500, obstacleSpawnInterval - 5);
            }

            // Detección de colisiones
            obstacles.forEach(obstacle => {
                if (
                    playerCar.x < obstacle.x + obstacle.width &&
                    playerCar.x + playerCar.width > obstacle.x &&
                    playerCar.y < obstacle.y + obstacle.height &&
                    playerCar.y + playerCar.height > obstacle.y
                ) {
                    gameOver();
                }
            });

            // Actualizar puntuación
            score += 1;
            scoreBoard.textContent = `Puntuación: ${score}`;

            // Limpiar el canvas y redibujar
            ctx.clearRect(0, 0, gameWidth, gameHeight);
            drawRoadLines();
            drawPlayerCar();
            obstacles.forEach(drawObstacle);

            animationFrameId = requestAnimationFrame(update);
        }

        // Función para iniciar el juego
        function startGame() {
            canvas.width = gameWidth;
            canvas.height = gameHeight;
            playerCar.x = gameWidth / 2 - playerCar.width / 2;
            playerCar.y = gameHeight - 70;
            obstacles = [];
            score = 0;
            obstacleSpeed = 3;
            obstacleSpawnInterval = 1500;
            scoreBoard.textContent = `Puntuación: 0`;
            gameOverScreen.style.display = 'none';
            startButton.style.display = 'none';
            touchControls.style.display = (window.innerWidth <= 768) ? 'flex' : 'none'; // Mostrar controles táctiles en móvil
            gameRunning = true;
            lastObstacleSpawnTime = performance.now(); // Reiniciar el tiempo de aparición
            animationFrameId = requestAnimationFrame(update);
        }

        // Función para terminar el juego
        function gameOver() {
            gameRunning = false;
            cancelAnimationFrame(animationFrameId);
            finalScoreSpan.textContent = score;
            gameOverScreen.style.display = 'flex';
            startButton.style.display = 'block'; // Mostrar botón de inicio para reiniciar
            touchControls.style.display = 'none'; // Ocultar controles táctiles
        }

        // Event listeners para teclado
        document.addEventListener('keydown', (e) => {
            if (gameRunning) {
                if (e.key === 'ArrowLeft' || e.key.toLowerCase() === 'a') {
                    keys.left = true;
                } else if (e.key === 'ArrowRight' || e.key.toLowerCase() === 'd') {
                    keys.right = true;
                }
            }
        });

        document.addEventListener('keyup', (e) => {
            if (gameRunning) {
                if (e.key === 'ArrowLeft' || e.key.toLowerCase() === 'a') {
                    keys.left = false;
                } else if (e.key === 'ArrowRight' || e.key.toLowerCase() === 'd') {
                    keys.right = false;
                }
            }
        });

        // Event listeners para botones táctiles
        leftButton.addEventListener('touchstart', (e) => {
            e.preventDefault(); // Prevenir el desplazamiento
            if (gameRunning) keys.left = true;
        });
        leftButton.addEventListener('touchend', (e) => {
            e.preventDefault();
            if (gameRunning) keys.left = false;
        });
        rightButton.addEventListener('touchstart', (e) => {
            e.preventDefault();
            if (gameRunning) keys.right = true;
        });
        rightButton.addEventListener('touchend', (e) => {
            e.preventDefault();
            if (gameRunning) keys.right = false;
        });

        // Event listeners para botones de inicio/reinicio
        startButton.addEventListener('click', startGame);
        restartButton.addEventListener('click', startGame);

        // Ajustar el tamaño del canvas al redimensionar la ventana
        function resizeCanvas() {
            const container = document.getElementById('game-container');
            const containerWidth = container.offsetWidth - 40; // Restar padding
            const containerHeight = container.offsetHeight - 40 - scoreBoard.offsetHeight - (startButton.offsetHeight || 0);

            // Mantener una proporción de 3:5 (ancho:alto)
            let newWidth = Math.min(containerWidth, gameWidth);
            let newHeight = (newWidth / 3) * 5;

            if (newHeight > containerHeight) {
                newHeight = containerHeight;
                newWidth = (newHeight / 5) * 3;
            }

            canvas.width = newWidth;
            canvas.height = newHeight;

            // Escalar los elementos del juego
            const scaleX = newWidth / gameWidth;
            const scaleY = newHeight / gameHeight;

            playerCar.width = 30 * scaleX;
            playerCar.height = 50 * scaleY;
            playerCar.x = (gameWidth / 2 - 15) * scaleX;
            playerCar.y = (gameHeight - 70) * scaleY;
            playerCar.speed = 5 * scaleX;

            obstacles.forEach(obstacle => {
                obstacle.width = obstacleWidth * scaleX;
                obstacle.height = obstacleHeight * scaleY;
                obstacle.x *= scaleX;
                obstacle.y *= scaleY;
            });

            // Mostrar u ocultar controles táctiles según el ancho de la ventana
            if (window.innerWidth <= 768 && gameRunning) {
                touchControls.style.display = 'flex';
            } else {
                touchControls.style.display = 'none';
            }

            // Redibujar el juego si está en ejecución
            if (gameRunning) {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                drawRoadLines();
                drawPlayerCar();
                obstacles.forEach(drawObstacle);
            }
        }

        window.addEventListener('resize', resizeCanvas);
        window.addEventListener('load', () => {
            resizeCanvas(); // Ajustar el tamaño inicial al cargar
            // No iniciar el juego automáticamente, esperar al botón
        });
    </script>
</body>
</html>
