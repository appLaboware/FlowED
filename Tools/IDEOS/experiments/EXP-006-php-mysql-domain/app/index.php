<?php
header('Content-Type: text/html; charset=utf-8');

$pdo = null;
$error = null;

for ($attempt = 1; $attempt <= 30; $attempt++) {
    try {
        $pdo = new PDO(
            'mysql:host=127.0.0.1;port=3306;dbname=app;charset=utf8mb4',
            'root',
            '',
            [
                PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                PDO::ATTR_TIMEOUT => 2,
            ]
        );
        break;
    } catch (Throwable $e) {
        $error = $e->getMessage();
        usleep(500000);
    }
}

if (!$pdo) {
    http_response_code(503);
    echo '<h1>Banco ainda não disponível</h1>';
    echo '<pre>' . htmlspecialchars((string) $error) . '</pre>';
    exit;
}

$pdo->exec(
    'CREATE TABLE IF NOT EXISTS visits (
        id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    )'
);
$pdo->exec('INSERT INTO visits () VALUES ()');
$count = (int) $pdo->query('SELECT COUNT(*) FROM visits')->fetchColumn();
?>
<!doctype html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <title>Aplicação PHP genérica</title>
</head>
<body>
    <h1>Aplicação PHP genérica</h1>
    <p>PHP + MySQL materializados no Azure.</p>
    <p>Visitas persistidas nesta instância: <?= $count ?></p>
</body>
</html>
