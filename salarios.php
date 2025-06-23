<?php

// Arthur Ribeiro Araújo
// Emerson Sebastião dos Santos
// Matheus Latorre de Assis
// Vinícius Mlaker de Oliveira Dias

function receberSalarioBruto(): array {

    $salariosBrutos = [];
    $salarioBruto = true;

    while($salarioBruto != 0){

        $salarioBruto = readline();
        $index = 0;

        while($index < count($salariosBrutos) && $salarioBruto > $salariosBrutos[$index]){
            $index++;
        }

        if($salarioBruto > 0){
            array_splice($salariosBrutos, $index, 0, $salarioBruto);
        }
    }

    return $salariosBrutos;
}

function calcularAliquotaINSS(float $salarioBruto): string|float{
    return match (true) {
        $salarioBruto <= 1518 => 7.5,
        $salarioBruto <= 2793.88 => 9,
        $salarioBruto <= 4190.84 => 12,
        $salarioBruto <= 8157.41 => 14,
        default => "Teto",
    };
}

function verificarDeducaoINSS(float $salarioBruto): float{
    if($salarioBruto <= 1518 || $salarioBruto >= 8157.42){
        return 0;
    } elseif($salarioBruto <= 2793.88){
        return 22.77;
    } elseif($salarioBruto <= 4190.84){
        return 106.59;
    } else{
        return 190.4;
    }
}

function calcularValorINSS(float $salarioBruto, float|string $aliquotaINSS, float $deducaoINSS): float{
    if($aliquotaINSS == "Teto"){
        return 951.62;
    } else {
        return round(($salarioBruto * ($aliquotaINSS / 100) - $deducaoINSS), 2);
    }
}

function calcularBaseIR(float $salarioBruto, float $valorINSS): float{
    return round(($salarioBruto - $valorINSS), 2);
}

function calcularAliquotaIR(float $baseIR): float{
    if ($baseIR <= 2259.2){
        return 0;
    } elseif($baseIR <= 2826.65){
        return 7.5;
    } elseif($baseIR <= 3751.05){
        return 15;
    } elseif($baseIR <= 4664.68){
        return 22.5;
    } else{
        return 27.5;
    }
}

function verificarDeducaoIR(float $baseIR): float{
    return match(true){
        $baseIR <= 2259.2 => 0,
        $baseIR <= 2826.65 => 169.44,
        $baseIR <= 3751.05 => 381.44,
        $baseIR <= 4664.68 => 662.77,
        default => 896,
    };
}

function calcularValorIR(float $baseIR, float $aliquotaIR, float $deducaoIR): float{
    if(($baseIR * ($aliquotaIR / 100) - $deducaoIR) < 10){
        return 0;
    } else {
        return round($baseIR * ($aliquotaIR / 100) - $deducaoIR, 2);
    }
}

function calcularSalarioLiquido(float $salarioBruto, float $valorINSS, float $valorIR): float{
    return round($salarioBruto - $valorINSS - $valorIR, 2);
}

function formatarSaida(array $salariosBrutos): string{
    $saida = "     Bruto   AliqINSS   Val.INSS    Base I.R.     AliqIR     Val.IR    Liquido\n";

    foreach($salariosBrutos as $salarioBruto){
        $aliquotaINSS = calcularAliquotaINSS($salarioBruto);
        $deducaoINSS = verificarDeducaoINSS($salarioBruto);
        $valorINSS = calcularValorINSS($salarioBruto, $aliquotaINSS, $deducaoINSS);
        $baseIR = calcularBaseIR($salarioBruto, $valorINSS);
        $aliquotaIR = calcularAliquotaIR($baseIR);
        $deducaoIR = verificarDeducaoIR($baseIR);
        $valorIR = calcularValorIR($baseIR, $aliquotaIR, $deducaoIR);
        $salarioLiquido = calcularSalarioLiquido($salarioBruto, $valorINSS, $valorIR);

        $saida .= sprintf("%10.2f %10s %10.2f %12.2f %10.2f %10.2f %10.2f\n", $salarioBruto, $aliquotaINSS, $valorINSS, $baseIR, $aliquotaIR, $valorIR, $salarioLiquido);
    }

    $saida .= "Fim dos dados\n";
    return $saida;
}

function gravarArquivo(string $saida): void{
    $arquivo = fopen("calculos.txt", "w");
    fwrite($arquivo, $saida);
    fclose($arquivo);
}

$salariosBrutos = receberSalarioBruto();
$saida = formatarSaida($salariosBrutos);
gravarArquivo($saida);

echo $saida;