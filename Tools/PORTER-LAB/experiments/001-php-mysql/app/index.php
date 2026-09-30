<?php

$host = getenv('DB_HOST') ?: 'db';
$name = getenv('DB_NAME') ?: 'app';
$user = getenv('DB_USER') ?: 'app';
$pass = getenv('DB_PASSWORD') ?: 'app';

$pdo = new PDO(
    "mysql:host={$host};dbname={$name};charset=utf8mb4",
    $user,
    $pass,
    [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]
);

$pdo->exec(
    'CREATE TABLE IF NOT EXISTS visits (
        id INT PRIMARY KEY AUTO_INCREMENT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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
    <title>PHP DB Demo</title>
</head>
<body>
    <h1>Aplicação PHP genérica</h1>
    <p>PHP + MySQL funcionando.</p>
    <p>Visitas persistidas: <?= $count ?></p>
</body>
</html>
