<?php

$host = getenv('DB_HOST') ?: 'db';
$name = getenv('DB_NAME') ?: 'iteos';
$user = getenv('DB_USER') ?: 'iteos';
$pass = getenv('DB_PASSWORD') ?: 'iteos';

$dsn = "mysql:host={$host};dbname={$name};charset=utf8mb4";
$pdo = new PDO($dsn, $user, $pass, [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
]);

$pdo->exec(
    'CREATE TABLE IF NOT EXISTS visits (
        id INT PRIMARY KEY AUTO_INCREMENT,
        visited_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )'
);

$pdo->exec('INSERT INTO visits () VALUES ()');

$count = (int) $pdo->query('SELECT COUNT(*) FROM visits')->fetchColumn();

header('Content-Type: text/html; charset=utf-8');
?>
<!doctype html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <title>ITEOS EXP-001</title>
</head>
<body>
    <h1>ITEOS EXP-001</h1>
    <p>Aplicação PHP + MySQL ativa.</p>
    <p>Visitas persistidas: <?= $count ?></p>
</body>
</html>
