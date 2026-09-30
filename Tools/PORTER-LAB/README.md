# PORTER-LAB

Laboratório para testar Porter/CNAB no máximo de sua capacidade **sem IDEOS** e sem modelar aplicações por produto específico.

## Regra

A aplicação de teste é tratada apenas pelas suas propriedades técnicas:

- código PHP;
- servidor HTTP;
- banco MySQL;
- variáveis de conexão;
- persistência.

Nenhuma lógica do bundle conhece WordPress ou qualquer aplicação de mercado.

## Objetivo

Descobrir empiricamente:

1. o que Porter resolve sozinho;
2. o que precisa ser declarado no bundle;
3. o que depende de mixins/ferramentas externas;
4. onde termina a portabilidade real.

## Experimentos

- `001-php-mysql`: código PHP arbitrário + MySQL, lifecycle completo local.
