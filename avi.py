<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First Website</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f0f4f8;
            text-align: center;
            padding: 60px 20px;
        }

        .card {
            background: white;
            max-width: 500px;
            margin: auto;
            padding: 30px;
            border-radius: 16px;
            box-shadow: 0 4px 15px #00000015;
        }

        h1 {
            color: #2563eb;
        }

        button {
            background: #2563eb;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Welcome to My Website!</h1>
        <p>I created my first project on GitHub.</p>
        <button onclick="alert('Hello! Your website is working!')">
            Click Me
        </button>
    </div>
</body>
</html>
